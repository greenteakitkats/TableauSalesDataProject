from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load your data
data = pd.read_csv('data/TableauSalesData.csv')

# Parse the Order Date to ensure 'Order Year' is extracted
data["Order Date"] = pd.to_datetime(data["Order Date"], format="%m/%d/%y", errors="coerce")
data["Order Year"] = data["Order Date"].dt.year

@app.route("/", methods=["GET", "POST"])
def index():
    # Initialize filter variables
    selected_category = ""
    selected_subcategory = ""
    selected_region = ""
    selected_segment = ""
    query = ""

    # Start with the full dataset
    filtered_data = data.copy()

    if request.method == "POST":
        # Capture filter inputs
        selected_category = request.form.get("category")
        selected_subcategory = request.form.get("subcategory")
        selected_region = request.form.get("region")
        selected_segment = request.form.get("segment")
        query = request.form.get("query")

        # Apply filters
        if selected_category:
            filtered_data = filtered_data[filtered_data["Category"] == selected_category]
        if selected_subcategory:
            filtered_data = filtered_data[filtered_data["Sub-Category"] == selected_subcategory]
        if selected_region:
            filtered_data = filtered_data[filtered_data["Region"] == selected_region]
        if selected_segment:
            filtered_data = filtered_data[filtered_data["Segment"] == selected_segment]

    # Initialize results and feedback
    result_columns = []
    result_data = []
    feedback_message = ""

    # Query logic
    if query == "total_sales_profit":
        result = filtered_data.groupby("Region")[["Sales", "Profit"]].sum().reset_index()
        result_columns = result.columns.tolist()
        result_data = result.values.tolist()
    elif query == "avg_discount":
        result = filtered_data.groupby("Product Name")[["Discount"]].mean().reset_index()
        result_columns = result.columns.tolist()
        result_data = result.values.tolist()
    elif query == "sales_by_year":
        if "Order Year" in filtered_data.columns:
            result = filtered_data.groupby("Order Year")[["Sales"]].sum().reset_index()
            result_columns = result.columns.tolist()
            result_data = result.values.tolist()
        else:
            feedback_message = "The 'Order Year' column could not be generated from the Order Date."
    elif query == "profit_by_region":
        result = filtered_data.groupby("Region")[["Profit"]].sum().reset_index()
        result_columns = result.columns.tolist()
        result_data = result.values.tolist()
    elif query == "negative_profit":
        result = filtered_data[filtered_data["Profit"] < 0][["Product Name", "Profit"]]
        result_columns = result.columns.tolist()
        result_data = result.values.tolist()
    else:
        feedback_message = "Please select filters and a query to see results."

    # Handle empty results
    if not result_data and not feedback_message:
        feedback_message = "No results found for the selected filters."

    # Populate dropdown options
    categories = sorted(data["Category"].unique())
    subcategories = sorted(data["Sub-Category"].unique())
    regions = sorted(data["Region"].unique())
    segments = sorted(data["Segment"].unique())

    return render_template(
        "index.html",
        categories=categories,
        subcategories=subcategories,
        regions=regions,
        segments=segments,
        result_columns=result_columns,
        result_data=result_data,
        selected_category=selected_category,
        selected_subcategory=selected_subcategory,
        selected_region=selected_region,
        selected_segment=selected_segment,
        query=query,
        feedback_message=feedback_message,
    )


if __name__ == "__main__":
    app.run(debug=True)