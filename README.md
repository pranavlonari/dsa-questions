# DSA Questions Collection

Welcome to my Data Structures and Algorithms questions repository! This collection contains detailed solutions, approaches, and complexity analyses for various DSA problems.

## 📚 Question List

| # | Problem | Difficulty | Topics | Solution |
|---|---------|------------|--------|----------|
| 1 | [All Nodes Distance K in Binary Tree](#all-nodes-distance-k-in-binary-tree) | Medium | Binary Tree, Tree, BFS | [View](./All%20Nodes%20Distance%20K%20in%20Binary%20Tree) |
| 2 | [Copy List with Random Pointer](#copy-list-with-random-pointer) | Medium | Graph, Linked List, Hash Table | [View](./Copy%20List%20with%20Random%20Pointer) |
| 3 | [Integer to English Words](#integer-to-english-words) | Medium | DFS, Graph, Array | [View](./Integer%20to%20English%20Words) |
| 4 | [LRU Cache](#lru-cache) | Medium | BFS, Graph, Linked List | [View](./LRU%20Cache) |
| 5 | [Maximum Number of Robots Within Budget](#maximum-number-of-robots-within-budget) | Medium | Tree, Graph, Array | [View](./Maximum%20Number%20of%20Robots%20Within%20Budget) |
| 6 | [Number of Ways to Select Buildings](#number-of-ways-to-select-buildings) | Medium | Graph, Array, String | [View](./Number%20of%20Ways%20to%20Select%20Buildings) |
| 7 | [Reorganize String](#reorganize-string) | Medium | BFS, DFS, Graph | [View](./Reorganize%20String) |
| 8 | [Rotting Oranges](#rotting-oranges) | Medium | BFS, Graph, Array | [View](./Rotting%20Oranges) |
| 9 | [Word Break II](#word-break-ii) | Medium | DFS, Graph, Hash Table | [View](./Word%20Break%20II) |

## 🔍 Search by Topic

### Array
- [Integer to English Words](./Integer%20to%20English%20Words)
- [LRU Cache](./LRU%20Cache)
- [Maximum Number of Robots Within Budget](./Maximum%20Number%20of%20Robots%20Within%20Budget)
- [Number of Ways to Select Buildings](./Number%20of%20Ways%20to%20Select%20Buildings)
- [Reorganize String](./Reorganize%20String)
- [Rotting Oranges](./Rotting%20Oranges)
- [Word Break II](./Word%20Break%20II)

### BFS
- [All Nodes Distance K in Binary Tree](./All%20Nodes%20Distance%20K%20in%20Binary%20Tree)
- [LRU Cache](./LRU%20Cache)
- [Reorganize String](./Reorganize%20String)
- [Rotting Oranges](./Rotting%20Oranges)

### Binary Tree
- [All Nodes Distance K in Binary Tree](./All%20Nodes%20Distance%20K%20in%20Binary%20Tree)

### DFS
- [All Nodes Distance K in Binary Tree](./All%20Nodes%20Distance%20K%20in%20Binary%20Tree)
- [Integer to English Words](./Integer%20to%20English%20Words)
- [Reorganize String](./Reorganize%20String)
- [Word Break II](./Word%20Break%20II)

### Graph
- [All Nodes Distance K in Binary Tree](./All%20Nodes%20Distance%20K%20in%20Binary%20Tree)
- [Copy List with Random Pointer](./Copy%20List%20with%20Random%20Pointer)
- [Integer to English Words](./Integer%20to%20English%20Words)
- [LRU Cache](./LRU%20Cache)
- [Maximum Number of Robots Within Budget](./Maximum%20Number%20of%20Robots%20Within%20Budget)
- [Number of Ways to Select Buildings](./Number%20of%20Ways%20to%20Select%20Buildings)
- [Reorganize String](./Reorganize%20String)
- [Rotting Oranges](./Rotting%20Oranges)
- [Word Break II](./Word%20Break%20II)

### Hash Table
- [Copy List with Random Pointer](./Copy%20List%20with%20Random%20Pointer)
- [LRU Cache](./LRU%20Cache)
- [Word Break II](./Word%20Break%20II)

### Linked List
- [Copy List with Random Pointer](./Copy%20List%20with%20Random%20Pointer)
- [LRU Cache](./LRU%20Cache)

### Stack
- [Integer to English Words](./Integer%20to%20English%20Words)

### String
- [Integer to English Words](./Integer%20to%20English%20Words)
- [Maximum Number of Robots Within Budget](./Maximum%20Number%20of%20Robots%20Within%20Budget)
- [Number of Ways to Select Buildings](./Number%20of%20Ways%20to%20Select%20Buildings)
- [Reorganize String](./Reorganize%20String)
- [Rotting Oranges](./Rotting%20Oranges)
- [Word Break II](./Word%20Break%20II)

### Tree
- [All Nodes Distance K in Binary Tree](./All%20Nodes%20Distance%20K%20in%20Binary%20Tree)
- [Maximum Number of Robots Within Budget](./Maximum%20Number%20of%20Robots%20Within%20Budget)

### Two Pointers
- [Copy List with Random Pointer](./Copy%20List%20with%20Random%20Pointer)
- [Maximum Number of Robots Within Budget](./Maximum%20Number%20of%20Robots%20Within%20Budget)
- [Number of Ways to Select Buildings](./Number%20of%20Ways%20to%20Select%20Buildings)
- [Rotting Oranges](./Rotting%20Oranges)

## 📖 Question Details

### All Nodes Distance K in Binary Tree
**Difficulty:** Medium  
**Topics:** Binary Tree, Tree, BFS, DFS, Graph  
**Key Concepts:**
- restatement...
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

**Quick Approach:**
1. DFS (or iterative traversal) to fill `parent` pointers and also find the `targetNode` matching the given `target` value....

[📄 View Full Solution](./All%20Nodes%20Distance%20K%20in%20Binary%20Tree)

---

### Copy List with Random Pointer
**Difficulty:** Medium  
**Topics:** Graph, Linked List, Hash Table, Two Pointers  
**Key Concepts:**
- statement: Given the head of a linked list where each node has an extra `random` pointer that can po...
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

**Quick Approach:**
1. **Weave copies**: For each original node `cur`, create `copy = new Node(cur.val)` and insert it after `cur` (`cur.next = copy; copy.next = nextOrig...

[📄 View Full Solution](./Copy%20List%20with%20Random%20Pointer)

---

### Integer to English Words
**Difficulty:** Medium  
**Topics:** DFS, Graph, Array, String, Stack  
**Key Concepts:**
- restatement...
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

**Quick Approach:**
1. **Handle zero:** If `num == 0`, return `"Zero"`....

[📄 View Full Solution](./Integer%20to%20English%20Words)

---

### LRU Cache
**Difficulty:** Medium  
**Topics:** BFS, Graph, Linked List, Hash Table, Array  
**Key Concepts:**
- ...
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

**Quick Approach:**
...

[📄 View Full Solution](./LRU%20Cache)

---

### Maximum Number of Robots Within Budget
**Difficulty:** Medium  
**Topics:** Tree, Graph, Array, String, Two Pointers  
**Key Concepts:**
- restatement Given two arrays `chargeTimes` and `runningCosts` of length `n` and a `budget`, find the...
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

**Quick Approach:**
...

[📄 View Full Solution](./Maximum%20Number%20of%20Robots%20Within%20Budget)

---

### Number of Ways to Select Buildings
**Difficulty:** Medium  
**Topics:** Graph, Array, String, Two Pointers  
**Key Concepts:**
- ...
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

**Quick Approach:**
...

[📄 View Full Solution](./Number%20of%20Ways%20to%20Select%20Buildings)

---

### Reorganize String
**Difficulty:** Medium  
**Topics:** BFS, DFS, Graph, Array, String  
**Key Concepts:**
- restatement: Given a string `s`, rearrange its characters so that no two adjacent characters are the...
- **Time Complexity:** O(n log k)
- **Space Complexity:** O(k)

**Quick Approach:**
1. Count frequencies of characters. Let `n = s.length()`. If any `freq[i] > (n+1)/2` return `""`....

[📄 View Full Solution](./Reorganize%20String)

---

### Rotting Oranges
**Difficulty:** Medium  
**Topics:** BFS, Graph, Array, String, Two Pointers  
**Key Concepts:**
- restatement**...
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

**Quick Approach:**
1. Initialize queue with all `2`s (rotten), and count all `1`s (fresh)....

[📄 View Full Solution](./Rotting%20Oranges)

---

### Word Break II
**Difficulty:** Medium  
**Topics:** DFS, Graph, Hash Table, Array, String  
**Key Concepts:**
- restatement...
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

**Quick Approach:**
1. Build `dict` from `wordDict` and compute `canBreak` boolean DP from back to front:...

[📄 View Full Solution](./Word%20Break%20II)

---

## 🚀 How to Use This Repository

1. **Browse by Topic:** Use the topic sections above to find questions by category
2. **Search:** Use GitHub's search feature (press `/` and type your query)
3. **View Solutions:** Click on any question link to see detailed solution with:
   - Problem restatement
   - Multiple approaches with pros/cons
   - Step-by-step explanation
   - Complexity analysis
   - Clean, commented code

## 📝 Solution Format

Each question includes:
- ✅ **Problem Restatement** - Clear problem description
- ✅ **Quick Script** - What to say to the interviewer
- ✅ **Multiple Approaches** - Different solutions with trade-offs
- ✅ **Detailed Explanation** - Step-by-step walkthrough
- ✅ **Complexity Analysis** - Time and space complexity
- ✅ **Implementation** - Clean, commented code

## 🛠️ Interactive Web Interface

For a better browsing experience with search and filtering, open [index.html](./index.html) in your browser!

## 📊 Statistics

- **Total Questions:** 9
- **Easy:** 0
- **Medium:** 9
- **Hard:** 0

---

## 🤝 Contributing

This is a personal learning repository. Questions and solutions are continuously being added as I practice more problems.

## 📌 Note

All solutions are interview-ready with detailed explanations, multiple approaches, and complexity analyses. The code is clean, well-commented, and follows best practices.

---

**Last Updated:** November 12, 2025

*Happy Coding! 🚀*
