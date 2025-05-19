import os
import time

def demo_fork_execve():
    pid = os.fork()

    if pid == 0:
        # Child Process
        print(f"[Child] PID: {os.getpid()}, PPID: {os.getppid()}")
        # Replacing this child with `ls` command using execve
        args = ["/bin/ls", "-l"]
        os.execve("/bin/ls", args, os.environ)
        print("[Child] This will not be printed if execve is successful.")
    else:
        # Parent Process
        print(f"[Parent] PID: {os.getpid()}, Waiting for child...")
        os.wait()  # Waiting for child to complete
        print("[Parent] Child has finished.")


def demo_zombie():
    pid = os.fork()

    if pid == 0:
        # Child process
        print(f"[Child-Zombie] PID: {os.getpid()}")
        print("[Child-Zombie] Exiting...")
        exit(0)
    else:
        # Parent process (does NOT call wait)
        print(f"[Parent-Zombie] PID: {os.getpid()}, Child PID: {pid}")
        print("[Parent-Zombie] Sleeping to create zombie...")
        time.sleep(10)  # During this time, child is zombie
        print("[Parent-Zombie] Done sleeping. Now calling wait.")
        os.wait()


def demo_orphan():
    pid = os.fork()

    if pid == 0:
        # Child process
        print(f"[Child-Orphan] PID: {os.getpid()}, Parent PID: {os.getppid()}")
        time.sleep(5)  # Give time for parent to exit
        print(f"[Child-Orphan] My new Parent PID after orphaning: {os.getppid()}")
    else:
        # Parent process
        print(f"[Parent-Orphan] PID: {os.getpid()}, Child PID: {pid}")
        print("[Parent-Orphan] Exiting immediately, child becomes orphan.")
        exit(0)

# MAIN MENU
def main():
    while True:
        print("\n--- Process Control System Calls Demo ---")
        print("1. fork + execve + wait demo")
        print("2. Zombie process demo")
        print("3. Orphan process demo")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            demo_fork_execve()
        elif choice == '2':
            demo_zombie()
        elif choice == '3':
            demo_orphan()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
