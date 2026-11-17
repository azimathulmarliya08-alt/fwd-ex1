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