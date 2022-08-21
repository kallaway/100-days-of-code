import { DOMImplementation, XMLSerializer } from 'xmldom';
import Graph from './svg/Graph.js';

function generate(data = []) {
  const xmlSerializer = new XMLSerializer();
  const document = new DOMImplementation().createDocument('http://www.w3.org/1999/xhtml', 'html', null);

  const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');

  const graph = Graph(document, svg, {
    data,
    startDate: new Date('2022-01-01'),
    endDate: new Date('2022-12-01'),
  });

  const xml = xmlSerializer.serializeToString(graph);
  return xml
}

const data = []
const svg = generate(data)
console.log(svg)
