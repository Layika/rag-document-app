The Flow:

    FastAPI receives a request at /chat.
    FastAPI creates a ChatRequest object from the incoming JSON.
    Your code sends that message to OpenAI using the client.
    OpenAI sends back a giant object; you "dig" through it to find the text.
    FastAPI packages your return dictionary into JSON for the user.

    from llama_index.llms.google_genai import GoogleGenAI