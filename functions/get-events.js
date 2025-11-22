const fetch = require('node-fetch');

exports.handler = async function(event, context) {
  const { calendarId, timeMin, timeMax } = event.queryStringParameters;
  const apiKey = process.env.GOOGLE_API_KEY;

  const url = `https://www.googleapis.com/calendar/v3/calendars/${calendarId}/events?key=${apiKey}&timeMin=${timeMin}&timeMax=${timeMax}&singleEvents=true&orderBy=startTime`;

  try {
    const response = await fetch(url);
    const data = await response.json();
    return {
      statusCode: 200,
      body: JSON.stringify(data),
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Error fetching calendar events' }),
    };
  }
};
