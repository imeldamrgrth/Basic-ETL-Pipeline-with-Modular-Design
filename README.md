# Basic ETL Pipeline with Modular Design

##  Overview
This project demonstrates a basic yet modular ETL (Extract, Transform, Load) pipeline in Python, using product data from Fashion Studio Dicoding. It is designed to teach clean, modular coding practices for data processing and provide a foundation for more advanced ETL projects.
Key aspects of the project:
- **Extract**: Collect data from CSV files (scrape from the Fashion Studio website).
- **Transform**: Clean and transform product data, including handling missing values, formatting prices, standardizing size and gender categories, and preparing the data for analysis.
- **Load**: Save the processed data into a clean CSV file for downstream use.
- **Unit Testing**: Ensure that each function in the pipeline works correctly and consistently.
- **Modular Design**: Separate modules for extraction, transformation, and loading for clarity, maintainability, and scalability.

## Dataset
The dataset represents synthetic fashion product data collected from Fashion Studio Dicoding, including product attributes and basic metadata. 
Key features include:
| Feature      | Description                                                                  |
| ------------ | ---------------------------------------------------------------------------- |
| product_name | Name of the product                                                          |
| price        | Price of the product (USD)                                                   |
| rating       | Customer rating (scale 1–5)                                                  |
| colors       | Number of available colors                                                   |
| size         | Available product sizes (S, M, L, XL, XXL)                                   |
| gender       | Target gender of the product (Men, Women, Unisex)                            |
| stock_status | Availability status of the product (In Stock, Out of Stock)                  |
| category     | Product category (e.g., T-shirt, Hoodie, Pants, Jacket, Outerwear, Crewneck) |
| Cluster      | Cluster label assigned by K-Means (optional, can be used for classification) |

**Data source**: [Fashion Studio Dicoding](https://fashion-studio.dicoding.dev)

---

## Technologies Used 
- Python 3.12 
- Libraries:
  - beautifulsoup4 
  - requests
  - pandas 
  - tabulate 
  - pytest

---
