# benchmark.py
import requests
import threading
import time

NUM_REQUESTS = 10000
FLASK_URL = "http://localhost:5002/chatbot-api/v1/chatbot/speed_test"
FASTAPI_URL = "http://localhost:5001/chatbot-api/v1/chatbot-api/v1/speed_test"

def send_request(url, data, results, index):
    try:

        response = requests.post(url, json=data)
        response.raise_for_status()
        results[index] = response.json().get('execution_time', 0)
    except requests.exceptions.RequestException as e:
        print(f"Request to {url} failed: {e}")
    except KeyError as e:
        print(f"KeyError: {e}")

def measure_time(url, data):
    threads = []
    results = [0] * NUM_REQUESTS
    
    start_time = time.perf_counter()
    
    for i in range(NUM_REQUESTS):
        thread = threading.Thread(target=send_request, args=(url, data, results, i))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    end_time = time.perf_counter()
    
    total_time = end_time - start_time
    avg_execution_time = sum(results) / NUM_REQUESTS if NUM_REQUESTS > 0 else 0
    print(f"Total time for {NUM_REQUESTS} requests to {url}: {total_time:.4f} seconds")
    print(f"Average execution time per request: {avg_execution_time:.4f} seconds")

if __name__ == '__main__':
    data = {"question": "ayuda"}

    print("Testing Flask...")
    measure_time(FLASK_URL, data)
    
    print("Testing FastAPI...")
    measure_time(FASTAPI_URL, data)
