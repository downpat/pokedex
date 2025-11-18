#!/usr/bin/env python

import subprocess
import sys
import time
import signal
import select
from typing import List

'''
I had Grok write this. Don't give me credit. I only tweaked it a bit
'''

class ProcessManager:
    def __init__(self):
        self.processes: List[subprocess.Popen] = []

    def start_process(self, command: List[str], name: str):
        print(f"Starting {name}: {' '.join(command)}")
        proc = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,  # line buffered
        )
        self.processes.append((name, proc))
        return proc

    def follow_logs(self):
        # Build a dict of fd -> (name, proc) for poll/select
        poll = select.poll()
        fd_to_info = {}

        for name, proc in self.processes:
            if proc.stdout:
                poll.register(proc.stdout.fileno(), select.POLLIN)
                fd_to_info[proc.stdout.fileno()] = (name, proc)

        while True:
            for fd, event in poll.poll(1000):  # 1 second timeout
                if event & (select.POLLIN | select.POLLHUP):
                    name, proc = fd_to_info[fd]
                    line = proc.stdout.readline()
                    if line:
                        print(f"[{name}] {line.rstrip()}")
                    elif proc.poll() is not None:
                        # Process died
                        remaining = proc.stdout.read()
                        if remaining:
                            print(f"[{name}] {remaining.rstrip()}")
                        print(f"{name} exited with code {proc.returncode}")
                        poll.unregister(fd)
                    # If process is dead and no more output, we still keep it in list

            # Check if all processes are dead
            if all(p.poll() is not None for _, p in self.processes):
                print("All child processes have terminated.")
                return max(p.returncode or 0 for _, p in self.processes)

            time.sleep(0.1)  # tiny sleep to avoid busy looping

    def shutdown(self, signum=None, frame=None):
        print(f"\nReceived signal, shutting down...")
        for name, proc in self.processes:
            if proc.poll() is None:
                print(f"Terminating {name} (PID {proc.pid})...")
                proc.terminate()
        
        # Give them a moment to shut down gracefully
        time.sleep(3)
        
        for name, proc in self.processes:
            if proc.poll() is None:
                print(f"Killing {name} (PID {proc.pid})...")
                proc.kill()
        
        sys.exit(0)

def main():
    manager = ProcessManager()

    manager.start_process(
        ["python", "manage.py", "migrate"],
        "run-migrations"
    )

    # Example: replace these with your actual services
    manager.start_process(
		["python", "manage.py", "runserver", "0.0.0.0:31001"],
		"web-server"
	)
    manager.start_process(
		["celery", "-A", "pokedex", "worker", "-l", "INFO"],
        "worker"
    )

    # Handle SIGTERM / SIGINT gracefully (critical for Docker/K8s)
    signal.signal(signal.SIGTERM, manager.shutdown)
    signal.signal(signal.SIGINT, manager.shutdown)

    # Block forever and stream logs
    exit_code = manager.follow_logs()
    sys.exit(exit_code)

if __name__ == "__main__":
    main()


