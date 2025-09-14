## Installing & Running:
To run this program you must have the following installed:

- Python 3.13 or later,
- SimConnect,

Python can be installed from the official python website downloads page (https://www.python.org/downloads/) or on the Microsoft store. SimConnect must be installed using the pip command in command prompt. This can be done with the following command:

```
pip install SimConnect
```

Should that fail, the following alternatives can be used:

```
python3 -m pip install SimConnect
```

```
pip3 install SimConnect
```

Having installed the prerequisites, the file "Flight_Sim_Snapshots.py" can be double clicked and run with the simulator running; the program will crash if the simulator is not already running. To view the code, open it in your IDE of choice.

## Functionality:
This tool can be used to take snapshots of your current position and speed to be restored later. This can be useful for saving before a critical phase of flight or when practicing landings if you don't want to have to set things up again or go through the whole flight again should things not go to plan.

Below is a screenshot of the tool:
<img width="402" height="182" alt="image" src="https://github.com/user-attachments/assets/a865e1d2-12be-443c-90ae-1efa72af49b1" />


To save your location, press the "Save Position" button. Having already saved a position, you can press the "Load Last Position Button" to reestore your saved position.

## Features To Come:
I would like to make it save acceleration vectors so that loading saved positions can be less jarring when there are large differences in acceleration between when the snapshot was saved and loaded. I would also like to make it save engine throttle position and prevent the program from crashing when it is opened without the simulator.
