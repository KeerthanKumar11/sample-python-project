"""
Example usage of DataAnalyzer

This module demonstrates how to use the DataAnalyzer class.
"""

import pandas as pd
from data_analyzer import DataAnalyzer
from data_analyzer.utils import clean_data, get_column_info


def example_1_basic_analysis():
    """
    Example 1: Basic data analysis
    """
    print("\n" + "="*50)
    print("Example 1: Basic Data Analysis")
    print("="*50)
    
    # Create sample data
    data = pd.DataFrame({
        'Age': [25, 30, 35, 40, 45, 50],
        'Salary': [50000, 60000, 75000, 80000, 95000, 100000],
        'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT']
    })
    
    # Save to CSV
    data.to_csv('sample_data.csv', index=False)
    
    # Load and analyze
    analyzer = DataAnalyzer('sample_data.csv')
    
    # Get statistics
    stats = analyzer.get_statistics()
    print("\nStatistics:")
    for stat_type, values in stats.items():
        print(f"  {stat_type}: {values}")
    
    # Get summary
    print("\nSummary:")
    print(analyzer.get_summary())
    
    # Get data info
    print(analyzer.get_data_info())


def example_2_data_cleaning():
    """
    Example 2: Data cleaning
    """
    print("\n" + "="*50)
    print("Example 2: Data Cleaning")
    print("="*50)
    
    # Create data with missing values
    import numpy as np
    data = pd.DataFrame({
        'A': [1, 2, np.nan, 4, 5],
        'B': [10, np.nan, 30, 40, 50],
        'C': [1, 1, 2, 2, 3]  # Has duplicates
    })
    
    print("\nOriginal data:")
    print(data)
    
    # Clean data
    cleaned = clean_data(data, remove_duplicates=True, handle_missing='mean')
    print("\nCleaned data:")
    print(cleaned)


def example_3_column_info():
    """
    Example 3: Get column information
    """
    print("\n" + "="*50)
    print("Example 3: Column Information")
    print("="*50)
    
    # Create sample data
    data = pd.DataFrame({
        'ID': [1, 2, 3, 4, 5],
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Score': [85, 90, None, 88, 92]
    })
    
    info = get_column_info(data)
    print("\nColumn Information:")
    for col, details in info.items():
        print(f"\n  {col}:")
        for key, value in details.items():
            print(f"    {key}: {value}")


def example_4_statistical_summary():
    """
    Example 4: Get statistical summary
    """
    print("\n" + "="*50)
    print("Example 4: Statistical Summary")
    print("="*50)
    
    # Create sample data
    import numpy as np
    np.random.seed(42)
    data = pd.DataFrame({
        'Sales': np.random.randint(1000, 10000, 100),
        'Profit': np.random.randint(100, 1000, 100),
        'Month': np.tile(range(1, 13), 9)[:100]
    })
    
    # Save and analyze
    data.to_csv('sales_data.csv', index=False)
    analyzer = DataAnalyzer('sales_data.csv')
    
    print("\nData Summary:")
    print(analyzer.get_summary())
    
    print("\nDetailed Statistics:")
    stats = analyzer.get_statistics(['Sales', 'Profit'])
    for stat_type, values in stats.items():
        print(f"\n  {stat_type}:")
        for col, val in values.items():
            print(f"    {col}: {val:.2f}")


if __name__ == '__main__':
    print("\nDataAnalyzer - Usage Examples")
    print("="*50)
    
    try:
        example_1_basic_analysis()
    except Exception as e:
        print(f"Example 1 error: {e}")
    
    try:
        example_2_data_cleaning()
    except Exception as e:
        print(f"Example 2 error: {e}")
    
    try:
        example_3_column_info()
    except Exception as e:
        print(f"Example 3 error: {e}")
    
    try:
        example_4_statistical_summary()
    except Exception as e:
        print(f"Example 4 error: {e}")
    
    print("\n" + "="*50)
    print("Examples completed!")
    print("="*50 + "\n")
