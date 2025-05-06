from prefect import flow, task, get_run_logger
from prefect.states import Paused
import os
import time
from datetime import datetime

DOC_PATH = "document.txt"

@task
def ingest_document():
    with open(DOC_PATH, "r") as file:
        content = file.read()
    return content

@task
def extract_facts(content):
    if "APPROVED" in content.upper():
        return {"status": "success", "data": "Extracted data..."}
    else:
        return {"status": "review_needed", "data": None}

@task
def final_step():
    print("✅ Document processing completed successfully!")

@task
def wait_for_human_input(last_modified_time):
    logger = get_run_logger()
    logger.info("⏸ Waiting for human intervention. Please add 'APPROVED' to the document and save.")
    while True:
        current_modified = os.path.getmtime(DOC_PATH)
        if current_modified > last_modified_time:
            logger.info("📄 Detected document update.")
            break
        time.sleep(5)

@flow
def document_processing_flow():
    logger = get_run_logger()

    logger.info("📥 Ingesting document...")
    content = ingest_document()
    result = extract_facts(content)

    if result["status"] == "success":
        final_step()
    else:
        logger.warning("🚧 Review needed. Pausing for human intervention.")
        last_modified = os.path.getmtime(DOC_PATH)
        wait_for_human_input(last_modified)

        logger.info("🔁 Re-ingesting and re-processing after human input...")
        updated_content = ingest_document()
        updated_result = extract_facts(updated_content)

        if updated_result["status"] == "success":
            final_step()
        else:
            logger.error("❌ Still missing 'APPROVED'. Workflow failed.")

if __name__ == "__main__":
    document_processing_flow()
