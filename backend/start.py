# just exists to run the production server
from waitress import serve
import server

print("Server is now running on port 5000")
serve(server.app, host='0.0.0.0', port=5000)
