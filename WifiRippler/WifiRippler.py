import subprocess
import time
import random

def disconnect_wifi(interval, duration):
    while True:
        try:
            mac = ':'.join(['{:02x}'.format(random.randint(0x00, 0xff)) for _ in range(6)])
            subprocess.call(['netsh', 'interface', 'set', 'interface', 'Wi-Fi', 'admin=DISABLED'])
            print("Wi-Fi disconnected")
            time.sleep(duration)
            subprocess.call(['netsh', 'interface', 'set', 'interface', 'Wi-Fi', 'admin=ENABLED'])
            print("Wi-Fi reconnected")
            time.sleep(interval)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    interval = int(input("Enter the interval between Wi-Fi disconnections (in seconds): "))
    duration = int(input("Enter the duration of each disconnection (in seconds): "))
    disconnect_wifi(interval, duration)
