import http.server
import socketserver
import webbrowser
import os
import subprocess

PORT = 8000 

Handler = http.server.SimpleHTTPRequestHandler

web_dir = '.'
os.chdir(web_dir)

subprocess.Popen(["python", "Hospital-management-system//app.py"])

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    webbrowser.open(f'http://localhost:{PORT}/index.html')
    httpd.serve_forever()
