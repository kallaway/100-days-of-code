// Calendar Widget
let currentMonth = new Date().getMonth();
let currentYear = new Date().getFullYear();

async function fetchGoogleCalendarEvents(month, year, calendarId) {
    const timeMin = new Date(year, month, 1).toISOString();
    const timeMax = new Date(year, month + 1, 0).toISOString();

    const url = `/.netlify/functions/get-events?calendarId=${calendarId}&timeMin=${timeMin}&timeMax=${timeMax}`;

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Error fetching calendar events: ${response.statusText}`);
        }
        const data = await response.json();
        return data.items || [];
    } catch (error) {
        console.error('Error fetching Google Calendar events:', error);
        alert('Error fetching Google Calendar events. Please check your Calendar ID.');
        return [];
    }
}

function renderEvents(events) {
    const calendarGrid = document.getElementById('calendarGrid');

    events.forEach(event => {
        const startDate = new Date(event.start.dateTime || event.start.date);
        const day = startDate.getDate();

        const dayCells = Array.from(calendarGrid.querySelectorAll('.calendar-day'));
        const dayCell = dayCells.find(cell => !cell.classList.contains('other-month') && parseInt(cell.textContent) === day);

        if (dayCell) {
            const eventElement = document.createElement('div');
            eventElement.className = 'calendar-event';
            eventElement.textContent = event.summary;
            dayCell.appendChild(eventElement);
        }
    });
}

async function generateCalendar(month, year) {
    const monthNames = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ];

    const dayNames = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];

    // Update month/year display
    document.getElementById('monthYear').textContent = `${monthNames[month]} ${year}`;

    // Get first day of month and number of days
    const firstDay = new Date(year, month, 1).getDay();
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    const daysInPrevMonth = new Date(year, month, 0).getDate();

    // Get today's date for highlighting
    const today = new Date();
    const isCurrentMonth = month === today.getMonth() && year === today.getFullYear();
    const todayDate = today.getDate();

    const calendarGrid = document.getElementById('calendarGrid');
    calendarGrid.innerHTML = '';

    // Add day headers
    dayNames.forEach(day => {
        const dayHeader = document.createElement('div');
        dayHeader.className = 'calendar-day-header';
        dayHeader.textContent = day;
        calendarGrid.appendChild(dayHeader);
    });

    // Add empty cells for days before month starts
    for (let i = firstDay - 1; i >= 0; i--) {
        const dayCell = document.createElement('div');
        dayCell.className = 'calendar-day other-month';
        dayCell.textContent = daysInPrevMonth - i;
        calendarGrid.appendChild(dayCell);
    }

    // Add days of current month
    for (let day = 1; day <= daysInMonth; day++) {
        const dayCell = document.createElement('div');
        dayCell.className = 'calendar-day';
        dayCell.textContent = day;

        // Highlight today
        if (isCurrentMonth && day === todayDate) {
            dayCell.classList.add('today');
        }

        calendarGrid.appendChild(dayCell);
    }

    // Add days from next month to fill grid
    const totalCells = calendarGrid.children.length;
    const remainingCells = 42 - totalCells + 7; // 6 rows × 7 days + 7 headers

    for (let day = 1; day <= remainingCells; day++) {
        const dayCell = document.createElement('div');
        dayCell.className = 'calendar-day other-month';
        dayCell.textContent = day;
        calendarGrid.appendChild(dayCell);
    }
    const calendarId = document.getElementById('googleCalendarId').value;

    if (calendarId) {
        const events = await fetchGoogleCalendarEvents(month, year, calendarId);
        renderEvents(events);
    }
}

function previousMonth() {
    currentMonth--;
    if (currentMonth < 0) {
        currentMonth = 11;
        currentYear--;
    }
    generateCalendar(currentMonth, currentYear);
}

function nextMonth() {
    currentMonth++;
    if (currentMonth > 11) {
        currentMonth = 0;
        currentYear++;
    }
    generateCalendar(currentMonth, currentYear);
}

// Folder management functions
function openFolder(folderName) {
    const folder = document.getElementById(folderName + 'Folder');
    if (folder) {
        folder.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
}

function closeFolder(folderName) {
    const folder = document.getElementById(folderName + 'Folder');
    if (folder) {
        folder.classList.remove('active');
        document.body.style.overflow = 'auto';
    }
}

// Search functionality
document.getElementById('searchForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const searchEngine = document.getElementById('searchEngine').value;
    const searchQuery = document.getElementById('searchInput').value.trim();

    if (!searchQuery) return;

    const searchUrls = {
        brave: 'https://search.brave.com/search?q=',
        ecosia: 'https://www.ecosia.org/search?q=',
        wikipedia: 'https://en.wikipedia.org/wiki/Special:Search?search=',
        duckduckgo: 'https://duckduckgo.com/?q=',
        mojeek: 'https://www.mojeek.com/search?q=',
        github: 'https://github.com/search?q=',
        tineye: 'https://tineye.com/search?url='
    };

    const url = searchUrls[searchEngine] + encodeURIComponent(searchQuery);
    window.open(url, '_blank');

    document.getElementById('searchInput').value = '';
});

// Time and date display
function updateDateTime() {
    const now = new Date();

    const timeOptions = {
        hour: '2-digit',
        minute: '2-digit',
        hour12: true
    };

    const dateOptions = {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    };

    const timeElement = document.getElementById('currentTime');
    const dateElement = document.getElementById('currentDate');

    if (timeElement) timeElement.textContent = now.toLocaleTimeString('en-US', timeOptions);
    if (dateElement) dateElement.textContent = now.toLocaleDateString('en-US', dateOptions);
}

document.addEventListener('click', function(e) {
    if (e.target.classList.contains('folder-popup')) {
        const activeFolder = document.querySelector('.folder-popup.active');
        if (activeFolder) {
            activeFolder.classList.remove('active');
            document.body.style.overflow = 'auto';
        }
    }
});

document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        const activeFolder = document.querySelector('.folder-popup.active');
        if (activeFolder) {
            activeFolder.classList.remove('active');
            document.body.style.overflow = 'auto';
        }
    }
});

document.addEventListener('keydown', function(e) {
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        document.getElementById('searchInput').focus();
    }
});

// Theme and background functionality
document.getElementById('toggleTheme').addEventListener('click', function() {
    document.body.classList.toggle('dark-theme');
    localStorage.setItem('theme', document.body.classList.contains('dark-theme') ? 'dark' : 'light');
});

document.getElementById('toggleBackground').addEventListener('click', function() {
    if (document.body.style.backgroundImage) {
        document.body.style.backgroundImage = '';
        document.body.style.backgroundSize = '';
        document.body.style.backgroundPosition = '';
        localStorage.removeItem('apodBackground');
    } else {
        fetch('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')
            .then(response => response.json())
            .then(data => {
                if (data.url) {
                    document.body.style.backgroundImage = `url(${data.url})`;
                    document.body.style.backgroundSize = 'cover';
                    document.body.style.backgroundPosition = 'center';
                    localStorage.setItem('apodBackground', data.url);
                }
            })
            .catch(error => console.error('Error fetching APOD:', error));
    }
});

// Load saved theme and background
document.addEventListener('DOMContentLoaded', () => {
    if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark-theme');
    }
    const savedApod = localStorage.getItem('apodBackground');
    if (savedApod) {
        document.body.style.backgroundImage = `url(${savedApod})`;
        document.body.style.backgroundSize = 'cover';
        document.body.style.backgroundPosition = 'center';
    }
});
