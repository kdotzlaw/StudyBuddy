# Stub Data
## Users Data

| PK uID |username | password|
|-|-|-|
|1|ryan2023|password|
|2|katDot|1234|
|3|andrea22|2222|
|4|EliStudy|2#!6A|
|5|sneakerbot101|Shoes!|

## Classes
|PK cID| class_Name|timeslot|is_Complete (1 true, 0 false)| | FK: uID|
|-|-|-|-|-|-|
|1| COMP 2080 | 10:00 | 0|-| 3|
|2| COMP 4350| 11:30 |0|- |1|
|3| COMP 4350| 11:30 |0| -|2|
|4| COMP 4350| 11:30 |0| -|3|
|5| COMP 4350| 11:30 |0| -|4|
|6| COMP 4350| 11:30 |0|- |5|
|7| COMP 3820| 14:30 |0|- |2|

## Tasks
|PK: tID| task_Name|deadline (DATETIME) | task_weight| task_grade| | FK: uID| FK:cID|
|-|-|-|-|-|-|-|-|
|1| A1| 2023-02-09 14:00| 0.10|0|-|2|7|
|2| Exam| 2023-02-16 10:00 |0.20|0|-|3|1|
|3| A1 | 2023-01-30 23:59| 0.10|0.96|-|3|1|
