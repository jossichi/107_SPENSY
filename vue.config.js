const { defineConfig } = require("@vue/cli-service");

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    https: true, // Bật HTTPS cho server
    hot: true,
    client: {
      webSocketURL: "wss://localhost:8080/ws", // Sử dụng wss thay vì ws
    },
  },
});
