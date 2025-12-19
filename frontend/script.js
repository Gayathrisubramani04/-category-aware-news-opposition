const analyzeBtn = document.getElementById('analyzeBtn');
const inputText = document.getElementById('inputText');
const status = document.getElementById('status');
const results = document.getElementById('results');
const errorBox = document.getElementById('error');

const categoryEl = document.getElementById('category');
const sentimentEl = document.getElementById('sentiment');
const oppositionEl = document.getElementById('opposition');
const disclaimerEl = document.getElementById('disclaimer');

function showError(msg) {
  errorBox.textContent = msg;
  errorBox.classList.remove('hidden');
  results.classList.add('hidden');
}

function clearError() {
  errorBox.textContent = '';
  errorBox.classList.add('hidden');
}

function showStatus(msg) {
  status.textContent = msg;
}

function showResults(payload) {
  categoryEl.textContent = payload.category || '-';
  sentimentEl.textContent = `${payload.sentiment.label} (${payload.sentiment.score})`;
  oppositionEl.textContent = payload.opposition_view || '-';
  disclaimerEl.textContent = payload.disclaimer || '-';
  results.classList.remove('hidden');
}

analyzeBtn.addEventListener('click', async () => {
  clearError();
  showStatus('');

  const text = inputText.value.trim();
  if (!text) {
    showError('Please enter some text to analyze.');
    return;
  }
  if (text.length < 10) {
    showError('Input must be at least 10 characters.');
    return;
  }
  if (text.length > 5000) {
    showError('Input exceeds maximum length of 5000 characters.');
    return;
  }

  analyzeBtn.disabled = true;
  showStatus('Analyzing...');

  try {
    const resp = await fetch('http://127.0.0.1:5000/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text })
    });

    if (!resp.ok) {
      const body = await resp.json().catch(() => null);
      const msg = body && body.error ? body.error : `Server returned ${resp.status}`;
      showError(msg);
      showStatus('');
      analyzeBtn.disabled = false;
      return;
    }

    const data = await resp.json();
    showResults(data);
    showStatus('Done');
  } catch (err) {
    showError('Network error: ' + err.message);
  } finally {
    analyzeBtn.disabled = false;
  }
});
