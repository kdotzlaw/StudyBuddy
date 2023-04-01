# Backend Readme

## Running flask server

        python -m flask --app server.py run

## Running the production server

        python start.py
        
## Dev DB Connection String
        conn = (r'Driver=SQL Server;'
            r'Server=(local);'
            r'Database=StudyBuddy;'
            r'Trusted_Connection=yes')
            
## LOAD-TESTING STEPS
1. `pip install locust`
2. In backend directory, run the production server: `python start.py`
3. In backend directory, run locust: `python -m locust`
4. Visit `http://localhost:8089/`
5. Enter **100 users**, **20 users started/second**, and **localhost:5000**
6. Start Swarm
7. On stop, view report. Alternatively, download the [load test report](/docs/load-test_report.pdf).


 
