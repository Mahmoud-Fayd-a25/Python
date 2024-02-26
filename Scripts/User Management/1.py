# Automating user management tasks
# Make sure to run the script with appropriate permissions (sudo) since user management tasks typically require administrative privileges.
# Customize the values of username, password, new_password, new_shell, new_home, and group according to your requirements.


import subprocess

# Example 1: Creating a user


def create_user(username, password):
    subprocess.run(["sudo", "useradd", username])
    subprocess.run(["sudo", "passwd", "--stdin", username],
                   input=password.encode())

# Example 2: Deleting a user


def delete_user(username):
    subprocess.run(["sudo", "userdel", "-r", username])

# Example 3: Changing a user's password


def change_password(username, new_password):
    subprocess.run(["sudo", "passwd", "--stdin", username],
                   input=new_password.encode())

# Example 4: Listing all users


def list_users():
    result = subprocess.run(["sudo", "cat", "/etc/passwd"],
                            capture_output=True, text=True)
    users = [line.split(":")[0]
             for line in result.stdout.split("\n") if line.strip()]
    print("Users:", users)

# Example 5: Changing a user's shell


def change_shell(username, new_shell):
    subprocess.run(["sudo", "chsh", "-s", new_shell, username])

# Example 6: Locking a user account


def lock_user(username):
    subprocess.run(["sudo", "passwd", "-l", username])

# Example 7: Unlocking a user account


def unlock_user(username):
    subprocess.run(["sudo", "passwd", "-u", username])

# Example 8: Modifying user's home directory


def modify_home_directory(username, new_home):
    subprocess.run(["sudo", "usermod", "-d", new_home, username])

# Example 9: Adding user to a group


def add_user_to_group(username, group):
    subprocess.run(["sudo", "usermod", "-aG", group, username])

# Example 10: Removing user from a group


def remove_user_from_group(username, group):
    subprocess.run(["sudo", "deluser", username, group])

# Execute examples


def main():
    username = "testuser"
    password = "testpassword"
    new_password = "newpassword"
    new_shell = "/bin/bash"
    new_home = "/home/newuser"
    group = "sudo"

    create_user(username, password)
    list_users()
    change_password(username, new_password)
    change_shell(username, new_shell)
    lock_user(username)
    unlock_user(username)
    modify_home_directory(username, new_home)
    add_user_to_group(username, group)
    remove_user_from_group(username, group)
    delete_user(username)
    list_users()


if __name__ == "__main__":
    main()
