import axios from 'axios';

//Endpoint Flask
const endpoint = 'http://chatbot-flask:5000/chatbot-api/v1/chatbot/chat';

//Endpoint FastAPI
//const endpoint = 'http://localhost:5001/chatbot-api/v1/chatbot-api/v1/chat/stream';

export const chatController = {
    async handleMessage(message: string): Promise<string> {
        try {
            //Call to endpoint to obtain response
            const response = await axios.get(endpoint, {
                params: { question: message },
            });
            
            //Process response & return bot message
            if (response.data) {
                const botMessage = this.extractBotMessage(response.data);
                console.log('Processed bot messge:', botMessage);
                return botMessage;
            } else {
                throw new Error('Respuesta inesperada del servidor');
            }

        } catch (error) {
            console.error('Error al obtener la respuesta del bot:', error);
            throw new Error('Error en el servidor');
        }
    },
    
    extractBotMessage(data: any): string {
        //Process & extract bot message
        const botMessageMatch = data.match(/^data: (.*?)\n\n/);
        const message = botMessageMatch ? botMessageMatch[1] : 'Respuesta no válida del bot';
        return message.replace(/\\n/g, '<br>');
    },
};
