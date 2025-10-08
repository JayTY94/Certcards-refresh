⚙️ Project & npm Workflow

Working Directory
The current folder your terminal commands operate in. npm expects package.json to be here.

cwd (Current Working Directory)
When you run a command like npx shadcn --cwd ., the --cwd flag tells it which folder to treat as the project root.

ENOENT
Error: “No such file or directory.” Means npm or Node tried to open a file that doesn’t exist (common when package.json or node_modules is missing).

npm install (or npm i)
Installs all dependencies listed in package.json into node_modules.

npx <package>
Executes a one-off command from a package (downloads temporarily if not installed locally).

Script Alias
A shortcut defined in package.json.
Example: "dev": "vite" lets you run npm run dev.

npm cache
A local store for previously downloaded packages. Sometimes needs clearing with npm cache clean --force if corrupt.

Debugger attached
A message from Node when running scripts in VS Code PowerShell or terminals that auto-attach a debugger. Normal for Vite dev runs.

📦 Package Management & Modules

Dependency Tree
The hierarchy of packages your project and its libraries depend on.

Peer Dependency
A package required by another, but expected to be installed at the project level (common with React versions).

Module Resolution
How Node or Vite figures out where an import points to. Uses the alias, paths in tsconfig.json, and node_modules.

Alias (in Vite)
Shortcut import path, set in vite.config.js. Example:

alias: { '@': path.resolve(__dirname, './src') }


Import Path Error
“Failed to resolve import” means the path or alias doesn’t match any existing file.

Shims / Polyfills
Code that mimics missing browser or Node features. Not usually needed in modern Vite setups.

📁 File & Config Structure

vite.config.js
Vite’s main configuration file for plugins, aliases, and dev server behavior.

tsconfig.json
TypeScript configuration — used even in JS projects for path alias support.

tailwind.config.js
Tells Tailwind where to look for class names and how to extend themes.

postcss.config.js
Specifies PostCSS plugins (like Tailwind + autoprefixer).

components.json (shadcn)
A manifest shadcn creates to track which UI components you’ve added.

index.html
The single HTML entry file that loads your React app.

src/main.jsx
Vite’s entry point that mounts your React app to the DOM.

src/App.jsx
The top-level React component rendered by main.jsx.

🧠 Build Tools & Frameworks

Vite Dev Server
A fast development server that supports hot reloading and modern JavaScript syntax.

Hot Reload / HMR (Hot Module Replacement)
Reloads changed modules instantly in the browser without refreshing the page.

Bundling
The process of combining many source files into fewer optimized files for deployment.

Transpiling
Converting code (like JSX or ES6) into older syntax browsers understand — done by Babel under the hood.

ESM (ECMAScript Modules)
The modern module format used by Vite (import/export).

CommonJS (CJS)
The older Node.js module system using require() and module.exports.

🧩 React & JSX Issues

JSX Syntax Error
Usually caused by a missing closing tag or stray character (like your blank line at line 42 earlier).

React Component
A function that returns JSX and defines part of the UI. Example:

function Button() { return <button>Click</button> }


Import Statement
The way to bring in another file or package.
Example: import { useState } from 'react';

Export Default
Marks the main thing a module provides.
Example: export default App;

Hooks (useState, useEffect)
React functions for managing state and side effects.

🎨 Tailwind & shadcn

Tailwind Directives
@tailwind base; @tailwind components; @tailwind utilities;
Tell PostCSS to include Tailwind’s layers in your CSS.

Tailwind Classes
Small styling utilities like bg-blue-500, rounded-lg, or flex justify-center.

shadcn/ui
A library that generates React + Tailwind component source files into your project (src/components/ui).

Preflight Checks (shadcn)
shadcn’s built-in validation for framework (Vite), Tailwind, and alias setup before adding components.

Import Alias Validation (shadcn)
shadcn checks tsconfig.json for "@/*": ["./src/*"]. If missing, you’ll get ✖ Validating import alias.

🧾 Common Error Messages You Saw

"Could not determine executable to run"
npm couldn’t find the binary file for a package — usually means it’s not installed locally (e.g., tailwindcss before running npx tailwindcss init).

"Failed to resolve import '@/components/ui/card'"
Alias or component files missing. Fix by ensuring:

vite.config.js has alias: { '@': path.resolve(__dirname, './src') }

tsconfig.json has "paths": { "@/*": ["./src/*"] }"

shadcn generated src/components/ui/card.tsx.

"Unexpected token" (Babel error)
JS syntax error — most often an extra brace, comma, or blank line in JSX.

"Debugger attached"
Harmless message printed by Node when VS Code’s PowerShell auto-attaches the debugger to scripts.

"No Tailwind CSS configuration found"
shadcn looked for tailwind.config.js and didn’t find it — create it with npx tailwindcss init -p.

💡 Environment & OS Concepts


Global npm install
Installs a package system-wide with -g. Usually not needed for modern projects.

Local npm install
Installs a package into the project folder (node_modules) — preferred for version control.


Network: use --host to expose
Vite’s message meaning your app is only visible on localhost; run npm run dev -- --host to expose to your LAN.

🧰 Debugging Tools & Skills to Build

Browser Console (F12)
Shows runtime errors. Always the first place to check a blank screen.

Terminal Output
Shows build or syntax errors from Vite, npm, or Node.

Logs (console.log)
Your own debug prints inside React components.

Error Stack
Trace of function calls that led to an error. The bottom-most line usually points to the cause.
