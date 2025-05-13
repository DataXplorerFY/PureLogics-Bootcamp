import argparse
import os
from scripts import summary

def main():
    parser = argparse.ArgumentParser(description='Process CSV data and compute summary statistics.')
    parser.add_argument('--input', type=str, required=True, help='Path to the input CSV file.')
    parser.add_argument('--output', type=str, required=True, help='Path to save the summary statistics.')
    args = parser.parse_args()

    # 1. Load data
    df = summary.load_data(args.input)
    print("[INFO] Data Loaded:")
    print(df.head(5))

    # 2. Clean data - Add this later if needed
    '''
    The data is clean already there is no null values in it. So, we don't need to clean it.
    '''

    # 3. Compute summary
    summary_stats = summary.compute_summary(df)
    print("[INFO] Summary Computed:")
    print(summary_stats)

    # 4. Save output
    summary.save_summary(summary_stats, args.output)
    print(f"[INFO] Summary statistics saved to: {args.output}")

if __name__ == '__main__':
    main()
