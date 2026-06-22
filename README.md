# Multi-Agent AI Research Assistant

## Overview

Multi-Agent AI Research Assistant is an intelligent research automation system built using LangChain and Mistral AI. The application uses a multi-agent architecture where specialized AI agents collaborate to perform web research, scrape relevant content, generate detailed reports, and evaluate report quality.

The system simulates a real-world research workflow by assigning different responsibilities to dedicated agents, resulting in more organized and accurate outputs.

---

## Features

* AI-powered web research
* Multi-agent workflow architecture
* Automated URL scraping and content extraction
* Structured research report generation
* AI-based report critique and scoring
* Interactive Streamlit interface
* Modular and extensible design

---

## Architecture

### Search Agent

Responsible for finding relevant and recent information using web search tools.

**Input:** Research topic

**Output:** Search results and source URLs

---

### Scrape Agent

Extracts detailed content from the most relevant web pages discovered by the Search Agent.

**Input:** URLs from search results

**Output:** Cleaned webpage content

---

### Writer Chain

Transforms collected information into a structured research report.

**Report Structure:**

* Introduction
* Key Findings
* Conclusion
* Sources

---

### Critic Chain

Evaluates the generated report and provides:

* Quality Score
* Strengths
* Areas of Improvement
* Final Verdict

---

## Workflow

User Topic
↓
Search Agent
↓
Scrape Agent
↓
Writer Chain
↓
Critic Chain
↓
Final Research Report

---

## Tech Stack

### AI & LLM

* LangChain
* Mistral AI

### Search & Data Collection

* Tavily Search API
* BeautifulSoup
* Requests

### Frontend

* Streamlit

### Backend

* Python

---

## Project Structure

```text
Multi-Agent-AI-Research-Assistant/
│
├── app.py
├── agents.py
├── workflow.py
├── tools.py
├── requirements.txt
├── .env
├── README.md
│
└── assets/
```

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd Multi-Agent-AI-Research-Assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## Run Application

```bash
streamlit run app.py
```

Application will be available at:

```text
http://localhost:8501
```

---
### Output

* Comprehensive research report
* Key findings from multiple sources
* Source references
* AI-generated quality review

## Learning Outcomes

This project demonstrates:

* Multi-Agent AI Systems
* LangChain Agents and Chains
* Tool Calling
* Prompt Engineering
* Retrieval and Web Research
* LLM Workflow Orchestration
* Streamlit Deployment



AI | Full Stack Development | Generative AI
