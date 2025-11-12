#!/usr/bin/env python3
"""
DSA Repository Auto-Generator
Automatically scans question files and generates/updates:
- questions.json
- README.md
- index.html

Usage: python generate.py
"""

import os
import json
import re
from datetime import datetime
from pathlib import Path

# Configuration
REPO_PATH = Path(__file__).parent
IGNORE_FILES = {'.git', 'README.md', 'index.html', 'questions.json', 
                'CONTRIBUTING.md', 'SETUP_COMPLETE.md', 'validator.html',
                'generate.py', '.gitignore', 'LICENSE', 'question-template.html',
                'QUICKSTART.md', 'HOW_IT_WORKS.md', 'AUTOMATION_COMPLETE.md',
                'update.sh', 'update.bat'}

def extract_metadata_from_file(filepath):
    """Extract metadata from a question file by parsing its content."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        metadata = {
            'title': filepath.name,
            'fileName': filepath.name,
            'difficulty': 'Medium',  # Default
            'topics': [],
            'summary': '',
            'keyApproach': '',
            'timeComplexity': 'O(n)',
            'spaceComplexity': 'O(n)',
            'companies': [],
            'leetcodeNumber': None
        }
        
        # Extract difficulty
        difficulty_match = re.search(r'(?:difficulty|Difficulty)[:\s]*([Ee]asy|[Mm]edium|[Hh]ard)', content, re.IGNORECASE)
        if difficulty_match:
            metadata['difficulty'] = difficulty_match.group(1).capitalize()
        
        # Extract topics from content (look for common keywords)
        topic_keywords = {
            'Binary Tree': ['binary tree', 'tree node', 'treenode'],
            'Tree': ['tree', 'parent pointer', 'traversal'],
            'BFS': ['bfs', 'breadth-first', 'level order', 'queue'],
            'DFS': ['dfs', 'depth-first', 'recursive'],
            'Graph': ['graph', 'adjacency', 'vertex', 'edge'],
            'Linked List': ['linked list', 'listnode', 'next pointer'],
            'Hash Table': ['hash', 'hashmap', 'dictionary', 'map<'],
            'Array': ['array', 'arr['],
            'String': ['string', 'char', 'substring'],
            'Dynamic Programming': ['dp[', 'dynamic programming', 'memoization', 'memo['],
            'DP': ['dp[', 'dynamic programming'],
            'Backtracking': ['backtrack', 'dfs'],
            'Greedy': ['greedy', 'priority queue', 'heap'],
            'Heap': ['heap', 'priorityqueue', 'pq.'],
            'Two Pointers': ['two pointer', 'left', 'right'],
            'Sliding Window': ['sliding window', 'window'],
            'Stack': ['stack', 'stack<'],
            'Queue': ['queue', 'deque'],
            'Sorting': ['sort', 'sorted'],
            'Binary Search': ['binary search', 'left < right'],
        }
        
        content_lower = content.lower()
        for topic, keywords in topic_keywords.items():
            if any(keyword in content_lower for keyword in keywords):
                if topic not in metadata['topics']:
                    metadata['topics'].append(topic)
        
        # Limit to most relevant topics (max 5)
        metadata['topics'] = metadata['topics'][:5]
        
        # Extract summary (first paragraph after problem restatement)
        summary_match = re.search(r'(?:problem|Problem)(.*?)(?:\n\n|\#)', content, re.DOTALL | re.IGNORECASE)
        if summary_match:
            summary_text = summary_match.group(1).strip()
            # Clean up the summary
            summary_text = re.sub(r'\n+', ' ', summary_text)
            summary_text = re.sub(r'\s+', ' ', summary_text)
            summary_text = re.sub(r'^[:\-\s]+', '', summary_text)
            metadata['summary'] = summary_text[:200] + '...' if len(summary_text) > 200 else summary_text
        
        # Extract key approach
        approach_match = re.search(r'(?:quick script|approach|steps?)[:\s]*\n([^#]+)', content, re.IGNORECASE)
        if approach_match:
            approach_text = approach_match.group(1).strip()
            # Get first meaningful line
            lines = [l.strip() for l in approach_text.split('\n') if l.strip() and not l.strip().startswith('```')]
            if lines:
                metadata['keyApproach'] = lines[0][:150]
        
        # Extract complexity
        time_match = re.search(r'(?:time|Time)[:\s]*O\([^)]+\)', content, re.IGNORECASE)
        if time_match:
            metadata['timeComplexity'] = time_match.group(0).split(':')[-1].strip()
        
        space_match = re.search(r'(?:space|Space)[:\s]*O\([^)]+\)', content, re.IGNORECASE)
        if space_match:
            metadata['spaceComplexity'] = space_match.group(0).split(':')[-1].strip()
        
        # Extract LeetCode number if present
        leetcode_match = re.search(r'(?:leetcode|LeetCode)\s*#?\s*(\d+)', content, re.IGNORECASE)
        if leetcode_match:
            metadata['leetcodeNumber'] = int(leetcode_match.group(1))
        
        return metadata
    
    except Exception as e:
        print(f"Warning: Could not parse {filepath.name}: {e}")
        return None

def scan_questions():
    """Scan repository for question files and extract metadata."""
    questions = []
    question_id = 1
    
    for item in sorted(REPO_PATH.iterdir()):
        # Skip directories and ignored files
        if item.is_dir() or item.name in IGNORE_FILES or item.name.startswith('.'):
            continue
        
        # Skip common file extensions that aren't questions
        if item.suffix in ['.json', '.html', '.py', '.md', '.txt', '.sh']:
            continue
        
        print(f"Processing: {item.name}")
        metadata = extract_metadata_from_file(item)
        
        if metadata:
            question = {
                'id': question_id,
                'title': metadata['title'],
                'fileName': metadata['fileName'],
                'difficulty': metadata['difficulty'],
                'topics': metadata['topics'],
                'summary': metadata['summary'],
                'keyApproach': metadata['keyApproach'],
                'complexity': {
                    'time': metadata['timeComplexity'],
                    'space': metadata['spaceComplexity']
                }
            }
            
            if metadata['companies']:
                question['companies'] = metadata['companies']
            if metadata['leetcodeNumber']:
                question['leetcodeNumber'] = metadata['leetcodeNumber']
            
            questions.append(question)
            question_id += 1
    
    return questions

def generate_questions_json(questions):
    """Generate questions.json file."""
    # Build indices
    topic_index = {}
    difficulty_index = {'Easy': [], 'Medium': [], 'Hard': []}
    
    for q in questions:
        # Difficulty index
        difficulty_index[q['difficulty']].append(q['id'])
        
        # Topic index
        for topic in q['topics']:
            if topic not in topic_index:
                topic_index[topic] = []
            topic_index[topic].append(q['id'])
    
    # Count by difficulty
    stats = {
        'easy': len(difficulty_index['Easy']),
        'medium': len(difficulty_index['Medium']),
        'hard': len(difficulty_index['Hard'])
    }
    
    data = {
        'metadata': {
            'repository': 'DSA Questions Collection',
            'description': 'Interview-ready solutions with detailed explanations',
            'lastUpdated': datetime.now().strftime('%Y-%m-%d'),
            'totalQuestions': len(questions)
        },
        'statistics': stats,
        'questions': questions,
        'topicIndex': topic_index,
        'difficultyIndex': difficulty_index,
        'instructions': {
            'addingNewQuestion': 'Simply add a new question file to the repository and run `python generate.py` to automatically update all files.',
            'requiredFields': ['id', 'title', 'fileName', 'difficulty', 'topics', 'summary', 'keyApproach', 'complexity'],
            'optionalFields': ['companies', 'leetcodeNumber', 'approaches', 'tags']
        }
    }
    
    with open(REPO_PATH / 'questions.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Generated questions.json with {len(questions)} questions")
    return data

def generate_readme(questions_data):
    """Generate README.md file."""
    questions = questions_data['questions']
    stats = questions_data['statistics']
    topic_index = questions_data['topicIndex']
    
    readme = f"""# DSA Questions Collection

