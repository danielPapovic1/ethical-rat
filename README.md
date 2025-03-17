# **Remote Access Tool (RAT) Project**

**Disclaimer:** This project is for **educational purposes and ethical hacking ONLY**. It demonstrates RAT construction for security professionals to understand attack techniques and develop defenses. **Unauthorized use is illegal and unethical.** All functionality is configured for localhost testing.

---

## **Overview**

This educational RAT demonstrates remote command execution, file transfer, and persistence across operating systems (only Linux right now). The client (Go) prioritizes performance and concurrency, while the server (Python 3\) leverages rapid development capabilities.

---

## **Features**

* **Reverse Shell:** Establishes an outbound connection from the target to the C2 server for interactive command execution.  
* **Secure File Transfer:** Employs Base64 encoding for safe transmission of binary files.  
* **Persistent Access (Linux):** Utilizes cron jobs to re-establish control after system reboots. *(Windows persistence is planned for future development.)*  
* **Cross-Platform Compatibility:** Core functionality (networking, command execution, file transfer) works on Windows and Linux.  
* **Pre-Built Binaries (Windows):** Includes pre-compiled Windows executables. You can also compile from source.  
* **Demonstrates** remote command execution, file transfer, file upload, screenshot, regular Linux shell commands, and persistence across operating systems (only Linux right now). The client (Go) prioritizes performance and concurrency, while the server (Python 3\) leverages rapid development capabilities.

* **Recommended OS:** Any Linux distro: Ubuntu, Debian, Kali, etc. 

---

## **System Requirements**

* **Golang (Client Compilation):** NOT NEEDED TO RUN THE EXECUTABLES: HOWEVER ( needed for custom client builds.)  
* **Python 3 (Server):** Latest version of Python 3\.  
* **Operating System Support:**  
  * **Client:** Compiles for Windows and Linux.  
  * **Server:** Runs on any system with Python 3\.  
  * **Persistence:** Only available on Linux distributions right now.

---

## **Installation & Setup**

### **1\. Clone the Repository**

mkdir ethical-rat-proj  
cd ethical-rat-proj  
git clone https://github.com/danielPapovic1/ethical-rat.git

## **For Linux:**

To run the main file I provided on Linux, run:

./main , inside of the correct directory

To compile the client I provided on Linux, run:

go build main.go

To compile a new version of the client on Linux, run: 

mkdir your-dir
touch your_file.go
code .
Then inside your VS Code terminal or a terminal in the same working directory type:
go mod init malware-module
go get github.com/kbinani/screenshot.git
Then import "github.com/kbinani/screenshot" in your new client file
You can test it with "go run your_file.go"

Once done writing compile it with "go build your_file.go"


## **Server Setup**

Ensure that Python 3 is installed, then start the server:

python3 server.py

The server listens on a specific IP and port for incoming connections from the client.

### **Interaction**

Once the client establishes a connection to the server through the web socket, you can issue commands, transfer files, and utilize the reverse shell for interactive control.

## **Contributing**

Contributions, suggestions, and improvements are welcome.

## **License**

This project is licensed under the MIT License.

Future updates may be in store.
