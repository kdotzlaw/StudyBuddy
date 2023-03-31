# Backend Readme

## Running flask server

        python server.py -t true

## Running the production server

        python server.py
        
## Dev DB Connection String
        conn = (r'Driver=SQL Server;'
            r'Server=(local);'
            r'Database=StudyBuddy;'
            r'Trusted_Connection=yes')
            
## LOAD-TESTING STEPS
1. `pip install locust`
2. In backend directory, run the production server: `python server.py`
3. In backend directory, run locust: `python -m locust`
4. Visit `http://localhost:8089/`
5. Enter **100 users**, **20 users started/second**, and **localhost:5000**
6. Start Swarm
7. On stop, view report. Alternatively, download `loadtest_report.html` in the backend directory.


 
