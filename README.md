# VPython Planetary Orbit Visualization
 A visualization of the different orbits of the solar system using the Vpython library


## Overview

3d Space Visualizer is a Python-based solar system visualization program that uses the VPython library to create a 3D representation of the solar system, including the sun, planets, and an exoplanet, in a graphical user interface. Additionally, a start menu allows you to start the visualization or quit the program.

## Requirements

To run PyGrapher and reproduce the experiment, you will need:

- Python 3.x installed on your system (https://www.python.org/downloads/)
- VPython library (VPython 7) for 3D visualization (install via pip: `pip install vpython`)
- Pygame library for the start menu (install via pip: `pip install pygame`)
- A compatible font file for the start menu (e.g., "Lato-Regular.ttf") in a "Fonts" directory within the same directory as your start menu script.

## Usage

### Start Menu (start.py)

- Execute `start.py` using Python: `python start.py` (or `python3 start.py` on some systems).

- The start menu will appear with two buttons: "Start" and "Quit."

- Click the "Start" button to begin the solar system visualization.

- Click the "Quit" button to exit the program.

### Solar System Visualization (main.py)

- Once you click "Start" in the start menu, the solar system visualization will begin.

- The visualization will display the sun, planets, and an exoplanet.

- The objects' positions and movements are calculated based on their orbital periods and radii. The `rate` function is used to control the animation speed.

- The positions of the sun and planets are calculated using real data from the "de421.bsp" ephemeris file.

- The Closest Habitable Zone (CHZ) is represented by two rings around the sun. The inner ring marks the minimum distance, while the outer ring marks the maximum distance from the sun where a planet could potentially support life.

## Customization

- You can customize the appearance of the objects, fonts, button sizes, and other aspects by modifying the code in `start.py` and `main.py`.

- You can replace the background image ("background.jpg") in the same directory with your own image to change the start menu's background.

## Credits

This project was developed by Kushal Prajapati as a visualization experiment.

The VPython library (https://vpython.org/) was used for 3D visualization.

The Pygame library (https://www.pygame.org/) was used for the start menu.

## License

This project is open-source and available under the MIT license. See the LICENSE file for details.
