// Storage keys
const STORAGE_KEYS = {
    START_DATE: 'challenge_start_date',
    COMPLETED_DAYS: 'completed_days'
};

// State
let startDate = null;
let completedDays = new Set();
let currentFilter = 'all';

// DOM Elements
const welcomeScreen = document.getElementById('welcomeScreen');
const cardsGrid = document.getElementById('cardsGrid');
const startButton = document.getElementById('startButton');
const startChallengeButton = document.getElementById('startChallengeButton');
const resetButton = document.getElementById('resetButton');
const progressFill = document.getElementById('progressFill');
const progressText = document.getElementById('progressText');
const filterButtons = document.querySelectorAll('.filter-btn');

// Initialize app
function init() {
    loadState();
    setupEventListeners();
    render();
}

// Load state from localStorage
function loadState() {
    const savedStartDate = localStorage.getItem(STORAGE_KEYS.START_DATE);
    const savedCompletedDays = localStorage.getItem(STORAGE_KEYS.COMPLETED_DAYS);

    if (savedStartDate) {
        startDate = new Date(savedStartDate);
    }

    if (savedCompletedDays) {
        completedDays = new Set(JSON.parse(savedCompletedDays));
    }
}

// Save state to localStorage
function saveState() {
    if (startDate) {
        localStorage.setItem(STORAGE_KEYS.START_DATE, startDate.toISOString());
    }
    localStorage.setItem(STORAGE_KEYS.COMPLETED_DAYS, JSON.stringify([...completedDays]));
}

// Setup event listeners
function setupEventListeners() {
    startButton.addEventListener('click', startChallenge);
    startChallengeButton.addEventListener('click', startChallenge);
    resetButton.addEventListener('click', resetChallenge);

    filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            filterButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            currentFilter = btn.dataset.filter;
            renderCards();
        });
    });
}

// Start challenge
function startChallenge() {
    if (!startDate) {
        startDate = new Date();
        saveState();
    }
    render();
}

// Reset challenge
function resetChallenge() {
    if (confirm('Are you sure you want to reset your progress? This cannot be undone.')) {
        startDate = null;
        completedDays.clear();
        localStorage.removeItem(STORAGE_KEYS.START_DATE);
        localStorage.removeItem(STORAGE_KEYS.COMPLETED_DAYS);
        render();
    }
}

// Calculate days elapsed since start
function getDaysElapsed() {
    if (!startDate) return 0;
    const now = new Date();
    const diffTime = Math.abs(now - startDate);
    const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
    return diffDays + 1; // Day 1 starts on day 0
}

// Check if a day is unlocked
function isDayUnlocked(dayNumber) {
    if (!startDate) return false;
    return dayNumber <= getDaysElapsed();
}

// Get time until unlock
function getTimeUntilUnlock(dayNumber) {
    if (!startDate || dayNumber <= 1) return null;

    const daysToWait = dayNumber - getDaysElapsed();
    if (daysToWait <= 0) return null;

    const unlockDate = new Date(startDate);
    unlockDate.setDate(unlockDate.getDate() + (dayNumber - 1));

    const now = new Date();
    const diffTime = unlockDate - now;

    const hours = Math.floor(diffTime / (1000 * 60 * 60));
    const minutes = Math.floor((diffTime % (1000 * 60 * 60)) / (1000 * 60));

    if (hours > 24) {
        const days = Math.floor(hours / 24);
        return `Unlocks in ${days} day${days > 1 ? 's' : ''}`;
    }

    return `Unlocks in ${hours}h ${minutes}m`;
}

// Toggle day completion
function toggleDayCompletion(dayNumber, event) {
    event.stopPropagation();

    if (!isDayUnlocked(dayNumber)) return;

    if (completedDays.has(dayNumber)) {
        completedDays.delete(dayNumber);
    } else {
        completedDays.add(dayNumber);
    }

    saveState();
    updateProgress();
    renderCards();
}

// Update progress bar
function updateProgress() {
    const completed = completedDays.size;
    const percentage = (completed / 100) * 100;

    progressFill.style.width = `${percentage}%`;
    progressText.textContent = `${completed} / 100 days completed`;
}

// Create card HTML
function createCard(prompt) {
    const unlocked = isDayUnlocked(prompt.day);
    const completed = completedDays.has(prompt.day);
    const timeUntilUnlock = getTimeUntilUnlock(prompt.day);

    let cardClasses = ['card'];
    if (unlocked) cardClasses.push('unlocked');
    if (!unlocked) cardClasses.push('locked');
    if (completed) cardClasses.push('completed');

    // Apply filter
    if (currentFilter !== 'all') {
        if (currentFilter === 'unlocked' && !unlocked) return '';
        if (currentFilter === 'locked' && unlocked) return '';
        if (currentFilter === 'completed' && !completed) return '';
    }

    const statusEmoji = completed ? '✅' : unlocked ? '🔓' : '🔒';

    return `
        <div class="${cardClasses.join(' ')}" data-day="${prompt.day}">
            <div class="card-content">
                <div class="card-header">
                    <span class="day-number">Day ${prompt.day}</span>
                    <span class="card-status">${statusEmoji}</span>
                </div>
                <h3 class="card-title">${prompt.title}</h3>
                <p class="card-prompt">${unlocked ? prompt.prompt : 'This challenge will unlock soon...'}</p>
                ${!unlocked && timeUntilUnlock ? `<div class="unlock-time">${timeUntilUnlock}</div>` : ''}
                ${unlocked ? `
                    <div class="checkbox-container">
                        <input
                            type="checkbox"
                            class="checkbox"
                            id="check-${prompt.day}"
                            ${completed ? 'checked' : ''}
                            data-day="${prompt.day}"
                        >
                        <label class="checkbox-label" for="check-${prompt.day}">Mark as completed</label>
                    </div>
                ` : ''}
            </div>
        </div>
    `;
}

// Render cards
function renderCards() {
    const cardsHTML = prompts.map(prompt => createCard(prompt)).join('');
    cardsGrid.innerHTML = cardsHTML;

    // Add event listeners to checkboxes
    document.querySelectorAll('.checkbox').forEach(checkbox => {
        checkbox.addEventListener('change', (e) => {
            const dayNumber = parseInt(e.target.dataset.day);
            toggleDayCompletion(dayNumber, e);
        });
    });
}

// Main render function
function render() {
    if (!startDate) {
        welcomeScreen.classList.remove('hidden');
        cardsGrid.innerHTML = '';
        startButton.style.display = 'inline-block';
        resetButton.style.display = 'none';
    } else {
        welcomeScreen.classList.add('hidden');
        startButton.style.display = 'none';
        resetButton.style.display = 'inline-block';
        updateProgress();
        renderCards();

        // Update unlock times every minute
        setInterval(() => {
            renderCards();
        }, 60000);
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', init);
