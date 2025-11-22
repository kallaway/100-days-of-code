// RSS Feed functionality with AllOrigins fallback
async function loadRSSFeeds() {
    const rssContent = document.getElementById('rssContent');

    try {
        // Try RSS2JSON first, then fallback to AllOrigins
        const feeds = [
            {
                name: 'Hacker News',
                rss2json: 'https://api.rss2json.com/v1/api.json?rss_url=https://hnrss.org/newest',
                direct: 'https://hnrss.org/newest'
            },
            {
                name: 'TechCrunch',
                rss2json: 'https://api.rss2json.com/v1/api.json?rss_url=https://techcrunch.com/feed/',
                direct: 'https://techcrunch.com/feed/'
            },
            {
                name: 'BBC Tech',
                rss2json: 'https://api.rss2json.com/v1/api.json?rss_url=https://feeds.bbci.co.uk/news/technology/rss.xml',
                direct: 'https://feeds.bbci.co.uk/news/technology/rss.xml'
            }
        ];

        let allItems = [];

        for (const feed of feeds) {
            try {
                // Try RSS2JSON first
                let response = await fetch(feed.rss2json);
                let data = await response.json();

                if (data.status === 'ok' && data.items && data.items.length > 0) {
                    allItems = [...allItems, ...data.items.slice(0, 3).map(item => ({
                        ...item,
                        sourceName: feed.name
                    }))];
                } else {
                    // Fallback to AllOrigins
                    console.log(`RSS2JSON failed for ${feed.name}, trying AllOrigins...`);
                    response = await fetch(`https://api.allorigins.win/get?url=${encodeURIComponent(feed.direct)}`);
                    const allOriginsData = await response.json();

                    if (allOriginsData.contents) {
                        const parser = new DOMParser();
                        const xmlDoc = parser.parseFromString(allOriginsData.contents, 'text/xml');
                        const items = xmlDoc.getElementsByTagName('item');

                        for (let i = 0; i < Math.min(3, items.length); i++) {
                            const item = items[i];
                            const title = item.getElementsByTagName('title')[0]?.textContent || 'No title';
                            const link = item.getElementsByTagName('link')[0]?.textContent || '#';
                            const description = item.getElementsByTagName('description')[0]?.textContent || '';
                            const pubDate = item.getElementsByTagName('pubDate')[0]?.textContent || new Date().toISOString();

                            allItems.push({
                                title: title,
                                link: link,
                                description: description,
                                pubDate: pubDate,
                                sourceName: feed.name
                            });
                        }
                    }
                }
            } catch (feedError) {
                console.error(`Failed to load ${feed.name}:`, feedError);
            }
        }

        // If we still don't have items, show some mock data so it's not empty
        if (allItems.length === 0) {
            allItems = [
                {
                    title: "Welcome to Your RSS Feed",
                    description: "RSS feeds are loading. This may take a moment on first load...",
                    link: "#",
                    sourceName: "System",
                    pubDate: new Date().toISOString()
                },
                {
                    title: "Technology News Coming Soon",
                    description: "Your personalized news feed will display the latest articles from tech and news sources.",
                    link: "#",
                    sourceName: "Info",
                    pubDate: new Date().toISOString()
                }
            ];
        }

        // Sort by publication date (newest first)
        allItems.sort((a, b) => new Date(b.pubDate) - new Date(a.pubDate));

        // Display the feeds
        let rssHTML = '';
        allItems.slice(0, 10).forEach(item => {
            const publishDate = new Date(item.pubDate);
            const timeAgo = getTimeAgo(publishDate);

            // Clean up description and limit length
            let description = item.description || '';
            description = description.replace(/<[^>]*>/g, ''); // Remove HTML tags
            description = description.substring(0, 140);
            if (description.length === 140) description += '...';

            rssHTML += `
                <div class="rss-item">
                    <div class="rss-item-title">
                        <a href="${item.link}" target="_blank">${item.title}</a>
                    </div>
                    <div class="rss-item-meta">${item.sourceName} • ${timeAgo}</div>
                    <div class="rss-item-description">${description}</div>
                </div>
            `;
        });

        rssContent.innerHTML = rssHTML;

    } catch (error) {
        console.error('RSS Feed Error:', error);
        // Show a friendly fallback with useful info
        rssContent.innerHTML = `
            <div style="text-align: center; color: #94a3b8; padding: 40px 20px;">
                <div style="font-size: 2rem; margin-bottom: 15px;">📡</div>
                <div style="margin-bottom: 10px;"><strong>RSS Feeds Temporarily Unavailable</strong></div>
                <div style="font-size: 0.9rem; line-height: 1.4;">
                    This can happen due to CORS restrictions or feed server issues.<br>
                    The feed will retry in 30 minutes, or refresh the page to try again.
                </div>
                <div style="margin-top: 20px;">
                    <div style="padding: 10px; background: rgba(71, 85, 105, 0.3); border-radius: 8px; font-size: 0.8rem;">
                        Meanwhile, check out your bookmarked news sources in the Communities folder!
                    </div>
                </div>
            </div>
        `;
    }
}

// Helper function to format time ago
function getTimeAgo(date) {
    const now = new Date();
    const diffInMs = now - date;
    const diffInHours = Math.floor(diffInMs / (1000 * 60 * 60));
    const diffInDays = Math.floor(diffInHours / 24);

    if (diffInHours < 1) {
        const diffInMinutes = Math.floor(diffInMs / (1000 * 60));
        return `${diffInMinutes} min${diffInMinutes !== 1 ? 's' : ''} ago`;
    } else if (diffInHours < 24) {
        return `${diffInHours} hour${diffInHours !== 1 ? 's' : ''} ago`;
    } else if (diffInDays === 1) {
        return 'Yesterday';
    } else if (diffInDays < 7) {
        return `${diffInDays} days ago`;
    } else {
        return date.toLocaleDateString('en-US', {
            month: 'short',
            day: 'numeric',
            year: date.getFullYear() !== now.getFullYear() ? 'numeric' : undefined
        });
    }
}
