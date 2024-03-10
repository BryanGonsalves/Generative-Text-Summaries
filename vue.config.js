module.exports = {
    devServer: {
      allowedHosts: "all",
      proxy: {
        '/summary': {
          target: "http://localhost:5000/",
          changeOrigin: true
        }
      }
    }
  }