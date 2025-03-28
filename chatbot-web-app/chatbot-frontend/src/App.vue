<template>
  <v-app>
    <v-main>
      <ChatBot/>
    </v-main>
  </v-app>
</template>

<script>
import ChatBot from './components/ChatBot.vue'

export default {
  name: 'App',

  components: {
    ChatBot,
  },

  data: () => ({
    //
  }),
}
</script>
