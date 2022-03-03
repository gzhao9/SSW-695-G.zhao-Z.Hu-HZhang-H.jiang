//const fetch = require("node-fetch");

const params = {
    api_key: 'JkdjMHjQobEeEAVSkii5eg1n5NtTKH0AAL0FgXBb',
    query: 'apple',
    generalSearchInput: "apple",
    pageNumber: 1,
    numberOfResultsPerPage: 50,
    pageSize: 5,
    requireAllWords: false,
}

// const api_url = 
// 'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=${encodeURIComponent(params.api_key)}&query=${encodeURIComponent(params.query)}'

const api_url = 
'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=JkdjMHjQobEeEAVSkii5eg1n5NtTKH0AAL0FgXBb&query=apple'

// function getData() {
//     return fetch(api_url)
//     .then(respone => respone.json())
// }

// getData().then(data => console.log(data))

window.location.href=api_url