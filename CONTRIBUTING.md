# Contributing Guide

## How to Add New Questions

When you add a new DSA question to this repository, follow these steps to maintain consistency:

### Step 1: Create the Question File

Create a new markdown file (or text file) with the question name as the filename. For example:

- `Two Sum`
- `Merge K Sorted Lists`
- `LRU Cache`

### Step 2: Follow the Standard Format

Each question file should include:

````markdown
# Problem restatement

[Clear problem description with examples]

# Quick script to say to the interviewer

1. "I will..."
2. "Then I'll..."
3. "This yields..."

# Approaches considered (pros/cons)

1. **Approach 1** — description
   - Pros: ...
   - Cons: ...
2. **Approach 2 (chosen)** — description
   - Pros: ...
   - Cons: ...

# Detailed chosen approach (step-by-step)

Data structures:

- ...

Steps:

1. ...
2. ...

# Complexity (discussion)

- Time: O(...)
- Space: O(...)

# Code implementation

```java
// Clean, commented code here
```
````

\```

````

### Step 3: Update questions.json

Add a new entry to the `questions` array in `questions.json`:

```json
{
  "id": 5,
  "title": "Your Question Title",
  "fileName": "Your Question Title",
  "difficulty": "Easy|Medium|Hard",
  "topics": ["Topic1", "Topic2"],
  "companies": ["Company1", "Company2"],
  "leetcodeNumber": 123,
  "summary": "Brief one-line summary",
  "keyApproach": "Quick approach overview",
  "complexity": {
    "time": "O(n)",
    "space": "O(1)"
  },
  "approaches": [
    "Approach 1",
    "Approach 2"
  ],
  "tags": ["tag1", "tag2"]
}
````

Also update:

- `metadata.totalQuestions` (increment by 1)
- `statistics` (increment the appropriate difficulty count)
- `topicIndex` (add question ID to relevant topics)
- `difficultyIndex` (add question ID to appropriate difficulty)

### Step 4: Update README.md

Add a new row to the question table:

```markdown
| 5 | [Your Question](#your-question) | Medium | Topics | [View](./Your%20Question%20Title) |
```

Add a new section in the "Question Details" area:

```markdown
### Your Question Title

**Difficulty:** Medium  
**Topics:** Topic1, Topic2  
**Key Concepts:**

- Key concept 1
- Key concept 2
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

**Quick Approach:**

1. Step 1
2. Step 2
3. Step 3

[📄 View Full Solution](./Your%20Question%20Title)

---
```

Update topic sections if needed.

### Step 5: Update index.html

Add a new question object to the `questions` array in the JavaScript section:

```javascript
{
    id: 5,
    title: "Your Question Title",
    difficulty: "Medium",
    topics: ["Topic1", "Topic2"],
    summary: "Brief description...",
    timeComplexity: "O(n)",
    spaceComplexity: "O(1)",
    file: "Your Question Title",
    keyApproach: "Brief approach..."
}
```

Update the stats in the header section:

- `id="totalQuestions"` (increment)
- Update difficulty count accordingly

### Step 6: Commit Your Changes

```bash
git add .
git commit -m "Add: Your Question Title"
git push origin master
```

## File Naming Conventions

- Use the exact problem name as the filename
- Spaces are allowed in filenames
- No file extensions needed (or use .md if preferred)
- Be consistent with capitalization

## Quality Checklist

Before committing a new question, ensure:

- [ ] Problem restatement is clear and includes examples
- [ ] Multiple approaches are discussed with pros/cons
- [ ] Chosen approach has step-by-step explanation
- [ ] Complexity analysis is included
- [ ] Code is clean, commented, and tested
- [ ] questions.json is updated
- [ ] README.md is updated
- [ ] index.html is updated
- [ ] All statistics are correct

## Topic Categories

Use consistent topic names:

- **Data Structures:** Array, String, Linked List, Stack, Queue, Tree, Binary Tree, Graph, Hash Table, Heap, Trie
- **Algorithms:** Sorting, Searching, BFS, DFS, Binary Search, Two Pointers, Sliding Window, Greedy, Divide and Conquer
- **Techniques:** Dynamic Programming, Backtracking, Recursion, Memoization, Bit Manipulation
- **Advanced:** Union Find, Segment Tree, Fenwick Tree, Topological Sort

## Difficulty Guidelines

- **Easy:** Basic data structure operations, simple algorithms
- **Medium:** Multiple approaches needed, moderate complexity
- **Hard:** Complex algorithms, multiple techniques combined, advanced data structures

## Example Pull Request Template

```
## New Question: [Question Title]

**Difficulty:** Medium
**Topics:** Topic1, Topic2
**LeetCode #:** 123

### Changes
- Added question file with detailed solution
- Updated questions.json
- Updated README.md
- Updated index.html
- Updated statistics

### Checklist
- [x] Followed standard format
- [x] Updated all necessary files
- [x] Verified statistics are correct
- [x] Tested index.html locally
```

## Testing Your Changes

### Test README.md

1. View on GitHub or use a markdown previewer
2. Check all links work correctly
3. Verify table formatting

### Test index.html

1. Open `index.html` in a browser
2. Test search functionality
3. Test all filter buttons
4. Click on question cards to verify links
5. Check responsive design on mobile

### Test questions.json

1. Validate JSON syntax using a JSON validator
2. Ensure all IDs are unique
3. Verify indices are updated correctly

## Tips

1. **Use URL encoding for links:** Replace spaces with `%20` in URLs
2. **Keep summaries concise:** One or two sentences maximum
3. **Be consistent:** Use the same terminology across all files
4. **Update regularly:** Keep the lastUpdated date current
5. **Backup:** Keep a backup of questions.json before major changes

## Need Help?

If you have questions about adding new questions or maintaining the repository, refer to existing questions as examples or check the questions.json instructions field.

---

**Happy Contributing! 🚀**
