

# 🧪 TestSphere – Selenium Automation Testing Framework

A clean, modular, and scalable automation framework built using **Python, Selenium, Pytest, and Page Object Model (POM)**.
This project demonstrates end-to-end test automation for **SauceDemo Login Flow**, along with reporting, utilities, and best practices used in modern QA engineering.

---

## 🚀 Features

✔ **Selenium WebDriver Automation**
✔ **Pytest Test Runner**
✔ **Page Object Model (POM) Architecture**
✔ **Reusable Helper Functions**
✔ **Browser Factory (Chrome / Edge supported)**
✔ **HTML Test Reports (pytest-html)**
✔ **Screenshot Capture on Failure**
✔ **Configurable Test Structure**
✔ **Easy to Scale & Maintain**

---

## 📁 Project Folder Structure

```
TestSphere/
│
├── helpers/
│   ├── driver_factory.py          # Creates WebDriver instance
│   ├── base_page.py               # Common page actions
│   └── __init__.py
│
├── pages/
│   ├── login_page.py              # Page Objects for SauceDemo login page
│   └── __init__.py
│
├── tests/
│   ├── test_saucedemo_login.py    # Test case for login validations
│   └── __init__.py
│
├── reports/
│   └── saucedemo_login_report.html  # Generated test reports
│
├── screenshots/                   # Auto-saved screenshots on test failure
│
├── requirements.txt               # Python dependencies
├── pytest.ini                     # Pytest configuration
├── README.md                      # Project documentation
└── .gitignore
```

---

## 🛠️ Tech Stack

| Component                | Technology              |
| ------------------------ | ----------------------- |
| **Programming Language** | Python                  |
| **Test Runner**          | Pytest                  |
| **Automation Tool**      | Selenium                |
| **Design Pattern**       | Page Object Model (POM) |
| **Reports**              | pytest-html             |
| **Browser Automation**   | Chrome WebDriver        |

---

## ⚙️ Installation & Setup

### **Step 1: Clone the Repository**

```
git clone https://github.com/GPCHANDU08/Test_Sphere.git
cd Test_Sphere
```

### **Step 2: Create a Virtual Environment**

```
python -m venv venv
```

### **Step 3: Activate the Virtual Environment**

**Windows:**

```
venv\Scripts\activate
```

**Linux/Mac:**

```
source venv/bin/activate
```

### **Step 4: Install Dependencies**

```
pip install -r requirements.txt
```

---

## ▶️ Running the Tests

### **Run all tests**

```
pytest
```

### **Run test with HTML Report**

```
pytest tests/test_saucedemo_login.py --html=reports/saucedemo_login_report.html
```

### **Run tests with verbosity**

```
pytest -v
```

---

## 📷 Screenshots

Screenshots are automatically captured when a test fails and saved in the **screenshots/** folder.

---

## 📊 HTML Reporting

The framework generates clean test execution reports using `pytest-html`.

Example:

```
reports/saucedemo_login_report.html
```

---

## 🧩 Page Object Model (POM)

The framework uses POM for maintainability:

### Example: `login_page.py`

* Username field locator
* Password field locator
* Login button locator
* Login action method
* Validation functions

This modular design ensures tests remain clean and readable.

---

## 🧪 Sample Test Case

### `test_saucedemo_login.py`

✔ Tests valid login
✔ Tests invalid login
✔ Verifies error messages
✔ Checks UI element visibility

---

## 📌 Future Enhancements

🔹 Add parallel execution using `pytest-xdist`
🔹 Integrate Allure reporting
🔹 Add Jenkins CI/CD pipeline
🔹 Add API testing module
🔹 Add data-driven testing support

---

## 🎯 Key Learning Outcomes (For Resume / Interview)

* Built a complete Selenium automation framework from scratch
* Implemented Page Object Model (POM) design
* Automated end-to-end login flow for a real website
* Integrated HTML reporting and screenshots
* Managed browser configuration using WebDriver factory
* Used Pytest fixtures for reusable setups

---

## 👨‍💻 Author

**Goparaju Poorna Chand**
Automation Testing • Python • Selenium • QA Engineer

---

## ⭐ Support

If you like this project, feel free to ⭐ star the repository!

---



