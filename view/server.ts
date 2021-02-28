import redis = require('redis');
import { isWhileStatement } from 'typescript';
const { promisify } = require("util");

export class painter {
  width: number = -1;
  height: number = -1;
  client: redis.RedisClient;
  constructor(redis_port: number, redis_host: string) {
    this.client = new redis.RedisClient(
    {
      port: redis_port, 
      host: redis_host
    });

    this.client.on("error", error => {
      console.error(error);
    });
  }

  public async init_params() {
    let getAsync = promisify(this.client.get).bind(this.client);
    this.width = await getAsync("width").then( function (x:string) {
        return x;
    });
    this.height = await getAsync("height").then( function (x:string) {
        return x;
    });
    return {"width":this.width,"height":this.height};
  }

  public async get_map() {
    let getAsync = promisify(this.client.get).bind(this.client);
    let tempNumber: number;
    let tempStr: string;
    let cells = new Array();
    for (let i = 0; i < this.height; i++) {
      let raw: number[] = new Array();
      for (let j = 0; j < this.width; j++) {
        tempStr = await getAsync(`${i}_${j}_t`).then( function (x:string) {
          return x;
        });
        tempNumber = +tempStr;
        raw.push(tempNumber);
      }
      cells.push(raw);
    }
    return cells;
  }
}