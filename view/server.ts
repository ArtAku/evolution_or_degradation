import redis = require('redis');
const { promisify } = require("util");

export interface Cell {
  temperature: number;
  hardness: number;
  energy: number;
  income: number;
}

export interface Map {
  rows: Cell[][]
}

class MyMap implements Map {
  rows: Cell[][] = [];

  constructor(rows: Cell[][]) {
    this.rows = rows;
  }
}

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

  public async get_map(): Promise<Map> {
    
    let cells = new Array();
    for (let i = 0; i < this.height; i++) {
      let rawT: number[] = new Array();
      let rawH: number[] = new Array();
      let rawE: number[] = new Array();
      let rawI: number[] = new Array();
      let raw: Cell[] = new Array();

      rawT = await this.get_redis_array(i, 't');
      rawH = await this.get_redis_array(i, 'h');
      rawE = await this.get_redis_array(i, 'e');
      rawI = await this.get_redis_array(i, 'i');

      let n = rawT.length;
      for (let i = 0; i < n; i++) {
        raw.push({
          'energy':rawE[i],
          'income':rawI[i],
          'temperature':rawT[i],
          'hardness':rawH[i]
        });
      }

      cells.push(raw);
    }
    return new MyMap(cells);
  }

  private async get_redis_array(row_number: number, array_type: string) {
    let tempStr: string;
    let getAsync = promisify(this.client.get).bind(this.client);

    tempStr = await getAsync(`${row_number}_${array_type}`).then( function (x:string) {
      return x;
    });
    tempStr = tempStr.substr(1,tempStr.length-4);
    return tempStr.split("array([").map(x => +(x.split("]")[0])).slice(1);
  }
}