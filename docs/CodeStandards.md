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
- Frontend testing done using **jest** on application level **Pinia** store functions
- Unit tests should only test **one** method/component
- Tests for components should be collected in `describe("<desc>", ()=>{<tests>})`
- Each feature should have its own seperate test suite
## Backend
### Python
- All SQL queries in python will be done using **Prepared Statements** to avoid SQL Injection. A valid SQL query using a prepared statement is: `cursor.execute("SELECT * FROM <tableName> WHERE <colName> = ?", username)`
### SQL
- Comments will be done using `/*  */`
- All SQL keywords will be capitalized
- Table names, row names, column names, and variable names will be camel case. For example, `userGrades`
- All SQL files will be pushed to `backend/`
### Testing
- Database is tested using **UnitTest**, API tested using **flask_unittest**
- Tests for database and API in seperate classes
- Unit tests should only test **one** component/method
- All tests should be prefaced with pass conditions and description of what test is testing
- Tests should include Negative Testing (ie test that ensure incorrect input fails correctly)
- Unit tests should be orderd by component (ie all User tests should be next to eachother in test suite)
