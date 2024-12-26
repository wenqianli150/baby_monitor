import sys
import time
import grovepi

# Define the ports for the LEDs 
LED1 = 2
LED2 = 6
LED3 = 4

# Initialize the LEDs
grovepi.pinMode(LED1, "OUTPUT")
grovepi.pinMode(LED2, "OUTPUT")
grovepi.pinMode(LED3, "OUTPUT")

def soothing_pattern():
    i = 0
    while (i<=5):
        # Turn on the soothing pattern
        grovepi.digitalWrite(LED1, 1)
        time.sleep(0.5)
        grovepi.digitalWrite(LED1, 0)
        grovepi.digitalWrite(LED2, 1)
        time.sleep(0.5)
        grovepi.digitalWrite(LED2, 0)
        grovepi.digitalWrite(LED3, 1)
        time.sleep(0.5)
        grovepi.digitalWrite(LED3, 0)
        
        i += 1
        
        # Check if 0 is passed via command line
        if input_available():
            command = input().strip()
            if command == '0':
                break

def input_available():
    import select
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

if __name__ == "__main__":
    if len(sys.argv) == 2:
        pattern_on = int(sys.argv[1])
        if pattern_on == 1:
            soothing_pattern()
        elif pattern_on == 0:
            grovepi.digitalWrite(LED1, 0)
            grovepi.digitalWrite(LED2, 0)
            grovepi.digitalWrite(LED3, 0)
    else:
        print("Usage: python script.py [0/1]")
