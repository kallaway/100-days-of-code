import fs from "fs"
import path from "path"

function calcWeight(parsedLine) {
    return {
        ...parsedLine,
        weight: (1 // mark that an entry was created
            + 1 * parsedLine.like_count // likes worth basic amount
            + 5 * parsedLine.retweet_count // retweet worth more than a like
            + 10 * parsedLine.reply_count // word reaction gives the most
            + 10 * parsedLine.quote_count // word reaction gives the most
        )
    }
}

export function stats(formatFn = (e) => e, weightFn = calcWeight) {
    let result = []
    try {
        const statsPath = path.join(process.cwd(), '..', 'twitter', 'STATS')
        // console.log(statsPath);
        result = fs
            .readFileSync(statsPath, 'utf8')
            .trim()
            .split("\n")
            .filter((_line, index) => index != 0) // ignore header
            .map((line) => {
                const lineData = line.split(",") // "csv parse"
                let i = 0
                return {
                    daynum: parseInt(lineData[i++]),
                    id: parseInt(lineData[i++]),
                    date: lineData[i++],
                    retweet_count: parseInt(lineData[i++]),
                    reply_count: parseInt(lineData[i++]),
                    like_count: parseInt(lineData[i++]),
                    quote_count: parseInt(lineData[i++]),
                }
            })
            .map(weightFn)
            .map(formatFn)
    } catch (err) {
        console.error(err);
    }
    return result
}
