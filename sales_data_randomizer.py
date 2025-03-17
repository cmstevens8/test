import shutil
import os
import csv
import random
import time
import logging

log_file = "sales_data_log.txt"
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

original_file = "sales_data.csv"
backup_directory = "backup"
backup_file = os.path.join(backup_directory, "sales_data_backup.csv")
backup_interval = 10

try:
    with open(original_file, "r", newline="") as file:
        reader = csv.reader(file)
        data = list(reader)

    os.makedirs(backup_directory, exist_ok=True)
    if not os.path.exists(backup_file):
        shutil.copy(original_file, backup_file)
        logging.info(f"Backup created: {backup_file}")

    header, rows = data[0], data[1:]
    random.shuffle(rows)

    with open(original_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

    logging.info("Sales data shuffled successfully.")
    logging.info(f"Waiting {backup_interval} seconds before next operation...")
    time.sleep(backup_interval)

except Exception as e:
    logging.error(f"An error occurred: {str(e)}")


