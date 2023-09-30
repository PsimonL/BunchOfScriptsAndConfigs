

// https://nodejs.org/en
// https://axios-http.com/docs/example

const axios = require('axios');

const url = 'https://example.com'; 

async function fetchPage(url) {
  try {
    const response = await axios.get(url);
    return response.data;
  } catch (error) {
    console.error('Błąd podczas pobierania strony:', error);
    throw error;
  }
}

async function main() {
  try {
    const html = await fetchPage(url);
    console.log('Zawartość strony:');
    console.log(html);
  } catch (error) {
    console.error('Błąd głównej funkcji:', error);
  }
}

main();
