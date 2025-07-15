# Browser MCP Agent 🌐

A powerful web browsing agent built with Streamlit, Puppeteer, and the Model Context Protocol (MCP) framework. This application allows you to interact with websites through natural language commands, enabling automated web browsing, data extraction, and multi-step web interactions.

## Features

- **Natural Language Commands**: Control web browsing using plain English
- **Real Browser Automation**: Uses Puppeteer for authentic browser interactions
- **Multi-step Tasks**: Execute complex browsing sequences
- **Screenshot Capabilities**: Capture specific page elements
- **Data Extraction**: Extract and summarize web content
- **Interactive UI**: Clean Streamlit interface for easy interaction

## Prerequisites

- Python 3.8 or higher
- Node.js and npm (for Puppeteer server)
- OpenAI API key

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd browser_mcp_agent
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Node.js dependencies**
   ```bash
   npm install -g @modelcontextprotocol/server-puppeteer
   ```

4. **Set up your OpenAI API key**
   
   Create a `mcp_agent.secrets.yaml` file in the project root:
   ```yaml
   openai:
     api_key: "your-openai-api-key-here"
   ```
   
   Or set it as an environment variable:
   ```bash
   export OPENAI_API_KEY="your-openai-api-key-here"
   ```

## Usage

1. **Start the application**
   ```bash
   streamlit run main.py
   ```

2. **Open your browser**
   Navigate to `http://localhost:8501`

3. **Enter your OpenAI API key** (if not set in environment)
   Use the sidebar to input your API key securely

4. **Start browsing!**
   Enter commands like:
   - "Go to wikipedia.org/wiki/computer_vision"
   - "Click on the link to object detection and take a screenshot"
   - "Scroll down to view more content"
   - "Navigate to wikipedia.org/wiki/computer_vision, scroll down, and report details"

## Example Commands

### Navigation
- `Go to wikipedia.org/wiki/computer_vision`
- `Navigate to google.com and search for "artificial intelligence"`

### Interactions
- `Click on the link to object detection and take a screenshot`
- `Scroll down to view more content`
- `Type "hello world" in the search box`

### Multi-step Tasks
- `Navigate to wikipedia.org/wiki/computer_vision, scroll down, and report details`
- `Scroll down and summarize the wikipedia page`
- `Go to amazon.com, search for "laptop", and show the first 3 results`

## Configuration

The application uses several configuration files:

### `mcp_agent.config.yaml`
Main configuration file for the MCP agent:
```yaml
execution_engine: asyncio
logger:
  transports: [console, file]
  level: debug
  progress_display: true
  path_settings:
    path_pattern: "logs/mcp-agent-{unique_id}.jsonl"
    unique_id: "timestamp"
    timestamp_format: "%Y%m%d_%H%M%S"

mcp:
  servers:
    puppeteer:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-puppeteer"]

openai:
  default_model: "gpt-4.1-mini-2025-04-14"
```

### `mcp_agent.secrets.yaml`
Store your API keys securely (create this file):
```yaml
openai:
  api_key: "your-openai-api-key-here"
```

## Project Structure

```
browser_mcp_agent/
├── main.py                 # Main Streamlit application
├── mcp_agent.config.yaml  # MCP agent configuration
├── requirements.txt        # Python dependencies
├── mcp_agent.secrets.yaml # API keys (create this)
├── logs/                  # Application logs
└── README.md             # This file
```

## Dependencies

### Python Packages
- `streamlit>=1.28.0` - Web application framework
- `mcp-agent>=0.0.14` - Model Context Protocol agent framework
- `openai>=1.0.0` - OpenAI API client
- `asyncio>=3.4.3` - Asynchronous I/O support

### Node.js Packages
- `@modelcontextprotocol/server-puppeteer` - Puppeteer MCP server

## How It Works

1. **User Input**: Commands are entered through the Streamlit interface
2. **Agent Processing**: The MCP agent processes natural language commands
3. **Browser Control**: Puppeteer executes browser actions (navigation, clicking, scrolling)
4. **LLM Integration**: OpenAI's language model interprets commands and generates responses
5. **Result Display**: Results are displayed back in the Streamlit interface

## Troubleshooting

### Common Issues

1. **"OPENAI_API_KEY is not set"**
   - Ensure your API key is set in `mcp_agent.secrets.yaml` or environment variables

2. **"module 'streamlit' has no attribute 'session'"**
   - This is a code issue that has been fixed in the latest version

3. **"Agent object has no attribute 'get_tools'"**
   - The method name is `list_tools()`, not `get_tools()`

4. **Puppeteer server not starting**
   - Ensure Node.js and npm are installed
   - Run `npm install -g @modelcontextprotocol/server-puppeteer`

### Logs
Check the `logs/` directory for detailed application logs that can help diagnose issues.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/) for the web interface
- Powered by [Puppeteer](https://pptr.dev/) for browser automation
- Uses the [Model Context Protocol](https://modelcontextprotocol.io/) framework
- Leverages [OpenAI](https://openai.com/) for natural language processing

---

**Note**: This agent uses Puppeteer to control a real browser, providing authentic web interactions and accurate data extraction. 