"""
Unit tests for DataAnalyzer
"""

import pytest
import pandas as pd
import numpy as np
import tempfile
from pathlib import Path
from data_analyzer import DataAnalyzer
from data_analyzer.utils import load_data, save_data, clean_data


class TestDataAnalyzer:
    """
    Test cases for DataAnalyzer class
    """
    
    @pytest.fixture
    def sample_data(self):
        """
        Create sample data for testing
        """
        return pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50],
            'C': ['a', 'b', 'c', 'd', 'e']
        })
    
    @pytest.fixture
    def temp_csv(self, sample_data):
        """
        Create a temporary CSV file
        """
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            sample_data.to_csv(f.name, index=False)
            yield f.name
        Path(f.name).unlink()
    
    def test_load_csv(self, temp_csv):
        """
        Test loading CSV file
        """
        analyzer = DataAnalyzer(temp_csv)
        assert analyzer.data is not None
        assert len(analyzer.data) == 5
    
    def test_get_statistics(self, temp_csv):
        """
        Test getting statistics
        """
        analyzer = DataAnalyzer(temp_csv)
        stats = analyzer.get_statistics()
        
        assert 'mean' in stats
        assert 'median' in stats
        assert 'std_dev' in stats
        assert 'min' in stats
        assert 'max' in stats
    
    def test_file_not_found(self):
        """
        Test handling of missing files
        """
        with pytest.raises(FileNotFoundError):
            DataAnalyzer('nonexistent_file.csv')
    
    def test_invalid_file_format(self):
        """
        Test handling of invalid file formats
        """
        with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as f:
            f.write(b'test')
            filepath = f.name
        
        try:
            with pytest.raises(ValueError):
                DataAnalyzer(filepath)
        finally:
            Path(filepath).unlink()
    
    def test_get_summary(self, temp_csv):
        """
        Test getting data summary
        """
        analyzer = DataAnalyzer(temp_csv)
        summary = analyzer.get_summary()
        assert summary is not None
        assert isinstance(summary, pd.DataFrame)


class TestUtilsFunctions:
    """
    Test cases for utility functions
    """
    
    @pytest.fixture
    def sample_data(self):
        """
        Create sample data for testing
        """
        return pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50]
        })
    
    def test_save_and_load_csv(self, sample_data):
        """
        Test saving and loading CSV
        """
        with tempfile.NamedTemporaryFile(suffix='.csv', delete=False) as f:
            filepath = f.name
        
        try:
            save_data(sample_data, filepath, format='csv')
            loaded_data = load_data(filepath)
            
            assert len(loaded_data) == len(sample_data)
            assert list(loaded_data.columns) == list(sample_data.columns)
        finally:
            Path(filepath).unlink()
    
    def test_clean_data_remove_duplicates(self):
        """
        Test removing duplicates
        """
        data = pd.DataFrame({
            'A': [1, 1, 2, 3],
            'B': [1, 1, 2, 3]
        })
        
        cleaned = clean_data(data, remove_duplicates=True, handle_missing='drop')
        assert len(cleaned) == 3
    
    def test_clean_data_handle_missing(self):
        """
        Test handling missing values
        """
        data = pd.DataFrame({
            'A': [1, 2, np.nan, 4],
            'B': [1, np.nan, 3, 4]
        })
        
        cleaned = clean_data(data, remove_duplicates=False, handle_missing='drop')
        assert len(cleaned) == 1


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
