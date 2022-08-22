import {
    diffDays, formatDate, noop, today, oneYearAgo, rectColor
} from './utils.js';
import Days from './Days.js';
import Months from './Months.js';
import DayTitles from './DayTitles.js';
import getStyles from './styles.js';

export default function Graph(document, root, {
    data = [],
    colorFun = rectColor,
    startDate = oneYearAgo(),
    endDate = today(),
    size = 12,
    space = 1,
    padX = 20,
    padY = 20,
    styleOptions = {},
    onClick = noop, 
    onHover = noop,
}) {
    const values = [];
    const days = diffDays(startDate, endDate);
    const dataTmp = data.reduce((memo, v) => {
        memo[v.date] = v.count;
        return memo;
    }, {});
    // Compute values
    let group = 0;
    for (let i = 0; i <= days; i += 1) {
        const date = new Date(startDate);
        date.setDate(date.getDate() + i);

        const day = date.getDay();
        const count = dataTmp[formatDate(date)] || 0;

        if ((day === 0 && i !== 0) || i === 0) {
            values.push([]);
            group += 1;
        }

        values[group - 1].push({ count, date, day, dayID: `day-${day}-${formatDate(date)}` });
    }

    const s = size + space * 2;
    const width = (group * s) + (padX * 2);
    const height = 7 * s + padY + 10;
    const box = `0 0 ${width} ${height}`;
    const styles = getStyles(styleOptions);

    const attrs = {
        styles, values, size, space, colorFun, padX, padY, onClick, onHover
    };
    
    root.setAttribute("width", width)
    root.setAttribute("height", height)
    root.setAttribute("viewBox", box)
    
    const borderNode = document.createElement("rect")
    borderNode.setAttribute("x", 0)
    borderNode.setAttribute("y", 0)
    borderNode.setAttribute("width", width)
    borderNode.setAttribute("height", height)
    borderNode.setAttribute("fill", "#fff")
    
    root.appendChild(borderNode)
    root.appendChild(Days(document,attrs))
    root.appendChild(Months(document,attrs))
    root.appendChild(DayTitles(document,attrs))

    return root
}
