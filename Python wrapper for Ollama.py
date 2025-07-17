import ollama

# Initialize the Ollama client
client = ollama.Client()

# Get user input at runtime
prompt = input("Enter your prompt: ")

# Define the model
model = "gemma3:1b"  # Replace with your model name if needed

# Send the query to the model
response = client.generate(model=model, prompt=prompt)

# Print the response from the model
print("Response from Ollama:")
print(response.response)