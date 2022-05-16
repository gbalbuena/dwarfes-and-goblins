const path = require('path');
const ModuleScopePlugin = require('@k88/ModuleScopePlugin');

module.exports = {
  entry: './src/index.ts',
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/,
      },
    ],
  },
  resolve: {
    extensions: ['.tsx', '.ts', '.js'],
    plugins: [
        new ModuleScopePlugin(APP_SOURCE_PATH, [ OTHER_PATHS, PACKAGE_JSON_PATH ]),
    ],
  },
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
};
