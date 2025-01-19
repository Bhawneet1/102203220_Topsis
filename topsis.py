import pandas as pd
import numpy as np
import sys

def main():
    if len(sys.argv) != 5:
        print("Usage: python script.py <input_file> <weights> <impacts> <result_file>")
        print("Example: python script.py data.csv \"1,1,1,1,1\" \"+,+,+,+,+\" results.csv")
        return

    input_filename = sys.argv[1]
    criteria_weights = list(map(float, sys.argv[2].split(',')))
    criteria_impacts = np.array(sys.argv[3].split(','))
    output_filename = sys.argv[4]

    try:
        dataset = pd.read_csv(input_filename)
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
        return

    if len(dataset.columns) < 3:
        print("Error: Input file must have at least three columns (alternatives + criteria).")
        return

    if len(criteria_weights) != len(dataset.columns) - 1 or len(criteria_impacts) != len(dataset.columns) - 1:
        print("Error: Number of weights and impacts must match the number of criteria.")
        return

    try:
        decision_matrix = dataset.iloc[:, 1:]  # Assume first column contains alternatives
        topsis_results = perform_topsis(decision_matrix, criteria_weights, criteria_impacts)
        topsis_results.insert(0, dataset.columns[0], dataset.iloc[:, 0])  # Add alternatives back to result

        topsis_results.to_csv(output_filename, index=False)
        print(f"Results saved to {output_filename}")
    except Exception as error:
        print(f"Error during TOPSIS analysis: {error}")

def perform_topsis(decision_matrix, weights, impacts):

    # Step 1: Normalize the Decision Matrix
    normalized_matrix = decision_matrix / np.sqrt((decision_matrix**2).sum(axis=0))

    # Step 2: Apply Weighting
    weighted_matrix = normalized_matrix * weights

    # Step 3: Identify Ideal and Negative-Ideal Solutions
    ideal_values = np.where(impacts == '+', weighted_matrix.max(axis=0), weighted_matrix.min(axis=0))
    negative_ideal_values = np.where(impacts == '+', weighted_matrix.min(axis=0), weighted_matrix.max(axis=0))

    # Step 4: Calculate Separation Measures
    distance_to_ideal = np.sqrt(((weighted_matrix - ideal_values) ** 2).sum(axis=1))
    distance_to_negative_ideal = np.sqrt(((weighted_matrix - negative_ideal_values) ** 2).sum(axis=1))

    # Step 5: Calculate Relative Closeness to Ideal Solution
    relative_closeness_scores = distance_to_negative_ideal / (distance_to_ideal + distance_to_negative_ideal)

    # Step 6: Rank Alternatives
    rankings = relative_closeness_scores.argsort()[::-1] + 1  # Higher score -> Higher rank

    result_df = decision_matrix.copy()
    result_df['Score'] = relative_closeness_scores
    result_df['Rank'] = rankings
    return result_df

if __name__ == "__main__":
    main()
