# Stub Data
## Users Data

| PK uID |username | password| hashed password |
|-|-|-|-|
|1|ryan2023|password| 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8|
|2|katDot|1234| 03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4|
|3|andrea22|2222| edee29f882543b956620b26d0ee0e7e950399b1c4222f5de05e06425b4c995e9|
|4|EliStudy|2#!6A| 3459d4e034fb958e5f6c836ac00558ee7a614c0234a55f4df16535845a6cb186|
|5|sneakerbot101|Shoes!| 73b2e90162bdd5ff6151294bee6fa72d602680e29b0bcb6702f952262ffb7055|

## Classes
|PK cID| class_Name|timeslot|is_Complete (1 true, 0 false)| study_time| breakdown| FK: uID|
|-|-|-|-|-|-|-|
|1| COMP 2080 | 10:00 | 0|0|'{A+:(90,100), A:(80,89), B+:(75,79), B:(70,74), C+:(65,69), C:(56,64), D:(50,55), F(0, 49)}'| 3|
|2| COMP 4350| 11:30 |0|0|1|
|3| COMP 4350| 11:30 |0| 0|2|
|4| COMP 4350| 11:30 |0| 0|3|
|5| COMP 4350| 11:30 |0| 0|4|
|6| COMP 4350| 11:30 |0|0|5|
|7| COMP 3820| 14:30 |0|0|2|

## Tasks
|PK: tID| task_Name|deadline (DATETIME) | task_weight| task_grade| xp| FK: uID| FK:cID|
|-|-|-|-|-|-|-|-|
|1| A1| 2023-02-09 14:00| 0.10|0|-|2|7|
|2| Exam| 2023-02-16 10:00 |0.20|0|-|3|1|
|3| A1 | 2023-01-30 23:59| 0.10|0.96|-|3|1|
