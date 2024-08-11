import React from 'react';
import styles from './HelloWorld.module.css';

const HelloWorld: React.FC = () => {
    return (
        <div className={styles.test_component}>
            <h1 className={styles.test_component__title}>Hello, World!</h1>
            <p className={styles.test_component__description}>This is a test component.</p>
            <button className={styles.test_component__button}>Click Me</button>
        </div>
    );
};

export default HelloWorld;
