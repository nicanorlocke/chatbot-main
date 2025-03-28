<template>
    <v-container fluid class="chat-container">
        <v-row justify="center">
            <v-col cols="12" sm="10" md="8">
                <v-card class="elevation-3 chat-card">
                    <v-toolbar color="indigo" dark>
                        <v-toolbar-title>Chat Bot</v-toolbar-title>
                    </v-toolbar>

                    <v-card-text ref="chatContainer" class="chat-messages">
                        <v-row v-for="message in messages" :key="message.id" align="start" :class="{'bot-message-row': message.type === 'bot', 'user-message-row': message.type !== 'bot'}">
                            <v-col cols="auto">
                                <v-card :class="message.type === 'bot' ? 'bot-message': 'user-message'" outlined>
                                    <span v-if="message.loading" class="typing-indicator">
                                        <span></span><span></span><span></span>
                                    </span>
                                    <span v-else v-html="message.text"></span>
                                </v-card>
                            </v-col>
                        </v-row>
                        <div ref="bottom"></div> <!-- Reference element for scrolling -->
                    </v-card-text>

                    <v-divider></v-divider>
                    
                    <v-card-actions class="input-actions">
                        <v-text-field 
                            v-model="newMessage" 
                            label="Escribe un mensaje" 
                            outlined 
                            dense 
                            @keyup.enter="sendMessage" 
                            class="message-input" 
                            hide-details
                            append-inner-icon="mdi-send"
                            @click:append="sendMessage"
                            @click:prepend-inner="toggleRecognition"
                            :prepend-inner-icon="isRecording ? 'mdi-microphone-off' : 'mdi-microphone'"  
                        ></v-text-field>
                    </v-card-actions>

                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>


<script>
/* global webkitSpeechRecognition */
import io from 'socket.io-client';
import '../styles/ChatBotComponent.css';

export default {
    data(){
        return{
            messages:[
                {id: 1, text: 'Hola, ¿en qué puedo ayudarte hoy?', type: 'bot'}
            ],
            newMessage: '',
            isRecording: false,
            recognition: null,
            socket: null
        };
    },

    mounted(){
        //Initialize socket connection
        this.socket = io('http://localhost:5000'); //Update with your backend socket URL

        this.socket.on('bot_response', (data) => {
            this.addMessage(data, 'bot');
            this.removeTypingIndicator();
        });

        //Initialize Speech RRecognition
        if ('webkitSpeechRecognition' in window){
            this.recognition = new webkitSpeechRecognition();
            this.recognition.continuous = false;
            this.recognition.interimResults = false;
            this.recognition.lang = 'es-ES';

            this.recognition.onstart = () =>{
                console.log('Starting speech recording');
            };

            this.recognition.onresult = (event) => {
                this.newMessage = event.results[0][0].transcript;
                this.isRecording = false;
            };

            this.recognition.onerror = (event) => {
                console.error(event.error);
                this.isRecording = false;
            };

            this.recognition.onend = () => {
                console.log('Stoping speech recording');
                this.isRecording = false;
            };
        }
    },

    methods: {
        sendMessage(){
            if (this.newMessage.trim() !== ''){
                this.addMessage(this.newMessage, 'user');
                const userMessage = this.newMessage;
                this.newMessage = ''
                this.$nextTick(() => {
                    this.scrollToBottom();
                    this.showTypingIndicator();
                    this.socket.emit('user_message', userMessage);
                });
            }
        },

        addMessage(text, type, loading = false){
            this.messages.push({
                id: Date.now(),
                text,
                type,
                loading
            });
            this.$nextTick(this.scrollToBottom);
        },

        showTypingIndicator(){
            this.addMessage('', 'bot', true);
        },

        removeTypingIndicator(){
            this.messages = this.messages.filter(message => !message.loading);
        },

        scrollToBottom(){
            this.$refs.bottom.scrollIntoView({ behaviour: 'smooth', block: 'end'});
        },

        toggleRecognition(){
            if(this.recognition) {
                if (this.isRecording) {
                    this.recognition.stop();
                }else{
                    this.isRecording = true;
                    this.recognition.start();
                }
            }
        }
    }
};
</script>
