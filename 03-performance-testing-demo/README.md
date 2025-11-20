# 03-LOAD & PERFORMANCE TESTING DEMO

## 🎯 Goal
To demonstrate expertise in non-functional testing by simulating high user load on the Sauce Demo login/purchase endpoint. The objective is to **identify potential performance bottlenecks** and determine the system's capacity under stress.

## 🛠️ Technologies
* **Apache JMeter**: Used to design and execute multi-threaded load test scenarios.
* **Python (Locust)**: Referenced as an alternative for code-based, distributed load testing.

## 🧪 Scenario (Sauce Demo Stress Test)
1.  **Test Plan:** Stress test the `/login` and `/checkout` API endpoints (simulating user actions without the browser).
2.  **Users:** 200 concurrent users.
3.  **Ramp-Up:** 60 seconds (200 users start within 1 minute).
4.  **Duration:** 5 minutes.

## 📊 Key Performance Indicators (KPIs)

A successful performance test focuses on these metrics:

| Metric | Goal | Rationale |
| :--- | :--- | :--- |
| **Average Response Time** | < 500 ms | Ensure rapid feedback for the user experience. |
| **Error Rate** | < 1% | Ensure API stability under high volume. |
| **Throughput (tps)** | > 50 transactions/sec | Confirm the system can handle the expected traffic volume. |

## 🔗 Test Artifact

The load test configuration is defined in the provided JMeter Test Plan file.

* `SauceDemo_LoadTest.jmx` (JMeter Test Plan File)
