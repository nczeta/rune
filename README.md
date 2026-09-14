# RUNE

**RUNE — Requests & Utilities for Network Endpoints**

RUNE is a lightweight AI agent built in Python that combines an LLM with a collection of external tools.

Instead of only generating text, RUNE can decide when to call a tool, execute it, receive the result, and use that result to continue the conversation.

The current version integrates tools for:

* **LLM inference** through Groq
* **GitHub** — repositories, users, followers and following
* **Web search and page fetching** through Tavily
* **Google Maps** place search
* **Weather forecasts** through Open-Meteo

The project is designed around a simple tool-calling loop:

```text
User
 ↓
RUNE
 ↓
LLM
 ↓
Tool call?
 ├── No → Response
 │
 └── Yes
       ↓
   Execute tool
       ↓
   Tool result
       ↓
      LLM
       ↓
    Response
```

---

## Requirements

* Python **3.13+**
* A Groq API key
* A Tavily API key
* A MAPS API key
* The dependencies listed in `requirements.txt`

---

## API Keys & Login

Before running RUNE, create the required credentials.

### Groq

RUNE uses Groq for LLM inference.

Create an API key from the **Groq Console**:

[Groq API Keys](https://console.groq.com/keys)

Set the key in your `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Groq recommends keeping API keys outside the source code and loading them through environment variables.

### Tavily

Tavily is used for web search and page fetching.

Create an account and generate an API key from the Tavily dashboard:

[Tavily](https://app.tavily.com/)

Add it to `.env`:

```env
TAVILY_API_KEY=your_tavily_api_key
```

Tavily currently provides a free monthly allowance for new accounts.

### MAPS

RUNE uses the MAPS API for maps-related tools.

Create a **Personal Access Token**, preferably a fine-grained token with only the permissions required by the project:

[Google Maps](https://mapsplatform.google.com/maps-demo-key/)

Then add it to `.env`:

```env
MAPS_API_KEY=your_github_token
```

GitHub recommends fine-grained tokens when possible because their permissions can be restricted to specific repositories and capabilities.

> **Never commit your `.env` file or expose your API keys.**
>
> Make sure `.env` is included in `.gitignore`.

---

## Installation

Clone the repository and enter the project directory:

```bash
git clone <repository-url>
cd RUNE
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
MAPS_API_KEY=your_maps_api_key
```
Check out the env.example.txt to see if you created the .env file correctly.

---

## Quick Start

Once everything is configured, start the FastAPI backend with Uvicorn:

```bash
uvicorn backend.api:app --reload
```

The `--reload` option automatically reloads the server when Python files are modified during development.

After starting the server, open the address shown by Uvicorn in your browser, usually:

```text
http://127.0.0.1:8000
```

RUNE's frontend is served by the FastAPI backend.

### Using RUNE

Once the interface is open:

1. Write a request in the chat.
2. RUNE sends the conversation to the LLM.
3. The model determines whether a tool is necessary.
4. If a tool is requested, RUNE executes the corresponding Python function.
5. The tool result is added back to the conversation.
6. The LLM receives the result and generates the final response.

For example:

```text
You:
What's the weather in Verona tomorrow?

RUNE:
→ calls the weather tool
→ receives the forecast
→ generates the answer
```

Or:

```text
You:
Find the repositories of a GitHub user.

RUNE:
→ calls the GitHub tool
→ receives the repository data
→ summarizes the results
```

---

## Project Structure

The main components of the project are:

### `agent.py`

Contains the FastAPI application and the main agent logic.

It manages the conversation, communicates with the LLM and handles the tool-calling loop.

### `tools.py`

Contains the actual Python implementations of RUNE's tools.

### `descriptions.py`

Contains the schemas and descriptions provided to the LLM so that it knows which tools are available and how to call them.

### `frontend/`

Contains RUNE's web interface.

---

## Security

API keys are loaded through environment variables and should never be hard-coded into the source code.

Do not commit:

```text
.env
```

to GitHub.

If a credential is accidentally exposed, revoke it immediately and generate a new one.

---

A more detailed explanation of the architecture and implementation will be provided separately in the project report.
