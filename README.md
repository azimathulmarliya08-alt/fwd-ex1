# EX01 Developing a Simple Webserver
## Date:11-11-26
## REG NO:26018986

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<!DOCTYPE html>
<html>
<head>
    <title>TCP and IP Protocol</title>
</head>
<body>

    <h1>TCP and IP Protocol</h1>

    <h2>1. TCP (Transmission Control Protocol)</h2>
    <p>
        TCP is a communication protocol that ensures
        reliable data transmission between devices.
    </p>

    <h3>Functions of TCP:</h3>
    <ul>
        <li>Establishes connection between devices.</li>
        <li>Ensures reliable data transmission.</li>
        <li>Checks for errors in data.</li>
        <li>Arranges data in correct order.</li>
    </ul>

    <h2>2. IP (Internet Protocol)</h2>
    <p>
        IP is a protocol used to identify devices
        and send data from one device to another
        through networks.
    </p>

    <h3>Functions of IP:</h3>
    <ul>
        <li>Provides IP addresses to identify devices.</li>
        <li>Routes data packets to their destination.</li>
        <li>Transfers packets across networks.</li>
    </ul>

    <h2>Difference Between TCP and IP</h2>

    <table border="1" cellpadding="10">
        <tr>
            <th>TCP</th>
            <th>IP</th>
        </tr>
        <tr>
            <td>Ensures reliable data delivery.</td>
            <td>Delivers packets to the destination.</td>
        </tr>
        <tr>
            <td>Works at Transport Layer.</td>
            <td>Works at Network Layer.</td>
        </tr>
        <tr>
            <td>Checks errors and data order.</td>
            <td>Handles addressing and routing.</td>
        </tr>
    </table>

</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
```


## OUTPUT:
![alt text](<Screenshot 2026-11-03 134920.png>)
![alt text](<Screenshot 2026-11-03 142243.png>)


## RESULT:
The program for implementing simple webserver is executed successfully.

