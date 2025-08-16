from python_a2a import A2AServer, skill, agent, run_server, TaskStatus, TaskState
from tavily import TavilyClient
import os
import requests
import logging

@agent(
    name="Tavily Search Agent",
    description="Performs internet search using Tavily Search API",
    version="1.0.0",
    url="https://yourdomain.com"
)
class TavilySearchAgent(A2AServer):
    @skill(
        name="Search Internet",
        description="Perform a web search using Tavily Search API",
        tags=["search", "internet", "tavily"],
        examples="Search 'best programming tutorials'"
    )
    def search(self, query: str):
        """Perform search using Tavily Search API"""
        api_key = os.getenv("TAVILY_API_KEY")
        if not api_key:
            return "Search service not available (missing Tavily API key)."

        try:
            tavily_client = TavilyClient(api_key=api_key)
            response = tavily_client.search(query)
            return response

        except Exception as e:
            logging.error(f"Error during Tavily search: {e}")
            return f"Search failed: {e}"

    def handle_task(self, task):
        message_data = task.message or {}
        content = message_data.get("content", {})
        text = content.get("text", "") if isinstance(content, dict) else ""

        if text.strip():
            query = text.strip()
            result = self.search(query)
            task.artifacts = [{
                "parts": [{"type": "text", "text": result}]
            }]
            task.status = TaskStatus(state=TaskState.COMPLETED)
        else:
            task.status = TaskStatus(
                state=TaskState.INPUT_REQUIRED,
                message={"role": "agent", "content": {"type": "text", 
                         "text": "Please provide a search query."}}
            )
        return task

if __name__ == "__main__":
    agent = TavilySearchAgent(google_a2a_compatible=True)
    run_server(agent, port=8002, debug=True)
