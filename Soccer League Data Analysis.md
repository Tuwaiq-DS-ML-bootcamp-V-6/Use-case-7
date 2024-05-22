<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Soccer League Data Analysis</title>
</head>
<body>
    <h1>Soccer League Data Analysis</h1>

    <h2>Overview</h2>
    <p>This project aims to analyze soccer league data from various continents, including Europe, America, Africa, and Asia. We perform exploratory data analysis (EDA) and build machine learning models to predict target variables using linear regression, logistic regression, and decision tree techniques.</p>

    <h2>Dataset</h2>
    <p>The dataset contains information about soccer leagues from different continents. The key features include:</p>
    <ul>
        <li><strong>continent</strong>: The continent where the league is located (e.g., Europe, America, Africa, Asia).</li>
        <li><strong>various features</strong>: Different attributes related to the soccer league (e.g., team statistics, match outcomes).</li>
        <li><strong>target</strong>: The target variable we aim to predict (e.g., team performance, match results).</li>
    </ul>

    <h2>Files</h2>
    <ul>
        <li><code>EDA_explain_template.ipynb</code>: The Jupyter Notebook containing the code for exploratory data analysis.</li>
        <li><code>logistic_regression.ipynb</code>: The Jupyter Notebook containing the code for logistic regression model building and evaluation.</li>
        <li><code>decision_tree.ipynb</code>: The Jupyter Notebook containing the code for decision tree model building and evaluation.</li>
        <li><code>final_data.csv</code>: The dataset used for the analysis.</li>
    </ul>

    <h2>Installation</h2>
    <p>To run the notebooks and replicate the analysis, you need to have Python and the following libraries installed:</p>
    <pre>
        <code>numpy, pandas, matplotlib, seaborn, scikit-learn</code>
    </pre>

    <h2>Usage</h2>
    <ol>
        <li>Clone the repository and navigate to the project directory.</li>
        <li>Place the <code>final_data.csv</code> file in the same directory as the notebooks.</li>
        <li>Open the Jupyter Notebooks.</li>
        <li>Follow the steps in the notebooks to load the data, perform exploratory data analysis, and build the machine learning models.</li>
    </ol>

    <h2>Analysis and Modeling</h2>

    <h3>Exploratory Data Analysis (EDA)</h3>
    <p>In the EDA section, we:</p>
    <ul>
        <li>Load and inspect the dataset.</li>
        <li>Check for null values and handle missing data.</li>
        <li>Visualize the distribution of key features.</li>
        <li>Identify and analyze outliers.</li>
    </ul>

    <h3>Model Building</h3>
    <p>We build and evaluate several machine learning models using different techniques. The models include:</p>
    <ul>
        <li><strong>Linear Regression</strong></li>
        <li><strong>Logistic Regression</strong></li>
        <li><strong>Decision Tree</strong></li>
    </ul>

    <h4>Creating Models for Different Player Positions</h4>
    <p>We create separate models for each player position (goalkeepers, defenders, midfielders, forwards) to predict the target variable.</p>

    <h2>Results</h2>
    <p>The results of the models are evaluated based on various metrics such as accuracy, precision, recall, and F1-score. The best parameters and scores for each model are printed and analyzed.</p>

    <h2>Contributing</h2>
    <p>If you would like to contribute to this project, please fork the repository and submit a pull request. We welcome all improvements and suggestions.</p>

    <h2>License</h2>
    <p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for details.</p>
</body>
</html>
