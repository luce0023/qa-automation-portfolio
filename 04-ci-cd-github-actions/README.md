# 04-CONTINUOUS INTEGRATION (CI/CD)

## 🎯 Goal
To demonstrate the ability to integrate test automation into the Software Development Life Cycle (SDLC) using **GitHub Actions**. This setup ensures that our automated tests run automatically upon every code change.

## 🛠️ Technologies
* **GitHub Actions**: The CI/CD tool used to define the automation workflow.
* **Ubuntu Latest Runner**: The virtual machine environment where the tests execute.

## ⚙️ Workflow Steps
1.  **Checkout Code:** Get the latest version of the automation framework.
2.  **Setup Python:** Configure the Python environment.
3.  **Install Dependencies:** Install required libraries (e.g., Selenium).
4.  **Run Tests:** Execute all Python tests (e.g., from the `01-web-e2e-saucedemo` folder) in a headless browser environment.
5.  **Report Status:** Send a success or failure status to the GitHub Pull Request.

## 🔗 Workflow File

The entire automation pipeline is defined in the configuration file:

* `.github/workflows/main.yml`
