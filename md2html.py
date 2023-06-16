import os
import markdown

def convert_markdown_to_html(markdown_file, output_folder):
    # Read the Markdown file
    with open(markdown_file, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_content)

    # Create the output filename
    markdown_filename = os.path.basename(markdown_file)
    html_filename = os.path.splitext(markdown_filename)[0] + '.html'
    output_path = os.path.join(output_folder, html_filename)

    # Write the HTML content to the output file
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

def convert_all_markdown_files(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get a list of all Markdown files in the input folder
    markdown_files = [file for file in os.listdir(input_folder) if file.lower().endswith('.md')]

    # Convert each Markdown file to HTML
    for markdown_file in markdown_files:
        markdown_path = os.path.join(input_folder, markdown_file)
        convert_markdown_to_html(markdown_path, output_folder)
        print(f"Converted {markdown_file} to HTML.")

# Specify the input and output folders
input_folder = 'mdbook'
output_folder = 'htmlbook'

# Convert all Markdown files in the input folder to HTML
convert_all_markdown_files(input_folder, output_folder)
