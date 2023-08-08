#!/usr/bin/node
const request = require('request')
const API_URL = 'https://swapi-api.hbtn.io/api/films'

if (process.argv.length > 2) {
  request(`${API_URL}/${process.argv[2]}/`, (err, _, body) => {
    if (err) console.log(err)
    const charsURL = JSON.parse(body).characters;
    const charsName = charsURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, __, charsReqBody) => {
          if (promiseErr) reject(promiseErr)
          resolve(JSON.parse(charsReqBody).name)
        })
      })
    )

    Promise.all(charsName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr))
  })
}
