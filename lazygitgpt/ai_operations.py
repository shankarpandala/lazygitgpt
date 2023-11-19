import openai
import os
import json
from tqdm import tqdm

def is_text_file(filepath):
    text_file_extensions = ['.txt', '.py', '.html', '.css', '.js', '.md', '.json', '.xml']
    return os.path.splitext(filepath)[1].lower() in text_file_extensions

def read_repository_contents():
    current_directory = os.getcwd()
    file_contents_dict = {}
    file_list = os.listdir(current_directory)

    for filename in tqdm(file_list, desc="Reading files", unit="file"):
        file_path = os.path.join(current_directory, filename)

        if not is_text_file(file_path):
            continue  # Skip non-text files

        # Read file contents
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_contents = file.read()
            file_contents_dict[filename] = file_contents
        except Exception as e:
            print(f"Error reading file {filename}: {e}")

    return file_contents_dict

def generate_response(prompt, sources=read_repository_contents()):
    client = openai.OpenAI()

    # Convert sources dictionary to a string representation
    sources_str = json.dumps(sources, indent=4)

    # Prepare the message with the prompt and sources
    messages = [
        {"role": "system", "content": "You are a helpful research assistant."},
        {"role": "user", "content": f"Prompt: {prompt}\nSources: {sources_str}"}
    ]

    # Send the prompt and sources to the API
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
    )

    return response.choices[0].message.content

# # Example usage
# prompt = "Please provide insights based on the following sources."
# sources = read_repository_contents()  # Reads files from the current directory
# analysis_result = analyze_text_with_gpt4(prompt, sources)
# print(analysis_result)
