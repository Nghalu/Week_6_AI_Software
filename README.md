# TCGA COAD Dataset Analysis Script
## Overview
This project provides a Python script for loading, cleaning, and performing exploratory data analysis (EDA) on the TCGA_COAD.dataset.csv file. The dataset is part of the TCGA Colon Adenocarcinoma (COAD) project and contains biological and gene-related variables.
Because TCGA files often come in different delimiter formats, the script includes robust logic to automatically detect and correctly parse the dataset before analysis.
## Features
- Automatic File Parsing
Attempts to read the data using:
- comma (,)
- tab (\t)
automatic separator inference
Detects cases where a CSV file actually contains tab-separated content.
Re-reads the file when needed to ensure accurate parsing.
## Data Cleaning
Removes rows with any missing values.
Displays dataset structure before and after cleaning.
## Exploratory Data Analysis (EDA)
Prints:
- First 5 rows
- Data types
- Summary statistics
- Automatically selects a numeric column for visualization:
## Visualization
Creates a histogram (with KDE) using Seaborn to display data distribution.
Helps in understanding gene expression or other numeric column patterns.
