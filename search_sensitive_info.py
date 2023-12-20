import os

# User sensitive information to search for
sensitive_info = ["password", "credit card", "social security number"]

# Function to check if a line in a file contains user sensitive information
def check_line(line):
    for info in sensitive_info:
        if info in line.lower():
            return True
    return False

# Function to search for user sensitive information in a log file
def search_log_file(file_path):
    with open(file_path, "r") as f:
        for line_num, line in enumerate(f):
            if check_line(line):
                print(f"Sensitive info found in file {file_path}, line {line_num + 1}: {line.strip()}")

# Function to recursively search for log files in a folder and its subfolders
def search_log_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".log"):
                file_path = os.path.join(root, file)
                search_log_file(file_path)

# Example usage
search_log_folder("Logs_2023_03_29_10_20AM")