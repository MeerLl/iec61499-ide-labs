import random
import subprocess
import time

try:
    subprocess.run(["zzuf", "-r", "0.038", "cp", "test_command.xml", "fuzzed.xml"])
except:
    print("zzuf not installed → skip")

with open('test_command.xml', 'rb') as f:
    data = bytearray(f.read())

for i in range(100):
    pos = random.randint(0, len(data)-1)
    data[pos] = random.randint(0, 255)
    with open('fuzzed.xml', 'wb') as f:
        f.write(data)
    print(f"Test {i+1}: mutated byte {pos}")
    time.sleep(1)