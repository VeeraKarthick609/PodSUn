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
            sendResponse({ summarized_text: data.summarized_text });
        })
        .catch(error => {
            console.error('Error:', error);
        });
        return true;
    }
});
