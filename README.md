# Max Fishing Path Finder 🐟

This Python program finds the **maximum sum of fish values** collectable in a grid, starting from any non-zero cell and moving through adjacent (up/down/left/right) non-zero cells without revisiting any cell.

## 💡 Problem Description

You are given a grid where each cell contains either:

- A positive integer: the amount of fish you can collect from that cell, or
- Zero: meaning the cell is empty and cannot be used.

The goal is to explore all valid paths from every non-zero cell and compute the maximum fish value that can be collected along any such path, without revisiting any cell.

---

## 📌 Example

Input grid:
```python
grid = [
    [0, 2, 1, 0],
    [4, 0, 0, 3],
    [1, 0, 0, 4],
    [0, 3, 2, 0]
]
````

Expected output:

```
7
```

Explanation: The optimal path collects the fish values `3 -> 4`.

---

## 🔍 Algorithm

* **Depth-First Search (DFS)** is used to explore all valid paths.
* A `visited` set is used to avoid revisiting cells.
* All directions (up, down, left, right) are considered from each cell.
* At each step, we track the current total and update a global maximum if a better path is found.

---

## 🧠 Functions Overview

* `start(grid, m, n)`: Iterates over the grid and starts a DFS from every non-zero cell.
* `check(grid, i, j, visited)`: Checks whether a cell is within bounds, non-zero, and not already visited.
* `maxFishing(...)`: Recursive DFS that computes the total fish sum for each valid path.

---

## ▶️ How to Run

```bash
python max_fishing.py
```

Make sure your Python version is 3.6+.

---

## 🛠 Developer

Developed by [Mohammad Amin Haji Alirezaei](https://github.com/mahajialirezaei)
Feel free to ⭐️ this repo or open an issue if you'd like to contribute or have questions!

---

