from python_a2a import A2AClient, run_server
from python_a2a.langchain import to_a2a_server
from langchain_ollama.llms import OllamaLLM
import os
import logging
import threading
import signal
import sys

# Create a LangChain LLM
#llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
llm = OllamaLLM(model="llama3.2")
# Convert LLM to A2A server
llm_server = to_a2a_server(llm)

# Add logging to verify skill registration
def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Initializing OllamaLLM model...")

    llm_thread = threading.Thread(
        target=lambda: run_server(llm_server, port=5001),
        daemon=True
    )
    llm_thread.start()

    logging.debug("LLM server started on port 5001.")

    # Wait here until Ctrl+C
    try:
        print("Servers are running. Press Ctrl+C to stop.")
        signal.pause()  # Wait for signals
    except KeyboardInterrupt:
        logging.debug("Stopping servers...")
        print("\nStopping servers...")
        sys.exit(0)
if __name__ == "__main__":
    main()