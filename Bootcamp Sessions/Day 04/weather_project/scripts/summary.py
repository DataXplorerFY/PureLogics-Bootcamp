import pandas as pd


def load_data(file_path):
    """
    Load data from a CSV file.    
    Parameters:
    file_path (str): Path of my CSV file.
    
    Returns:
    df: Loaded data as a DataFrame.
    """

    df = pd.read_csv(file_path)
    return df




def compute_summary(df):
    """
    Compute summary statistics (mean, min, max) for each numeric column in the DataFrame.

    Parameters:
    df (DataFrame): The input data.

    Returns:
    dict: A dictionary with columns as keys and their corresponding mean, min, and max as values.
    """
    summary = {}
    numeric_cols = df.select_dtypes(include='number')
    for column in numeric_cols.columns:
        summary[column] = {
            'mean': numeric_cols[column].mean(),
            'min': numeric_cols[column].min(),
            'max': numeric_cols[column].max()
        }
    return summary


def save_summary(summary, output_path):
    """
    Save the summary statistics dictionary to a result.txt file.

    """
    with open(output_path, 'w') as f:
        for column, stats in summary.items():
            f.write(f"{column}:\n")
            for stat_name, value in stats.items():
                f.write(f"  {stat_name}: {value}\n")
            f.write("\n")
