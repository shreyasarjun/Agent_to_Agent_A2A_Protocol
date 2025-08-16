# Travel Planner Agent System

## Overview
The Travel Planner Agent System is a modular and intelligent framework designed to assist users in planning their trips. It leverages multiple agents to provide weather forecasts, search recommendations, and local language model (LLM) insights. The system is built using Python and integrates with external APIs and resources to deliver accurate and personalized results.

## Architecture
The system consists of the following components:

### 1. **Travel Planner Agent Server**
The central server that coordinates requests and responses between various agents. It processes user input and delegates tasks to the appropriate agents.

### 2. **Weather Agent**
- **Purpose**: Provides weather information for a specified location.
- **Integration**: Uses the OpenWeather API to fetch real-time weather data.
- **Endpoint**: `http://localhost:8001`

### 3. **Tavily Search Agent**
- **Purpose**: Performs internet searches using the Tavily Search API.
- **Integration**: Fetches top search results based on user queries.
- **Endpoint**: `http://localhost:8002`

### 4. **Local LLM Agent**
- **Purpose**: Processes complex queries and generates insights using a local language model.
- **Integration**: Utilizes the Ollama LLM (Llama 3.2).
- **Endpoint**: `http://localhost:5001`

### External Resources
- **OpenWeather API**: Provides weather data.
- **Tavily Search API**: Delivers search results.

## Workflow
1. **User Input**: The user provides natural language input specifying their travel destination and dates.
2. **Weather Agent**: Fetches the weather forecast for the destination.
3. **Tavily Search Agent**: Suggests activities based on the weather conditions.
4. **Local LLM Agent**: Summarizes the plan and provides additional recommendations.

## Installation
### Prerequisites
- Python 3.12 or higher
- Virtual environment (recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd A2A
   ```
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add the following keys:
     ```env
     OPENWEATHER_API_KEY=<your_openweather_api_key>
     TAVILY_API_KEY=<your_tavily_api_key>
     ```

## Usage
1. Start the agents:
   - **Weather Agent**:
     ```bash
     python WeatherAgent.py
     ```
   - **Tavily Search Agent**:
     ```bash
     python TavilySearchAgent.py
     ```
   - **Local LLM Agent**:
     ```bash
     python local_llm.py
     ```
   - **Travel Planner Agent**:
     ```bash
     python Travel_Planner_Agent.py
     ```
2. Provide natural language input when prompted, e.g., "Plan a trip to Paris from June 21-25."

## Example Output
```
Available Agents:
- weather: Provides weather information
- search: Performs internet search using Tavily Search API

Weather forecast: The weather in Paris is clear sky with a temperature of 80.74°F.
Prompt: You are a travel assistant. Based on the weather forecast result The weather in Paris is clear sky with a temperature of 80.74°F. and the recommendations [Top results for 'Recommend outdoor activities in Paris':
- Eiffel Tower: https://eiffel.com
- Seine River Cruise: https://seinecruise.com], suggest me a few must-see attractions on date June 21-25.
LLM response: Visit the Eiffel Tower, enjoy a Seine River Cruise, and explore Montmartre.
```

## Diagram
![Architecture Diagram](./architecture_diagram.png)

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## References
- [Google Agent-to-Agent (A2A) Protocol Explained](https://medium.com/@shamim_ru/google-agent-to-agent-a2a-protocol-explained-with-real-working-examples-99e362b61ba8)

## Contact
For any questions or support, please contact [your-email@example.com].
