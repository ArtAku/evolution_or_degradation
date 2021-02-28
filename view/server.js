const http = require('http')

const requestHandler = (request, response) => {
  console.log(request.url)
  response.end('Hello Node.js Server!')
}

export const server = http.createServer(requestHandler);
