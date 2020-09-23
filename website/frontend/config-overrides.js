const multipleEntry = require('react-app-rewire-multiple-entry')([
    {
        entry: 'src/index.js',
        template: 'public/index.html',
        outPath: '/index.html'
    },
    {
        entry: 'src/book.js',
        template: 'public/index.html',
        outPath: '/book.html'
    }
]);

module.exports = {
    webpack: function (config, env) {
        multipleEntry.addMultiEntry(config);
        return config;
    }
};