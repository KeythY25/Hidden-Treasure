# Hidden-Treasure
 2D simulation game where players navigate a grid map to locate hidden treasure using artificial intelligence search algorithms

This repository contains the implementation of Hidden Treasure Hunt AI, a 2D simulation game that leverages artificial intelligence (AI) search algorithms to guide players in locating hidden treasure on a grid-based map. The project showcases the practical use of BFS (Breadth-First Search), A* (A-Star) Algorithm, and Hill Climbing techniques for efficient pathfinding and decision-making.
 
# Features

Dynamic Gameplay: Randomized grid initialization, starting point, and treasure location.

AI Search Algorithms:

BFS: Systematic exploration for uncovering clues.

A*: Optimized pathfinding using heuristics.

Hill Climbing: Efficient fine-tuning when close to the treasure.

Obstacle Navigation: Avoid static obstacles while exploring the map.

Energy Management: Players must reach the treasure before running out of energy.

# Repository Contents
p1.py: Main script containing the game logic and AI algorithms.

flowchart.png: Visual representation of the AI decision-making process.

README.md: This documentation file.

# FlowChart
<img width="359" alt="image" src="https://github.com/user-attachments/assets/1f5aa46b-4794-4226-8969-52c59bc6d8d8" />

# Getting Started

## Prerequisites

- Python 3.10 or higher

## Dependencies

-Standard libraries: collections, heapq, random

## Installation

1. Clone this  repository to your local machine:

 git clone <repository-link>

2. Navigate to the project folder:

 cd hidden-treasure-hunt

## Running the Game

1. Ensure Python 3.10 or higher is installed on your machine.
 
2. Execute the game script:
 python3 p1.py

3.Follow on-screen instructions to play the game.

## How It Works

1.Grid Initialization: A 10x10 grid is generated with random starting and treasure locations. Obstacles are predefined.

2.Search Techniques:

 - BFS is used to locate the nearest clue.
  
 - A* navigates towards the treasure using cost and heuristic estimation.
  
 - Hill Climbing is employed for final adjustments when the treasure is within proximity.

3. Winning Condition: The treasure is found before energy depletion.

# Tools Used

- Programming Language: Python 3.10

 Chosen for its readability and support for AI and algorithmic implementations.

- IDE: Visual Studio Code

 Features: Debugging tools, syntax highlighting, and extensions for Python.

- Screen Recording: Screencastify

 Used for creating a screencast to demonstrate the game's execution.

- Flowchart Design: Lucidchart

 Created the flowchart visualizing the AI search logic.

- Version Control: GitHub

 Repository management and collaboration.

- Operating System: macOS

 Development and testing were performed on macOS.

# License

This project is open-source and available under the MIT License.

# Acknowledgments

Python Standard Library: Documentation and tools.

Amit Patel: Insightful explanation of A* Algorithm (Game Programming).





