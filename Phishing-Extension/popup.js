document.getElementById('scan').addEventListener('click', () => {
    chrome.tabs.query({ active: true, currentWindow: true }, tabs => {
      chrome.scripting.executeScript({
        target: { tabId: tabs[0].id },
        function: () => {
          alert("Scanned all links. Suspicious links are highlighted in red.");
        }
      });
    });
  });