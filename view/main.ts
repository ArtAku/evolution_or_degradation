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
let map_painter = new painter(1, 1, 10);

async function do_all(size: number | undefined = undefined) {
  if(size)
    map_painter.updateSize(size);

  let params = await worker.init_params();
  let my_map = await worker.get_map();
  map_painter.height = params.height;
  map_painter.width = params.width;
  return  map_painter.createSVGFromMap(my_map);
}

app.route('/').get(async (_req, res) => {
  res.send(await do_all());
});

app.route('/:id').get(async (_req, res) => {
  res.send(await do_all(+_req.params.id));
});

app.route('/set/size/:id').get(async (_req, res) => {
  map_painter.updateSize(+_req.params.id);
  res.status(200);
  res.end();
});

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
