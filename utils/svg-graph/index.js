import { DOMImplementation, XMLSerializer } from 'xmldom';
import Graph from './svg/Graph.js';

const xmlSerializer = new XMLSerializer();
const document = new DOMImplementation().createDocument('http://www.w3.org/1999/xhtml', 'html', null);

const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');

var data = []
const graph = Graph(document, svg, {
  data,
  startDate: new Date('2022-01-01'),
  endDate: new Date('2022-12-01'),
  colorFun: (v) => {
    return '#d6e685';
  }
});

let xml = xmlSerializer.serializeToString(graph);

console.log(xml)