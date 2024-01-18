import openai
import os

def read_html_file(html_file_path):
    try:
        with open(html_file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except IOError as e:
        print(f"Error reading HTML file: {e}")
        return None

def write_html_file(output_file_path, content):
    try:
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except IOError as e:
        print(f"Error writing HTML file: {e}")

# Get OpenAI API key from user input
#openai.api_key = input("Enter your OpenAI API key: ")
openai.api_key = ""

# Specify the path to your HTML file
html_file_path = input("Enter the path to the HTML file: ")

# Read the content of the HTML file
input_text = read_html_file(html_file_path)

if input_text is not None:
    # Make a request to the OpenAI API for text completion
    response = openai.Completion.create(
        model="text-davinci-003",  # Specify the GPT-3 model
        prompt=f"Rephrase the following text:\n\"{input_text}\"",
        max_tokens=100,  # Adjust max_tokens as needed
        temperature=0.7  # Adjust temperature as needed
    )

    # Extract the generated text from the response
    output_text = response['choices'][0]['text']

    # Replace the content of the HTML file with the generated text
    updated_html_content = input_text.replace(input_text, output_text)

    # Specify the path for the output HTML file
    output_file_path = input("Enter the path for the output HTML file: ")

    # Write the updated content to a new HTML file
    write_html_file(output_file_path, updated_html_content)

    print(f"HTML file updated successfully. New file: {output_file_path}")
