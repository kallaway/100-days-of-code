const MONTH = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

export default function Months(document, {
  styles={text: "", text2: ""}, values = [], size, space, padX = 0, padY = 0
}) {
  const s = size + space * 2;
  const s2 = s * 2;
  const months = [];
  values.forEach((group = [], i) => {
    group.forEach((d, j) => {
      if (j === 0 && d.day === 0) {
        const month = d.date.getMonth();
        const x = i * s + padX + space;
        const last = months.slice(-1).pop();
        if (!last || (month !== last.month && (x - last.x) > s2)) {
          months.push({ month, x });
        }
      }
    });
  });
  const group = document.createElement("g")

  for (const value of months) {
    const monthNode = document.createElement("text")
    monthNode.setAttribute("x", value.x.toString())
    monthNode.setAttribute("y", (padY / 2).toString())
    monthNode.setAttribute("style", styles.text)
    monthNode.appendChild(document.createTextNode(MONTH[value.month]))

    group.appendChild(monthNode)
  }

  return group
}
