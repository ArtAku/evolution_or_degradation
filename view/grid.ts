const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const { window } = new JSDOM(`<!DOCTYPE html><body><p>Hello world</p></body>`);
const Honeycomb = require('honeycomb-grid');
const svg = require('@svgdotjs/svg.js');
svg.registerWindow(window, window.document);
 
interface MyCorner {
  x: number;
  y: number;
}

export class painter {
  grid: any; 
  size: number;
  height: number;
  width: number;
  Hex: any;
  Grid: any;
  constructor(width: number, height: number, size: number) {
    this.width = width;
    this.height = height;
    this.size = size;
    this.Hex = Honeycomb.extendHex({ size: this.size });
    this.Grid = Honeycomb.defineGrid(this.Hex);

    // this.grid = Honeycomb.defineGrid();
    // this.grid.rectangle({ width: width, height: height });
    console.log("grid created");
  }

  public createSVG() {

    const draw = svg.SVG();
    // get the corners of a hex (they're the same for all hexes created with the same Hex factory)
    const corners = this.Hex().corners();
    // an SVG symbol can be reused
    const hexSymbol = draw.symbol()
        // map the corners' positions to a string and create a polygon
        .polygon(corners.map((p:MyCorner) => `${p.x},${p.y}`))
        .fill('none')
        .stroke({ width: 1, color: '#999' });

    // render 10,000 hexes
    this.Grid.rectangle({ width: this.width, height: this.height }).forEach((hex:any) => {
        const { x, y } = hex.toPoint();
        // use hexSymbol and set its position for each hex
        let a = draw.use(hexSymbol);
console.log(a);
          // translate(x, y);
    });
    return "element";
  }
}