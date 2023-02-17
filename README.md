<p align="center">
<img height="300" width="300" src="https://raw.githubusercontent.com/kdotzlaw/StudyBuddy/main/frontend/public/assets/title_sq.png" alt="Study Buddy logo" align="center">
</p><br>

# Project Summary and Vision


### Test Plan and Sequence Diagrams
The project test plan and sequence diagrams are located: https://github.com/kdotzlaw/StudyBuddy/wiki/Sprint-2

### About
The Study Buddy is an application that allows students to keep track of their study progress with an incentive through a buddy that can be leveled up as they progress with their studies.  Being called “The Procrastinators,” as a team we felt this would be a great way to help students with their studies.

### Our Vision
The purpose of our Study Buddy is to help assist a student succeed in their academics while staying organized.

### Who will Study Buddy help?
Our primary stakeholders and stakeholders for this application are students who are currently enrolled in school.


# Core Features
The Study Buddy will have at least four functional features and one non-functional feature implemented.

### I. User Accounts (sprint 2)
This feature will allow users to create accounts that will allow them to sign in and out of the Study Buddy to save their progress.

### II. Track Study Time (sprint 2)
This feature will allow users to track their study time and be presented with the progress of their time usage over a period of time. 

### III. Calendar 
This feature will allow users to store any important dates and reminders and have it displayed in a scrollable list. This list will display the up coming important dates and how close it is to that date.

### IV. Grade Calculator
The grade tracker will allow users to enter and store their grades and also calculate their current grade in the course. An extension of this feature would be able to calculate grades a user would need to achieve on future assignments/tests/projects in order to obtain a certain letter grade.

### V. Capacity and User Requests
The Study buddy will have a capacity of 100 users and can handle 1000 requests per minute.

## Future Features

### VI. Buddy Level System
This feature will allow for users to level up their buddy.

# Technologies

<p align="center">
<img height="75" width="75" src="https://raw.githubusercontent.com/kdotzlaw/StudyBuddy/main/frontend/public/assets/tech/docker.png" alt="Vue logo" align="center">
<img height="75" width="75" src="https://raw.githubusercontent.com/kdotzlaw/StudyBuddy/main/frontend/public/assets/tech/nodejs.png" alt="NodeJS logo" align="center">
<img height="75" width="75" src="https://raw.githubusercontent.com/kdotzlaw/StudyBuddy/main/frontend/public/assets/tech/vue.png" alt="Docker logo" align="center">
<img height="75" width="75" src="https://raw.githubusercontent.com/kdotzlaw/StudyBuddy/main/frontend/public/assets/tech/ghactions.png" alt="Github Actions logo" align="center">
<img height="75" width="75" src="https://raw.githubusercontent.com/kdotzlaw/StudyBuddy/main/frontend/public/assets/tech/flask.png" alt="Flask logo" align="center">
<img height="75" width="75" src="https://raw.githubusercontent.com/kdotzlaw/StudyBuddy/main/frontend/public/assets/tech/python.png" alt="Python logo" align="center">
<img height="75" width="75" src="https://raw.githubusercontent.com/kdotzlaw/StudyBuddy/main/frontend/public/assets/tech/sql.png" alt="SQL logo" align="center">
</p>

### CI/CD

- **GitHub Actions**
- **Docker**

### Frontend Technologies

- Frontend framework: **Vue.js**
- Application logic: **JavaScript** and **Typescript**
- Environment: **Node.js**

### Backend

