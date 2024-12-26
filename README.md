# baby_monitor
Created an IoT-based baby monitor using Raspberry Pi &amp; Grove Pi 8 sensors and actuators to real-time monitor the baby's environment and rocking crib 
Steps to Implement.
1. Start node red from the RPI.
2. Import the flow from Flows.json
3. Execute the capture.py file in the terminal to run the flask server.
4. In the Execute node in the node red flow make sure to give the path of the sooth.py where you may place it in the RPI.
5. Create appropriate Influx Server and connections.
6. Create the connections to the azure dashboard.
7. Grafana Dahboard file -> Grafana Dashboard.json
8. Access the node red dahboard at the https:RIP-IPaddress:1880/ui
9. Train and link a Custom Vision model to the output buffer of the camera image.
10. Connect the camera to the RPI via PCIE slot.
11. Fasten the motor to the crib.
12. Setup the twilio messaging service by creating a free account on twilio.
    It takes a while for them to authenticate your account and provide you with a functioning Number for message notifications.
13. Create a TTS and STT service on azure using speech services and plugin the details into the voice node.

Influx DB Structure:
DB name: Group 4:
Measurements:
Al_cohol
Ambient_Light
Ambient_Sound
Baby_Distance
Baby_Room_Conditions
Baby_status
CH_4
C_O
H_2
L_PG
Movement_count
Not_Gas_Conditions
Not_Ideal_Env
Not_Ideal_Light
Not_Ideal_Noise
Pro_pane
Sm_oke

requirements for running the model:
RPI
16GB or more of SD card
Node red and grafana installed on the RPI

Sensors:
DH11 Temperature Sensor.
Ultrasonic Ranger.
Blue, Red, Green LEDs.
Sound Sensor.
Light Sensor.
Servo Motor.
Camera.
MQ2 Gas Sensor Which was simulated.

Technologies used:
Node red for development.
Node red dahboard for simple data visualisation and manual controls.
Azure services for STT, Dashboard and Custom Vision Model for Machine Learning and Detecting the baby status.
Influx DB for storing the Data.
Grafan Dashboard for localized Data analysis and visualization.

