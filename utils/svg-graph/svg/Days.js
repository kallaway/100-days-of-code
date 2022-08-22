import { formatDate } from './utils.js';

export default function Days(document, {
  values, size, space, padX, padY, colorFun, onClick, onHover
}) {
  const weekGroup = document.createElement("g")
  let i = 0
  for (const week of values) {
    const dayGroup = document.createElement("g")
    const s = size + space * 2;
    const x = padX + i * s + space;
    const y0 = padY + space;

    for (const day of week) {
      const dayNode = document.createElement("rect")
      dayNode.setAttribute("class", "cg-day")
      dayNode.setAttribute("x", x)
      dayNode.setAttribute("y", day.day * s + y0)
      dayNode.setAttribute("width", size)
      dayNode.setAttribute("height", size)
      dayNode.setAttribute("fill", colorFun(day))
      dayNode.setAttribute("data-count", day.count)
      dayNode.setAttribute("data-date", formatDate(day.date))
      dayNode.setAttribute("onclick", onClick(day))
      dayNode.setAttribute("onmouseover", onHover(day))
      dayGroup.appendChild(dayNode)
    }
    weekGroup.appendChild(dayGroup)
    i++
  }
  return weekGroup
}
