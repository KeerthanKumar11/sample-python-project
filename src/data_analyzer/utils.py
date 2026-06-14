"""
Utility functions for DataAnalyzer

This module contains helper functions for data loading and processing.
"""

import pandas as pd
import json
from pathlib import Path
from typing import Union, Dict, Any


def load_data(filepath: Union[str, Path]) -> pd.DataFrame:
    """
    Load data from CSV or JSON file.
    
    Args:
        filepath (str or Path): Path to the data file
        
    Returns:
        pd.DataFrame: Loaded data
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file format is not supported
    """
    filepath = Path(filepath)
    
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    suffix = filepath.suffix.lower()
    
    if suffix == '.csv':
        return pd.read_csv(filepath)
    elif suffix == '.json':
        return pd.read_json(filepath)
    else:
        raise ValueError(f"Unsupported file format: {suffix}")


def save_data(data: pd.DataFrame, filepath: Union[str, Path], format: str = 'csv') -> None:
    """
    Save data to file.
    
    Args:
        data (pd.DataFrame): Data to save
        filepath (str or Path): Output file path
        format (str): File format ('csv' or 'json')
        
    Raises:
        ValueError: If format is not supported
    """
    filepath = Path(filepath)
    
    if format.lower() == 'csv':
        data.to_csv(filepath, index=False)
    elif format.lower() == 'json':
        data.to_json(filepath)
    else:
        raise ValueError(f"Unsupported format: {format}")


def get_column_info(data: pd.DataFrame) -> Dict[str, Any]:
    """
    Get information about columns in the dataset.
    
    Args:
        data (pd.DataFrame): Input dataframe
        
    Returns:
        dict: Information about each column
    """
    info = {}
    for col in data.columns:
        info[col] = {
            'dtype': str(data[col].dtype),
            'non_null_count': data[col].notna().sum(),
            'null_count': data[col].isna().sum(),
            'unique_values': data[col].nunique(),
        }
    return info


def clean_data(data: pd.DataFrame, remove_duplicates: bool = True, 
               handle_missing: str = 'drop') -> pd.DataFrame:
    """
    Clean the dataset.
    
    Args:
        data (pd.DataFrame): Input dataframe
        remove_duplicates (bool): Remove duplicate rows
        handle_missing (str): How to handle missing values ('drop', 'mean', 'median')
        
    Returns:
        pd.DataFrame: Cleaned dataframe
    """
    data = data.copy()
    
    if remove_duplicates:
        data = data.drop_duplicates()
    
    if handle_missing == 'drop':
        data = data.dropna()
    elif handle_missing == 'mean':
        numeric_cols = data.select_dtypes(include=['number']).columns
        data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())
    elif handle_missing == 'median':
        numeric_cols = data.select_dtypes(include=['number']).columns
        data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].median())
    
    return data
