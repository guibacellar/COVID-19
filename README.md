# COVID-19
COVID-19 Data Analysis

> **This project uses Python 3.7**

## Data Explanation
Location: */data*

* all_timeline.json > Raw Data Downloaded from https://thevirustracker.com/timeline/map-data.json

* all_timeline.csv > Just the *all_timeline.json* file sanitized and in *csv* format.

* all_timeline_with_features.csv > *all_timeline.csv* file processed with some features that I consider helpful

## Files Explanation

* cv19_constants.py > Just constants for code organization

* cv19_downloader.py > Responsible to download the Raw Timeline Data from https://thevirustracker.com

* cv19_parser.py > *all_timeline.json* to *all_timeline.csv* converter and sanitizer

* main.py > Application Entrypoint

## Jypiter Notebooks
* exploration.ipynb > One Country Only Data Exploration, Insights and Graph Generation

* exploration_compare_countries.ipynb > Many Countries Data Exploration, Insights and Graph Generation

* feature_generation.ipynb > Feature Generation for *all_timeline.csv* file

* logistic_regression.ipynb > WIP: Predictions using Logistic Regression
