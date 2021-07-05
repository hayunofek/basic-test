import json
import sys
from json import JSONDecodeError


def usage():
    print(f"""
    usage: {sys.argv[0]} [filename.json]

    The provided file should be a JSON.
    """)


if len(sys.argv) != 2:
    usage()
    exit(1)

filename = sys.argv[1]

logs_json = []
try:
    with open(filename) as f:
        logs_json = json.load(f)
except Exception as e:
    if isinstance(e, JSONDecodeError):
        print("The provided file was not formatted properly, it should be a json file.")
    elif isinstance(e, FileNotFoundError):
        print(f"The provided file: {filename} was not found.")
    else:
        print("An error occured with opening and reading the provided file.")
    exit(1)

print(f"Number of logs records: {len(logs_json)}")

if len(logs_json) > 0:
    logs_per_action = {}
    successful_actions = 0
    for log in logs_json:
        if 'result' in log and log['result'] == 'success':
            successful_actions += 1
        if 'action' in log:
            if not log['action'] in logs_per_action:
                logs_per_action[log['action']] = 0
            logs_per_action[log['action']] += 1

    success_percent = (successful_actions / len(logs_json)) * 100

    if logs_per_action:
        print(f"Number of logs per action: ")
        for action in logs_per_action:
            print(f"    action_name: {action}, amount of logs: {logs_per_action[action]}")

    print(f"Percentage of actions whose result is success: {success_percent}%")
