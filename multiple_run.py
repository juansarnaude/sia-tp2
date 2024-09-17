import subprocess
import sys
import time


def run_command(times):

    for i in range(times):
        print(f"Running command iteration {i + 1}")
        command = ['python', 'main.py', 'config/config.json', sys.argv[1] + str(i)]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Output:", result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)



if __name__ == "__main__":
    # Define how many times you want to run the command
    num_times = 5
    run_command(num_times)
