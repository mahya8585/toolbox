const { default: axios } = require("axios");

const headers = {
'maaya-test': 'this-is-test-header'
}

const result = axios.get(
    'https://xxxxxxxxx',
    {headers: headers}
);

// console.log(result.headers);
