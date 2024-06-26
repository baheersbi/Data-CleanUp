import pandas as pd
from data_cleanup import clean_data

def test_clean_data():
    # Create a sample DataFrame
    data = {
        'A': [1, 2, None, 4, 5, 5],
        'B': [5, 6, 7, 8, None, 8]
    }
    df = pd.DataFrame(data)

    # Expected result
    expected_data = {
        'a': [1, 2, 4, 5],
        'b': [5, 6, 8, 8]
    }
    expected_df = pd.DataFrame(expected_data)

    # Clean the data
    cleaned_df = clean_data(df)

    # Check if the cleaned DataFrame matches the expected DataFrame
    pd.testing.assert_frame_equal(cleaned_df, expected_df)

if __name__ == "__main__":
    test_clean_data()
    print("All tests passed!")
