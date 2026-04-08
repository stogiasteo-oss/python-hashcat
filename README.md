# 🔐 MD5 Password Cracker (Python)

A simple and educational Python tool for cracking MD5 hashes using wordlists.

---

## 📌 Description

This project demonstrates how hashed passwords (specifically MD5) can be cracked using dictionary attacks. It is designed for learning purposes and basic experimentation with password security concepts.

---

## ⚙️ Features

* Crack MD5 hashes using a wordlist
* Fast lookup using standard Python libraries
* Simple and easy-to-use command line interface
* Works with large wordlists (e.g. rockyou.txt)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/md5-password-cracker.git
cd md5-password-cracker
```

### 2. Download a wordlist

You can use a common wordlist such as rockyou.txt:
https://github.com/zacheller/rockyou

Make sure the file is extracted and placed in the same directory as the script.

---

## ▶️ Usage

```bash
python python-hashcat-main.py <hash> <wordlist>
```

### Example:

```bash
python python-hashcat-main.py 5f4dcc3b5aa765d61d8327deb882cf99 rockyou.txt
```

---

## 🧠 How it works

The script:

1. Takes an MD5 hash as input
2. Reads each password from the wordlist
3. Hashes each password using MD5
4. Compares it with the target hash
5. Stops when a match is found

---

## ⚠️ Disclaimer

This project is intended for **educational purposes only**.

Do NOT use this tool on systems, networks, or data that you do not own or have explicit permission to test. Unauthorized use may be illegal.

---

## 🛠️ Requirements

* Python 3.x

(No external libraries required)

---

## 📂 Project Structure

```
md5-password-cracker/
│── python-hashcat-main.py
│── README.md
```

---

## 💡 Future Improvements

* Support for multiple hash types (SHA-1, SHA-256)
* Add GPU acceleration (advanced)
* Progress indicator / statistics
* GUI version

---

## 👤 Author

Your Name

---

## ⭐ Contributing

Feel free to fork this project and improve it!
