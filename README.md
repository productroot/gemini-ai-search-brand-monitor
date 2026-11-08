# Gemini AI Search Brand Position Monitor

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Google GenAI SDK](https://img.shields.io/badge/google--genai-%3E%3D2.30.1-4285F4?logo=google&logoColor=white)](https://aistudio.google.com/)

An open-source CLI and Python library to monitor, audit, and benchmark **brand visibility, rank position, sentiment, and grounded source citations** in AI-powered search responses using the **Google Gemini Interactions API (`google-genai`)** with **Google Search Grounding** and **Structured Outputs**.

Built for hospitality (hotels, direct booking platforms), e-commerce, and SaaS teams tracking **Generative Engine Optimization (GEO)** and brand discoverability.

---

## ✨ Key Features

- 🔍 **Google Search Grounding (`google_search` tool):** Evaluates live web-grounded responses via `gemini-3.8-flash` (or `gemini-4-argon` for deep competitive synthesis).
- 📐 **Strict Structured Outputs:** Uses top-level JSON Schema validation on `client.interactions.create()` to extract deterministic rankings, sentiment scores, and citation URLs.
- 📊 **Competitive Share-of-Voice Reports:** Generates Markdown and JSON audit reports showing exactly where target brands rank across high-intent search queries.
- 🧪 **Deterministic Offline & Live Modes:** Includes unit tests and mock fixtures for CI/CD pipelines.

---

## 🏗️ Project Structure

```text
gemini-ai-search-brand-monitor/
├── brand_monitor/
│   ├── __init__.py
│   ├── schemas.py          # Pydantic & JSON Schema definitions for grounded rankings
│   ├── analyzer.py         # Gemini Interactions API + Google Search Grounding engine
│   └── reporter.py         # Markdown & JSON report generator
├── tests/
│   └── test_analyzer.py    # Unit tests for ranking extraction & report formatting
├── main.py                 # CLI entrypoint
├── requirements.txt
├── .env.example
└── LICENSE
```

---

## 🚀 Quick Start

### 1. Installation

```bash
git clone https://github.com/productroot/gemini-ai-search-brand-monitor.git
cd gemini-ai-search-brand-monitor
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure API Key

```bash
cp .env.example .env
export GEMINI_API_KEY="your-google-ai-studio-api-key"
```

### 3. Run a Brand Visibility Audit

```bash
python main.py \
  --brands "Grand Hotel Krakow, Hotel Copernicus, PURO Krakow" \
  --queries "best luxury spa hotels in Krakow old town, boutique hotels in Krakow with direct booking perks" \
  --model "gemini-3.8-flash" \
  --output report.md
```

---

## 🧠 How It Works (Gemini Interactions API)

Unlike brittle HTML scrapers, `gemini-ai-search-brand-monitor` uses the official `google-genai` SDK (`>= 2.30.1`) and the **Interactions API** (`client.interactions.create`) combining live **Google Search Grounding** with **Structured Output**:

```python
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Find and rank the top luxury spa hotels in Krakow Old Town with direct booking benefits.",
    tools=[{"type": "google_search"}],
    generation_config={"thinking_level": "low"},
)
print(interaction.output_text)
```

---

## 📄 License

Released under the [MIT License](LICENSE). Created by [Patryk Wodniak](https://github.com/productroot).
