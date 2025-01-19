# TOPSIS Implementation

This project implements the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) for decision-making problems.

## Prerequisites

Ensure you have Python installed on your system along with the required libraries. Install dependencies using:

```bash
pip install pandas numpy
```

## Input File

The input file should be a CSV file with the following structure:

1. **First column**: Name or identifier for each alternative (e.g., "Fund Name").
2. **Subsequent columns**: Criteria values (e.g., "P1", "P2", "P3", etc.).

### Example Input File

| Fund Name | P1   | P2   | P3  | P4   | P5    |
|-----------|-------|-------|------|-------|-------|
| M1        | 0.7   | 0.49  | 4.3  | 45.9  | 12.85 |
| M2        | 0.62  | 0.38  | 6.3  | 32.8  | 10.03 |
| M3        | 0.8   | 0.64  | 6.0  | 36.7  | 11.04 |
| M4        | 0.73  | 0.53  | 5.2  | 54.5  | 15.24 |
| M5        | 0.94  | 0.88  | 4.4  | 35.9  | 10.53 |

### Constraints

- The file must have at least three columns (one for alternatives and at least two for criteria).
- Ensure criteria values are numeric.

## Usage

Run the script using the following syntax:

```bash
python script.py <input_file> <weights> <impacts> <result_file>
```

### Arguments

1. **`<input_file>`**: Path to the input CSV file.
2. **`<weights>`**: Comma-separated list of criteria weights (e.g., "1,1,1,1,1").
3. **`<impacts>`**: Comma-separated list of impacts for each criterion (`+` for benefit, `-` for cost) (e.g., "+,+,-,+,-").
4. **`<result_file>`**: Path to save the output CSV file.

### Example

```bash
python script.py data.csv "1,2,1,3,2" "+,+,-,+,-" results.csv
```

## Output

The output file will contain the following columns:

1. **Original columns**: All columns from the input file.
2. **`Score`**: Relative closeness to the ideal solution.
3. **`Rank`**: Rank of each alternative based on the score.

### Example Output File

| Fund Name | P1   | P2   | P3  | P4   | P5    | Score   | Rank |
|-----------|-------|-------|------|-------|-------|---------|------|
| M5        | 0.94  | 0.88  | 4.4  | 35.9  | 10.53 | 0.7854  | 1    |
| M1        | 0.7   | 0.49  | 4.3  | 45.9  | 12.85 | 0.6521  | 2    |
| M3        | 0.8   | 0.64  | 6.0  | 36.7  | 11.04 | 0.6345  | 3    |
| M4        | 0.73  | 0.53  | 5.2  | 54.5  | 15.24 | 0.5123  | 4    |
| M2        | 0.62  | 0.38  | 6.3  | 32.8  | 10.03 | 0.4789  | 5    |

## Notes

- Ensure that the weights and impacts match the number of criteria columns in the input file.
- For incorrect input formats or mismatched weights/impacts, the program will raise an error.

## License

This project is released under the MIT License.
