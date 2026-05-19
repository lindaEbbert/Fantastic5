# Fantastic 5

Fantastic 5 is a tool developed by **Five Fact Foundry** that helps users discover fascinating facts about any topic. It leverages the Wikipedia API to find relevant articles and uses OpenAI's GPT models to extract and present five "mind-blowing" facts.

## Overview

The application follows a simple workflow:
1. User provides a topic.
2. The app searches Wikipedia for related articles.
3. User selects a specific article.
4. The app generates subtopics using AI.
5. User selects or provides a subtopic.
6. The app presents the **Fantastic 5** facts about the selected topic and subtopic.

## Requirements

- Python 3.10+
- OpenAI API Key

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Fantastic5
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configuration**:
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key:
     ```env
     OPENAI_API_KEY=your_api_key_here
     ```
   - Alternatively, you can use `api_key.txt` (though `.env` is preferred).

## Usage

Run the main application:
```bash
python main.py
```
Follow the interactive prompts in the terminal to explore your favorite topics.

## Project Structure

```text
Fantastic5/
├── main.py              # Entry point of the application
├── models/
│   ├── __init__.py
│   ├── openai_api.py    # OpenAI API integration and Pydantic models
│   └── wiki.py          # Wikipedia API integration
├── requirements.txt     # Project dependencies
├── .env                 # Environment variables (not tracked by git)
└── api_key.txt          # Alternative API key storage
```

## Scripts

- `main.py`: The primary entry point for the interactive CLI tool.
- `models/wiki.py`: Can be run standalone for a quick Wikipedia search test.
- `models/openai_api.py`: Can be run standalone for testing the OpenAI integration.

## Env Vars

| Variable | Description |
|----------|-------------|
| `OPENAI_API_KEY` | Required for generating facts and subtopics via OpenAI. |

## Tests

- TODO: Implement a formal testing suite (e.g., using `pytest`).
- Currently, manual testing can be performed by running individual module files.

## License

- TODO: Add license information.

---
**Developed by:** Günter, Linda, Marcel & Thorsten - *Five Fact Foundry*
