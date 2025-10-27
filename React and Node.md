⚛️ React Concepts

React Component (React)
A reusable piece of UI. Can be a function or class. Components accept props and manage their own state. They are the building blocks of React apps.

JSX (JavaScript XML) (React)
A syntax extension that lets you write HTML-like code inside JavaScript. React uses JSX to describe UI components in a readable way.

Props (React)
Short for “properties.” Props are inputs passed to components to customize their behavior or appearance. They are read-only and flow from parent to child.

State (React)
A way to store data that changes over time within a component. Managed using hooks like useState. State changes trigger re-renders.

useState Hook (React)
Adds local state to functional components. Example: const [count, setCount] = useState(0); updates count and re-renders the component.

useEffect Hook (React)
Runs side effects in components (e.g., data fetching, subscriptions). Can be configured to run on mount, update, or cleanup.

useRef Hook (React)
Creates a persistent reference to a DOM element or value that doesn’t trigger re-renders. Useful for accessing input fields or storing timers.

useContext Hook (React)
Allows components to access shared data without prop drilling. Works with React.createContext() to manage global state.

Controlled Component (React)
A form element (like <input>) whose value is managed by React state. Ensures React has full control over the input’s behavior.

Uncontrolled Component (React)
A form element that manages its own state internally. Accessed via useRef instead of useState.

React Fragment (<> </>) (React)
A wrapper that lets you group multiple elements without adding extra nodes to the DOM. Useful when returning multiple elements from a component.

Keys (in lists) (React)
Unique identifiers used when rendering lists of elements. Helps React track changes and optimize rendering. Example: <li key={item.id}>.

Reconciliation (React)
The process React uses to update the DOM efficiently. It compares the new virtual DOM with the previous one and applies minimal changes.

React Router (React)
A library for handling navigation in React apps. Allows you to define routes and link between pages without full page reloads.

Context API (React)
A way to share data across components without passing props manually. Ideal for themes, user authentication, or language settings.

Custom Hook (React)
A reusable function that uses React hooks to encapsulate logic. Example: useFetch() for data fetching.

Memoization (React.memo, useMemo, useCallback) (React)
Techniques to optimize performance by caching values or functions. Prevents unnecessary re-renders or recalculations.

Portals (React)
Allow rendering children into a DOM node outside the parent hierarchy. Useful for modals, tooltips, or overlays.

Error Boundaries (React)
Components that catch JavaScript errors in their child component tree and display fallback UI. Implemented using class components.

Suspense (React)
A React feature for handling asynchronous rendering. Often used with React.lazy() to load components dynamically.


🖥️ Command Line Tools (Windows Environment)

npx create-react-app my-app (React / Node.js)
Bootstraps a new React project with sensible defaults. npx runs the package without installing it globally. Creates a folder with all necessary files to start coding immediately.

npm start (React / Node.js)
Launches the development server for a React app. Opens the app in your default browser and watches for file changes to auto-refresh.

npm run build (React / Node.js)
Compiles the React app into static files for production. Outputs to the build folder with minified and optimized assets.

npm run eject (React / Node.js)
Exposes the underlying configuration of Create React App (CRA). Useful for advanced customization, but irreversible—use with caution.

npm install <package> (Node.js)
Installs a package into your project. For example, npm install react-router-dom adds routing capabilities.

npm uninstall <package> (Node.js)
Removes a package from your project. Cleans up node_modules and updates package.json.

npm audit (Node.js)
Scans your project for known security vulnerabilities in dependencies. Useful before deploying to production.

npm ci (Node.js)
Installs dependencies strictly from package-lock.json. Faster and more reliable for CI/CD pipelines than npm install.

vite / npm run dev (Vite / React)
Starts the Vite development server. Offers fast startup and Hot Module Replacement (HMR) for React apps.

vite build (Vite / React)
Bundles your Vite-based React app for production. Outputs optimized static files to the dist folder.

where node (Windows CLI)
Windows command to locate the installed path of Node.js. Useful for troubleshooting environment issues.

setx PATH "%PATH%;C:\Program Files\nodejs" (Windows CLI)
Adds Node.js to the system PATH on Windows. Ensures you can run node and npm from any command prompt.
