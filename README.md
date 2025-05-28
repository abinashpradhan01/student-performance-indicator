# Student Performance Indicator

[![Live Demo](https://img.shields.io/badge/Live-Demo-blue)](https://student-performance-indicator-bvyl.onrender.com)

## Overview

**Student Performance Indicator** is a web application designed to predict and analyze the academic performance of students based on various input parameters. The project uses machine learning techniques to help educators and stakeholders identify students' potential outcomes and provide timely interventions for improvement.

This tool leverages student data such as study habits, demographics, and past academic records to generate insightful predictions about their future performance.

## Features

* Predict student performance using an ML model trained on real data.
* User-friendly web interface for easy input and results viewing.
* Interactive and actionable insights to support academic guidance.
* Deployment on a scalable platform with a live demo available.

## Technologies Used

* Python
* Scikit-learn (for machine learning)
* Flask (backend API)
* HTML/CSS (frontend)
* Render.com (for deployment)

## Exploratory Data Analysis (EDA)

The EDA process is thoroughly documented in:  
📄 `notebook/1. EDA STUDENT PERFORMANCE.ipynb`

Key insights and operations:

- **Initial Data Audit:** Inspected data types, missing values, and value distributions.
- **Univariate & Bivariate Analysis:** 
  - Visualized feature distributions using histograms, box plots, and count plots.
  - Explored correlations between numerical and categorical features with heatmaps and grouped statistics.
- **Key Findings:** 
  - Factors such as **parental education**, **lunch type**, and **test preparation course** showed strong influence on students' math, reading, and writing scores.




## Model Training & Evaluation

The model training workflow is detailed in:  
📄 `notebook/2. MODEL TRAINING.ipynb`

**Steps:**
- **Preprocessing:** Categorical features were encoded; numerical features scaled where necessary.
- **Model Benchmarking:** Multiple regression models were trained and compared using `r2_score`.

### R² Scores Comparison

| Model Name               | R² Score  |
|--------------------------|-----------|
| Ridge                    | 0.8806    |
| Linear Regression        | 0.8803    |
| CatBoost Regressor       | 0.8516    |
| AdaBoost Regressor       | 0.8498    |
| Random Forest Regressor  | 0.8473    |
| Lasso                    | 0.8253    |
| XGBRegressor             | 0.8216    |
| K-Neighbors Regressor    | 0.7838    |
| Decision Tree Regressor | 0.7603    |

- **Best Performer:** Ridge and Linear Regression achieved the highest R² scores.
- **Final Prediction:** Used **Linear Regression** for final predictions.  
  Plotted the predicted vs actual scores to visually assess model fit.


## Usage

You can try the live application here:
[https://student-performance-indicator-bvyl.onrender.com](https://student-performance-indicator-bvyl.onrender.com)

### Running Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/abinashpradhan01/student-performance-indicator.git
   cd student-performance-indicator
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:

   ```bash
   python application.py
   ```

5. Open your browser and go to `http://localhost:5000`



## License

This project is open source and available under the MIT License.

---

