
// TODO: finish 
// https://nodejs.org/en
// https://axios-http.com/docs/example

const axios = require('axios');

const url = 'https://example.com'; 

async function fetchPage(url) {
  try {
    const response = await axios.get(url);
    return response.data;
  } catch (error) {
    console.error('Error during downloading page', error);
    throw error;
  }
}

async function main() {
  try {
    const html = await fetchPage(url);
    console.log('Page content:');
    console.log(html);
  } catch (error) {
    console.error('Main func error:', error);
  }
}

main();
