import re

class LogProcessor:
    def __init__(self, log_file):
        self.log_file = log_file

    def extract_error_logs(self):
        """Extracts lines containing 'ERROR'."""
        try:
            with open(self.log_file, 'r') as file:
                errors = [line for line in file if "ERROR" in line]
            return errors
        except FileNotFoundError:
            print(f"Error: File '{self.log_file}' not found.")
            return []

    def replace_error_with_critical(self):
        """Replaces 'ERROR' with 'CRITICAL' in logs."""
        try:
            with open(self.log_file, 'r') as file:
                content = file.read().replace("ERROR", "CRITICAL")
            return content
        except FileNotFoundError:
            print(f"Error: File '{self.log_file}' not found.")
            return ""

    def convert_to_uppercase(self):
        """Converts all log content to uppercase."""
        try:
            with open(self.log_file, 'r') as file:
                content = file.read().upper()
            return content
        except FileNotFoundError:
            print(f"Error: File '{self.log_file}' not found.")
            return ""

    def find_cpu_logs(self):
        """Finds logs containing 'CPU'."""
        try:
            with open(self.log_file, 'r') as file:
                cpu_logs = [line for line in file if "CPU" in line]
            return cpu_logs
        except FileNotFoundError:
            print(f"Error: File '{self.log_file}' not found.")
            return []

if __name__ == "__main__":
    log_file = "logs.txt"
    processor = LogProcessor(log_file)

    print("AWK - Extract only ERROR logs:")
    print("".join(processor.extract_error_logs()))

    print("\nSED - Replace 'ERROR' with 'CRITICAL':")
    print(processor.replace_error_with_critical())

    print("\nTR - Convert all lowercase to uppercase:")
    print(processor.convert_to_uppercase())

    print("\nGREP - Find all logs with 'CPU':")
    print("".join(processor.find_cpu_logs()))
