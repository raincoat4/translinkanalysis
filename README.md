# Translink Arrival Time Analysis

## How we built it 
The project was a collaborative effort between two team members. We started by developing an algorithm to clean the raw CSV data, addressing issues such as missing values, duplicates, and formatting inconsistencies. This process was critical in ensuring that the data was accurate and compatible with the statistical tools provided by SciPy. Once the data was cleaned, we conducted a series of statistical tests to analyze bus arrival times, focusing on identifying delays and patterns. By applying methods such as t-tests and confidence interval analysis, we determined that the average delay in bus arrivals was approximately 30 seconds. These insights provide a quantitative basis for recommending schedule adjustments.

## Built With
- **Python**: Used for data manipulation and analysis, leveraging its robust libraries for handling large datasets.
- **Pandas**: Facilitated the cleaning and preparation of raw CSV data, ensuring its compatibility with statistical tools.
- **SciPy**: Provided the statistical tools necessary for conducting rigorous tests and deriving insights from the data.
- **CSV Data**: Supplied the raw data on bus arrival times, serving as the foundation for the analysis.

## Try it out
To run the code yourself, cd into the sortedData repository and run 'statsTest.py'.  
  
You can find the report documenting our findings here: https://docs.google.com/document/d/e/2PACX-1vTJ1CqsLitCOCogyi9Ht9H_clBj_q7bt978zVMVaCpiTGDKYYnvsOY06fmQgo1Fy8SKX4gI9H7qdv28/pub 
