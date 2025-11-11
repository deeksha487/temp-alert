import sys
import time

def temperature_alert(temp):
    if temp < 15:
        print(f"Temperature: {temp}°C → Cold ❄")
    elif 15 <= temp <= 30:
        print(f"Temperature: {temp}°C → Normal 🌤")
    else:
        print(f"Temperature: {temp}°C → Hot ☀")

# Check if user provided an argument
if len(sys.argv) != 2:
    print("Usage: python temp_alert.py <temperature_in_Celsius>")
    sys.exit(1)

try:
    temperature = float(sys.argv[1])
except ValueError:
    print("Please enter a valid number for temperature.")
    sys.exit(1)

# Run automatically every 2 minutes (120 seconds)
while True:
    temperature_alert(temperature)
    print("Checking again in 2 minutes...\n")
    time.sleep(120)
