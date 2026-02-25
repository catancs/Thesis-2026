import sys
from openai import OpenAI

def main():
    print("Testing connection to local llama.cpp server...")
    
    # Connect to the local server
    client = OpenAI(
        base_url="http://localhost:8000/v1",
        api_key="local"
    )
    
    try:
        response = client.chat.completions.create(
            model="default",  # Model name doesn't matter for single-model llama.cpp server
            messages=[
                {"role": "user", "content": "Hello, what is your name and what is 2+2?"}
            ]
        )
        
        print("\nSuccess! The local API bridge and chat templates are functioning correctly.\n")
        print("--- Response ---")
        print(response.choices[0].message.content)
        print("----------------")
    except Exception as e:
        print(f"\nError: Failed to connect to the server or retrieve completion.\n{e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