- Backend framework: **Flask**
- Application logic : **Python**
- **Microsoft SQL Server Management Studio** to manage a database written in **SQL**
- Testing: **Unittest**
- [Backend API](https://petstore.swagger.io/?url=https://raw.githubusercontent.com/kdotzlaw/StudyBuddy/main/backend/api.yaml)

## Software Architecture

![Study Buddy architecture diagram](/docs/architecture_v1.png)

# User Stories

**_As a new user, I want to be able to create an account._** *(ref. [Feature 1](#i-user-accounts))*
- Given I’m a new user on the log-in page. 
- When I hit the “Create Account” button and fill out the username and password fields in the dialogue and click the confirmation button. 
- Then the system creates my account and logs me in.

**_As a returning user, I want to be able to log in._** *(ref. [Feature 1](#i-user-accounts))*
- Given I’m a returning user on the log-in page.
- When I fill in the username and password fields and click the “Log-In” button.
- Then the system logs me in.

**_As a user, I want to be able to create a new tracking workspace for each of my classes._** *(ref. [Feature 2](#ii-track-study-time), [3](#iii-calendar))*
- Given I’m logged into my account.
- When I click the “Add a Class” button on my homepage, fill out the fields in the dialogue box, and click the confirmation button.
- Then the system creates a new tracking workspace for my new class.

**_As a user, I want to set up metadata about my class, such as section, classroom, location, professor name, email, phone number, and office hours._** *(ref. [Feature 2](#ii-track-study-time))*
- Given I’m in the tracking workspace for my class.
- When I click the metadata fields, enter the metadata, and click the “Save” button.
- Then the system should store that metadata for my class.

**_As a user, I want to track assignments, tests, etc. that contribute to my grade for a class._** *(ref. [Feature 2](#ii-track-study-time), [3](#iii-calendar), [4](#iv-grade-calculator))*
- Given I’m in the tracking workspace for my class.
- When I click the “Track Task” button, and fill out the associated fields (name, type of task, weight, due date, etc.), and click the confirmation button.
- Then the system should create a task with the associated information in the current workspace.

**_As a user, I want to edit tasks that have been created._**  *(ref. [Feature 2](#ii-track-study-time), [3](#iii-calendar), [4](#iv-grade-calculator))*
- Given I’m in the tracking workspace for my class.
- When I expand a task and change the information fields in the dialog and click the “Save” button.
- The system modifies my task to reflect the changes I just made.

**_As a user, I want to delete tasks that have been created._** *(ref. [Feature 2](#ii-track-study-time), [3](#iii-calendar), [4](#iv-grade-calculator))*
- Given I’m in the tracking workspace for my class.
- When I expand a class, click the delete button, and click “Yes” in the confirmation dialog.
- The system removes the task from my tracking workspace.

**_As a user, I want to keep track of my grades for tasks._** *(ref. [Feature 4](#iv-grade-calculator))*
- Given I’m in the tracking workspace for my class.
- When I click on a task that is being tracked, in the dialog that appears, after I input a value in the “Grade” field, and click the “Complete Task” button.
- Then the system should mark the task as complete and record the grade I got.

**_As a user, I want to know an estimated letter grade for a class._** *(ref. [Feature 4](#iv-grade-calculator))*
- Given I’m in the tracking workspace for my class, and I have created and completed some tasks that contribute to my class grade.
- The system should display an estimate of my class grade using the weights of the completed tasks, and the grades input for completed tasks.

**_As a user, I want to be able to keep track of the time spent studying in each class._** *(ref. [Feature 2](#ii-track-study-time))*
- Given I’m in the tracking workspace for my class.
- When I click on the “Track Studying” button and fill out the fields and click the confirmation button.
- The system records the time spent studying for that class.

**_As a user, I want to be able to view important dates for each class._** *(ref. [Feature 3](#iii-calendar))*
- Given I’m in the tracking workspace for my class.
- Then I should be able to see a list of important dates.

**_As a user, I want my companion to let me know about approaching deadlines._** *(ref. [Feature 3](#iii-calendar))*
- Given I’m a user at my homepage.
- Then my companion should give me a list of approaching deadlines

**_As a user, I want my companion to let me know about my study progress._**
- Given I’m a user at my homepage
- Then my companion should give me a breakdown of my study progress for each class.

**_As a user, I want to be able to unlock customization options as I progress in my class._** *(ref. [Feature 6](#iv-buddy-level-system))*
- Given I’m a user tracking at least one class.
- When I reach milestones in that class (complete a certain amount of tasks, reach a certain grade in task/class, etc.).
- The system will unlock customization options associated with the milestone for me to use.

**_As a user, I want to be able to customize my companion with unlockables._** *(ref. [Feature 6](#iv-buddy-level-system))*
- Given I’m a user with some customization options unlocked on my homepage..
- When I click on the customization button and select an unlocked customizable option for my companion.
- The system changes the appearance of my companion to reflect the selected customizable.


# Team Members

| Name | Role | Skills |
|---|---|---|
|Andrea Abellera| Team Leader, Frontend, Graphic Designer | Vue.Js, Node.Js, UI/UX, Accessibility|
|Katrina Dotzlaw| Backend, Database| Python, C#, SQL, Java|
|Ryan Dotzlaw| Backend, API Designer | Python, Java, C, SQL |
|Millan David| Frontend, Presenter | HTML/CSS, Vue.Js, Java, JavaScript |
|Elieser Capillar| Frontend, Graphic Designer | React Native, Java, JavaScript |

<p align="center">
<br>
<b><i>The Procrastinators © 2023</i></b>
<br>
</p>

![Study Buddy banner](/frontend/public/assets/banner.png)
