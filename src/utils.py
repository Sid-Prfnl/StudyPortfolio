import pandas as pd

def validate_dataset(df, name="Dataset"):
    """
    Basic data quality validation for sports analytics datasets
    """

    print(f"\n--- Data Validation Report: {name} ---\n")

    # 1. Shape
    print("1. Dataset Shape")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}\n")

    # 2. Missing values
    print("2. Missing Values")
    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if missing.empty:
        print("No missing values found.\n")
    else:
        print(missing.sort_values(ascending=False))
        print()

    # 3. Duplicates
    print("3. Duplicate Rows")
    dupes = df.duplicated().sum()

    if dupes == 0:
        print("No duplicate rows.\n")
    else:
        print(f"{dupes} duplicate rows found.\n")

    # 4. Data types
    print("4. Column Data Types")
    print(df.dtypes, "\n")

    # 5. Junk columns
    print("5. Suspicious Columns (Unnamed)")
    junk = [c for c in df.columns if "unnamed" in c.lower()]

    if not junk:
        print("No junk columns found.\n")
    else:
        print("Junk columns:", junk, "\n")

    # 6. Basic sanity checks
    print("6. Numerical Sanity Checks")

    numeric = df.select_dtypes(include="number")

    if numeric.empty:
        print("No numeric columns found.\n")
    else:
        print(numeric.describe().T[["min", "max", "mean"]])
        print()

    print("--- Validation Complete ---\n")
