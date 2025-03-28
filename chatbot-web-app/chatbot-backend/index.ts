import express from 'express';
import { createServer } from 'http';
import { Server } from 'socket.io';
import { chatController } from './src/controller/chatController';

const app = express();
const httpServer = createServer(app);
const io = new Server(httpServer, {
  cors: {
    origin: "*"
  }
});

app.use(express.json());

io.on('connection', (socket) => {
  console.log('User connected:', socket.id);

  socket.on('user_message', async (message: string) => {
    console.log('Received message:', message);
    try {
        const botResponse = await chatController.handleMessage(message);
        socket.emit('bot_response', botResponse);
        
    } catch (error) {
      console.error('Error fetching bot response:', error);
      socket.emit('bot_response', 'Error: Could not get response');
    }
  });

  socket.on('disconnect', () => {
    console.log('user disconnected:', socket.id);
  });
});


const PORT = process.env.PORT || 5000;
httpServer.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
