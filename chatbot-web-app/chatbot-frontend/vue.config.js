const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,

  devServer: {

    hot: true, //habilita Hot Module Replacement

    client: {
      overlay: {
        warnings: false,
        errors: true
      }
    },
    
    watchFiles: {
      options: {
        ignored: /node_modules/,
        aggregateTimeout: 300,
        poll: 1000,
      }
    }

  },

  pluginOptions: {
    vuetify: {
			// https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vuetify-loader
		}
  }
})
