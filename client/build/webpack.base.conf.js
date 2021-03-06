var path = require("path");
var utils = require("./utils");
var config = require("../config");
var vueLoaderConfig = require("./vue-loader.conf");
var webpack = require("webpack");

function resolve(dir) {
  return path.join(__dirname, "..", dir);
}

module.exports = {
  // plugins: [// 3. 配置全局使用 jquery
  //   new webpack.ProvidePlugin({
  //   $: "jquery",
  //   jQuery: "jquery",
  //   jquery: "jquery",
  //   "window.jQuery": "jquery"
  // })],
  entry: {
    app: "./client/src/main.js"
  },
  output: {
    path:
      process.env.NODE_ENV === "production"
        ? config.build.assetsRoot
        : config.dev.assetsRoot,
    filename: "[name].js",
    publicPath:
      process.env.NODE_ENV === "production"
        ? config.build.assetsPublicPath
        : config.dev.assetsPublicPath
  },
  resolve: {
    extensions: [".js", ".vue", ".json"],
    alias: {
      vue$: "vue/dist/vue.esm.js",
      "@": resolve("src"),
      scss_vars: "@/styles/vars.scss"
    }
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: "vue-loader",
        options: vueLoaderConfig
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        options: {
          presets: ['es2015']
        },
        include: [resolve('src'), resolve('test')]
      },
      {
        test: /\.pug$/,
        loader: 'pug'
      },
      {
        test: /\.(png|jpe?g|gif|svg)(\?.*)?$/,
        loader: "url-loader",
        options: {
          limit: 10000,
          name: utils.assetsPath("img/[name].[hash:7].[ext]")
        }
      },
      {
        test: /\.(woff2?|eot|ttf|otf)(\?.*)?$/,
        loader: "url-loader",
        options: {
          limit: 80000,
          name: utils.assetsPath("fonts/[name].[hash:7].[ext]")
        }
      }
    ]
  }
};
