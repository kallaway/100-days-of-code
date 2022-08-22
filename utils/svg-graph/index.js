import { DOMImplementation, XMLSerializer } from 'xmldom';
import { stats } from './dayStats.js';
import Graph from './svg/Graph.js';
import { oneYearPlus } from './svg/utils.js';

function generate(data = []) {
  const xmlSerializer = new XMLSerializer();
  const document = new DOMImplementation().createDocument('http://www.w3.org/1999/xhtml', 'html', null);

  const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  const startDate = new Date('2022-06-15')
  const endDate = oneYearPlus(startDate)
  const graph = Graph(document, svg, {
    data,
    startDate: startDate,
    endDate: endDate,
    // onClick: (v) => `window.open("#asd", "_blank")`,
    onClick: (v) => { return `document.getElementById('${v.dayID}')?.scrollIntoView();` },
  });

  const xml = xmlSerializer.serializeToString(graph);
  return xml
}

const data = stats((line) => ({ date: line.date, count: line.weight }))
// show the stats on hover
const svg = generate(data)
console.log(svg)
