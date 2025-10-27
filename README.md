# Real Estate Analytics - Price Prediction

A comprehensive data science project for analyzing and predicting real estate prices by integrating multiple datasets including customer information, broker details, property listings, and deal transactions.

## Project Overview

This project aims to:
- Clean and integrate 6 different CSV datasets related to real estate transactions
- Perform exploratory data analysis on property data
- Build predictive models for real estate price prediction
- Handle data quality issues including city name typos and duplicate records

## Datasets

The project works with the following datasets (to be placed in `01_data_raw/`):

1. **customers.csv** - Customer demographic and contact information
2. **brokers.csv** - Real estate broker details and credentials
3. **properties.csv** - Property listings with features and locations
4. **deals.csv** - Transaction and deal information
5. **transactions.csv** - Financial transaction records
6. **property_features.csv** - Detailed property characteristics

## Project Structure

```
Real-Estate-Price-Prediction/
│
├── 01_data_raw/              # Raw data files (CSV)
│   ├── customers.csv
│   ├── brokers.csv
│   ├── properties.csv
│   ├── deals.csv
│   ├── transactions.csv
│   └── property_features.csv
│
├── 02_data_processed/        # Cleaned and processed data
│
├── 03_notebooks/             # Jupyter notebooks for analysis
│   └── real_estate_analysis.ipynb
│
├── .gitignore                # Python gitignore file
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/deshmukh-sakshi/Real-Estate-Price-Prediction.git
cd Real-Estate-Price-Prediction
```

### 2. Create Virtual Environment (Recommended)

```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# OR using conda
conda create -n realestate python=3.9
conda activate realestate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your Data

Place your CSV files in the `01_data_raw/` folder:
- customers.csv
- brokers.csv
- properties.csv
- deals.csv
- transactions.csv
- property_features.csv

### 5. Run the Analysis

```bash
jupyter notebook 03_notebooks/real_estate_analysis.ipynb
```

## Workflow

### 1. Data Ingestion
- Load all 6 CSV files
- Perform initial data exploration
- Check data types and missing values

### 2. Data Cleaning
- **Fix city name typos**: Standardize city names across datasets
- **Remove duplicates**: Identify and remove duplicate records
- **Handle missing values**: Impute or remove missing data
- **Standardize formats**: Ensure consistent date, currency, and text formats

### 3. Data Integration
- Merge datasets on common keys (customer_id, broker_id, property_id)
- Create a unified dataset for analysis
- Validate data integrity after merging

### 4. Exploratory Data Analysis (EDA)
- Visualize price distributions
- Analyze correlations between features
- Identify outliers and anomalies
- Generate insights about market trends

### 5. Feature Engineering
- Create new features from existing data
- Encode categorical variables
- Scale/normalize numerical features

### 6. Modeling
- Split data into training and testing sets
- Train multiple regression models (Linear Regression, Random Forest, Gradient Boosting, etc.)
- Evaluate model performance (RMSE, MAE, R²)
- Tune hyperparameters
- Select the best model

### 7. Results & Interpretation
- Analyze feature importance
- Make predictions on new data
- Generate business insights

## Key Features

- **Automated Data Cleaning**: Scripts to handle common data quality issues
- **Modular Code**: Well-organized notebooks for easy maintenance
- **Reproducible Results**: All steps documented in Jupyter notebooks
- **Comprehensive EDA**: Detailed visualizations and statistical analysis
- **Multiple Models**: Comparison of different machine learning algorithms

## Technologies Used

- **Python 3.9+**
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib & Seaborn**: Data visualization
- **Scikit-learn**: Machine learning models
- **Jupyter**: Interactive notebooks

## Expected Outputs

- Cleaned datasets in `02_data_processed/`
- Trained models for price prediction
- Visualizations showing key insights
- Model performance metrics
- Feature importance analysis

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

This project is open source and available for educational purposes.

## Contact

For questions or suggestions, please open an issue in the GitHub repository.

## Future Enhancements

- Add deep learning models (Neural Networks)
- Implement time series analysis for price trends
- Create a web dashboard for interactive exploration
- Add automated data validation pipelines
- Integrate external APIs for real-time market data