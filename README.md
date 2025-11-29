# FactSphere AI

**Smart Research Assistant**

FactSphere AI is a lightweight multi-agent research assistant. It breaks down your queries, searches for information, synthesizes summaries, and evaluates results. It also keeps track of previous searches so repeated queries are faster.  

Think of it as a mini research team in code.

---

## Features

- **Planner Agent:** Breaks queries into subtopics.  
- **Search Agent:** Retrieves results for each subtopic (currently simulated).  
- **Synthesis Agent:** Combines results into a clear, readable summary.  
- **Evaluator Agent:** Provides feedback on the summary quality.  
- **Memory:** Remembers past queries and summaries to avoid repeating work.  

---

## Setup

Clone the repo:

```bash
git clone https://github.com/your-username/FactSphere-AI.git
cd FactSphere-AI

**Create a virtual environment and activate it:**
python -m venv venv
*PowerShell:*
 .\venv\Scripts\Activate.ps1
*CMD:*
 venv\Scripts\activate.bat
*Mac/Linux:*
 source venv/bin/activate

**Install dependencies:**
pip install -r requirements.txt

**Usage**
*Run the main program:*
 python main.py


*Enter your query when prompted.*
---
## How it works
**The agents will:

*Plan the query
*Search for results
*Generate a summary
*Evaluate the summary
*Past queries are cached in memory to speed up repeated searches**


---

## Project Structure
FactSphere-AI/
├─ agents/
│  ├─ planner.py
│  ├─ search_agent.py
│  ├─ synthesis_agent.py
│  └─ evaluator_agent.py
├─ tools/
│  ├─ search_tool.py
│  └─ memory_tool.py
├─ memory/
│  └─ long_term_memory.json
├─ main.py
├─ requirements.txt
└─ README.md



Built as part of the Kaggle 5-Day AI Agents Capstone Project.

License: MIT

*This project runs on Python 3.10+ and requires standard dependencies listed in `requirements.txt`.*
