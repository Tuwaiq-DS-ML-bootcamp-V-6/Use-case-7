# Soccer League Data Analysis

## Overview

This project aims to analyze soccer league data from various continents, including Europe, America, Africa, and Asia. We perform exploratory data analysis (EDA) and build machine learning models to predict target variables using linear regression techniques.

## Dataset

The dataset contains information about soccer leagues from different continents. The key features include:

- **continent**: The continent where the league is located (e.g., Europe, America, Africa, Asia).
- **various features**: Different attributes related to the soccer league (e.g., team statistics, match outcomes).
- **target**: The target variable we aim to predict (e.g., team performance, match results).

## Files

- `EDA_explain_template.ipynb`: The Jupyter Notebook containing the code for data analysis and model building.
- `final_data.csv`: The dataset used for the analysis.

## Installation

To run the notebook and replicate the analysis, you need to have Python and the following libraries installed:


## Usage

1. Clone the repository and navigate to the project directory.
2. Place the `final_data.csv` file in the same directory as the notebook.
3. Open the Jupyter Notebook.
4. Follow the steps in the notebook to load the data, perform exploratory data analysis, and build the machine learning models.

## Analysis and Modeling

### Exploratory Data Analysis (EDA)

In the EDA section, we:

- Load and inspect the dataset.
- Check for null values and handle missing data.
- Visualize the distribution of key features.
- Identify and analyze outliers.

### Model Building

We build and evaluate linear regression models using GridSearchCV for hyperparameter tuning. The models include:

- **Linear Regression**
- **Ridge Regression**
- **Lasso Regression**

#### Creating Models for Different Continents

We create separate models for each continent (Africa, America, Asia, and Europe) to predict the target variable.


## Results

The results of the GridSearchCV for Ridge and Lasso regression models are printed, including the best parameters and R2 scores.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. We welcome all improvements and suggestions.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
