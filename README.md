
# React Component Builder (RCBuilder)

## Overview

The **React Component Builder (RCBuilder)** is a Python-based tool designed to convert your static HTML and CSS components into React (Next.js) components using TypeScript (`.tsx`). The script automates the process of creating a React component, converting HTML classes to `className`, and preparing CSS as a locally scoped CSS module.

## Features

- **Automated Conversion**: Converts static HTML and CSS files into React (Next.js) components.
- **Component Structure**: Automatically creates the necessary folder structure for each component.
- **JSX Conversion**: Replaces HTML `class` attributes with React's `className` attributes.
- **CSS Modules**: Converts your CSS to be compatible with React’s CSS modules, ensuring styles are locally scoped.

## Prerequisites

- **Python 3.10 or later**: Ensure you have Python installed on your system.
- **Bash**: The installation and environment setup scripts are written in Bash and should be run in a Unix-like environment (e.g., Linux, macOS).
- **Next.js**: The output components are intended for use in a Next.js project with TypeScript enabled.

## Project Structure

```
RCBuilder/
├── convert.py
├── env.sh
├── install.sh
├── inputs/
│   ├── input.html
│   └── input.css
└── outputs/
```

- **`install.sh`**: Bash script to install the necessary Python version and dependencies.
- **`env.sh`**: Bash script to set up and activate the Python virtual environment.
- **`convert.py`**: The main Python script that performs the conversion.
- **`inputs/`**: Directory containing your static HTML and CSS files (`input.html` and `input.css`).
- **`outputs/`**: Directory where the converted React components will be saved.

## How to Use

### 1. Set Up Your Environment

1. **Run the Installation Script**:  
   First, navigate to the `RCBuilder` directory and run the installation script to ensure Python and the necessary packages are installed:

   ```bash
   chmod 777 install.sh env.sh convert.sh
   install.sh
   ```

2. **Set Up the Virtual Environment**:  
   Next, run the environment setup script to create and activate a Python virtual environment:

   ```bash
   env.sh
   ```

   The script will create a virtual environment in your home directory and activate it. To activate it manually in the future, use:

   ```bash
   source ~/my_venv/bin/activate
   ```

3. **Run the Conversion Script**:  
   With the virtual environment activated, run the conversion script to transform your static HTML and CSS into React components:

   ```
   python convert.py
   ```

### 2. Enter the Component Name

When prompted, enter the desired name for your React component (e.g., `HomeVideoSection`). The script will automatically create the component files in the `outputs/` directory.

### 3. Output

The script will generate the following structure in the `outputs/` directory:

```
outputs/
└── HomeVideoSection/
    ├── HomeVideoSection.module.css
    └── HomeVideoSection.tsx
```

### 4. Integrate with Your Next.js Project

Move the generated component folder from `outputs/` to your Next.js project, typically under `components/pages`, and import it into your application.

```typescript
import HomeVideoSection from './components/pages/home/HomeVideoSection';
```

## License

This project is open-source and free to use under the MIT License.

## Contributions

Feel free to submit issues or pull requests to enhance the functionality of this script. Any contributions are welcome!

---

Happy coding! 🎉
