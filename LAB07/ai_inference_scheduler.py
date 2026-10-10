import time
from collections import deque


def run_fcfs():
    print("\n--- FCFS: ให้คำขอแรกทำจนเสร็จก่อน ---")
    for user, tokens in [("User A", 10), ("User B", 2)]:
        print(f"{user} เริ่มสร้าง {tokens} tokens")
        for _ in range(tokens):
            time.sleep(0.5)
        print(f"{user} เสร็จแล้ว")


def run_round_robin():
    print("\n--- Round Robin: สลับสร้างทีละ token ---")
    requests = deque([["User A", 10], ["User B", 2]])

    while requests:
        user, remaining = requests.popleft()
        print(f"{user} สร้าง token")
        time.sleep(0.05)
        remaining -= 1

        if remaining > 0:
            requests.append([user, remaining])
        else:
            print(f"{user} เสร็จแล้ว")


if __name__ == "__main__":
    run_fcfs()
    run_round_robin()