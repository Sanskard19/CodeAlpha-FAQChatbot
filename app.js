const chatForm = document.getElementById('chat-form');
const questionInput = document.getElementById('question-input');
const chatBox = document.getElementById('chat-box');
const relatedBox = document.getElementById('related-box');
const relatedList = document.getElementById('related-list');

function appendMessage(text, sender) {
  const message = document.createElement('div');
  message.className = `message ${sender}`;

  const bubble = document.createElement('div');
  bubble.className = 'bubble';
  bubble.textContent = text;

  message.appendChild(bubble);
  chatBox.appendChild(message);
  chatBox.scrollTop = chatBox.scrollHeight;
}

chatForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  const question = questionInput.value.trim();
  if (!question) return;

  appendMessage(question, 'user');
  questionInput.value = '';

  try {
    const response = await fetch('/api/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question })
    });

    const data = await response.json();
    if (!response.ok) {
      appendMessage(data.error || 'Something went wrong.', 'bot');
      return;
    }

    appendMessage(`${data.answer} (confidence: ${data.score.toFixed(3)})`, 'bot');

    relatedList.innerHTML = '';
    if (data.related && data.related.length > 0) {
      data.related.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.question} (${item.score.toFixed(3)})`;
        relatedList.appendChild(li);
      });
      relatedBox.classList.remove('hidden');
    } else {
      relatedBox.classList.add('hidden');
    }
  } catch (error) {
    appendMessage('Unable to reach the server. Please make sure Flask is running.', 'bot');
  }
});
