# Use case 7 (Lab)

## **Data Overview**
- The dataset contains various columns related to football players, including their names, teams, positions, physical attributes, performance statistics, and financial values.
- Key columns include `player`, `team`, `position`, `height`, `age`, `appearance`, `goals`, `assists`, `yellow cards`, `red cards`, `minutes played`, `days_injured`, `current_value`, and `highest_value`.

## **Data Cleaning**
- The notebook includes steps for handling missing values, outliers, and data inconsistencies.
- Data types of the columns are verified and corrected where necessary.

## **Descriptive Statistics**
- Summary statistics such as mean, median, and standard deviation are calculated for numerical columns.
- Distribution plots (e.g., histograms, box plots) are used to visualize the distributions of key variables like `age`, `height`, `goals`, `assists`, and `current_value`.

## **Data Visualization**
- Bar plots, scatter plots, and heatmaps are used to visualize relationships between variables.
- Examples include:
  - Distribution of players' ages and heights.
  - Correlation between `current_value` and `highest_value`.
  - Relationship between `appearances` and `goals`.

## **Feature Engineering**
- New features are created based on existing data to enhance the analysis. For example:
  - `position_encoded` to represent positions numerically.
  - Binary encoding of categorical variables such as `winger`.

# Machine Learning (ML) Results

## **Modeling**
- The notebook explores machine learning models to predict `current_value` of players based on their attributes.
- Regression models like Linear Regression, Decision Trees, and Random Forests are used for this purpose.

## **Model Evaluation**
- Performance metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared are used to evaluate the models.
- Cross-validation techniques are employed to ensure the robustness of the model results.

## **Feature Importance**
- Feature importance analysis is conducted to understand which variables most significantly impact the `current_value` of players.
- Visualizations like bar charts are used to display the importance of features.
## **My insights**
the model isn't great needs more revisions, if there was league name column that will help a lot since every football league bay different prices for players due to league competition.
in my next try I will try feature engineer to add the column and create another model and compare it. 