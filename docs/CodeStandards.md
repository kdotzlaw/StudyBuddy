# Code Standards

## Frontend
### Vue Practices
The standard Vue composition for StudyBuddy will be based on [Vue3's SFC Syntax](https://vuejs.org/api/sfc-spec.html).
Orders of the HTML and Javascript block may be interchanged. CSS must always be affixed at the bottom of the document.

- **Body of any `.vue` file**  
	```
	<script setup>
		//  Javascript code
	</script>

	<template>
		<!--  HTML code  -->
	</template>

	<styles scoped>
		/*  CSS code  */
	</styles>
	```
- **Component props** will use the [defineProps](https://vuejs.org/api/sfc-script-setup.html#defineprops-defineemits) convention.  
	```
	const props = defineProps({
		propValue: {type: Array, required: false, default: []}
	})
	```
### Javascript Practices
- Semi-colons are mandatory at the end of single lines.  
	- **Exemption:** Cypress command chains in tests
- Use  `let`  for variables,  `const`  for constants and refs.
- Brackets should be written on the same line as declaration.  
	```
	function toggleTime() {
		// ...
	}
	```
- Brackets may be skipped if encapsulating only one line.  
	```
	if(file)
		console.log(file.name)
	```
### Readability-First Approach
- Affix an **introductory header** on the top of all component, page, logic, and test files to describe the purpose of the file.  
  ```  
  /*
   * validate.ts
   *    Form input validation functions to identify empty fields and enforce security checks.
   */
  ```    
  ```  
  <!-- 
    Login.vue 
      Renders form fields and controls, and runs validation checks for logging in an existing account.
  -->
  ```  
- Nested HTML or Javascript command chains may be compacted in the same line or distributed between lines, using a design choice that will maximize readability. Minimize very long or very sparse lines.
- Lines between code may be spaced to ensure sufficient readability.
- Use **single line or inline comments** to provide context of use, breakdown complex commands, or briefly describe sections of code.  
	`private pauseTotal: number = 0;  // Total of all intervals of paused times to deduct from study time`
- Use **multiline comments** to describe large functions with multiple tasks, or with purpose not immediately discerned from function name. `@params` and `@returns` may be indicated optionally.  
  ```  
  /* manageTimer
   *   Starts new Timer instance if no Timer running
   *   Pauses current Timer if provided class or user params are current
   *   Create new Timer instance if provided class or user params are new
   *   @params - userId: string , classId: string
   */
  ```  
### Filesystem Structure and Resource Location
- Routed page components (e.g. Dashboard, Class): `frontend/src/pages`
- Modular components (e.g. Accordion, Buddy): `frontend/src/components`
- Business logic functions and classes: `frontend/src/logic`
- Images and static files: `frontend/public`
- Test files and utils: `frontend/test`
### Testing
- See [StudyBuddy test plan](https://github.com/kdotzlaw/StudyBuddy/blob/main/docs/SE2%20Test%20Plan.pdf) for development prerequisites and standards.

## Backend
### Python
- All SQL queries in python will be done using **Prepared Statements** to avoid SQL Injection. A valid SQL query using a prepared statement is: `cursor.execute("SELECT * FROM <tableName> WHERE <colName> = ?", username)`
- All database methods will go into `db.py`
- All server methods will go into `server.py`
- Database and server methods should be organized by functionality (ie all User methods should be next to each other)
- All database and server methods should be prefaced by preconditions, postconditions and a description of the method. Server methods should indicate endpoint requirements. 
- All database method names should be in camelCase (ie `getTasks()`)
- All multi-word server method names should be seperated by `_`. For example, `complete_class`.

### SQL
- Comments will be done using `/*  */`
- All SQL keywords will be capitalized
- Table names and function names will be camel case. For example, `userGrades`.
- Names of rows and columns with multiple words will be seperated with a `_`. For example, `task_goal` or `task_Goal`.
- All SQL files will be pushed to `develop/backend/` 

### Database and Server Testing
- Database is tested using **UnitTest**, API tested using **flask_unittest**
- All backend tests should be contained in `backend_test.py`
- Tests for database and API must be in seperate classes
- Unit tests should only test **one** component/method
- All tests should be prefaced with pass conditions and a description of what test is testing
- Tests should include Negative Testing (ie test that ensure incorrect input fails correctly)
- Unit tests should be orderd by component (ie all User tests should be next to each other in test suite)
- See [StudyBuddy test plan](https://github.com/kdotzlaw/StudyBuddy/blob/main/docs/SE2%20Test%20Plan.pdf) for development prerequisites and standards.

### Locust Testing
- All load-testing will be done in `locustfile.py`
- All tasks must be indicated with `@task` tag.
- All task definitions must be camelCase (ie `getClasses()`
