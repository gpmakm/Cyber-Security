# 🔐 Pentest Toolkit (Python)

A **Python-based modular penetration testing toolkit** designed for learning, experimentation, and basic security analysis.

This project demonstrates core concepts of networking, security testing, and modular software design using Python.

---

## 🚀 Features

* 🔍 **Port Scanner**
  Scan a target for open TCP ports.

* 🌐 **Subdomain Enumeration** *(optional)*
  Discover subdomains using wordlists.

* 📂 **Directory Bruteforce** *(optional)*
  Identify hidden directories on web servers.

* 🔐 **Login Bruteforce (Demo Only)** *(optional)*
  Test login systems in controlled environments.

* 🧩 **Modular Architecture**
  Each feature is implemented as an independent module.

---

## 📁 Project Structure

```
pentest_toolkit/
│
├── main.py
├── modules/
│   ├── port_scanner.py
│   ├── directory_bruteforce.py
│   ├── subdomain_enum.py
│
├── utils/
│   ├── logger.py
│   ├── helpers.py
│
├── wordlists/
│   ├── common.txt
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pentest-toolkit.git
cd pentest-toolkit
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run Port Scanner

```bash
python main.py --target 127.0.0.1 --start 1 --end 1024
```

### Example (Python usage)

```python
from modules.port_scanner import scan_ports

result = scan_ports("127.0.0.1", 1, 1024)

for port in result:
    print(port)
```

---

## 📊 Example Output

```
Scanning target: 127.0.0.1

Port 80 OPEN (http)
Port 443 OPEN (https)
```

---

## 🧠 How It Works

* Uses Python `socket` library for TCP connections
* Attempts connection on each port
* Identifies open ports based on successful responses
* Returns structured results for further use

---

## ⚠️ Disclaimer

This project is developed **for educational purposes only**.

* Do **NOT** use this tool on systems without proper authorization
* Unauthorized scanning or attacks may be illegal
* The developer is not responsible for misuse

---

## 🛠️ Future Improvements

* Multi-threaded scanning (faster performance)
* Banner grabbing (service detection)
* CLI enhancements (`argparse`)
* Reporting system (JSON/CSV output)
* Web-based dashboard

---

## 🤝 Contributing

Contributions are welcome!

* Fork the repository
* Create a new branch
* Submit a pull request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed as part of a cybersecurity learning project.

---
