import sys
from Adafruit_IO import MQTTClient
from simple_ai import *
from physical import *
from uart import *

AIO_FEED_IDs = ["nutnhan1","nutnhan2"]
AIO_USERNAME = "phuhd4"
AIO_KEY = ""

# Open the file for reading (change 'your_file.txt' to the actual file path)
file_path = 'key.txt'

def getKeyAIO():
    try:
        with open(file_path, 'r') as file:
            # Read and process one line at a time
            line = file.readline()
            while line:
                # Do something with the line (e.g., print it)
                print(line.strip())  # strip() removes leading/trailing whitespace
                # Read the next line
                line = file.readline()
            return line
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")


def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs :
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")
def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def  message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " ,feed id: " + feed_id)


AIO_KEY = getKeyAIO()
print(AIO_KEY)
client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
print("Hello world")