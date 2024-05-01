const path = require("path");
const HtmlWebPackPlugin = require("html-webpack-plugin");

module.exports = {
    entry: "./src/index.js",
    output: {
        path: path.join(__dirname, "/dist"),
        filename: "bundle.js",
    },
    devServer: {
        historyApiFallback: true
    },
    module: {
        rules:[
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
                use: ["babel-loader"]
            },
            {
                test: /\.css$/,
                exclude: /node_modules/,
                use: ["style-loader", "css-loader"]
            },
            {
                test: /\.(jpe?g|png|gif|svg)$/i,
                exclude: /node_modules/,
                use: ["url-loader?limit=10000", "img-loader"]
            }
        ]

    },
    plugins:[
        new HtmlWebPackPlugin({template: "./src/index.html"})
    ]
};