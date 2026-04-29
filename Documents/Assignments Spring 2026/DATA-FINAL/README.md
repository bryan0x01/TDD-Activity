# Wellness Grocery Inventory Analysis

## Overview
This project analyzes grocery products based on their nutritional values using **PCA** and **k-Means clustering**. The goal is to identify patterns in food composition and group similar products into meaningful categories.

---

## Tools Used
- KNIME (main pipeline)
- Python (elbow method support)
- `pandas`, `scikit-learn`, `matplotlib`

---

## Process
1. Data cleaning (handling missing values)
2. Normalization (Standard Scaling)
3. PCA (dimensionality reduction)
4. k-Means clustering (**k = 5**)
5. Visualization (PCA scatter plot)
6. Validation (Silhouette Coefficient)

---

## Key Results
- Optimal number of clusters: **k = 5**
- Clear separation observed in PCA visualization
- Silhouette score ≈ **0.425** (moderate cluster quality)
- Identified clusters:
  - Low-calorie / high-water foods
  - Balanced foods
  - Moderate to high energy foods
  - High-fat / high-calorie foods (outliers)

---

## Files
- `Final Report.pdf` — Full analysis and results
- `workflow.knwf` — KNIME pipeline
- `food.csv` — Dataset
- `elbow_method.py` — Python script for elbow method

---

## How to Run

### KNIME
1. Open the `.knwf` file in KNIME
2. Execute all nodes (run entire workflow)

### Python (Optional)
```bash
python elbow_method.py