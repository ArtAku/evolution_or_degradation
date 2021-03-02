const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const { window } = new JSDOM(`<!DOCTYPE html><body><p>Hello world</p></body>`);
const Honeycomb = require('honeycomb-grid');
const svg = require('@svgdotjs/svg.js');
import { Color } from "@svgdotjs/svg.js";
import { Map } from "./server";
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
  }

  public updateSize(size:number) {
    this.size = size;
    this.Hex = Honeycomb.extendHex({ size: this.size });
    this.Grid = Honeycomb.defineGrid(this.Hex);
  }

  public createSVGFromMap(myMap: Map) {
    const draw = svg.SVG();
    const corners = this.Hex().corners();
    const hexSymbol = draw.symbol()
        .polygon(corners.map((p:MyCorner) => `${p.x},${p.y}`))
        .stroke({ width: 1, color: '#999' });
    let i:number ,j: number;
    let r:number,g:number,b: number;
    let dx: number = this.size * 2 * myMap.rows[0].length;
    let dy: number = this.size * 2 * myMap.rows.length;
    this.Grid.rectangle({ width: this.width, height: this.height }).forEach((hex:any, index:number) => {
        const { x, y } = hex.toPoint();
        i = Math.floor(index / this.width);
        j = index % this.width;
        r = myMap.rows[i][j].temperature * 255; // depend on max energy or setup 0..1
        draw.use(hexSymbol).move(x,y).fill(new Color(r,0,0));

        // let text = draw.plain(`${myMap.rows[i][j].temperature}`);
        // text.move(x,y).fill(new Color(255,255,255));
    });
    
    this.Grid.rectangle({ width: this.width, height: this.height }).forEach((hex:any, index:number) => {
      const { x, y } = hex.toPoint();
      i = Math.floor(index / this.width);
      j = index % this.width;
      b = myMap.rows[i][j].hardness * 255; // depend on max energy or setup 0..1
      draw.use(hexSymbol).move(x + dx,y).fill(new Color(0,0,b));
      
      // let text = draw.plain(`${myMap.rows[i][j].hardness}`);
      // text.move(x + dx,y).fill(new Color(255,255,255));
    });
    
    this.Grid.rectangle({ width: this.width, height: this.height }).forEach((hex:any, index:number) => {
      const { x, y } = hex.toPoint();
      i = Math.floor(index / this.width);
      j = index % this.width;
      g = myMap.rows[i][j].energy * 255; // depend on max energy or setup 0..1
      draw.use(hexSymbol).move(x,y + dy).fill(new Color(0,g,0));
      
      // let text = draw.plain(`${myMap.rows[i][j].energy}`);
      // text.move(x,y + dy).fill(new Color(255,255,255));
      
    });
    
    this.Grid.rectangle({ width: this.width, height: this.height }).forEach((hex:any, index:number) => {
      const { x, y } = hex.toPoint();
      i = Math.floor(index / this.width);
      j = index % this.width;
      g = myMap.rows[i][j].income * 255; // depend on max energy or setup 0..1
      draw.use(hexSymbol).move(x + dx,y + dy).fill(new Color(0,g,0));
      
      // let text = draw.plain(`${myMap.rows[i][j].energy}`);
      // text.move(x + dx,y + dy).fill(new Color(255,255,255));
    });
    console.log("grid created");
    return '<svg width=100% height=100%>' + draw.node.innerHTML + '</svg>';
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

    this.Grid.rectangle({ width: this.width, height: this.height }).forEach((hex:any) => {
        const { x, y } = hex.toPoint();
        draw.use(hexSymbol).move(x,y);
    });
    return '<svg>' + draw.node.innerHTML + '</svg>';
  }
}
