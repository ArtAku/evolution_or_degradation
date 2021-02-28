import express from 'express';
import { server } from './server';
import { painter } from './grid';
import dotenv from "dotenv";
dotenv.config();
const app = express();
const redis_host = process.env.REDIS_HOST || "localhost"
const redis_port = +(process.env.REDIS_PORT || "6379")
const port = +(process.env.PORT || 8000)

const worker = new server(redis_port, redis_host);
const map_painter = new painter(10,4);

app.route('/map').get(async (_req, res) => {
  let cells = await worker.get_map();

  res.status(200).send({
    cells: cells,
  });
});

app.route('/init').get(async (_req, res) => {
  let params = await worker.init_params();

  res.status(200).send({
    params
  });
});

app.listen(port, () => {
  return console.log(`server is listening on ${port}`);
});
