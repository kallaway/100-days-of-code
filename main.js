// Initialize everything
updateTimeZones();
setInterval(updateTimeZones, 1000);

// Initialize calendar
generateCalendar(currentMonth, currentYear);

loadWeather();
loadRSSFeeds();
loadQuoteOfTheDay();
loadWordOfTheDay();
checkSiteStatus();

setInterval(loadWeather, 600000);
setInterval(loadRSSFeeds, 1800000);
setInterval(() => {
    const now = new Date();
    if (now.getHours() === 0 && now.getMinutes() < 5) {
        loadQuoteOfTheDay();
        loadWordOfTheDay();
    }
}, 3600000);
setInterval(checkSiteStatus, 300000);

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('searchInput').focus();
    loadNotes();

    // Load saved Google Calendar credentials
    const savedCalendarId = localStorage.getItem('googleCalendarId');
    if (savedCalendarId) {
        document.getElementById('googleCalendarId').value = savedCalendarId;
    }

    // Setup calendar navigation
    document.getElementById('prevMonth').addEventListener('click', previousMonth);
    document.getElementById('nextMonth').addEventListener('click', nextMonth);
    document.getElementById('loadGoogleCalendar').addEventListener('click', () => {
        const calendarId = document.getElementById('googleCalendarId').value;
        localStorage.setItem('googleCalendarId', calendarId);
        generateCalendar(currentMonth, currentYear);
    });

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
