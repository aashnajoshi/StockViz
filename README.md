# StockViz
This project analyzes and visualizes stock price data for Microsoft (MSFT) and Salesforce (CRM) over the last year, using data sourced from Yahoo Finance.

## Features
- Fetches stock price data for MSFT and CRM.
- Visualizes stock prices using interactive Plotly graphs.
- Allows for date range selection for viewing historical data.

## Usage
### All required libraries can be installed using a single-line command:
```bash
pip install -r requirements.txt
```

### While to run the code:
#### Console-based version:
```bash
python main.py
```

#### Streamlit-based version:
```bash
streamlit run app.py
```

## Description about various files:
- **app.py:** Contains a streamlit-based version of the main code. 
- **requirements.txt:** File containing all required Python modules.
- **stock_price.py:** Main script for fetching and visualizing stock price data.
