import pandas as pd

# Reading Flipkart Sales Report
input_file = "b106e77d-500c-4954-aa98-2cc9086526fc_1754557563000.xlsx"
df = pd.read_excel(input_file, sheet_name="Sales Report")

# DataFrameing for Tally Format
sales_report = pd.DataFrame()

# ---- Mapping ----
sales_report["Voucher No"] = df["Buyer Invoice ID"]
sales_report["Voucher Date"] = df["Buyer Invoice Date"]
sales_report["Customer Name"] = "Sale through Flipkart"
sales_report["Group"] = "Sundry Debtors"
sales_report["Address"] = df["Customer's Billing State"]
sales_report["State"] = df["Customer's Delivery State"]
sales_report["GST Type"] = "Unregistered"
sales_report["GST Number"] = ""
sales_report["Sales Ledger Name"] = "Sales through Ecommerce"
sales_report["Item Name"] = df["Product Title/Description"]
sales_report["Batch No."] = ""
sales_report["Expiry"] = ""
sales_report["HSN Code"] = df["HSN Code"]
sales_report["Quantity"] = df["Item Quantity"]

# Calculating Rate = Amount ÷ Quantity
sales_report["Rate"] = df["Final Invoice Amount (Price after discount+Shipping Charges)"] / df["Item Quantity"]

# Amount
sales_report["Amount"] = df["Final Invoice Amount (Price after discount+Shipping Charges)"]

# Taxes (from Flipkart tax columns)
# !fillna(0): Replace NaN with 0 to avoid errors OKAY
sales_report["Taxes"] = (
    df["CGST Amount"].fillna(0) +
    df["SGST Amount (Or UTGST as applicable)"].fillna(0) +
    df["IGST Amount"].fillna(0)
)

# CGST
sales_report["CGST Ledger Name"] = "Output CGST"
sales_report["CGST Amount"] = df["CGST Amount"].fillna(0)

# SGST
sales_report["SGST Ledger Name"] = "Output SGST"
sales_report["SGST Amount"] = df["SGST Amount (Or UTGST as applicable)"].fillna(0)

# IGST
sales_report["IGST Ledger Name"] = "Output IGST"
sales_report["IGST Amount"] = df["IGST Amount"].fillna(0)

# Total Amount
sales_report["Total Amount"] = df["Buyer Invoice Amount"]

# Other Charges (Blank)
sales_report["Other Charges Ledger"] = ""
sales_report["Other Charges Amount"] = ""



# 3. Save to new Excel
output_file = "Tally_Sales_Voucher_Converted.2.0.xlsx"
sales_report.to_excel(output_file, index=False)

print(f"Completed! \n File saved as: {output_file}")
