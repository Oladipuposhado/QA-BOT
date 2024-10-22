import subprocess

#function to pull the models

def pull_models():
    models = [
        
        "Mixtral 8B": "mixtral-8x7b-32768",
        "Llama 3groq 7b": "llama3-groq-70b-8192-tool-use-preview",
        "Llama 3-7b": "llama3-70b-8192",
        "Llama 3.1 -70b Preview": "llama-3.1-70b-versatile",
        "Llama 3.1-8b Instant ": "llama-3.1-8b-instant",
        "Gemma 2": "gemma2-9b-it",
        "Gemma 7b": "gemma-7b-it"
    ]
    
    for model in models:
        print(f"pulling model: {model}")
        subprocess.run(["ollama", "pull", model])
    
    
if __name__ =="__main__":
    pull_models()                 
                       