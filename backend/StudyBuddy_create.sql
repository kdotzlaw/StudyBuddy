IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'StudyBuddy')
BEGIN
	CREATE DATABASE StudyBuddy;
END;
GO

USE StudyBuddy;
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Users' AND xtype = 'U')
BEGIN
	CREATE TABLE Users (
	uID INT NOT NULL IDENTITY (1,1) PRIMARY KEY,
	username VARCHAR(50) NOT NULL UNIQUE,
	password VARCHAR(512) NOT NULL,
	user_email VARCHAR(50),
	xp FLOAT DEFAULT 0.0,
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
	/*breakdown form: "{key1:(min,max), key2:(min,max)}"*/
	breakdown varchar(255),
	/* Metadata */
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
	task_Weight FLOAT NOT NULL,
	task_grade FLOAT DEFAULT 0.0,
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
	VALUES ('ryan2023','password');
INSERT INTO Users(username,password)
	VALUES('katDot','1234');
INSERT INTO Users(username,password)
	VALUES('andrea22','2222');
INSERT INTO Users(username,password)
	VALUES('EliStudy','2#!6A');
INSERT INTO Users(username,password)
	VALUES('sneakerbot101','Shoes!');

/* ADD CLASSES STUB DATA */

INSERT INTO Classes(class_Name, timeslot, is_Complete, studyTime,FK_uID )
	VALUES ('COMP 2080', '10:00:00',0,0,'{A+:(90,100), A:(80,89), B+:(75,79), B:(70,74), C+:(65,69), C:(56,64), D:(50,55), F(0, 49)}',3);
INSERT INTO Classes(class_Name, timeslot, is_Complete, studyTime,FK_uID )
	VALUES ('COMP 4350', '11:30:00',0,0,'',1);
INSERT INTO Classes(class_Name, timeslot, is_Complete, studyTime,FK_uID )
	VALUES ('COMP 4350', '11:30:00',0,0,'',2);
INSERT INTO Classes(class_Name, timeslot, is_Complete, studyTime,FK_uID )
	VALUES ('COMP 4350', '11:30:00',0,0,'',3);
INSERT INTO Classes(class_Name, timeslot, is_Complete, studyTime,FK_uID )
	VALUES ('COMP 4350', '11:30:00',0,0,'',4);
INSERT INTO Classes(class_Name, timeslot, is_Complete, studyTime,FK_uID )
	VALUES ('COMP 4350', '11:30:00',0,0,'',5);
INSERT INTO Classes(class_Name, timeslot, is_Complete, studyTime,FK_uID )
	VALUES ('COMP 3820', '14:30:00',0,0,'',2);

INSERT INTO Tasks (task_Name, deadline,task_Weight,task_grade,task_xp, FK_uID,FK_cID)
	VALUES('A1','2023-02-09 14:00:00',0.10,0,0,2,7)
INSERT INTO Tasks (task_Name, deadline,task_Weight,task_grade,task_xp, FK_uID,FK_cID)
	VALUES('Exam','2023-02-16 10:00:00',0.20,0,0,3,1)
INSERT INTO Tasks (task_Name, deadline,task_Weight,task_grade,task_xp, FK_uID,FK_cID)
	VALUES('A1','2023-01-30 23:59:59',0.10,0.96,0,3,1)
