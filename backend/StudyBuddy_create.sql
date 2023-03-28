IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'StudyBuddy')
BEGIN
	CREATE DATABASE StudyBuddy;
END
GO

USE StudyBuddy;
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Users' AND xtype = 'U')
BEGIN
	CREATE TABLE Users (
	uID INT NOT NULL IDENTITY (1,1) PRIMARY KEY,
	username VARCHAR(50) NOT NULL UNIQUE,
	password VARCHAR(8) NOT NULL,
	user_email VARCHAR(50),
	xp FLOAT DEFAULT 0.0
	);
END

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Classes' AND xtype = 'U')
BEGIN
	CREATE TABLE Classes(
	cID INT NOT NULL IDENTITY (1,1) PRIMARY KEY,
	class_Name VARCHAR(50) NOT NULL,
	timeslot TIME NOT NULL,
	is_complete BIT,
	CONSTRAINT ck_testbool_ischk CHECK (is_complete IN (1,0)),
	studyTime FLOAT DEFAULT 0.0,
	/* Metadata */
	breakdown VARCHAR(255) DEFAULT '{"A+":"(90,100)", "A":"(80,89)", "B+":"(75,79)", "B":"(70,74)", "C+":"(65,69)", "C":"(56,64)", "D":"(50,55)", "F":"(0, 49)"}',
	courseCode varchar(50) DEFAULT '',
	section VARCHAR(8),
	classroom VARCHAR(50), /* room number, building*/
	prof_Name VARCHAR(50),
	prof_Email VARCHAR(50),
	prof_Phone VARCHAR(10),
	prof_Office VARCHAR(50),
	prof_Hours TIME,
	FK_uID INT,
	FOREIGN KEY (FK_uID) REFERENCES Users(uID)
	);
END

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Tasks' AND xtype = 'U')
BEGIN
	CREATE TABLE Tasks(
	tID INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
	task_Name VARCHAR(50) NOT NULL,
	deadline DATETIME,
	task_Weight INT NOT NULL,
	task_grade INT DEFAULT 0,
	task_goal VARCHAR(50) DEFAULT 'A',
	task_xp FLOAT, /* would be determined by system not user, might drop this*/
	FK_uID INT,
	FK_cID INT,
	FOREIGN KEY (FK_uID) REFERENCES Users(uID),
	FOREIGN KEY (FK_cID) REFERENCES Classes(cID)
	);
END
GO

/*Create stub data*/

/* ADD USER STUB DATA */
INSERT INTO Users (username,password)
	VALUES ('ryan2023','5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8');
INSERT INTO Users(username,password)
	VALUES('katDot','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4');
INSERT INTO Users(username,password)
	VALUES('andrea22','edee29f882543b956620b26d0ee0e7e950399b1c4222f5de05e06425b4c995e9');
INSERT INTO Users(username,password)
	VALUES('EliStudy','3459d4e034fb958e5f6c836ac00558ee7a614c0234a55f4df16535845a6cb186');
INSERT INTO Users(username,password)
	VALUES('sneakerbot101','73b2e90162bdd5ff6151294bee6fa72d602680e29b0bcb6702f952262ffb7055');

/* ADD CLASSES STUB DATA */
INSERT INTO Classes(class_Name, timeslot, is_Complete, studyTime,breakdown,FK_uID )
	VALUES ('COMP 2080', '10:00:00',0,0,'{"A+":"(95,100)", "A":"(80,94)", "B+":"(75,79)", "B":"(70,74)", "C+":"(65,69)", "C":"(56,64)", "D":"(50,55)", "F":"(0, 49)"}',3);
INSERT INTO Classes(class_Name, timeslot, is_Complete, studyTime,FK_uID )
	VALUES ('COMP 4350', '11:30:00',0,0,1);
INSERT INTO Classes(class_Name, timeslot, is_Complete, studyTime,FK_uID )
	VALUES ('COMP 4350', '11:30:00',0,0,2);
INSERT INTO Classes(class_Name, timeslot, is_Complete, studyTime,FK_uID )
	VALUES ('COMP 4350', '11:30:00',0,0,3);
INSERT INTO Classes(class_Name, timeslot, is_Complete, studyTime,FK_uID )
	VALUES ('COMP 4350', '11:30:00',0,0,4);
INSERT INTO Classes(class_Name, timeslot, is_Complete, studyTime,FK_uID )
	VALUES ('COMP 4350', '11:30:00',0,0,5);
INSERT INTO Classes(class_Name, timeslot, is_Complete, studyTime,FK_uID )
	VALUES ('COMP 3820', '14:30:00',0,0,2);

INSERT INTO Tasks (task_Name, deadline,task_Weight,task_grade,task_xp, FK_uID,FK_cID)
	VALUES('A1','2023-02-09 14:00:00',10,0,0,2,7)
INSERT INTO Tasks (task_Name, deadline,task_Weight,task_grade,task_goal,task_xp, FK_uID,FK_cID)
	VALUES('Exam','2023-02-16 10:00:00',20,0,'A+',0,3,1)
INSERT INTO Tasks (task_Name, deadline,task_Weight,task_grade,task_xp, FK_uID,FK_cID)
	VALUES('A1','2023-01-30 23:59:59',10,96,0,3,1)
