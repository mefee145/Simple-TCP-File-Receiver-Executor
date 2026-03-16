##Simple TCP File Receiver & Executor
This script connects to a local server via TCP, receives a file, executes it immediately, and then removes it from the system to ensure a clean workspace.

Connection: Connects to localhost:5555.

Header Parsing: Reads the first line to determine the filename.

Execution: Uses os.system() to run the received file.

Cleanup: Automatically deletes the file after execution.
