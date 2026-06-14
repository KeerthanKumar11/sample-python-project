"""
Core analyzer module for DataAnalyzer

This module contains the main DataAnalyzer class for data analysis and visualization.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from typing import Dict, List, Optional, Union


class DataAnalyzer:
    """
    A comprehensive data analysis tool for CSV and JSON files.
    
    This class provides methods for loading, analyzing, and visualizing data.
    
    Attributes:
        filepath (str): Path to the data file
        data (pd.DataFrame): The loaded dataframe
    """
    
    def __init__(self, filepath: Union[str, Path]):
        """
        Initialize the DataAnalyzer.
        
        Args:
            filepath (str or Path): Path to the CSV or JSON file
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            ValueError: If the file format is not supported
        """
        self.filepath = Path(filepath)
        self.data = None
        self._load_data()
    
    def _load_data(self) -> None:
        """
        Load data from CSV or JSON file.
        
        Raises:
            FileNotFoundError: If the file doesn't exist
            ValueError: If the file format is not supported
        """
        if not self.filepath.exists():
            raise FileNotFoundError(f"File not found: {self.filepath}")
        
        suffix = self.filepath.suffix.lower()
        
        try:
            if suffix == '.csv':
                self.data = pd.read_csv(self.filepath)
            elif suffix == '.json':
                self.data = pd.read_json(self.filepath)
            else:
                raise ValueError(f"Unsupported file format: {suffix}")
        except Exception as e:
            raise ValueError(f"Error loading file: {str(e)}")
    
    def get_statistics(self, columns: Optional[List[str]] = None) -> Dict:
        """
        Get statistical summary of the data.
        
        Args:
            columns (list, optional): Specific columns to analyze. If None, analyzes all numeric columns.
            
        Returns:
            dict: Dictionary containing statistical measures
        """
        if self.data is None:
            return {}
        
        numeric_data = self.data.select_dtypes(include=[np.number])
        
        if columns:
            numeric_data = numeric_data[columns]
        
        stats = {
            'mean': numeric_data.mean().to_dict(),
            'median': numeric_data.median().to_dict(),
            'std_dev': numeric_data.std().to_dict(),
            'min': numeric_data.min().to_dict(),
            'max': numeric_data.max().to_dict(),
            'count': numeric_data.count().to_dict(),
        }
        
        return stats
    
    def get_summary(self) -> pd.DataFrame:
        """
        Get a summary of the data.
        
        Returns:
            pd.DataFrame: Summary statistics
        """
        return self.data.describe()
    
    def plot_distribution(self, column: str, bins: int = 30) -> None:
        """
        Plot the distribution of a column.
        
        Args:
            column (str): Column name to plot
            bins (int): Number of bins for histogram
        """
        if column not in self.data.columns:
            raise ValueError(f"Column '{column}' not found")
        
        plt.figure(figsize=(10, 6))
        plt.hist(self.data[column], bins=bins, edgecolor='black', alpha=0.7)
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.title(f'Distribution of {column}')
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        plt.show()
    
    def plot_scatter(self, x_column: str, y_column: str) -> None:
        """
        Create a scatter plot of two columns.
        
        Args:
            x_column (str): Column for x-axis
            y_column (str): Column for y-axis
        """
        if x_column not in self.data.columns or y_column not in self.data.columns:
            raise ValueError("One or more columns not found")
        
        plt.figure(figsize=(10, 6))
        plt.scatter(self.data[x_column], self.data[y_column], alpha=0.6)
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title(f'Scatter: {x_column} vs {y_column}')
        plt.grid(alpha=0.3)
        plt.tight_layout()
        plt.show()
    
    def plot_correlation_matrix(self) -> None:
        """
        Plot correlation matrix heatmap.
        """
        numeric_data = self.data.select_dtypes(include=[np.number])
        
        if numeric_data.empty:
            print("No numeric columns found")
            return
        
        plt.figure(figsize=(12, 8))
        correlation_matrix = numeric_data.corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
        plt.title('Correlation Matrix')
        plt.tight_layout()
        plt.show()
    
    def export_to_json(self, output_path: Union[str, Path]) -> None:
        """
        Export statistics to JSON file.
        
        Args:
            output_path (str or Path): Path for output JSON file
        """
        import json
        
        stats = self.get_statistics()
        # Convert to serializable format
        serializable_stats = {}
        for key, value in stats.items():
            serializable_stats[key] = {k: float(v) if pd.notna(v) else None 
                                       for k, v in value.items()}
        
        with open(output_path, 'w') as f:
            json.dump(serializable_stats, f, indent=4)
    
    def get_data_info(self) -> str:
        """
        Get information about the dataset.
        
        Returns:
            str: Information about the dataset
        """
        info = f"""
        Dataset Information:
        - Shape: {self.data.shape}
        - Columns: {', '.join(self.data.columns)}
        - Data Types:\n"""
        
        for col, dtype in self.data.dtypes.items():
            info += f"    {col}: {dtype}\n"
        
        return info
