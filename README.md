# Use case 7 (Lab)

# Football Players Transfer Value Prediction

## Project Overview
This project aims to develop a predictive model to estimate the transfer values of football players based on their demographics and performance metrics. Two different linear regression models were trained and evaluated to achieve this goal.

## Models

### Model 1:
- **R2 Score**: 0.7691
- **RMSE**: 4,649,973.54
- **Key Features and Coefficients**:
  - Age: -856,850.8
  - Appearance: -1,712,675
  - Goals: 141,764.3
  - Assists: 163,510.9
  - Goals Conceded: -236,561
  - Minutes Played: 2,752,375
  - Days Injured: 665,057.5
  - Games Injured: -1,119,712
  - Award: -1,396,247
  - Highest Value: 7,180,668
  - Various team and position coefficients

### Model 2:
- **R2 Score**: 0.7384
- **RMSE**: 4,949,877.29
- **Key Features and Coefficients**:
  - Appearance: -1,066,031
  - Minutes Played: 2,015,534
  - Award: -1,856,366
  - Highest Value: 7,962,301
  - Manchester City: 425,875.3

## Data
The dataset includes player demographics (age, height, playing position) and performance metrics (goals, assists, injury history) for the seasons 2021-2022 and 2022-2023.

## Data Preprocessing
- **Handling Missing Values**: Missing values were filled using appropriate strategies (e.g., mean for numerical features, mode for categorical features).
- **Outlier Removal**: Outliers were removed using the Interquartile Range (IQR) method.
- **Feature Engineering**: Features were standardized and encoded as needed.

## Model Training and Evaluation
- The models were trained using the linear regression algorithm.
- Model performance was evaluated using metrics such as R2 score, RMSE, and Mean Absolute Error (MAE).
- Hyperparameter tuning was performed using GridSearchCV to optimize model performance.

## Results

### Model 1:
- **R2 Score**: 0.7691
- **RMSE**: 4,649,973.54

### Model 2:
- **R2 Score**: 0.7384
- **RMSE**: 4,949,877.29

## Conclusion
Model 1 provides a more detailed analysis with a higher R2 score and lower RMSE, while Model 2 simplifies the analysis by focusing on significant features. Depending on the priority of either interpretability and simplicity or detailed accuracy, one can choose between the two models. Future improvements could include incorporating additional features and exploring non-linear models.
