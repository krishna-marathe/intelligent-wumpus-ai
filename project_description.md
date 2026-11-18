# Intelligent Wumpus Agent Simulator
**A Comprehensive Exploration of Artificial Intelligence & Mathematical Logic**

---

## 1. Project Overview & Core Idea

The **Intelligent Wumpus Agent Simulator** is a full-stack, visually rich web application built to demonstrate advanced concepts in Artificial Intelligence. Based on the classic "Wumpus World" computer science problem, this project goes far beyond a simple game by implementing an autonomous AI agent capable of logical deduction, probabilistic reasoning, and sensory-driven navigation.

The core idea is to drop an AI agent into a dark, procedurally generated maze filled with bottomless pits, a deadly Wumpus, and a bar of gold. The agent cannot "see" the maze; it can only perceive localized sensory inputs (percepts) such as a Breeze, a Stench, or a Glitter. Using pure mathematics and logic, the agent must map the environment, deduce the locations of traps, safely navigate to the gold, and escape.

This project serves as an interactive dashboard to visualize how an AI "thinks" in real-time, bridging the gap between theoretical AI mathematics and practical application.

---

## 2. Academic Constraints & Compliance
This project was specifically architected to adhere strictly to rigorous academic guidelines. The entire engine operates as a "white-box" mathematical model:
1. **No standard libraries (like `scikit-learn`, `TensorFlow`, `SymPy`) are used.** The logic deduction and probability engines rely exclusively on raw Python data structures.
2. **The project is implemented using a purely mathematical model.** The AI's decisions are calculated through custom-built First-Order Logic (FOL) Resolution Theorem Proving and fractional Bayesian probability equations.
3. **No built-in models or "black-box" machine learning models are used.** Every algorithm, from the A* pathfinding to the Conjunctive Normal Form (CNF) converter, was written entirely from scratch to prove mathematical competency.

---

## 2. Evolution of the Project

### Phase 1: The Foundation (What We Did First)
We started by building the core architecture of the classic AI problem:
*   **The World Engine:** We built a Python backend that generates the grid, places the Wumpus, Pits, and Gold, and enforces the rules of movement and scoring.
*   **The Logic Brain (FOL):** We built a Knowledge Base that uses strict **First-Order Propositional Logic**. As the agent moves, it records facts (Axioms) like `"No Breeze at (1,1)"` and uses mathematical resolution to *prove* whether an adjacent cell is guaranteed safe or contains a hazard.
*   **The UI Dashboard:** We created a premium, dark-mode web dashboard featuring a "Fog of War" canvas, allowing you to watch the agent explore while peering directly into its "thoughts" and "axioms" in real-time.

### Phase 2: The Enhancements (What We Added Later)
Once the foundation worked, we heavily upgraded the AI to make it truly intelligent and stabilized the system:
*   **Directional Percepts:** We added "High" and "Low" intensity to Stenches and Breezes. This acts like a radar, allowing the AI to instantly deduce hazard locations without needing to circle around them.
*   **Probabilistic Gambling:** Because mazes are random, strict logic sometimes fails (e.g., all paths are dangerous). We added a Bayesian probability engine so the AI can calculate the risk of surrounding cells and gamble its life on the lowest-risk tile (e.g., 15% risk vs 50% risk).
*   **Advanced Pathfinding (A* Search):** We upgraded the agent from basic BFS (Breadth-First Search) to A* Search, making its navigation to targets significantly faster and more efficient.
*   **Batch Simulation Engine:** We built an API that runs 100 games invisibly in the background, complete with "circuit breakers" to prevent the server from hanging, allowing us to get statistical win rates.
*   **Loop Prevention & "Graceful Give-Up":** We fixed edge cases where the AI would get stuck endlessly bouncing in corners by implementing a `known_pits` memory cache and teaching it to gracefully climb out and quit if the gold is completely walled off.

---

## 3. How the AI Thinks (The Core Pipeline)

Every time the agent takes a step, it executes this specific pipeline in a fraction of a second:
1.  **Perceive:** The agent looks at the tile it is standing on and reads the sensors (Breeze, Stench, Glitter).
2.  **Deduce (Logic):** It feeds those sensors to the Logic Engine, which updates its Axioms and returns a list of cells it has mathematically proven are 100% safe.
3.  **Evaluate:** 
    *   If it sees Glitter, it grabs the Gold.
    *   If it has the Gold, it activates "Homing" mode to pathfind back to the Exit and climb out.
    *   If it smells a High Stench, it shoots its arrow to kill the Wumpus.
4.  **Explore (Pathfind):** If it's just exploring, it uses **A* Search** to find the shortest path to the nearest unvisited safe cell.
5.  **Gamble (Fallback):** If there are no safe cells left to explore, it asks the Probability Engine for the lowest-risk tile and moves there, hoping it survives.

---

## 4. Modernizing a Classic: Differences from the Original Game

We took the classic 1973 academic Wumpus World and modernized it significantly:
*   **Interior Walls:** The original game is a completely open grid. Our version randomly generates interior walls, turning it into a true maze and making pathfinding drastically more complex.
*   **Grid Scale:** The original game is strictly a 4x4 grid. Ours is highly scalable (we use 8x8 by default), which requires much more advanced memory and pathfinding to solve.
*   **Intensity Sensors:** In the original game, percepts are binary (You either smell a stench, or you don't). Our game introduces `High` (directly facing) and `Low` (diagonal/distant) intensities, mimicking modern sensory radar.
*   **The Live UI:** Traditional Wumpus World is played in a text terminal. Ours features a dynamic graphical interface with a Fog of War, live axiom tracking, and probabilistic overlays, making the AI's internal math completely transparent to the user.

---

## 5. Technical Stack & Implementation

The project is structured as a decoupled Full-Stack application:

### Backend (Python / Flask)
- **`simulator.py`:** Contains the physical game engine, maze generation, state management, and the execution of physical actions.
- **`ai/logic_engine.py` & `probability_engine.py`:** Houses the Knowledge Base, First-Order Logic deduction routines, and the Probabilistic Risk Engine.
- **`ai/agent.py`:** The "brain" of the agent. It routes percepts, calculates paths, reacts to intensities, and executes the core pipeline.
- **`app.py`:** A Flask server that exposes the simulator and AI engine via REST API endpoints (`/api/init`, `/api/step`, `/api/batch`).

### Frontend (HTML / CSS / JavaScript)
- **Dynamic Dashboard:** A professional, dark-mode, glassmorphism UI built with Vanilla HTML/CSS.
- **Canvas Rendering (`renderer.js`):** The game grid is drawn using the HTML5 `<canvas>` API featuring dynamic gradients and a Fog of War layer.
- **Live AI Telemetry (`main.js`):** Displays exactly what the AI is thinking in real-time, tracking Axioms, Nodes Expanded, and printing the agent's logical deductions line-by-line.
