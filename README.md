SauceDemo Automation Framework (Selenium + Python + Pytest)

This project is a complete automation framework for the SauceDemo website using
Python, Selenium, Pytest, the Page Object Model (POM), and JSON-based test data.

The framework automates the complete purchase flow:
Login → Product Sorting → Add to Cart → Checkout → Overview → Order Completion,
with detailed assertions at every step.

---

 Tech Stack

* Python
* Selenium WebDriver
* Pytest
* Page Object Model (POM)
* JSON-based Test Data
* HTML Test Reporting (pytest-html)
* Screenshots of error

---

 Supported Browsers

The test framework supports running tests on the following browsers:
* Chrome
* Edge
* Firefox
  
You can choose the browser at runtime using:

    --browser_name=edge

If no browser is provided, Edge is used as the default.

---

 Test Scenarios Automated

 1. Login Page – 6 User Types

The test loads users from users.json and checks multiple SauceDemo user types:

* Standard User
* Locked Out User
* Problem User
* Error User
* Performance Glitch User
* Visual User
---

 2. Product Page – Sorting Assertions

Validations for all sorting filters:

* A → Z
* Z → A
* Low Price → High Price
* High Price → Low Price

Each sorting operation is asserted to verify correct ordering.

---

 3. Add to Cart – JSON-Driven

The framework reads product names from:
items_to_buy.json

The script:
* Loads the list of items from JSON
* Adds them to the cart

---

 4. Cart Page Assertions

Validates that:

* Items in the cart match the items listed in items_to_buy.json
* No extra or missing products are present

---

 5. Checkout Page Validations

Form validation includes:

* Clicking Continue without any input → asserts First Name required
* Filling First Name only → asserts Last Name required
* Filling Last Name only → asserts Postal Code required

Only after all validations pass does the flow proceed.

---

 6. Checkout Overview – Price Assertions

The framework asserts:
* Item Subtotal
* Tax
* Total Amount
Values are extracted from the UI and validated.

---

 7. Order Completion Page

Validates:

* Final confirmation message: “Thank you for your order!”
* Complete success text is printed after final assertion

---

 How to Run the Tests

Execute the order flow test with HTML reporting by following command:

    python -m pytest SauceDemo_Automation/Tests/test_login.py --browser_name=edge --html=reports/report.html --self-contained-html -q -vv

Explanation:

* `--browser_name=edge` : choose browser (chrome / edge / firefox)
* `--html=reports/report.html` : generates an HTML test report
* `--self-contained-html` : keeps report in a single file
* `-q -vv` : quiet mode + detailed logs

---

 Project Highlights

* Complete end-to-end purchase flow automation
* Strong Page Object Model implementation
* JSON-driven test data (users, items)
* Detailed assertions on every page
* Sorting, form validation, cart verification, and price checks included
* Clean folder structure
* HTML reports with screenshots

Suggestions and improvements are welcome!


