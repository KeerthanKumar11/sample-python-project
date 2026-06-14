"""
DataAnalyzer - A comprehensive data analysis and visualization tool

This package provides tools for loading, analyzing, and visualizing data
from various formats including CSV and JSON files.

Main Classes:
    - DataAnalyzer: Main class for data analysis and visualization

Usage:
    >>> from data_analyzer import DataAnalyzer
    >>> analyzer = DataAnalyzer('data.csv')
    >>> stats = analyzer.get_statistics()
"""

__version__ = "1.0.0"
__author__ = "Keerthan Kumar"
__email__ = "keerthan@example.com"

from .analyzer import DataAnalyzer
from .utils import load_data, save_data

__all__ = ['DataAnalyzer', 'load_data', 'save_data']
