# 02-REST API Testing Demo

## 🎯 Goal
To demonstrate skill in **code-based API testing** using Python. This framework validates API contract integrity, status codes, and data payload structure, providing rapid feedback on backend changes.

This approach complements manual/exploratory testing performed with **Postman** by providing an efficient, repeatable regression suite.

## 🛠️ Technologies
* **Python `requests`**: The core library used to send HTTP requests (GET, POST, PUT, DELETE).
* **`pytest`**: The testing framework used to organize and execute tests.
* **`jsonschema`**: Used to validate the structure and data types (schema) of API responses, ensuring **API contract validation**.

## 🧪 Test Scenarios Covered
This framework focuses on critical CRUD (Create, Read, Update, Delete) operations using a public API (`Reqres`):

* **Successful GET Request:** Fetching a single user and validating the response data and contract.
* **Successful POST Request:** Creating a new user and validating the successful `201 Created` status code and the generated ID.
* **Error Handling:** Testing boundary conditions (e.g., requesting a resource that does not exist, expecting a `404 Not Found`).
