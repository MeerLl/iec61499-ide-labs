import socket

HOST = '127.0.0.1'
PORT = 61499

commands = [
    '<Request ID="1" Action="CREATE"><FB Name="EMB_RES" Type="EMB_RES"/></Request>',
    '<Request ID="2" Action="CREATE"><FB Name="HELLO" Type="STRING2STRING"/></Request>',
    '<Request ID="3" Action="CREATE"><FB Name="WORLD" Type="STRING2STRING"/></Request>',
    '<Request ID="4" Action="CREATE"><FB Name="APPEND" Type="APPEND_STRING_2"/></Request>',
    '<Request ID="5" Action="CREATE"><Connection Source="HELLO.OUT" Destination="APPEND.IN1"/></Request>',
    '<Request ID="6" Action="CREATE"><Connection Source="WORLD.OUT" Destination="APPEND.IN2"/></Request>',
    '<Request ID="7" Action="CREATE"><Connection Source="APPEND.OUT" Destination="CONSOLE.IN"/></Request>',
    '<Request ID="8" Action="START"/>'
]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for cmd in commands:
        s.sendall(cmd.encode('utf-8') + b'\n')
        resp = s.recv(1024).decode('utf-8', errors='ignore')
        print(f"Ответ: {resp.strip()}")