# Task 19 — Top 10 Products by Sales

## Objective
Identify and rank the top 10 products by total sales and visualize the results.

## Tools
- **Excel:** inspect data, sort and rank products, view a bar chart.
- **Python:** pandas for grouping/aggregation/ranking; matplotlib for visualization.

## Dataset
`data/superstore_sample.csv` is a synthetic Superstore-style practice dataset created for this task, not the official Tableau Sample Superstore dataset and not real company sales. It has 1,500 sample orders with Order ID, Order Date, Region, Segment, Category, Product Name, Quantity, Discount, and Sales.

## Deliverables
- `data/superstore_sample.csv` — input dataset.
- `python/top_10_products.py` — Python analysis script.
- `output/Top_10_Products.xlsx` — raw data, ranked top 10 table, embedded bar chart.
- `output/top_10_products.csv` — ranked result.
- `output/top_10_products_chart.png` — bar chart.
- `output/project_summary.txt` — summary statistics.

## Run Python
1. Install Python 3.10+.
2. Open terminal in the extracted project folder.
3. Install dependencies: `python -m pip install pandas matplotlib`
4. Run: `python python/top_10_products.py`

## Excel method
Open `output/Top_10_Products.xlsx`. In Excel, you can reproduce the analysis with a PivotTable: Product Name in Rows, Sales in Values (Sum), sort descending, and apply a Top 10 filter.

## Ranking and ties
Products are sorted by total sales from highest to lowest. For equal totals, product name is sorted alphabetically as a consistent tie-break. If the business requires equal ranks for ties, use a ranking method that assigns the same rank to identical totals.

## Interview questions
**How do you handle ties?** I use a consistent secondary sort such as product name alphabetically, or assign the same rank to products with equal sales if that is the business rule.

**Why use Top 10 analysis?** It quickly highlights products generating the highest sales and can help prioritize inventory and promotions. Sales alone does not measure profitability, so profit should be considered if available.

## Submission checklist
- [ ] Run the Python script and verify the generated table and chart.
- [ ] Open the Excel workbook and check the ranking.
- [ ] Add screenshots if evidence is required.
- [ ] Upload the project to a public GitHub repository.
- [ ] Submit the repository URL in the internship portal.
- [ ] Share the completed project on LinkedIn if required.

**Data note:** Describe this as a synthetic/sample Superstore-style dataset, not official or actual company data.
