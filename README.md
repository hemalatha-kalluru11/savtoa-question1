# Candidate ID: SAV116

# savtoa-Question1
Savtoa Technologies Round 2 Technical Assessment -Question1

# Simple Smart Device Control System

This project is a small Python program created to understand and apply
Object-Oriented Programming concepts.

The idea is to control different devices like a Motor and a Light using
the same controller. Each device manages its own ON and OFF state, and
the controller works without knowing the internal details of the device.

# What this project shows
- How a base class can be used for common behavior
- How different devices can inherit from the same class
- How a controller can work with any device type
- How device state can be protected from direct external changes

# How to run the program
Make sure Python 3 is installed on your system.

python main.py

# Output
Motor has started
Motor has stopped
Light switched on
Light switched off

# Note
This solution is designed to be easily extended by adding new device
classes without changing the existing controller logic.
