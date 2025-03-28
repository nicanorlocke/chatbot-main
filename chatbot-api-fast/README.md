## chatbot-api API

Chatbot to act as an assistant while the user is navigating the website.


## Install requirements

```bash
sudo apt update
sudo apt install python3 python3-pip nodejs npm -y
sudo npm install -g pm2
```

## Deploy application

### PM2 deployment

Application can be launched with the launch script:
```bash
sudo bash launch.sh
```
Or using PM2:
```bash
sudo pm2 start pm2.json
```
Note: if the script `launch.sh` doesn't works, you can use `launch2.sh` instead.

### Docker deployment

Build image and run

```bash
sudo docker build -t chatbot_api .
sudo docker run -it --rm --name chatbot-api chatbot_api
```

## Run application

For running directly the application in a "raw" way:
```bash
sudo python3 -m pip install pip --upgrade
sudo python3 -m pip install . --upgrade
sudo chatbot_api
```


## Disclaimer

Component developed by AIR Institute (@tobeal on GitHub) on 2024. For manteinance and bug reports please contact the developer at amontero@air-institute.com.
Copyright AIR Institute 2024. All rights reserved. See license for details.