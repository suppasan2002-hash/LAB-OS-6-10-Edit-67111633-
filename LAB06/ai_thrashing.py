import os
import time


def fast_ram_access(iterations):
    """จำลองการทำงานเมื่อข้อมูลอยู่ใน RAM"""
    simulated_ram = [0.0] * 1000
    start_time = time.time()

    for _ in range(iterations):
        for i in range(len(simulated_ram)):
            simulated_ram[i] += 1.5

    return time.time() - start_time


def slow_swap_thrashing_access(iterations, filename="swap_file.bin"):
    """จำลองการอ่านเขียนดิสก์ซ้ำ ๆ เมื่อหน่วยความจำไม่พอ"""
    with open(filename, "wb") as f:
        f.write(b"\x00" * 1000)

    start_time = time.time()

    for _ in range(iterations):
        with open(filename, "r+b") as f:
            data = bytearray(f.read())

            for i in range(len(data)):
                data[i] = (data[i] + 1) % 255

            f.seek(0)
            f.write(data)

    os.remove(filename)
    return time.time() - start_time


def main():
    iterations = 10000
    print("--- Simulating AI Training Batch (10,000 Iterations) ---")

    print("\n1. Scenario: Batch fits in RAM")
    ram_time = fast_ram_access(iterations)
    print(f"   -> Processing Time: {ram_time:.4f} seconds")

    print("\n2. Scenario: OS is swapping data to disk")
    swap_time = slow_swap_thrashing_access(iterations)
    print(f"   -> Processing Time: {swap_time:.4f} seconds")

    performance_drop = swap_time / ram_time
    print(f"\n>>> Thrashing made the system {performance_drop:.0f} times slower!")


if __name__ == "__main__":
    main()