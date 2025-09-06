# Chatbot LangChain Project

## Overview
This project implements a chatbot using [LangChain](https://langchain.dev/), enabling advanced conversational AI capabilities.

## Features
- Natural language understanding
- Context-aware responses
- Extensible architecture

## Installation

```bash
git clone https://github.com/yourusername/chatbot_langchain_proj.git
cd chatbot_langchain_proj
pip install -r requirements.txt
```

## Usage

```bash
python app.py
```

Create a `.env` file and add your OpenAI API key as `OPENAI_API_KEY=your-key-here`.  
This ensures your credentials are kept secure and not hard-coded in the source files.

## Running with Ollama

To use Ollama for local model inference, run:

```cmd
ollama run <model_name>
```

Replace `<model_name>` with your desired model (e.g., `llama2`, `mistral`, etc.).

## Configuration
Edit `config.py` to customize model parameters and data sources.

## Contributing
Pull requests are welcome. For major changes, open an issue first.

## License
[MIT](LICENSE)

## References
- [LangChain Documentation](https://langchain.dev/)
- [OpenAI API](https://platform.openai.com/docs/)

