import pandas as pd

def get_data():
    """Load student data dynamically from Excel file"""
    excel_path = "assets/DSA LeaderBoard spreadsheet.xlsx"
    df = pd.read_excel(excel_path)

    # Strip spaces just in case
    df.rename(columns=lambda c: c.strip(), inplace=True)

    # Correct mapping for your file
    df.rename(columns={
        "Name": "Student",
        "Batch": "Batch",
        "Total Solved": "Total solved",
        "Weekely": "Solved this week"
    }, inplace=True)

    # Convert DataFrame to dictionary
    data = {
        "Student": df["Student"].tolist(),
        "Batch": df["Batch"].tolist(),
        "Total solved": df["Total solved"].tolist(),
        "Solved this week": df["Solved this week"].tolist(),
    }
    return data
