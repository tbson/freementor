module.exports = {
    env: {
        browser: true,
        es6: true
    },
    extends: 'standard',
    globals: {
        Atomics: 'readonly',
        SharedArrayBuffer: 'readonly'
    },
    parserOptions: {
        ecmaFeatures: {
            jsx: true
        },
        ecmaVersion: 2018,
        sourceType: 'module'
    },
    plugins: ['react', 'react-hooks'],
    rules: {
        indent: ['error', 4],
        'comma-dangle': 0,
        'react/jsx-filename-extension': 0,
        'react/prefer-stateless-function': 0,
        'react/jsx-indent': ['error', 4],
        'react/no-danger': 0,
        'react-hooks/rules-of-hooks': 'error',
        'react-hooks/exhaustive-deps': 'warn'
    }
};
