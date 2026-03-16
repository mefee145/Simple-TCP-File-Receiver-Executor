# Simple TCP File Receiver & Executor

A lightweight Python-based client that receives files over a TCP socket connection, executes them locally, and performs automatic cleanup.

## 🚀 How It Works

1.  **Connection:** Connects to a specified server (default: `localhost:5555`).
2.  **Handshake:** Reads the first line from the server to determine the filename (supports `filename|metadata` format).
3.  **Transfer:** Downloads the file data in 32KB chunks.
4.  **Execution:** Automatically runs the file using the system's default handler.
5.  **Cleanup:** Deletes the file immediately after execution to keep the host system clean.

## 🛠️ Installation & Usage

### Prerequisites
- Python 3.x installed on your system.
- A TCP server sending a file stream (the first line must be the filename).

### Running the Client
1. Clone this repository:
   ```bash
   git clone [https://github.com/username/repository-name.git](https://github.com/username/repository-name.git)
   ```
2. Navigate to the directory:
   ```bash
   cd repository-name
   ```
3. Run the script:
   ```bash
   python client.py
   ```

## 📝 Code Structure

The script is designed to be minimal and efficient:
- **Socket:** Uses `socket.AF_INET` for IPv4 and `socket.SOCK_STREAM` for TCP.
- **Buffer Management:** `4096 * 8` (32KB) buffer size for optimized data transfer.
- **Automation:** Uses `os.system()` and `os.remove()` for a seamless "receive-run-delete" workflow.

## ⚠️ Disclaimer
This tool is for educational purposes only. Be cautious when executing files from untrusted servers, as it can execute arbitrary code on your machine.
