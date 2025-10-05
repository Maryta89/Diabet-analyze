# 🩺 Diabetes Dataset Cleaning & Visualization (Individual Plots)

This project performs **data cleaning** and **visual analysis** on a diabetes dataset using Python.  
It generates six **separate charts** for easier inspection and saves them individually as `.png` files.

---

## 📊 Features

The script does the following:

1. **Load the Dataset**  
   Reads a CSV file (`diabetes_dataset.csv`) using `pandas`.

2. **Clean the Data**  
   - Removes missing values and duplicates  
   - Trims extra spaces from column names  
   - Removes outliers using the IQR method  

3. **Visualize the Data**  
   Generates and saves 6 different plots individually:

   | Plot | Description | Output File |
   |------|--------------|-------------|
   | 1️⃣ Distribution Plot | Shows distribution of a numerical feature | `1_distribution.png` |
   | 2️⃣ Boxplot | Displays outliers and spread of data | `2_boxplot.png` |
   | 3️⃣ Correlation Heatmap | Shows correlations between numerical variables | `3_heatmap.png` |
   | 4️⃣ Barplot | Visualizes categorical feature counts | `4_barplot.png` |
   | 5️⃣ Scatter Plot | Shows relationship between two numerical variables | `5_scatterplot.png` |
   | 6️⃣ Pairplot | Displays pairwise relationships across numerical features | `6_pairplot.png` |

---

## 🧰 Requirements

Install the required Python libraries before running the script:

```bash
pip install pandas matplotlib seaborn
