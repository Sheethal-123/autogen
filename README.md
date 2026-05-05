# 🤖 Analyzer GPT — AI-Powered Data Analysis Agent

Analyzer GPT is a cloud-native AI application that enables users to perform data analysis on CSV files using natural language. Built using a multi-agent architecture powered by AutoGen, the system automatically generates Python code, executes it safely inside Docker, and returns insights, visualizations, and reports in real time.

---

## 🚀 Project Overview

Traditional data analysis requires manual coding and technical expertise. Analyzer GPT simplifies this by allowing users to:

* Upload a dataset (CSV)
* Ask questions in plain English
* Automatically generate and execute analysis code
* Receive charts, summaries, and insights instantly

The system leverages **LLM-powered agents + code execution** to create an end-to-end intelligent data analysis pipeline.

---

## 🧠 Key Features

* 🔍 Natural language → Python code generation
* 🤖 Multi-agent collaboration (AutoGen)
* 🐳 Secure Docker-based code execution
* 📊 Automated visualization generation (`output.png`)
* 💬 Interactive Streamlit chat interface
* ⚡ Real-time execution and feedback loop

---

## 🏗️ Architecture

![Architecture](Analyzer%20GPT/assets/architecture.png)

---

## 🧩 Architecture Explanation

The system follows a **multi-agent orchestration pipeline**:

### 1. User Interface (Streamlit)

* Users upload CSV files and submit queries
* Provides chat-based interaction for analysis

### 2. AutoGen Orchestration

* Uses `RoundRobinGroupChat` to coordinate agents 
* Controls execution flow and task completion

### 3. AI Agents

* **Data Analyzer Agent**

  * Understands the query
  * Generates Python code for analysis


* **Code Executor Agent**

  * Executes generated code safely


### 4. Docker Execution Layer

* Runs Python code in isolated environment
* Prevents unsafe execution


### 5. Output Layer

* Saves charts as `output.png`
* Displays results in Streamlit UI


---

## 🛠️ Tech Stack

| Category        | Tools             |
| --------------- | ----------------- |
| Language        | Python            |
| Frontend        | Streamlit         |
| AI Framework    | AutoGen AgentChat |
| LLM API         | Groq (LLaMA 3)    |
| Execution       | Docker            |
| Data Processing | Pandas            |
| Visualization   | Matplotlib        |

Dependencies:


---

## 📂 Project Structure

```text
analyzer-gpt/
│
├── assets/
│   └── architecture.png
│
├── agents/
│   ├── Code_Executor_agent.py
│   ├── Data_analyzer_agent.py
│   └── prompts/
│       └── DataAnalyzerAgentPrompt.py
│
├── config/
│   ├── constants.py
│   ├── docker_utils.py
│   └── openai_model_client.py
│
├── team/
│   └── analyzer_gpt.py
│
├── main.py
├── streamlit_app.py
├── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/analyzer-gpt.git
cd analyzer-gpt
```

---

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Set environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Running the Application

Make sure Docker is running.

```bash
streamlit run streamlit_app.py
```

---

## 🧪 How It Works

1. Upload a CSV file
2. Enter a natural language query
3. AI generates Python code
4. Code executes in Docker
5. Output is returned (text/chart)

---

## 💡 Example Queries

```text
Show me number of rows and columns
```

```text
Create a bar chart of survived vs died and save as output.png
```

```text
Find missing values in each column
```

---

## 📊 Example Use Case

For a Titanic dataset:

```text
Can you give me a graph of survived and died?
```

✔ Generates Python code
✔ Executes inside Docker
✔ Displays visualization

## 📸 Demo

### User Interface
![UI](Analyzer%20GPT/assets/ui.png)

### Generated Output
![Output](Analyzer%20GPT/assets/code.png)
![Output](Analyzer%20GPT/assets/output.png)
---

## 🎯 Why This Project Stands Out

This project demonstrates:

* AI agent orchestration (AutoGen)
* LLM-based code generation
* Secure execution systems (Docker)
* Real-world data analysis workflows
* Interactive AI applications

👉 Moves beyond notebooks into **production-style system design**

---

## 🔮 Future Improvements

* Support Excel / JSON files
* Add persistent storage (S3 / DB)
* Improve prompt handling & validation
* Add user authentication
* Deploy to cloud (AWS/GCP)
* Add downloadable reports

---

## ⚠️ Disclaimer

This project executes AI-generated code. Use in a controlled environment. Docker isolation is recommended for safety.

---


