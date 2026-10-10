import os
import time


def setup_test_files(num_files, file_size_bytes):
    print("Setting up test environments...")

    os.makedirs("raw_images_folder", exist_ok=True)

    for i in range(num_files):
        with open(f"raw_images_folder/img_{i}.bin", "wb") as f:
            f.write(b"\x00" * file_size_bytes)

    with open("packed_dataset.tfrecord", "wb") as f:
        f.write(b"\x00" * (num_files * file_size_bytes))

    print("Setup complete.\n")


def test_random_small_files(num_files):
    print(f"Test 1: Reading {num_files} separate small files")
    start_time = time.time()

    for i in range(num_files):
        with open(f"raw_images_folder/img_{i}.bin", "rb") as f:
            data = f.read()

    elapsed = time.time() - start_time
    print(f"-> Time Taken: {elapsed:.4f} seconds")


def test_sequential_large_file(num_files, file_size_bytes):
    print("\nTest 2: Reading 1 large packed file")
    start_time = time.time()

    with open("packed_dataset.tfrecord", "rb") as f:
        for _ in range(num_files):
            data = f.read(file_size_bytes)

    elapsed = time.time() - start_time
    print(f"-> Time Taken: {elapsed:.4f} seconds")


def cleanup(num_files):
    for i in range(num_files):
        os.remove(f"raw_images_folder/img_{i}.bin")

    os.rmdir("raw_images_folder")
    os.remove("packed_dataset.tfrecord")


def main():
    num_files = 1000
    file_size = 4096

    setup_test_files(num_files, file_size)
    test_random_small_files(num_files)
    test_sequential_large_file(num_files, file_size)
    cleanup(num_files)


if __name__ == "__main__":
    main()