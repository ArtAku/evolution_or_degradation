import express from 'express';
import { painter } from './server'
const app = express();
const port = process.env.PORT || 5000
const redis_host = process.env.REDIS_HOST || "localhost"
const redis_port = +(process.env.REDIS_PORT || "6379")

app.get('/', (req, res) => {
  res.send('The sedulous hyena ate the antelope!');
});

function main() {
  let server = new painter(redis_port, redis_host);
  server.get_params();
  app.listen( port, () => {
    return console.log(`server is listening on ${port}`);
  });
}

main();
