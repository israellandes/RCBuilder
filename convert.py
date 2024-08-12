import os
import re
from bs4 import BeautifulSoup, Comment

def convert_html_to_tsx(html_content, component_name):
    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove comments
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    # Function to convert class to className
    def convert_class_to_classname(tag):
        if 'class' in tag.attrs:
            classes = tag['class']
            del tag['class']
            if len(classes) > 1:
                # Correct handling of multiple classes
                class_string = ' '.join([f"${{{component_name}_styles['{cls}']}}" for cls in classes])
                tag['className'] = f"{{`{class_string}`}}"
            else:
                tag['className'] = f"{{{component_name}_styles['{classes[0]}']}}"

    # Apply conversion to all tags
    for tag in soup.find_all(True):
        convert_class_to_classname(tag)
        # Convert self-closing tags
        if tag.name in ['img', 'br', 'hr', 'input']:
            tag.can_be_empty_element = True

    # Convert to string and fix quotation marks
    jsx_content = str(soup)
    jsx_content = jsx_content.replace('"', "'")
    
    # Fix self-closing tags
    jsx_content = re.sub(r'(<(img|br|hr|input)[^>]*)/>', r'\1/>', jsx_content)

    # Remove extra quotes around className values
    jsx_content = re.sub(r"className='(\{[^}]+\})'", r"className=\1", jsx_content)

    # Fix multiple classes
    jsx_content = re.sub(r"className='(\{\`.+?\`\})'", r"className=\1", jsx_content)

    # Remove any remaining extra braces and quotes
    jsx_content = re.sub(r"\}\}`\}", r"}`}", jsx_content)
    jsx_content = re.sub(r"'(\{\`.+?\`\})'", r"\1", jsx_content)

    # Indent JSX content
    jsx_lines = jsx_content.split('\n')
    indented_jsx = '\n'.join(['        ' + line.strip() for line in jsx_lines if line.strip()])

    # Create TSX content
    tsx_content = f"""import React from 'react';
import {component_name}_styles from './{component_name}.module.css';

const {component_name}: React.FC = () => {{
    return (
{indented_jsx}
    );
}};

export default {component_name};
"""

    return tsx_content

def main():
    try:
        component_name = input("Enter the React component name (e.g., SimpleComponent): ")
        
        # Create output directory
        output_dir = os.path.join("outputs", component_name)
        os.makedirs(output_dir, exist_ok=True)
        print(f"Created output directory: {output_dir}")

        # Read input HTML
        html_file_path = "inputs/input.html"
        if not os.path.exists(html_file_path):
            raise FileNotFoundError(f"Input HTML file not found: {html_file_path}")
        
        with open(html_file_path, "r") as file:
            html_content = file.read()

        # Convert HTML to TSX
        tsx_content = convert_html_to_tsx(html_content, component_name)

        # Write TSX file
        tsx_file_path = os.path.join(output_dir, f"{component_name}.tsx")
        with open(tsx_file_path, "w") as file:
            file.write(tsx_content)
        print(f"Created {component_name}.tsx file")

        # Copy CSS file
        css_input_path = "inputs/input.css"
        if not os.path.exists(css_input_path):
            raise FileNotFoundError(f"Input CSS file not found: {css_input_path}")
        
        css_output_path = os.path.join(output_dir, f"{component_name}.module.css")
        with open(css_input_path, "r") as input_file, open(css_output_path, "w") as output_file:
            output_file.write(input_file.read())
        print(f"Copied CSS file to {component_name}.module.css")

        print(f"Conversion complete! {component_name} component has been created in the {output_dir} directory.")

        # Display contents of created files
        print(f"Contents of {component_name}.tsx:")
        print(tsx_content)

        print(f"Contents of {component_name}.module.css:")
        with open(css_output_path, "r") as file:
            print(file.read())

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()