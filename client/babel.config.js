'use strict';

module.exports = function(api) {
    api.cache(true);

    const presets = ['@babel/preset-env', '@babel/preset-react', '@babel/preset-flow'];

    const plugins = [
        'react-hot-loader/babel',
        '@babel/plugin-proposal-partial-application',
        ['@babel/plugin-proposal-optional-chaining', {loose: false}],
        ['@babel/plugin-proposal-pipeline-operator', {proposal: 'minimal'}],
        ['@babel/plugin-proposal-nullish-coalescing-operator', {loose: false}],
        '@babel/plugin-proposal-do-expressions',
        ['@babel/plugin-proposal-decorators', {legacy: true}],
        '@babel/plugin-proposal-numeric-separator',
        '@babel/plugin-syntax-dynamic-import',
        ['@babel/plugin-proposal-class-properties', {loose: false}],
        '@babel/plugin-transform-regenerator',
        'babel-plugin-dynamic-import-node',
        [
            '@babel/transform-runtime',
            {
                corejs: 2
            }
        ]
    ];

    const env = {
        test: {
            presets,
            plugins
        }
    };

    return {
        presets,
        plugins,
        env
    };
};
