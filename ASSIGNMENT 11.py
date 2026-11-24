import pandas as pd
import numpy as np

# Generate 10 random numbers
numbers = np.random.randint(1, 100, 10)

# Create Pandas Series
ser = pd.Series(numbers)

# Display the Series
print("Pandas Series:")
print(ser)
