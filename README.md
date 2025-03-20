# BMI Calculator

A simple web application to calculate Body Mass Index (BMI) based on user input. The frontend is built using **HTML**, **Bootstrap**, and **JavaScript**, while the backend is powered by **Python** and **Flask**. The app takes height (in centimeters) and weight (in kilograms) as input and calculates the BMI, along with a health status.

---

## Features

- **User Input**: Accepts height (in cm) and weight (in kg).
- **BMI Calculation**: Computes BMI using the formula:  
  **BMI = weight (kg) / (height (m)²)**.
- **Health Status**: Provides a health status based on the BMI value:
  - Underweight (BMI < 18.5)
  - Normal weight (18.5 ≤ BMI < 24.9)
  - Overweight (25 ≤ BMI < 29.9)
  - Obese (BMI ≥ 30)
- **Responsive Design**: Built with **Bootstrap** for a clean and responsive user interface.
- **API Integration**: The frontend communicates with the backend via a REST API to fetch BMI results.

---

## Technologies Used

- **Frontend**:
  - HTML
  - Bootstrap (for styling)
  - JavaScript (for fetching data from the backend)
- **Backend**:
  - Python
  - Flask (for creating the API)
  - Flask-CORS (to handle cross-origin requests)

---

## How to Use

### Prerequisites

1. **Python**: Make sure Python is installed on your system. You can download it from [here](https://www.python.org/downloads/).
2. **Flask**: Install Flask and Flask-CORS using pip:
   ```bash
   pip install flask flask-cors