Welcome to my Data Structures and Algorithms questions repository! This collection contains detailed solutions, approaches, and complexity analyses for various DSA problems.

## 📚 Question List

| # | Problem | Difficulty | Topics | Solution |
|---|---------|------------|--------|----------|
"""
    
    # Add table rows
    for i, q in enumerate(questions, 1):
        topics_str = ', '.join(q['topics'][:3])
        encoded_filename = q['fileName'].replace(' ', '%20')
        title_anchor = q['title'].lower().replace(' ', '-').replace('(', '').replace(')', '')
        readme += f"| {i} | [{q['title']}](#{title_anchor}) | {q['difficulty']} | {topics_str} | [View](./{encoded_filename}) |\n"
    
    # Add search by topic section
    readme += f"""
## 🔍 Search by Topic

"""
    
    for topic, question_ids in sorted(topic_index.items()):
        readme += f"### {topic}\n"
        for qid in question_ids:
            q = next(qu for qu in questions if qu['id'] == qid)
            encoded_filename = q['fileName'].replace(' ', '%20')
            readme += f"- [{q['title']}](./{encoded_filename})\n"
        readme += "\n"
    
    # Add question details
    readme += """## 📖 Question Details

"""
    
    for q in questions:
        title_anchor = q['title'].lower().replace(' ', '-').replace('(', '').replace(')', '')
        encoded_filename = q['fileName'].replace(' ', '%20')
        topics_str = ', '.join(q['topics'])
        
        readme += f"""### {q['title']}
