document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('summarizeButton').addEventListener('click', function() {
        // Add shimmer effect while summarizing
        var summaryElement = document.getElementById('summary');
        summaryElement.classList.add('shimmer');

        // Change text to "Summarizing..."
        summaryElement.textContent = 'Summarizing...';

        // Change text color to grey
        summaryElement.style.color = '#888';

        chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
            var tab = tabs[0];
            chrome.runtime.sendMessage({ url: tab.url }, function(response) {
                // Remove shimmer effect
                summaryElement.classList.remove('shimmer');

                if (response && response.summarized_text) {
                    // Update summary with response
                    summaryElement.textContent = response.summarized_text;
                    // Change text color back to default
                    summaryElement.style.color = 'black';
                    // Show paste icon
                    var pasteIcon = document.querySelector('.paste-icon');
                    pasteIcon.style.display = 'inline-block';

                    // Add click event listener to paste icon
                    pasteIcon.addEventListener('click', function() {
                        // Copy summarized text to clipboard
                        navigator.clipboard.writeText(response.summarized_text)
                            .then(function() {
                                console.log('Summarized text copied to clipboard successfully');
                                // Change icon to tick icon
                                pasteIcon.src = 'tick.png'; // Replace with the path to your tick icon
                            })
                            .catch(function(error) {
                                console.error('Error copying summarized text to clipboard:', error);
                                // Optionally, provide feedback to the user about the error
                                // For example: alert('Error copying summarized text to clipboard');
                            });
                    });
                } else if (response && response.error) {
                    // Display error message if there's an error
                    summaryElement.textContent = 'Error: ' + response.error;
                } else {
                    // Handle no response case
                    summaryElement.textContent = 'Error: No response from server';
                }
            });
        });
    });
});
