# Terminus_Raze


Terminus Raze
-
Terminus Raze is an autonomous defense and surveillance system designed to secure high-risk environments with minimal human intervention. Built with an emphasis on intelligent perception, precise locomotion, and real-time response, it combines computer vision, embedded control, and mechanical design into one cohesive platform.

We were not able to complete the automation and app deployment. We plan to implement them later on, as our experience in those domains increase. Though we did use Flask to stream the Computer Vison output, and give the servos simple control.

Overview:
-
Terminus Raze was to function as an autonomous patrol and defense bot Which is Capable of the following features:
    
*   Navigating secure or sensitive areas autonomously.
* Detecting and tracking potential threats using computer vision.
* Deploying defensive mechanisms (weapons, alarms, or deterrents) upon confirmed threat detection
* Communicating with a mobile app for manual control, live monitoring, and data updates.

Components and Tech stack used:
-
The Computer Vison was run on a Raspberry Pi 4 Model B, using an External Third Party Camera. and the Servo motors and locomotion was done using an ESP32 WROOM1 board.

The Python Libraries used on this were OpenCV, Tensorflow, Serial, and Flask. 

The Shooter underwent two iterations, the first one was based on the Airsoft Guns. We used Pneumatics to achieve this, and it was sufficient for an early demonstration. The Pneumatics operation and lack of constant Air Pressure caused us to change the idea later.

The Second iteration was based on the CrunchLabs turret. We 3D Printed the parts for it and tried it. It was not as good as the pneumatic gun in terms of performance, but served to be barely sufficient for demonstration.

The STL Files for 3D printing the crunchlabs turret is here

https://www.printables.com/model/1258347-ir-turret-crunchlabs-io1-ver
