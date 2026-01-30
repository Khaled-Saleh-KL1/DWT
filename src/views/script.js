// Helper functions to get/set values
const v = (id) => document.getElementById(id).value;
const val = (id, txt) => document.getElementById(id).value = txt;
const out = (id, txt) => document.getElementById(id).textContent = txt;

/**
 * Generic function to send POST requests
 */
async function post(url, body) {
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(body)
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        return await response.json();
    } catch (error) {
        console.error("Fetch error:", error);
        return { error: error.message };
    }
}

/**
 * Button Handler: Add Context
 */
async function addContext() {
    const content = v('ctx');
    if (!content) {
        alert("Please enter some context text first.");
        return;
    }

    // specific UI feedback could go here
    const res = await post('/add-data', { content: content });

    if (res.error) {
        alert("Failed to add data: " + res.error);
    } else {
        alert(res.message || "Context added successfully!");
    }
}

/**
 * Button Handler: Clear Context
 */
async function clearContext() {
    // Send empty content to clear the store
    const res = await post('/add-data', { content: '' });

    if (res.error) {
        alert("Failed to clear context: " + res.error);
    } else {
        val('ctx', ''); // Clear the text box
        alert("Context cleared!");
    }
}

/**
 * Button Handler: Ask Question
 */
async function ask() {
    const question = v('q');
    if (!question) return;

    out('ans', "Thinking...");

    const res = await post('/ask', { question: question });

    if (res.error) {
        out('ans', "Error: " + res.error);
    } else {
        out('ans', res.answer);
    }
}

/**
 * Button Handler: Extract Identity
 */
async function extract() {
    const base64 = v('b64');
    if (!base64) {
        alert("Please paste a Base64 string.");
        return;
    }

    out('json', "Extracting...");

    const res = await post('/extract', { base64_image: base64 });

    // Format JSON for display
    out('json', JSON.stringify(res, null, 2));
}
