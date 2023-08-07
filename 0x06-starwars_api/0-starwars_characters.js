#!/usr/bin/node
const request = require('request')
const movieId = process.argv[2]
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + movieId,
  method: 'GET'
}

const printCharacters = (chars, idx) => {
  request(chars[idx], (err, res, body) => {
    if (!err) {
      console.log(JSON.parse(body).name)
      if (idx + 1 < chars.length) printCharacters(chars, idx + 1)
    }
  })
}

request(options, (err, res, body) => {
  if (!err) {
    const chars = JSON.parse(body).characters
    printCharacters(chars, 0)
  }
})
