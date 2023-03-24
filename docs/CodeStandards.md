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
	- **Exemption:** Cypress command chains for tests.
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
- Nested HTML or Javascript command chains may be compacted in the same line or distributed between lines, using a design choice that will maximize readability. Minimize very long or very sparse lines.
- Lines between code may be spaced to ensure sufficient readability.
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
