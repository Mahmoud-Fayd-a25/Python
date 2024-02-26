# Automating process management tasks using the subprocess module
# You can customize the commands and parameters passed to subprocess.run() 


import subprocess

# Example 1: Running a simple shell command


def run_simple_command():
    result = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE)
    print("Example 1:")
    print(result.stdout.decode())

# Example 2: Running a command with shell expansion


def run_shell_expansion():
    result = subprocess.run("echo $HOME", shell=True, stdout=subprocess.PIPE)
    print("Example 2:")
    print(result.stdout.decode())

# Example 3: Running a command and capturing its output


def capture_command_output():
    result = subprocess.run(["echo", "Hello, World!"], stdout=subprocess.PIPE)
    print("Example 3:")
    print(result.stdout.decode())

# Example 4: Running a command with input


def run_command_with_input():
    result = subprocess.run(
        ["grep", "World"], input=b"Hello\nWorld\nPython", stdout=subprocess.PIPE)
    print("Example 4:")
    print(result.stdout.decode())

# Example 5: Running a command in a specific directory


def run_command_in_directory():
    result = subprocess.run(["ls", "-l"], cwd="/tmp", stdout=subprocess.PIPE)
    print("Example 5:")
    print(result.stdout.decode())

# Example 6: Running a command with environment variables


def run_command_with_environment():
    result = subprocess.run(["echo", "$HOME"], shell=True, env={
                            "HOME": "/tmp"}, stdout=subprocess.PIPE)
    print("Example 6:")
    print(result.stdout.decode())

# Example 7: Running a command asynchronously


def run_async_command():
    process = subprocess.Popen(["sleep", "3"])
    print("Example 7:")
    print("Waiting for process to complete...")
    process.wait()
    print("Process completed")

# Example 8: Running a command and capturing stderr


def capture_stderr():
    result = subprocess.run(["ls", "nonexistentfile"],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("Example 8:")
    print("STDOUT:")
    print(result.stdout.decode())
    print("STDERR:")
    print(result.stderr.decode())

# Example 9: Running a command and checking its return code


def check_return_code():
    result = subprocess.run(["ls", "nonexistentfile"],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("Example 9:")
        print("Command failed with return code:", result.returncode)

# Example 10: Running a command with timeout


def run_command_with_timeout():
    try:
        result = subprocess.run(["sleep", "5"], timeout=3)
    except subprocess.TimeoutExpired:
        print("Example 10:")
        print("Command timed out")

# Execute examples


def main():
    run_simple_command()
    run_shell_expansion()
    capture_command_output()
    run_command_with_input()
    run_command_in_directory()
    run_command_with_environment()
    run_async_command()
    capture_stderr()
    check_return_code()
    run_command_with_timeout()


if __name__ == "__main__":
    main()
