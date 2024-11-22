# Tableau Sales Data Analysis Project - Fall 2024

**Authors:** Christine Santos, Oliva Rivera Garcia, Ryan Do  
**Course:** BUS4-110A - Fundamentals of Management Information Systems  
**Professor:** Yasin Ceran

---

## Project Description

This project is a Flask-based web application for analyzing and visualizing sales data. It was built as part of the BUS4-110A course to apply fundamental management information systems concepts and demonstrate practical skills in web development and data visualization.

### Motivation and Purpose
- To create a user-friendly platform for exploring sales trends, discounts, and profits in a structured and interactive way.
- To practice dynamic filtering, predefined queries, and responsive UI/UX design in a real-world scenario.

### Features
1. Dynamic Filters:
   - Filter results by **Category**, **Sub-Category**, **Region**, and **Segment**.
2. Predefined Queries:
   - Total Sales and Profit
   - Average Discount by Product
   - Total Sales by Year
   - Profit by Region
   - Products with Negative Profit
3. Light/Dark Mode Toggle:
   - Saves user preferences across sessions using localStorage.
4. Persistent Filters:
   - Retains user-selected filters after running queries for seamless exploration.
5. Reset Filters Button:
   - Clears all filters and resets the interface.
6. Improved Error Handling:
   - Provides meaningful feedback for invalid inputs or empty results.

---

## Table of Contents
1. [How to Install and Run the Project](#how-to-install-and-run-the-project)
2. [How to Use the Project](#how-to-use-the-project)
3. [Credits](#credits)

---

## How to Install and Run the Project

### Step 1: Extract Files
Download and extract the project files into a folder. The folder structure should look like this:

### File Structure
```
.
├── app.py                    # Backend logic and Flask server
├── static/
│   └── style.css             # Styling for the application
├── templates/
│   └── index.html            # Frontend HTML file
├── data/
│   └── TableauSalesData.csv  # Dataset for analysis
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

### Step 2: Install Python
Ensure Python 3.7 or higher is installed. Download it from [python.org](https://www.python.org/).

### Step 3: Install Dependencies
1. Open a terminal or command prompt.
2. Navigate to the project folder:
```bash
cd path-to-extracted-folder
```
3. Use pip to install the required dependencies listed in the requirements.txt file:
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
Start the Flask server:
```bash
python app.py
```

### Step 5: Access the Web App
Open your browser and go to:
```
http://127.0.0.1:5000/
```

---

## How to Use the Project

## Queries and Filters
### Filters
Users can apply the following filters to refine their data:
- **Category**
- **Sub-Category**
- **Region**
- **Segment**

### Queries
1. **Total Sales and Profit:**  
   Summarizes sales and profit grouped by region.
2. **Average Discount by Product:**  
   Displays the average discount applied to each product.
3. **Total Sales by Year:**  
   Groups sales data by year based on order dates.
4. **Profit by Region:**  
   Summarizes profit grouped by region.
5. **Products with Negative Profit:**  
   Lists products with negative profit margins.

---

## Enhancements and Improvements
This project includes several enhancements and improvements beyond the minimum requirements:

1. **Reset Filters Button:**  
   - Added for user convenience, allowing users to clear all filters with a single click.

2. **Light/Dark Mode Toggle:**  
   - Includes a toggle for switching between themes, with preferences saved across sessions.

3. **Improved Date Parsing:**  
   - Ensures consistent and reliable parsing of `Order Date` with explicit format handling.

4. **Alignment and Layout Improvements:**  
   - Buttons and dropdowns are perfectly aligned for a clean, professional look.
   - Results are displayed in a responsive, scrollable table that adapts to different screen sizes.

5. **Enhanced Feedback System:**  
   - Displays clear and user-friendly messages when no results are found or if filters are reset.

6. **Modern UI/UX Design:**  
   - Added alternating row colors in the results table for better readability.
   - Adjusted padding, font sizes, and button styles for consistency and accessibility.

---

## Credits

- **Christine Santos**
- **Oliva Rivera Garcia**
- **Ryan Do**