// Pomodoro Timer
let pomodoroTimer = null;
let pomodoroSeconds = 25 * 60;
let pomodoroMode = 'work';
let pomodoroRunning = false;

function updatePomodoroDisplay() {
    const minutes = Math.floor(pomodoroSeconds / 60);
    const seconds = pomodoroSeconds % 60;
    document.getElementById('pomodoroDisplay').textContent =
        `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}

function startPomodoro() {
    if (pomodoroRunning) {
        clearInterval(pomodoroTimer);
        pomodoroRunning = false;
        document.getElementById('pomodoroStart').textContent = 'Start';
    } else {
        pomodoroRunning = true;
        document.getElementById('pomodoroStart').textContent = 'Pause';
        pomodoroTimer = setInterval(() => {
            pomodoroSeconds--;
            updatePomodoroDisplay();

            if (pomodoroSeconds <= 0) {
                clearInterval(pomodoroTimer);
                pomodoroRunning = false;
                document.getElementById('pomodoroStart').textContent = 'Start';

                if (pomodoroMode === 'work') {
                    pomodoroMode = 'break';
                    pomodoroSeconds = 5 * 60;
                    document.getElementById('pomodoroMode').textContent = 'Break';
                } else {
                    pomodoroMode = 'work';
                    pomodoroSeconds = 25 * 60;
                    document.getElementById('pomodoroMode').textContent = 'Work';
                }
                updatePomodoroDisplay();

                if (Notification.permission === 'granted') {
                    new Notification(`Pomodoro: ${pomodoroMode} time!`);
                }
            }
        }, 1000);
    }
}

function resetPomodoro() {
    clearInterval(pomodoroTimer);
    pomodoroRunning = false;
    pomodoroMode = 'work';
    pomodoroSeconds = 25 * 60;
    document.getElementById('pomodoroStart').textContent = 'Start';
    document.getElementById('pomodoroMode').textContent = 'Work';
    updatePomodoroDisplay();
}

// Site Status Checker
async function checkSiteStatus() {
    const sites = [
        { name: 'blog', url: 'https://bigjoesfullplate.com', elementId: 'blogStatus', timeId: 'blogResponseTime' },
        { name: 'zzzBlog', url: 'https://zzz.bigjoesfullplate.com', elementId: 'zzzBlogStatus', timeId: 'zzzBlogResponseTime' },
        { name: 'haddon', url: 'https://haddonworld.xyz', elementId: 'haddonStatus', timeId: 'haddonResponseTime' }
    ];

    for (const site of sites) {
        try {
            const startTime = Date.now();
            const response = await fetch(`https://api.allorigins.win/get?url=${encodeURIComponent(site.url)}`);
            const endTime = Date.now();
            const responseTime = endTime - startTime;

            const statusElement = document.getElementById(site.elementId);
            const timeElement = document.getElementById(site.timeId);

            if (response.ok) {
                statusElement.className = 'status-indicator status-online';
                timeElement.textContent = `${responseTime}ms`;
            } else {
                statusElement.className = 'status-indicator status-offline';
                timeElement.textContent = 'Error';
            }
        } catch (error) {
            const statusElement = document.getElementById(site.elementId);
            const timeElement = document.getElementById(site.timeId);
            statusElement.className = 'status-indicator status-offline';
            timeElement.textContent = 'Error';
        }
    }
}

// Quote of the Day
async function loadQuoteOfTheDay() {
    try {
        const response = await fetch('https://api.quotable.io/random?maxLength=120');
        const data = await response.json();

        document.getElementById('quoteText').textContent = `"${data.content}"`;
        document.getElementById('quoteAuthor').textContent = `— ${data.author}`;
    } catch (error) {
        document.getElementById('quoteText').textContent = '"The best way to predict the future is to create it."';
        document.getElementById('quoteAuthor').textContent = '— Peter Drucker';
    }
}

