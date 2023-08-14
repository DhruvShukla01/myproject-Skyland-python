# Skyland Game

**Author:** Dhruv Shukla
**Date:** 9 June, 2023

The "Skyland" game is a one-level platform video game where the player controls an avatar to navigate through a challenging landscape, avoid obstacles, and collect trophies. The game features dynamic obstacles, trophies, and an AI-controlled enemy.

## Table of Contents

- [Introduction](#skyland-game)
- [Table of Contents](#table-of-contents)
- [File Structure](#file-structure)
- [Getting Started](#getting-started)
- [Gameplay](#gameplay)
- [In-Depth File Breakdown](#in-depth-file-breakdown)
  - [Part A: skyland.py](#part-a-skylandpy)
  - [Part B: obstacles.py](#part-b-obstaclespy)
  - [Part C: avatar.py](#part-c-avatarpy)
  - [Part D: main.py](#part-d-mainpy)
- [License](#license)
    
## File Structure

The "Skyland" game is divided into multiple Python files, each responsible for specific aspects of the game's functionality. Here's an overview of the file structure:

- `skyland.py`: Main game controller and GUI setup.
- `obstacles.py`: Contains the `Land`, `Trophy`, and `AI` classes for creating obstacles, trophies, and AI-controlled enemies.
- `avatar.py`: Defines the `Avatar` class for the player's character.
- `main.py`: The main execution script that sets up the game and GUI.
  
## Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Installation
1. Clone this repository:
   ```bash
   git clone [repo-link]
   ```
2. Navigate to the directory
   ```
   cd [directory-name]
   ```
3. **Running the Game**
   Execute the skyland.py game file:
   ``` bash
   python skyland.py
   
## Gameplay

The objective of the "Skyland" game is to control the player's avatar through the game's landscape, avoiding obstacles and collecting trophies. 

-Use the arrow keys to control the avatar:
  - Left Arrow: Move left
  - Right Arrow: Move right
  - Up Arrow: Jump
  - Down Arrow: Move down

Navigate through the landscape, strategically avoiding obstacles and AI-controlled enemies, while aiming to collect all trophies placed within the game environment.

The game concludes under the following conditions:
- You successfully collect all trophies, achieving victory.
- Your avatar collides with obstacles or AI-controlled enemies, leading to defeat.

Master the controls and explore the game's mechanics to achieve the highest score and conquer the challenging landscape!


## In-Depth File Breakdown

### Part A: skyland.py

This file contains the main game controller and GUI setup. It includes the `Skyland` class, which initializes the game environment, obstacles, trophies, and AI-controlled enemies. The class manages player interactions and updates the game state.

### Part B: obstacles.py

This file defines the `Land`, `Trophy`, and `AI` classes. The `Land` class creates the landscape and obstacles. The `Trophy` class handles trophy creation, replacement, and collision detection. The `AI` class manages the behaviour of AI-controlled enemies.

### Part C: avatar.py

This file contains the `Avatar` class, which represents the player's character. The class handles avatar movement, collision detection with obstacles, and trophy collection.

### Part D: main.py

This script sets up the game's graphical user interface (GUI) using the `Tkinter` library. It creates a canvas to display game elements and initializes an instance of the `Skyland` class, representing the main game controller.

## License

Theis project is licensed under the [BSD 2-Clause License](LICENSE)
