# Study Buddy

## Study with a Buddy

# Project Summary and Vision

## Project Summary
The Study Buddy is an application that allows students to keep track of their study progress with an incentive through a buddy that can be leveled up as they progress with their studies.  Being called “The Procrastinators,” as a team we felt this would be a great way to help students with their studies.

## Project Vision
The purpose of our Study Buddy is to help assist a student succeed in their academics while staying organized.

## Stakeholders
The target audience of this application are for students who are currently enrolled in school.

# Core Features

The Study Buddy will have at least four functional features and one non-function feature implemented.

## Track Study Time

This feature will allow users to track their study time and be presented with the progress of their time usage over a period of time. 

## Calendar

This feature will allow users to store any important dates and reminders and have it displayed in a scrollable list. This list will display the up coming important dates and how close it is to that date.

## Grade Calculator

The grade tracker will allow users to enter and store their grades and also calculate their current grade in the course. An extension of this feature would be able to calculate grades a user would need to achieve on future assignments/tests/projects in order to obtain a certain letter grade.

## Buddy Level System

This feature will allow for users to level up their buddy.

## Capacity and User Requests

The Study buddy will have a capacity of 100 users and can handle 1000 requests per minute.

# Technologies

## CI/CD

- **GitHub Actions**
- **Docker**

## Frontend Technologies

- Frontend framework: **Vue.js**
- Application logic: **JavaScript** and **Typescript**
- Environment: **Node.js**

## Backend

- Application logic written in either **Java** or **Python**
- **Microsoft SQL Server Management Studio** to manage a database written in either **SQL** or **PostgreSQL**
- Testing done with either **JUnit** or **Unittest** (Python equivalent JUnit)

# User Stories

## As a new user, I want to be able to create an account.
- Given I’m a new user on the log-in page. 
- When I hit the “Create Account” button and fill out the username and password fields in the dialogue and click the confirmation button. 
- Then the system creates my account and logs me in.

## As a returning user, I want to be able to log in.
- Given I’m a returning user on the log-in page.
- When I fill in the username and password fields and click the “Log-In” button.
- Then the system logs me in.

## As a user, I want to be able to create a new tracking workspace for each of my classes. (Feature 1, 2) 
- Given I’m logged into my account.
- When I click the “Add a Class” button on my homepage, fill out the fields in the dialogue box, and click the confirmation button.
- Then the system creates a new tracking workspace for my new class.

## As a user, I want to set up metadata about my class, such as section, classroom, location, professor name, email, phone number, and office hours. (Feature 1)
- Given I’m in the tracking workspace for my class.
- When I click the metadata fields, enter the metadata, and click the “Save” button.
- Then the system should store that metadata for my class.

## As a user, I want to track assignments, tests, etc. that contribute to my grade for a class. (Feature 1, 2, 3)
- Given I’m in the tracking workspace for my class.
- When I click the “Track Task” button, and fill out the associated fields (name, type of task, weight, due date, etc.), and click the confirmation button.
- Then the system should create a task with the associated information in the current workspace.

## As a user, I want to edit tasks that have been created. (Feature 1, 2, 3) 
- Given I’m in the tracking workspace for my class.
- When I expand a task and change the information fields in the dialog and click the “Save” button.
- The system modifies my task to reflect the changes I just made.

## As a user, I want to delete tasks that have been created. (Feature 1, 2, 3)
- Given I’m in the tracking workspace for my class.
- When I expand a class, click the delete button, and click “Yes” in the confirmation dialog.
- The system removes the task from my tracking workspace.

## As a user, I want to keep track of my grades for tasks. (Feature 3)
- Given I’m in the tracking workspace for my class.
- When I click on a task that is being tracked, in the dialog that appears, after I input a value in the “Grade” field, and click the “Complete Task” button.
- Then the system should mark the task as complete and record the grade I got.

## As a user, I want to know an estimated letter grade for a class. (Feature 3)
- Given I’m in the tracking workspace for my class, and I have created and completed some tasks that contribute to my class grade.
- The system should display an estimate of my class grade using the weights of the completed tasks, and the grades input for completed tasks.

## As a user, I want to be able to keep track of the time spent studying in each class. (Feature 1)
- Given I’m in the tracking workspace for my class.
- When I click on the “Track Studying” button and fill out the fields and click the confirmation button.
- The system records the time spent studying for that class.

## As a user, I want to be able to view important dates for each class. (Feature 2)
- Given I’m in the tracking workspace for my class.
- Then I should be able to see a list of important dates.

## As a user, I want my companion to let me know about approaching deadlines. (Feature 2)
- Given I’m a user at my homepage.
- Then my companion should give me a list of approaching deadlines

## As a user, I want my companion to let me know about my study progress.
- Given I’m a user at my homepage
- Then my companion should give me a breakdown of my study progress for each class.

## As a user, I want to be able to unlock customization options as I progress in my class. (Feature 4)
- Given I’m a user tracking at least one class.
- When I reach milestones in that class (complete a certain amount of tasks, reach a certain grade in task/class, etc.).
- The system will unlock customization options associated with the milestone for me to use.

## As a user, I want to be able to customize my companion with unlockables. (Feature 4)
- Given I’m a user with some customization options unlocked on my homepage..
- When I click on the customization button and select an unlocked customizable option for my companion.
- The system changes the appearance of my companion to reflect the selected customizable.

## As a user, I want to be able to customize my User Interface with unlockables (Feature 4)
- Given I’m a user with some customization options unlocked on my homepage..
- When I click on the customization button and select an unlocked customizable option for my User Interface.
- The system changes the appearance of my User Interface to reflect the selected customizable.


# Team Members

| Name | Role | Skills |
|---|---|---|
|Andrea Abellera| Team Leader, Frontend, Graphic Designer | Vue.Js, Node.Js, UI/UX, Accessibility|
|Katrina Dotzlaw| Backend, Database| Python, C#, SQL, Java|
|Ryan Dotzlaw| Backend, API Designer | Python, Java, C, SQL |
|Millan David| Frontend, Presenter | HTML/CSS, Vue.Js, Java, JavaScript |