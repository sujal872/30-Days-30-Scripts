# ------------------------------
# Simple Log Analyzer
# ------------------------------
import collections

LOG_FILE = "server.log"

def read_logs():
    """Read log file and return lines"""
    try:
        with open(LOG_FILE, "r") as file:
            logs = file.readlines()
        return logs
    except FileNotFoundError:
        print("Log file not found.")
        return []


def find_failed_logins(logs):
    """Find failed login attempts"""
    failed_ips = []

    for line in logs:
        if "Failed login" in line:
            ip = line.split("-")[0].strip()
            failed_ips.append(ip)

    return failed_ips


def analyze_ips(failed_ips):
    """Count failed attempts per IP"""
    counter = collections.Counter(failed_ips)
    return counter


def print_report(counter):
    """Print suspicious activity report"""

    print("\n===== Log Analysis Report =====\n")

    if not counter:
        print("No failed login attempts found.")
        return

    for ip, count in counter.items():

        print(f"IP Address: {ip}")
        print(f"Failed Attempts: {count}")

        if count >= 3:
            print("⚠ Possible Brute Force Attack")

        print("---------------------------")


def main():

    logs = read_logs()

    if not logs:
        return

    failed_ips = find_failed_logins(logs)
    counter = analyze_ips(failed_ips)
    print_report(counter)


if __name__ == "__main__":
    main()