**Difficulty:** {q['difficulty']}  
**Topics:** {topics_str}  
**Key Concepts:**
- {q['summary'][:100]}...
- **Time Complexity:** {q['complexity']['time']}
- **Space Complexity:** {q['complexity']['space']}

**Quick Approach:**
{q['keyApproach'][:200]}...

[📄 View Full Solution](./{encoded_filename})

---

"""
    
    # Add footer
    readme += f"""## 🚀 How to Use This Repository

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

- **Total Questions:** {len(questions)}
- **Easy:** {stats['easy']}
- **Medium:** {stats['medium']}
- **Hard:** {stats['hard']}

---

## 🤝 Contributing

This is a personal learning repository. Questions and solutions are continuously being added as I practice more problems.

## 📌 Note

All solutions are interview-ready with detailed explanations, multiple approaches, and complexity analyses. The code is clean, well-commented, and follows best practices.

---

**Last Updated:** {datetime.now().strftime('%B %d, %Y')}

*Happy Coding! 🚀*
"""
    
    with open(REPO_PATH / 'README.md', 'w', encoding='utf-8') as f:
        f.write(readme)
    
    print(f"✅ Generated README.md")

def generate_index_html(questions_data):
    """Generate index.html file."""
    questions = questions_data['questions']
    stats = questions_data['statistics']
    
    # Convert questions to JavaScript format
    js_questions = []
    for q in questions:
        js_q = {
            'id': q['id'],
            'title': q['title'],
            'difficulty': q['difficulty'],
            'topics': q['topics'],
            'summary': q['summary'],
            'timeComplexity': q['complexity']['time'],
            'spaceComplexity': q['complexity']['space'],
            'file': q['fileName'],
            'keyApproach': q['keyApproach']
        }
        js_questions.append(js_q)
    
    questions_json_str = json.dumps(js_questions, indent=12)
    
    # Get all unique topics
    all_topics = sorted(set(topic for q in questions for topic in q['topics']))
    topic_buttons = '\n                    '.join([
        f'<button class="filter-btn" data-topic="{topic}">{topic}</button>'
        for topic in all_topics[:8]  # Limit to 8 most common topics
    ])
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DSA Questions Collection</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}

        header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}

        h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}

        .subtitle {{
            font-size: 1.1em;
            opacity: 0.9;
        }}

        .stats {{
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-top: 20px;
            flex-wrap: wrap;
        }}

        .stat-item {{
            background: rgba(255,255,255,0.2);
            padding: 10px 20px;
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }}

        .stat-number {{
            font-size: 2em;
            font-weight: bold;
        }}

        .controls {{
            padding: 30px;
            background: #f8f9fa;
            border-bottom: 2px solid #e9ecef;
        }}

        .search-box {{
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }}

        #searchInput {{
            flex: 1;
            min-width: 250px;
            padding: 12px 20px;
            font-size: 16px;
            border: 2px solid #ddd;
            border-radius: 10px;
            transition: border-color 0.3s;
        }}

        #searchInput:focus {{
            outline: none;
            border-color: #667eea;
        }}

        .filters {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}

        .filter-group {{
            display: flex;
            gap: 5px;
        }}

        .filter-btn {{
            padding: 8px 16px;
            border: 2px solid #ddd;
            background: white;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s;
            font-size: 14px;
        }}

        .filter-btn:hover {{
            background: #f8f9fa;
        }}

        .filter-btn.active {{
            background: #667eea;
            color: white;
            border-color: #667eea;
        }}

        .difficulty-easy {{ border-color: #28a745; color: #28a745; }}
        .difficulty-easy.active {{ background: #28a745; border-color: #28a745; color: white; }}
        .difficulty-medium {{ border-color: #ffc107; color: #e6a800; }}
        .difficulty-medium.active {{ background: #ffc107; border-color: #ffc107; color: white; }}
        .difficulty-hard {{ border-color: #dc3545; color: #dc3545; }}
        .difficulty-hard.active {{ background: #dc3545; border-color: #dc3545; color: white; }}

        .questions-container {{
            padding: 30px;
        }}

        .question-card {{
            background: white;
            border: 2px solid #e9ecef;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 20px;
            transition: all 0.3s;
            cursor: pointer;
        }}

        .question-card:hover {{
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            transform: translateY(-2px);
            border-color: #667eea;
        }}

        .question-header {{
            display: flex;
            justify-content: space-between;
            align-items: start;
            margin-bottom: 15px;
            flex-wrap: wrap;
            gap: 10px;
        }}

        .question-title {{
            font-size: 1.4em;
            font-weight: 600;
            color: #333;
            flex: 1;
            min-width: 250px;
        }}

        .difficulty-badge {{
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: 600;
        }}

        .difficulty-Easy {{ background: #d4edda; color: #155724; }}
        .difficulty-Medium {{ background: #fff3cd; color: #856404; }}
        .difficulty-Hard {{ background: #f8d7da; color: #721c24; }}

        .question-topics {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 15px;
        }}

        .topic-tag {{
            background: #e7f3ff;
            color: #0066cc;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 0.85em;
        }}

        .question-summary {{
            color: #666;
            margin-bottom: 15px;
            line-height: 1.8;
        }}

        .complexity-info {{
            display: flex;
            gap: 20px;
            margin-bottom: 15px;
            font-size: 0.9em;
            flex-wrap: wrap;
        }}

        .complexity-item {{
            background: #f8f9fa;
            padding: 8px 15px;
            border-radius: 8px;
        }}

        .complexity-label {{
            font-weight: 600;
            color: #667eea;
        }}

        .view-solution-btn {{
            display: inline-block;
            padding: 10px 25px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 600;
            transition: transform 0.3s;
        }}

        .view-solution-btn:hover {{
            transform: scale(1.05);
        }}

        .no-results {{
            text-align: center;
            padding: 60px 20px;
            color: #666;
        }}

        .no-results-icon {{
            font-size: 4em;
            margin-bottom: 20px;
        }}

        footer {{
            background: #f8f9fa;
            padding: 30px;
            text-align: center;
            color: #666;
            border-top: 2px solid #e9ecef;
        }}

        @media (max-width: 768px) {{
            h1 {{
                font-size: 1.8em;
            }}
            
            .question-header {{
                flex-direction: column;
            }}
            
            .stats {{
                gap: 15px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🚀 DSA Questions Collection</h1>
            <p class="subtitle">Interview-Ready Solutions with Detailed Explanations</p>
            <div class="stats">
                <div class="stat-item">
                    <div class="stat-number" id="totalQuestions">{len(questions)}</div>
                    <div>Total Questions</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number" id="easyCount">{stats['easy']}</div>
                    <div>Easy</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number" id="mediumCount">{stats['medium']}</div>
                    <div>Medium</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number" id="hardCount">{stats['hard']}</div>
                    <div>Hard</div>
                </div>
            </div>
        </header>

        <div class="controls">
            <div class="search-box">
                <input type="text" id="searchInput" placeholder="🔍 Search questions by name, topic, or keyword...">
            </div>
            <div class="filters">
                <div class="filter-group">
                    <button class="filter-btn difficulty-easy" data-difficulty="Easy">Easy</button>
                    <button class="filter-btn difficulty-medium" data-difficulty="Medium">Medium</button>
                    <button class="filter-btn difficulty-hard" data-difficulty="Hard">Hard</button>
                </div>
                <div class="filter-group">
                    {topic_buttons}
                </div>
                <button class="filter-btn" id="clearFilters">Clear All</button>
            </div>
        </div>

        <div class="questions-container" id="questionsContainer">
            <!-- Questions will be dynamically inserted here -->
        </div>

        <footer>
            <p><strong>Last Updated:</strong> {datetime.now().strftime('%B %d, %Y')}</p>
            <p>💡 All solutions include problem restatement, multiple approaches, complexity analysis, and clean code.</p>
            <p>🤖 Auto-generated by generate.py - Just add questions and run the script!</p>
        </footer>
    </div>

    <script>
        // Questions data (auto-generated)
        const questions = {questions_json_str};

        let activeFilters = {{
            difficulty: new Set(),
            topics: new Set(),
            search: ""
        }};

        // Initialize
        function init() {{
            renderQuestions(questions);
            setupEventListeners();
        }}

        // Render questions
        function renderQuestions(questionsToRender) {{
            const container = document.getElementById('questionsContainer');
            
            if (questionsToRender.length === 0) {{
                container.innerHTML = `
                    <div class="no-results">
                        <div class="no-results-icon">🔍</div>
                        <h2>No questions found</h2>
                        <p>Try adjusting your filters or search terms</p>
                    </div>
                `;
                return;
            }}

            container.innerHTML = questionsToRender.map(q => `
                <div class="question-card" onclick="openQuestion('${{q.file}}')">
                    <div class="question-header">
                        <div class="question-title">${{q.title}}</div>
                        <span class="difficulty-badge difficulty-${{q.difficulty}}">${{q.difficulty}}</span>
                    </div>
                    <div class="question-topics">
                        ${{q.topics.map(topic => `<span class="topic-tag">${{topic}}</span>`).join('')}}
                    </div>
                    <div class="question-summary">${{q.summary}}</div>
                    <div class="complexity-info">
                        <div class="complexity-item">
                            <span class="complexity-label">Time:</span> ${{q.timeComplexity}}
                        </div>
                        <div class="complexity-item">
                            <span class="complexity-label">Space:</span> ${{q.spaceComplexity}}
                        </div>
                    </div>
                    <div style="margin-top: 10px; padding-top: 15px; border-top: 1px solid #e9ecef;">
                        <strong>💡 Key Approach:</strong> ${{q.keyApproach}}
                    </div>
                    <div style="margin-top: 15px;">
                        <a href="${{encodeURIComponent(q.file)}}.html" class="view-solution-btn" onclick="event.stopPropagation()">View Full Solution →</a>
                    </div>
                </div>
            `).join('');
        }}

        // Filter questions
        function filterQuestions() {{
            let filtered = questions;

            // Filter by difficulty
            if (activeFilters.difficulty.size > 0) {{
                filtered = filtered.filter(q => activeFilters.difficulty.has(q.difficulty));
            }}

            // Filter by topics
            if (activeFilters.topics.size > 0) {{
                filtered = filtered.filter(q => 
                    q.topics.some(topic => 
                        Array.from(activeFilters.topics).some(filter => 
                            topic.toLowerCase().includes(filter.toLowerCase())
                        )
                    )
                );
            }}

            // Filter by search
            if (activeFilters.search) {{
                const searchLower = activeFilters.search.toLowerCase();
                filtered = filtered.filter(q =>
                    q.title.toLowerCase().includes(searchLower) ||
                    q.summary.toLowerCase().includes(searchLower) ||
                    q.topics.some(topic => topic.toLowerCase().includes(searchLower)) ||
                    q.keyApproach.toLowerCase().includes(searchLower)
                );
            }}

            renderQuestions(filtered);
        }}

        // Setup event listeners
        function setupEventListeners() {{
            // Search input
            document.getElementById('searchInput').addEventListener('input', (e) => {{
                activeFilters.search = e.target.value;
                filterQuestions();
            }});

            // Difficulty filters
            document.querySelectorAll('[data-difficulty]').forEach(btn => {{
                btn.addEventListener('click', () => {{
                    const difficulty = btn.dataset.difficulty;
                    if (activeFilters.difficulty.has(difficulty)) {{
                        activeFilters.difficulty.delete(difficulty);
                        btn.classList.remove('active');
                    }} else {{
                        activeFilters.difficulty.add(difficulty);
                        btn.classList.add('active');
                    }}
                    filterQuestions();
                }});
            }});

            // Topic filters
            document.querySelectorAll('[data-topic]').forEach(btn => {{
                btn.addEventListener('click', () => {{
                    const topic = btn.dataset.topic;
                    if (activeFilters.topics.has(topic)) {{
                        activeFilters.topics.delete(topic);
                        btn.classList.remove('active');
                    }} else {{
                        activeFilters.topics.add(topic);
                        btn.classList.add('active');
                    }}
                    filterQuestions();
                }});
            }});

            // Clear filters
            document.getElementById('clearFilters').addEventListener('click', () => {{
                activeFilters = {{ difficulty: new Set(), topics: new Set(), search: "" }};
                document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
                document.getElementById('searchInput').value = '';
                filterQuestions();
            }});
        }}

        // Open question file
        function openQuestion(filename) {{
            window.location.href = encodeURIComponent(filename) + '.html';
        }}

        // Initialize on load
        init();
    </script>
</body>
</html>
"""
    
    with open(REPO_PATH / 'index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ Generated index.html")

def generate_question_html_pages(questions_data):
    """Generate individual HTML pages for each question."""
    questions = questions_data['questions']
    
    # Load template
    template_path = REPO_PATH / 'question-template.html'
    if not template_path.exists():
        print("⚠️  Warning: question-template.html not found. Skipping HTML generation.")
        return
    
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    
    print("📄 Generating individual question pages...")
    
    for question in questions:
        try:
            # Read question content
            question_file = REPO_PATH / question['fileName']
            if not question_file.exists():
                continue
            
            with open(question_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Convert markdown-style content to HTML
            html_content = markdown_to_html(content)
            
            # Replace placeholders in template
            html = template.replace('{{QUESTION_TITLE}}', question['title'])
            html = html.replace('{{DIFFICULTY}}', question['difficulty'])
            html = html.replace('{{DIFFICULTY_LOWER}}', question['difficulty'].lower())
            html = html.replace('{{CONTENT}}', html_content)
            
            # Add topics to meta section
            topics_html = ''.join([f'<span class="topic-tag">{topic}</span>' for topic in question['topics']])
            html = html.replace('<!-- Topics will be dynamically added -->', topics_html)
            
            # Save HTML file
            html_filename = REPO_PATH / f"{question['fileName']}.html"
            with open(html_filename, 'w', encoding='utf-8') as f:
                f.write(html)
            
        except Exception as e:
            print(f"   ⚠️  Error generating HTML for {question['title']}: {e}")
    
    print(f"✅ Generated {len(questions)} question HTML pages")

def markdown_to_html(content):
    """Convert markdown-style content to HTML."""
    # Simple markdown to HTML conversion
    html = content
    
    # Headers
    html = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    
    # Code blocks (preserve them)
    code_blocks = []
    def save_code_block(match):
        code_blocks.append(match.group(0))
        return f'___CODE_BLOCK_{len(code_blocks)-1}___'
    
    html = re.sub(r'```[\s\S]*?```', save_code_block, html)
    html = re.sub(r'````[\s\S]*?````', save_code_block, html)
    
    # Bold
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    
    # Italic
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    
    # Inline code
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
    
    # Lists (simple)
    lines = html.split('\n')
    in_list = False
    result = []
    
    for line in lines:
        if re.match(r'^\s*[-*•]\s+', line):
            if not in_list:
                result.append('<ul>')
                in_list = True
            item = re.sub(r'^\s*[-*•]\s+', '', line)
            result.append(f'<li>{item}</li>')
        elif re.match(r'^\s*\d+\.\s+', line):
            if not in_list:
                result.append('<ol>')
                in_list = 'ol'
            item = re.sub(r'^\s*\d+\.\s+', '', line)
            result.append(f'<li>{item}</li>')
        else:
            if in_list:
                result.append('</ol>' if in_list == 'ol' else '</ul>')
                in_list = False
            result.append(line)
    
    if in_list:
        result.append('</ol>' if in_list == 'ol' else '</ul>')
    
    html = '\n'.join(result)
    
    # Paragraphs
    paragraphs = html.split('\n\n')
    html_paragraphs = []
    for para in paragraphs:
        para = para.strip()
        if para and not para.startswith('<'):
            html_paragraphs.append(f'<p>{para}</p>')
        else:
            html_paragraphs.append(para)
    
    html = '\n\n'.join(html_paragraphs)
    
    # Restore code blocks
    for i, code_block in enumerate(code_blocks):
        # Remove markdown code fence markers
        code_content = re.sub(r'^```[a-z]*\n|^````[a-z]*\n', '', code_block)
        code_content = re.sub(r'\n```$|\n````$', '', code_content)
        html = html.replace(f'___CODE_BLOCK_{i}___', f'<pre><code>{code_content}</code></pre>')
    
    return html

def main():
    """Main function to generate all files."""
    print("=" * 60)
    print("🚀 DSA Repository Auto-Generator")
    print("=" * 60)
    print()
    
    # Scan questions
    print("📁 Scanning repository for questions...")
    questions = scan_questions()
    print(f"   Found {len(questions)} question files")
    print()
    
    if not questions:
        print("⚠️  No questions found. Add question files and run again.")
        return
    
    # Generate files
    print("📝 Generating files...")
    questions_data = generate_questions_json(questions)
    generate_readme(questions_data)
    generate_index_html(questions_data)
    generate_question_html_pages(questions_data)
    
    print()
    print("=" * 60)
    print("✨ All files generated successfully!")
    print("=" * 60)
    print()
    print("📊 Summary:")
    print(f"   - Total Questions: {len(questions)}")
    print(f"   - Easy: {questions_data['statistics']['easy']}")
    print(f"   - Medium: {questions_data['statistics']['medium']}")
    print(f"   - Hard: {questions_data['statistics']['hard']}")
    print(f"   - Topics: {len(questions_data['topicIndex'])}")
    print()
    print("💡 Next steps:")
    print("   1. Review the generated files")
    print("   2. Open index.html in your browser to test")
    print("   3. Commit and push to GitHub")
    print()
    print("🎉 To add more questions: Just add the file and run 'python generate.py' again!")
    print()

if __name__ == '__main__':
    main()
