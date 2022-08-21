const SIZE = '12px';
const TYPE = '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif';

export default function getStyles({
  textColor = '#959494',
  fontSize = SIZE,
  fontFamily = TYPE
} = {}) {
  const text = {
    fill: textColor,
    'font-size': fontSize,
    'font-family': fontFamily,
    'dominant-baseline': 'central'
  };
  const text2 = {
    ...text,
    'text-anchor': 'middle'
  }
  return {
    text: Object.entries(text).map(([k,v]) => `${k}: ${v}`).join(";"),
    text2: Object.entries(text).map(([k,v]) => `${k}: ${v}`).join(";"),
  };
}
