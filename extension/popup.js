document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('summarizeButton').addEventListener('click', function() {
        // Add shimmer effect while loading
        document.getElementById('summary').classList.add('shimmer');

        chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
            var tab = tabs[0];
            chrome.runtime.sendMessage({url: tab.url}, function(response) {
                // Remove shimmer effect
                document.getElementById('summary').classList.remove('shimmer');

                // Update summary with response
                document.getElementById('summary').textContent = response.summarized_text;
            });
        });
    });
});
