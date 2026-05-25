# Auto-MPG Data Exploratory Analysis

A comprehensive statistical analysis of the Auto MPG dataset containing 398 vehicles manufactured between 1970 and 1982.

## Overview

This report analyzes the Auto MPG dataset, a transformative period marked by significant shifts in automotive design driven by oil crises and fuel economy regulations. The analysis reveals that **engine displacement** and **vehicle weight** are the primary mechanical drivers of fuel consumption, with both showing strong negative correlations with fuel efficiency.

## Key Findings

- Larger engines and heavier vehicles consistently produce lower MPG
- Clear regional manufacturing philosophies identified:
  - **American manufacturers**: focused on larger, heavier vehicles with powerful engines
  - **Japanese & European manufacturers**: prioritized compact, lightweight designs achieving superior fuel economy

## Authors

- Ali Ahmadi
- Ramez Chreide
- Jawad Ahmed
- Md Foyzullah

## Files

| File | Description |
|------|-------------|
| `Group_P_RMarkDown.Rmd` | Complete R Markdown source with full analysis, visualizations, and statistical tests |

## How to Run

1. Open `Group_P_RMarkDown.Rmd` in RStudio
2. Install required packages:
   ```r
   install.packages(c("ggplot2", "dplyr", "knitr"))
   ```
3. Ensure `auto-mpg.csv` is in the same directory
4. Click "Knit" to generate the report

## Data

The dataset (`auto-mpg.csv`) includes vehicle specifications:
- Miles per gallon (MPG)
- Number of cylinders
- Engine displacement
- Horsepower
- Vehicle weight
- Acceleration
- Model year (70-82)
- Manufacturing origin (USA, Europe, Japan)