document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('summarizeButton').addEventListener('click', function() {
        // Add shimmer effect while summarizing
        document.getElementById('summary').classList.add('shimmer');

        // Change text to "Summarizing..."
        document.getElementById('summary').textContent = 'Summarizing...';

        // Change text color to grey
        document.getElementById('summary').style.color = '#888';

        chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
            var tab = tabs[0];
            chrome.runtime.sendMessage({ url: tab.url }, function(response) {
                // Remove shimmer effect
                document.getElementById('summary').classList.remove('shimmer');

                if (response && response.summarized_text) {
                    // Update summary with response
                    document.getElementById('summary').textContent = response.summarized_text;
                    // Change text color back to default
                    document.getElementById('summary').style.color = 'black';
                } else if (response && response.error) {
                    // Display error message if there's an error
                    document.getElementById('summary').textContent = 'Error: ' + response.error;
                } else {
                    // Handle no response case
                    document.getElementById('summary').textContent = 'Error: No response from server';
                }
            });
        });
    });
});
