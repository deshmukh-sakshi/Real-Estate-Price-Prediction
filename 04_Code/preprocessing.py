import pandas as pd
import numpy as np

# -------------------------------
# Load the CSVs
# -------------------------------
brokers = pd.read_csv("01_data_raw/Brokers.csv")
customers = pd.read_csv("01_data_raw/Customers.csv")
deals = pd.read_csv("01_data_raw/Deals.csv")
properties = pd.read_csv("01_data_raw/Properties.csv")
property_features = pd.read_csv("01_data_raw/PropertyDetails.csv")

# -------------------------------
# Standardize City Names Function
# -------------------------------
def clean_city(city):
    if pd.isna(city):
        return np.nan
    city = city.strip().title()
    corrections = {
    "Nodia": "Noida", "Dehli": "Delhi", "Mumbaai": "Mumbai", "Mumbay": "Mumbai", "Punna": "Pune", "Jaypur": "Jaipur", "Hydrabad": "Hyderabad", "Hyderbad": "Hyderabad", "Bengluru": "Bangalore", "Ahemdabad": "Ahmedabad", "Kalkata": "Kolkata", "Calcutta": "Kolkata", "Surrat": "Surat", "Gurugrm": "Gurugram", "Gurgaon": "Gurugram", "Poona": "Pune", "Chennnai": "Chennai"
    }
    return corrections.get(city, city)

# Clean city names in all relevant tables
for df, col in [(brokers, 'city'), (customers, 'city'), (properties, 'city')]:
    df[col] = df[col].apply(clean_city)

# -------------------------------
# Handle Missing Values
# -------------------------------
# Replace missing strings or spaces with NaN
for df in [brokers, customers, deals, properties, property_features]:
    df.replace(["", " ", "na", "NA", "N/A"], np.nan, inplace=True)

# Fill missing categorical with mode, numerical with median
def fill_missing(df):
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else "Unknown", inplace=True)
        else:
            df[col].fillna(df[col].median(), inplace=True)
    return df

brokers = fill_missing(brokers)
customers = fill_missing(customers)
deals = fill_missing(deals)
properties = fill_missing(properties)
property_features = fill_missing(property_features)

# -------------------------------
# Data Type Conversion
# -------------------------------
# Convert date columns to datetime
for col in ['deal_date', 'close_date']:
    if col in deals.columns:
        deals[col] = pd.to_datetime(deals[col], errors='coerce')

# Convert numeric columns to correct types
numeric_cols = ['experience_years', 'rating', 'annual_income',
                'offer_price', 'final_price', 'loan_rate', 'area_sqft', 'year_built']
for col in numeric_cols:
    if col in brokers.columns: brokers[col] = pd.to_numeric(brokers[col], errors='coerce')
    if col in customers.columns: customers[col] = pd.to_numeric(customers[col], errors='coerce')
    if col in deals.columns: deals[col] = pd.to_numeric(deals[col], errors='coerce')
    if col in properties.columns: properties[col] = pd.to_numeric(properties[col], errors='coerce')

# -------------------------------
# Fix Duplicates
# -------------------------------
brokers.drop_duplicates(inplace=True)
customers.drop_duplicates(inplace=True)
deals.drop_duplicates(inplace=True)
properties.drop_duplicates(inplace=True)
property_features.drop_duplicates(inplace=True)

# -------------------------------
# Merge All Tables into One Master Dataset
# -------------------------------
merged_df = (
    deals
    .merge(customers, on='customer_id', how='left', suffixes=('', '_customer'))
    .merge(brokers, on='broker_id', how='left', suffixes=('', '_broker'))
    .merge(properties, on='property_id', how='left', suffixes=('', '_property'))
    .merge(property_features, on='property_id', how='left')
)

# -------------------------------
# Quick Sanity Checks
# -------------------------------
print("✅ Shape after merging:", merged_df.shape)
print("\n✅ Columns:\n", merged_df.columns.tolist())
print("\n✅ Missing values:\n", merged_df.isnull().sum().sort_values(ascending=False).head(10))
print("\n✅ Sample cleaned data:\n", merged_df.head(5))

merged_df.to_csv("merged_cleaned_data.csv", index=False)
print("💾 Merged cleaned data saved as 'merged_cleaned_data.csv'")

