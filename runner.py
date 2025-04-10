import json
import time
import os
from utils.timer import Timer

def run_question(q_num, func, test_func):
    timer = Timer()
    timer.start()

    test_cases = test_func()
    failed_case = None
    status = "passed"
    error = None

    for inputs, expected in test_cases:
        try:
            output = func(*inputs)
            if output != expected:
                status = "failed"
                failed_case = {
                    "input": list(inputs),
                    "expected": expected,
                    "got": output
                }
                break
        except Exception as e:
            status = "error"
            error = str(e)
            break

    timer.stop()

    log = {
        "question": q_num,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "duration": timer.duration,
        "status": status,
        "error": error,
        "failed_case": failed_case
    }

    os.makedirs("logs", exist_ok=True)
    with open(f"logs/q{q_num}_{int(time.time())}.json", "w") as f:
        json.dump(log, f, indent=2)

    # Colored feedback
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    if status == "passed":
        print(f"{GREEN}All tests passed!{RESET}")
    elif status == "failed":
        print(f"{RED}Test failed.{RESET}")
        print("Input:", failed_case["input"])
        print("Expected:", failed_case["expected"])
        print("Got:", failed_case["got"])
    else:
        print(f"{RED}Error during execution:{RESET} {error}")
