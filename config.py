# Configuration settings for Ollama and browser automation

OLLAMA_SETTINGS = {
    'model': 'your_model_name', # Replace with your model name
    'api_key': 'your_api_key', # Replace with your API key if required
    'timeout': 30 # Timeout in seconds for requests
}

BROWSER_SETTINGS = {
    'headless': True, # Set to False to see browser actions
    'browser_path': '/path/to/your/browser', # Path to the browser executable
    'window_size': {'width': 1920, 'height': 1080}, # Default window size
}  
