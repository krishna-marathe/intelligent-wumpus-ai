# Mathematical Foundations & Algorithms: In-Depth Guide

## 🚨 Academic Compliance & Constraint Adherence 🚨
This project was strictly engineered to comply with the highest academic standards, specifically adhering to the following constraints:
1. **No external AI/ML libraries** (e.g., `scikit-learn`, `TensorFlow`, `SymPy`) were used.
2. **No built-in or pre-trained models** (black-box algorithms) were utilized.
3. **Pure Mathematical Implementation**: Every single logical deduction, probability heuristic, and pathfinding algorithm was written 100% from scratch using pure Python mathematics and data structures. The Resolution Theorem Prover, the CNF Converter, and the Bayesian Probability calculator are entirely custom-built to prove a deep understanding of the underlying math.

---

This document is a technical deep-dive into the mathematical foundations, algorithms, and logic systems that power the Intelligent Wumpus Agent. It is designed to explain the theory so that anyone reading it can understand exactly how the AI operates under the hood.

---

## 1. The Language of the AI: Propositional Logic

The AI does not think in English; it thinks in **First-Order Propositional Logic**. When you look at the "Knowledge Base" panel in the UI, you are seeing the raw mathematical formulas (the "green scribbles") that the AI is using to deduce the state of the world.

### What is an Axiom?
In logic, an **Axiom** is a fundamental rule or a proven fact that is accepted as absolute truth. The AI's brain is essentially just a giant list of axioms. 
*   Some axioms are **Rules of the Game** (e.g., "A stench means a Wumpus is nearby").
*   Some axioms are **Observations** (e.g., "I am standing at (0,0) and I feel a breeze").
By cross-referencing these axioms, the AI can mathematically *prove* if a tile is safe or deadly.

### Decoding the Green Scribbles
The UI prints the AI's internal axioms using standard mathematical symbols. Here is how to read them:

#### Example 1: `¬S_0_0`
*   **`¬`** (Logical NOT): This symbol negates whatever comes after it.
*   **`S`** (Stench): Represents the presence of a Stench.
*   **`0_0`**: The X, Y coordinates on the grid.
*   **Translation:** *"It is a proven fact that there is NO Stench at coordinate (0,0)."*

#### Example 2: `Equivalent(S_7_7, W_6_7 ∨ W_7_6)`
*   **`Equivalent`** (↔): This means both sides of the equation imply each other. If the left side is true, the right side is true (and vice versa).
*   **`W`** (Wumpus): Represents the location of the Wumpus.
*   **`∨`** (Logical OR): This means at least one of the conditions is true.
*   **Translation:** *"Smelling a Stench at cell (7,7) means the EXACT SAME THING as the Wumpus being located at (6,7) OR the Wumpus being located at (7,6)."*

### Why does the AI start with 132 Axioms?
Before the agent takes a single step, the Knowledge Base lists 132 axioms. Why? Because the AI does not magically know how the game works! It must be explicitly taught the **Laws of Physics** for the maze. 
For every single one of the 64 cells in the 8x8 grid, the backend must generate a rule defining exactly which adjacent cells could contain a Wumpus if a Stench is smelled there. Generating the "Stench Rule" and "Breeze Rule" for all 64 cells takes over 100 structural axioms.

---

## 2. Navigating the Graph: Pathfinding Algorithms

The maze is mathematically treated as a **Graph** (a collection of connected points). 

### What is a Node?
A **Node** is simply a single tile or square on the grid. When the dashboard tracks **"Nodes Expanded,"** it is counting how many individual tiles the algorithm had to mathematically calculate and check before it found a path to its destination.

### Breadth-First Search (BFS)
When the AI wants to move from point A to point B, it can use BFS.
*   **How it works:** BFS explores the maze like a ripple in a pond. It checks all tiles 1 step away, then all tiles 2 steps away, expanding uniformly in all directions.
*   **Pros & Cons:** It mathematically guarantees it will find the shortest path. However, it is "dumb"—it wastes time checking nodes in the complete opposite direction of the target. This results in a high "Nodes Expanded" count.

### A* (A-Star) Search
To make the AI more efficient, we implemented A* Search.
*   **How it works:** A* is a "smart" search algorithm. It uses a mathematical guess called a **Heuristic** (in this case, the *Manhattan Distance*, which calculates the straight-line distance to the target). Instead of expanding in a perfect circle, A* prioritizes checking tiles that physically move it closer to the target.
*   **Pros & Cons:** It still guarantees the shortest path, but it ignores the "wrong directions," resulting in a drastically lower "Nodes Expanded" count. It is much faster and computationally lighter than BFS.

---

## 3. Code Architecture: Which Part Does What?

The project is cleanly decoupled into specialized files. Here is an in-depth map of the backend architecture:

### `backend/simulator/simulator.py` (The Physical World)
*   **Role:** The Game Engine.
*   **What it does:** It generates the physical 8x8 grid. It runs a Randomized Depth-First Search (DFS) algorithm to carve a valid maze layout, then drops the walls, Pits, Wumpus, and Gold into the world. It enforces the laws of physics (e.g., if the agent moves into a pit, it updates `agent_alive = False`).

### `backend/ai/logic_engine.py` (The Logical Brain)
*   **Role:** The First-Order Logic Theorem Prover.
*   **What it does:** It stores the 132 structural axioms. When the agent observes a percept, this engine converts the observation into Conjunctive Normal Form (CNF). It then runs a **Resolution Algorithm**—a mathematical proof system that tests if a specific cell contains a pit or a Wumpus by looking for logical contradictions.

### `backend/ai/probability_engine.py` (The Gambling Brain)
*   **Role:** The Bayesian Risk Calculator.
*   **What it does:** If the `logic_engine` cannot prove any safe paths (because the maze is random and sometimes unfair), this engine takes over. It calculates the fractional probability of a pit existing in an unknown cell by dividing the number of adjacent breezy cells by the total number of safe neighboring cells. It outputs a risk percentage (e.g., 20% risk of death).

### `backend/ai/agent.py` (The Central Nervous System)
*   **Role:** The AI Controller.
*   **What it does:** This script manages the core pipeline. It asks the `simulator` what it senses, passes those senses to the `logic_engine`, retrieves the safe cells, and then runs the `A*` algorithm to plot a course to the nearest safe cell. If no safe cells exist, it asks the `probability_engine` for the best gamble. It returns the final chosen action (e.g., `TURNLEFT` or `FORWARD`) to the simulator.

### `backend/app.py` (The Web Server)
*   **Role:** The API Router.
*   **What it does:** It wraps the entire Python simulation in a Flask web server. It listens for HTTP requests from the frontend UI (like clicking the "Step" button) and triggers the AI to take a turn, returning the updated state of the game as JSON data. It also hosts the `batch_simulate` endpoint, which runs 100 simulations in a silent `while` loop to generate statistical reports.
