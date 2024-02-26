# Fabric is a library for streamlining the use of SSH for application deployment or systems administration tasks.
# It provides a high-level interface for executing commands on remote hosts, copying files, and managing connections.
# In this example, we use Fabric to connect to multiple remote hosts and execute various tasks, such as running commands, copying files, and executing scripts.
# We define tasks using the @task decorator and then connect to each host to execute the tasks.
# The connect_kwargs parameter is used to provide the password for connecting to the remote hosts.
# Replace 'user@host1', 'user@host2' and 'password' with actual SSH login information for your remote hosts.


from fabric import Connection, task

# Define hosts and user
hosts = ['user@host1', 'user@host2']
password = 'password'

# Example 1: Run a command on remote hosts


@task
def run_command(c):
    c.run('uname -a')

# Example 2: Run multiple commands sequentially


@task
def run_multiple_commands(c):
    c.run('ls -l')
    c.run('df -h')

# Example 3: Copy a file from local to remote hosts


@task
def copy_file(c):
    c.put('local_file.txt', '/remote/path/file.txt')

# Example 4: Copy a file from remote to local host


@task
def copy_file_from_remote(c):
    c.get('/remote/path/file.txt', 'local_file.txt')

# Example 5: Execute a script on remote hosts


@task
def execute_script(c):
    c.put('local_script.sh', '/remote/path/script.sh')
    c.run('chmod +x /remote/path/script.sh')
    c.run('/remote/path/script.sh')


# Connect to hosts and execute tasks
for host in hosts:
    conn = Connection(host, connect_kwargs={"password": password})

    print(f"Running tasks on {host}:")
    run_command(conn)
    run_multiple_commands(conn)
    copy_file(conn)
    copy_file_from_remote(conn)
    execute_script(conn)
    print()
