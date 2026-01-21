import socket
import xml.etree.ElementTree as ET

PORT = 61499

def vulnerable_parse(data):
    buffer = bytearray(64)
    try:
        buffer[:len(data)] = data
    except:
        print("Overflow detected!")

s = socket.socket()
s.bind(('', PORT))
s.listen(5)
print(f"Mock runtime listening on {PORT}")

while True:
    conn, addr = s.accept()
    data = conn.recv(4096)
    try:
        root = ET.fromstring(data)
        print(f"Command: {root.get('Action')}")
        conn.send(b'<Response Status="OK"/>\n')
    except:
        print("Parse error → trigger vuln")
        vulnerable_parse(data)
    conn.close()