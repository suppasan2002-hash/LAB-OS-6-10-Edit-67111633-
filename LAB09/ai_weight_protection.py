import os


def simulate_hpc_cluster():
    weight_file = "production_resnet50.pth"

    if os.path.exists(weight_file):
        os.chmod(weight_file, 0o666)
        os.remove(weight_file)

    print("Downloading 250MB Production Model Weights...")
    with open(weight_file, "w") as f:
        f.write("0101010101010101010")

    print("AI Ops: Securing model weights at the OS level (Read-Only)...")
    os.chmod(weight_file, 0o444)

    print("\n[Junior Dev] Running script: training_job.py")
    print("[Junior Dev] 'Oops, I opened the production model in Write mode!'")

    try:
        with open(weight_file, "w") as model:
            model.write("Initializing random weights... Overwriting!")
        print("Write succeeded.")
    except PermissionError:
        print(">>> [DISASTER AVERTED] OS Kernel denied write access.")
        print(">>> The multi-million dollar model is safe.")


if __name__ == "__main__":
    simulate_hpc_cluster()