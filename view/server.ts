import redis = require('redis');
const { promisify } = require("util");

export class server {
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
    let tempStr: string;
    
    let cells = new Array();
    for (let i = 0; i < this.height; i++) {
      let raw: number[] = new Array();
        tempStr = await getAsync(`${i}_t`).then( function (x:string) {
          return x;
        });
        tempStr = tempStr.substr(1,tempStr.length-4);
        raw = tempStr.split("array([").map(x => +(x.split("]")[0])).slice(1);
      cells.push(raw);
    }
    return cells;
  }
}