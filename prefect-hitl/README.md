# 🧠 Human-in-the-Loop Document Processing with Prefect 2.x

This Proof of Concept demonstrates how to orchestrate a document processing workflow using [Prefect 2.x](https://docs.prefect.io/), featuring a pause for human intervention when automated extraction fails. It simulates a pipeline with ingestion, fact extraction, and manual review before completion.

---

## 📦 Features

- Document ingestion from a local file
- Simulated fact extraction (OCR)
- Human-in-the-loop (HITL) step with `pause_flow_run`
- Resumption based on manual document correction
- Prefect UI tracking for visibility

---

## 🧰 Setup Instructions

### 1. 🔧 Environment Setup

```bash
# 1. Clone the repo or copy files
git clone https://github.com/your-username/prefect-hitl-demo.git
cd prefect-hitl-demo

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

```bash
pip install prefect


2. ⚙️ Prefect Setup

# Start Prefect Orion (local) server
prefect server start

# In another terminal, start a Prefect agent
prefect agent start --work-queue "default"

Open the UI at: http://127.0.0.1:4200


## 👨‍💻 Simulating Human Intervention

1. When prompted in logs to add "APPROVED", open document.txt.

2.Add the word "APPROVED" somewhere in the file.

3.Save the file.

4.The workflow will detect the change and continue automatically.


🧪 Features Demonstrated
@flow and @task usage in Prefect 2.x

State handling and conditional flow logic

Simulated pause for human-in-the-loop (via file timestamp monitoring)

Resumption after human edits