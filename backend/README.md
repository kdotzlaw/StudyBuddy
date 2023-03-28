# Backend Readme

## Running flask server

        python3 -m flask --app server.py run
        
## Dev DB Connection String
        conn = (r'Driver=SQL Server;'
            r'Server=(local);'
            r'Database=StudyBuddy;'
            r'Trusted_Connection=yes')
            
## LOAD-TESTING STEPS
1. `pip install locust`
2. In backend directory, run the flask server: `python3 -m flask --app server.py run`
3. In backend directory, run locust: `python -m locust`
4. Visit `http://localhost:8089/`
5. Enter **100 users**, **20 users started/second**, and **localhost:5000**
6. Start Swarm
Report: http://localhost:8089/stats/report
 
