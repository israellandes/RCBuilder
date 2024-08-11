#!/bin/bash

# Enable verbose mode
set -x

# Prompt for the component name
read -p "Enter the React component name (e.g., SimpleComponent): " componentName

# Create the necessary folder structure in the outputs directory
outputDir="outputs/$componentName"
mkdir -p "$outputDir"
echo "Created output directory: $outputDir"

# Check if input files exist
if [[ ! -f inputs/input.html ]]; then
  echo "Error: inputs/input.html does not exist."
  exit 1
fi

if [[ ! -f inputs/input.css ]]; then
  echo "Error: inputs/input.css does not exist."
  exit 1
fi

# Convert HTML to JSX, handling className conversion properly
jsxContent=$(sed -e 's/class="/className={styles./g' \
                 -e 's/">/}>/' \
                 -e 's/ "/={styles./g' \
                 inputs/input.html | sed 's/^/        /')

# Check if the JSX content was generated correctly
if [[ -z "$jsxContent" ]]; then
  echo "Error: JSX content could not be generated."
  exit 1
fi

echo "Generated JSX content:"
echo "$jsxContent"

# Generate the .tsx file with the correct layout
cat <<EOL > "$outputDir/$componentName.tsx"
import React from 'react';
import styles from './$componentName.module.css';

const $componentName: React.FC = () => {
    return (
$jsxContent
    );
};

export default $componentName;
EOL

echo "Created $componentName.tsx file"

# Check if the .tsx file was created
if [[ ! -f "$outputDir/$componentName.tsx" ]]; then
  echo "Error: The $componentName.tsx file could not be created."
  exit 1
fi

# Generate the CSS module file
# Copy the input CSS file to the output directory as a module
cp inputs/input.css "$outputDir/$componentName.module.css"

echo "Copied CSS file to $componentName.module.css"

# Check if the CSS module file was copied correctly
if [[ ! -f "$outputDir/$componentName.module.css" ]]; then
  echo "Error: The $componentName.module.css file could not be copied."
  exit 1
fi

echo "Conversion complete! $componentName component has been created in the $outputDir directory."

# Display contents of created files
echo "Contents of $componentName.tsx:"
cat "$outputDir/$componentName.tsx"

echo "Contents of $componentName.module.css:"
cat "$outputDir/$componentName.module.css"

# Disable verbose mode
set +x