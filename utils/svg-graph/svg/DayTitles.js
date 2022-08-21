export default function DayTitles(document, {
  styles, size, space, padX, padY
}) {
  const s = size + space * 2;
  const half = s / 2;
  const days = [{
    v: 'M',
    y: padY + (s * 1) + half,
  }, {
    v: 'W',
    y: padY + (s * 3) + half,
  }, {
    v: 'F',
    y: padY + (s * 5) + half,
  }];
  const group = document.createElement("g")

  for (const d of days) {
    const dayNode = document.createElement("text")
    dayNode.setAttribute("x", (padX / 2).toString())
    dayNode.setAttribute("y", d.y)
    dayNode.setAttribute("style", styles.text2)
    dayNode.appendChild(document.createTextNode(d.v))
    
    group.appendChild(dayNode)
  }

  return group
}
