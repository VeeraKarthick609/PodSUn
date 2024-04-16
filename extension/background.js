// Background script (background.js)

// Listen for messages from the content script
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.url) {
        fetch('http://localhost:5000/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: request.url })
        })
        .then(response => response.json())
        .then(data => {
            // Send the summarized text back to the content script
            sendResponse({ summarized_text: data.summarized_text });
        })
        .catch(error => {
            console.error('Error:', error);
            // Send an error message back to the content script
            sendResponse({ error: 'An error occurred while fetching data' });
        });
        
        // Keep the message channel open until `sendResponse` is called
        return true;
    }
});

// Keep the background script running
chrome.runtime.onInstalled.addListener(function() {
    // This event listener is just to keep the background script running
    // It doesn't need to do anything
});