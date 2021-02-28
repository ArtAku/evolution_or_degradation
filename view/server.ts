import redis = require('redis');

export class painter {
  width: number = -1;
  height: number = -1;
  client;
  constructor(redis_port: number, redis_host: string) {
    this.client = redis.createClient(redis_port, redis_host);

    this.client.on("error", function(error) {
      console.error(error);
    });
  }

  public get_params() {
    this.client.get("width", (err, reply) => this.height = +(reply || "-1"));
    this.client.get("height", (err, reply) => this.height = +(reply || "-1"));
    console.log(`width ${this.width} height ${this.height}`)
  }
}