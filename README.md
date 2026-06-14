# DataAnalyzer

A comprehensive Python project for data analysis and visualization.

## Features

- **Data Processing**: Read and process CSV and JSON files
- **Statistical Analysis**: Calculate mean, median, standard deviation, and more
- **Data Visualization**: Generate beautiful charts and graphs
- **Easy to Use**: Simple and intuitive API
- **Well Tested**: Comprehensive unit tests included
- **Professional Structure**: Follows Python best practices

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/KeerthanKumar11/sample-python-project.git
cd sample-python-project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install the package:
```bash
pip install -e .
```

## Usage

### Quick Start

```python
from data_analyzer import DataAnalyzer

# Create an analyzer instance
analyzer = DataAnalyzer('data.csv')

# Get statistics
stats = analyzer.get_statistics()
print(f"Mean: {stats['mean']}")
print(f"Median: {stats['median']}")
print(f"Std Dev: {stats['std_dev']}")

# Generate visualizations
analyzer.plot_distribution('column_name')
analyzer.plot_correlation_matrix()
```

### Advanced Usage

See `examples/example_usage.py` for more detailed examples.

## Project Structure

```
sample-python-project/
├── README.md                 # This file
├── requirements.txt          # Project dependencies
├── setup.py                  # Package setup configuration
├── LICENSE                   # Project license
├── .gitignore               # Git ignore patterns
├── src/
│   └── data_analyzer/       # Main package
│       ├── __init__.py
│       ├── main.py          # Main module
│       ├── analyzer.py      # Core analyzer class
│       └── utils.py         # Utility functions
├── tests/
│   ├── __init__.py
│   └── test_analyzer.py     # Unit tests
└── examples/
    └── example_usage.py     # Usage examples
```

## Testing

Run the test suite:

```bash
python -m pytest tests/ -v
```

With coverage report:

```bash
python -m pytest tests/ --cov=src/data_analyzer
```

## Dependencies

- pandas: Data manipulation and analysis
- numpy: Numerical computing
- matplotlib: Visualization library
- seaborn: Statistical data visualization
- pytest: Testing framework

## Documentation

For detailed API documentation, see the docstrings in the source files.

## Examples

### Example 1: Load and Analyze Data

```python
from data_analyzer import DataAnalyzer

analyzer = DataAnalyzer('sales_data.csv')
stats = analyzer.get_statistics()
print(stats)
```

### Example 2: Visualize Data

```python
analyzer.plot_distribution('sales')
analyzer.plot_scatter('date', 'amount')
```

### Example 3: Export Results

```python
results = analyzer.get_summary()
analyzer.export_to_json('results.json')
```

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Keerthan Kumar (@KeerthanKumar11)

## Support

If you encounter any issues or have questions, please open an issue on GitHub.