// Word of the Day
async function loadWordOfTheDay() {
    try {
        const words = ['serendipity', 'ephemeral', 'luminous', 'resilience', 'eloquent', 'innovative', 'profound', 'authentic'];
        const randomWord = words[Math.floor(Math.random() * words.length)];

        const response = await fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${randomWord}`);
        const data = await response.json();

        if (data && data[0]) {
            const entry = data[0];
            document.getElementById('wordTerm').textContent = entry.word;
            document.getElementById('wordPronunciation').textContent =
                entry.phonetic || entry.phonetics?.[0]?.text || '';
            document.getElementById('wordDefinition').textContent =
                entry.meanings?.[0]?.definitions?.[0]?.definition || 'Definition not available';
        }
    } catch (error) {
        document.getElementById('wordTerm').textContent = 'Serendipity';
        document.getElementById('wordPronunciation').textContent = '/ˌserənˈdipədē/';
        document.getElementById('wordDefinition').textContent = 'The occurrence and development of events by chance in a happy or beneficial way.';
    }
}

// Weather API
async function loadWeather() {
    try {
        const response = await fetch('https://api.open-meteo.com/v1/forecast?latitude=41.7658&longitude=-72.6734&current=temperature_2m,relative_humidity_2m,apparent_temperature,weather_code&temperature_unit=fahrenheit&timezone=America/New_York');
        const data = await response.json();

        const temp = Math.round(data.current.temperature_2m);
        const feelsLike = Math.round(data.current.apparent_temperature);
        const humidity = data.current.relative_humidity_2m;
        const weatherCode = data.current.weather_code;

        const weatherConditions = {
            0: { text: 'Clear sky', icon: '☀️' },
            1: { text: 'Mainly clear', icon: '🌤️' },
            2: { text: 'Partly cloudy', icon: '⛅' },
            3: { text: 'Overcast', icon: '☁️' },
            45: { text: 'Foggy', icon: '🌫️' },
            48: { text: 'Depositing rime fog', icon: '🌫️' },
            51: { text: 'Light drizzle', icon: '🌦️' },
            53: { text: 'Moderate drizzle', icon: '🌦️' },
            55: { text: 'Dense drizzle', icon: '🌧️' },
            61: { text: 'Slight rain', icon: '🌧️' },
            63: { text: 'Moderate rain', icon: '🌧️' },
            65: { text: 'Heavy rain', icon: '⛈️' },
            71: { text: 'Slight snow', icon: '🌨️' },
            73: { text: 'Moderate snow', icon: '❄️' },
            75: { text: 'Heavy snow', icon: '❄️' },
            95: { text: 'Thunderstorm', icon: '⛈️' }
        };

        const condition = weatherConditions[weatherCode] || { text: 'Unknown', icon: '🌤️' };

        document.getElementById('weatherTemp').textContent = `${temp}°F`;
        document.getElementById('weatherCondition').textContent = condition.text;
        document.getElementById('weatherIcon').textContent = condition.icon;
        document.getElementById('feelsLike').textContent = `${feelsLike}°F`;
        document.getElementById('humidity').textContent = `${humidity}%`;

    } catch (error) {
        console.error('Weather loading failed:', error);
        document.getElementById('weatherCondition').textContent = 'Unable to load';
    }
}

// Time zones update
function updateTimeZones() {
    const now = new Date();

    document.getElementById('localTime').textContent = now.toLocaleTimeString('en-US', {
        timeZone: 'America/New_York',
        hour: '2-digit',
        minute: '2-digit'
    });

    document.getElementById('londonTime').textContent = now.toLocaleTimeString('en-US', {
        timeZone: 'Europe/London',
        hour: '2-digit',
        minute: '2-digit'
    });

    document.getElementById('tokyoTime').textContent = now.toLocaleTimeString('en-US', {
        timeZone: 'Asia/Tokyo',
        hour: '2-digit',
        minute: '2-digit'
    });

    document.getElementById('pacificTime').textContent = now.toLocaleTimeString('en-US', {
        timeZone: 'America/Los_Angeles',
        hour: '2-digit',
        minute: '2-digit'
    });
}

// Save notes to memory
function saveNotes() {
    const notes = document.getElementById('quickNotes').value;
    window.userNotes = notes;
}

function loadNotes() {
    const notes = window.userNotes || '';
    document.getElementById('quickNotes').value = notes;
}

document.addEventListener('DOMContentLoaded', function() {
    loadNotes();

    document.getElementById('pomodoroStart').addEventListener('click', startPomodoro);
    document.getElementById('pomodoroReset').addEventListener('click', resetPomodoro);

    if ('Notification' in window && Notification.permission === 'default') {
        Notification.requestPermission();
    }

    const notesTextarea = document.getElementById('quickNotes');
    if (notesTextarea) {
        notesTextarea.addEventListener('input', saveNotes);
    }
});
