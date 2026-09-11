import pandas as pd


def prepare_data(data):
    """
    Prepare patient data for the machine learning model.
    """

    data = data.copy()

    # Remove unnecessary ID column if it exists
    if "id" in data.columns:
        data = data.drop(columns=["id"])

    # Convert common yes/no fields into numbers
    yes_no_columns = [
        "hypertension",
        "heart_disease"
    ]

    for column in yes_no_columns:
        if column in data.columns:
            data[column] = data[column].map({
                "Yes": 1,
                "No": 0,
                "yes": 1,
                "no": 0
            })

    return data
