# Threads Fact Checker Bot

A Threads bot that monitors specified Threads handles and provides fact-checking responses using LLM models.

## Features

- Monitors specified Threads handles for new posts
- Uses Hugging Face models for fact-checking
- Automatically replies with fact-check responses
- Configurable monitoring intervals
- Docker support for easy deployment

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a .env file with your API keys:
```env
THREADS_API_KEY=your_threads_api_key
OPENAI_API_KEY=your_openai_api_key
```

3. Configure the bot in `config/config.py`:
- Add target Threads handles
- Adjust ping interval
- Select LLM model
- Customize prompt template
- Set token lengths

## Running the Bot

### Using Python directly:
```bash
python main.py
```

### Using Docker:
```bash
# Build the image
docker build -t threads-fact-checker .

# Run the container
docker run -d --env-file .env threads-fact-checker
```

## Project Structure

```
threads-fact-checker/
├── config/
│   └── config.py         # Configuration classes
├── services/
│   ├── llm_service.py    # LLM integration
│   └── threads_service.py # Threads API integration
├── main.py               # Main application
├── Dockerfile            # Docker configuration
├── requirements.txt      # Python dependencies
└── .env                 # API keys (create this)
