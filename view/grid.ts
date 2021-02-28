const Honeycomb = require('honeycomb-grid')
 

export class painter {
  grid: any; 
  constructor(width: number, height: number) {
    this.grid = Honeycomb.defineGrid();
    this.grid.rectangle({ width: width, height: height });
    console.log("grid painted");
  }
}