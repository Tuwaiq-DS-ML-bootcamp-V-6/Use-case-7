# Soccer League Data Analysis

## Overview

This project aims to analyze soccer league data from various continents, including Europe, America, Africa, and Asia. We perform exploratory data analysis (EDA) and build machine learning models to predict target variables using linear regression, logistic regression, and decision tree techniques.

## Dataset

The dataset contains information about soccer leagues from different continents. The key features include:

- **continent**: The continent where the league is located (e.g., Europe, America, Africa, Asia).
- **various features**: Different attributes related to the soccer league (e.g., team statistics, match outcomes).
- **target**: The target variable we aim to predict (e.g., team performance, match results).

## Files

- `EDA_explain_template.ipynb`: The Jupyter Notebook containing the code for exploratory data analysis.
- `logistic_regression.ipynb`: The Jupyter Notebook containing the code for logistic regression model building and evaluation.
- `decision_tree.ipynb`: The Jupyter Notebook containing the code for decision tree model building and evaluation.
- `final_data.csv`: The dataset used for the analysis.

## Installation

To run the notebooks and replicate the analysis, you need to have Python and the following libraries installed:


## Usage

1. Clone the repository and navigate to the project directory.
2. Place the `final_data.csv` file in the same directory as the notebooks.
3. Open the Jupyter Notebooks.
4. Follow the steps in the notebooks to load the data, perform exploratory data analysis, and build the machine learning models.

## Analysis and Modeling

### Exploratory Data Analysis (EDA)

In the EDA section, we:

- Load and inspect the dataset.
- Check for null values and handle missing data.
- Visualize the distribution of key features.
- Identify and analyze outliers.

### Model Building

We build and evaluate several machine learning models using different techniques. The models include:

- **Linear Regression**
- **Logistic Regression**
- **Decision Tree**

#### Creating Models for Different Player Positions

We create separate models for each player position (goalkeepers, defenders, midfielders, forwards) to predict the target variable.

## Results

The results of the models are evaluated based on various metrics such as accuracy, precision, recall, and F1-score. The best parameters and scores for each model are printed and analyzed.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. We welcome all improvements and suggestions.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
