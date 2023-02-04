# Code Standards
## Frontend
### Vue Components, CSS, HTML, Javascript, Node.js
- Reference https://component-party.dev/ for syntax on Vue Props
- Semicolons at the end of lines.
- Use `let` for variables, `const` for constants/refs.
- Brackets `{` on the same line as declaration.   
  For example: `function toggleTime() {...`
- Brackets can be skipped if encapsulating only one line.    
  For example: `if(file)`   
                   `console.log(file.name)`
- **Avoid** one line functions or conditionals unless significantly improving readability.       
For example: **Dont do:** `if(file){console.log(file.name)}`
- Can compact or distribute nested HTML or JS code in any way.
- Can space your lines of code.
- Both inline and seperate line comments are acceptable.
- CSS that structures or layouts of components will be written inside the component file itself within `<style scoped> </style>`
- Route or page components (eg. home, login, accountCreate) will go to `frontend/src` 
- Modular components (eg. header, button, card) will go to `frontend/src/components`
- Logic layer Node.js classes will be housed in `frontend/src/logic`
- Images will go in the `frontend/public` folder for easy linking
- Raw text files, .json files and .yml files will be in `frontend/public`
### Testing
tbd
## Backend
### Python
### SQL
### Testing
