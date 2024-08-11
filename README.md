# React Component Builder (RCBuilder)

## Overview

The **React Component Builder (RCBuilder)** is a simple Bash script designed to convert your static HTML and CSS components into React (Next.js) components using TypeScript (`.tsx`). The script automates the process of creating a React component, converting HTML classes to `className`, and preparing CSS as a locally scoped CSS module.

## Features

- **Automated Conversion**: Converts static HTML and CSS files into React (Next.js) components.
- **Component Structure**: Automatically creates the necessary folder structure for each component.
- **JSX Conversion**: Replaces HTML `class` attributes with React's `className` attributes.
- **CSS Modules**: Converts your CSS to be compatible with React’s CSS modules, ensuring styles are locally scoped.

## Prerequisites

- **Bash**: The script is written in Bash and should be run in a Unix-like environment (e.g., Linux, macOS).
- **Next.js**: The output components are intended for use in a Next.js project with TypeScript enabled.

## Project Structure

```
RCBuilder/
├── convert.sh
├── inputs/
│   ├── input.html
│   └── input.css
└── outputs/
```

- **`convert.sh`**: The main Bash script that performs the conversion.
- **`inputs/`**: Directory containing your static HTML and CSS files (`input.html` and `input.css`).
- **`outputs/`**: Directory where the converted React components will be saved.

## How to Use

### 1. Set Up Your Project

1. Clone or download the **RCBuilder** project.
2. Place your static HTML and CSS files into the `inputs/` directory.

Example:
```
RCBuilder/
├── convert.sh
└── inputs/
    ├── input.html
    └── input.css
```

### 2. Run the Script

Navigate to the `RCBuilder` directory and run the script using the following command:
```bash
bash convert.sh
```

### 3. Enter the Component Name

When prompted, enter the desired name for your React component (e.g., `HomeVideoSection`). The script will automatically create the component files in the `outputs/` directory.

### 4. Output

The script will generate the following structure in the `outputs/` directory:

```
outputs/
└── HelloWorld/
    ├── HelloWorld.module.css
    └── HelloWorld.tsx
```

### 5. Integrate with Your Next.js Project

Move the generated component folder from `outputs/` to your Next.js project, typically under `components/pages`, and import it into your application.

```typescript
import HelloWorld from './components/HelloWorld';
```

## Example Output

Here’s an example of what the script-generated component might look like:

**HomeVideoSection.tsx**
```tsx
import React from 'react';
import styles from './HelloWorld.module.css';

const HelloWorld: React.FC = () => {
    return (
        <div className={styles.simple_component}>
            <img src="image.jpg" alt="Simple Image" className={styles.simple_component__img} />
            <p className={styles.simple_component__text}>This is a simple component.</p>
        </div>
    );
};

export default HelloWorld;
```

**HomeVideoSection.module.css**
```css
.test__videoBgSection { /* Your CSS here */ }
.test__videoBgSection__picture { /* Your CSS here */ }
/* Additional styles */
```

## License

This project is open-source and free to use under the MIT License.

## Contributions

Feel free to submit issues or pull requests to enhance the functionality of this script. Any contributions are welcome!

---

Happy coding! 🎉
