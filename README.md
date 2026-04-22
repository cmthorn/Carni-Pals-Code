# Carni-Pals-Code
Claw Machine Project 🎮🦾
Overview

This project is a custom-built claw machine, designed to simulate the functionality of an arcade-style prize grabber using hardware components and embedded programming.

The system combines mechanical design, electronics, and software to control movement, gripping, and user interaction. The goal is to create a fully functional, responsive claw machine that can pick up and move objects with precision.

Features
3-Axis Movement System
Controls horizontal (X, Y) and vertical (Z) motion of the claw.
Claw Gripping Mechanism
Opens and closes to grab objects.
User Input Controls
Allows users to move the claw and trigger the grab action.
Microcontroller-Based Control
Uses an Arduino to process inputs and control motors.
Modular Design
Components can be upgraded or swapped as needed.
Hardware Components
Arduino Nano (or similar microcontroller)
DC Motors (for movement and claw operation)
Motor Drivers (to control motor speed and direction)
Power Supply (appropriate voltage for motors and Arduino)
Frame/Chassis (custom-built structure)
Wiring and connectors
Software Overview

The software handles:

Reading user inputs
Controlling motor direction and speed
Coordinating movement sequences
Operating the claw mechanism

The code is structured to keep hardware control modular, making it easier to debug and expand.

How It Works (Conceptually)
The user provides input (buttons, joystick, etc.)
The Arduino interprets the input signals
Motor drivers receive commands from the Arduino
Motors move the claw in the desired direction
The claw opens/closes to grab objects
Project Structure
/claw-machine
│── /src            # Main Arduino code
│── /hardware       # Schematics, wiring diagrams
│── /docs           # Design notes and planning
│── README.md


Embedded systems programming
Motor control and power management
Mechanical design and stability
Debugging hardware/software interactions
Contributing

Contributions are welcome. If you have ideas for improvements or new features, feel free to submit a pull request or open an issue.

License

This project is open-source and available under the MIT License.
