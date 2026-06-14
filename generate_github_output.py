#!/usr/bin/env python3
"""
Auto-run script that generates output files visible on GitHub
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

import pandas as pd
import numpy as np
from data_analyzer import DataAnalyzer

def generate_output_files():
    """Generate analysis output files that GitHub will display"""
    
    print("\n" + "="*70)
    print("DATAANALYZER - GENERATING GITHUB-VISIBLE OUTPUT")
    print("="*70 + "\n")
    
    # Create output directory
    output_dir = Path('OUTPUT')
    output_dir.mkdir(exist_ok=True)
    
    # Step 1: Create sample data
    print("[1/5] Creating sample data...")
    np.random.seed(42)
    data = pd.DataFrame({
        'Month': pd.date_range('2026-01-01', periods=12, freq='M').strftime('%B'),
        'Sales': np.random.randint(10000, 100000, 12),
        'Profit': np.random.randint(1000, 10000, 12),
        'Expenses': np.random.randint(5000, 50000, 12),
    })
    
    data_file = Path('sample_data.csv')
    data.to_csv(data_file, index=False)
    print(f"✓ Sample data saved: {data_file}")
    
    # Step 2: Analyze data
    print("\n[2/5] Analyzing data...")
    analyzer = DataAnalyzer(str(data_file))
    stats = analyzer.get_statistics()
    print("✓ Analysis complete")
    
    # Step 3: Create statistics markdown
    print("\n[3/5] Creating statistics report...")
    stats_md = generate_statistics_markdown(analyzer, stats)
    stats_file = output_dir / 'STATISTICS.md'
    with open(stats_file, 'w') as f:
        f.write(stats_md)
    print(f"✓ Statistics saved: {stats_file}")
    
    # Step 4: Create summary markdown
    print("\n[4/5] Creating summary report...")
    summary_md = generate_summary_markdown(analyzer)
    summary_file = output_dir / 'SUMMARY.md'
    with open(summary_file, 'w') as f:
        f.write(summary_md)
    print(f"✓ Summary saved: {summary_file}")
    
    # Step 5: Create data table markdown
    print("\n[5/5] Creating data table...")
    table_md = generate_data_table_markdown(data)
    table_file = output_dir / 'DATA_TABLE.md'
    with open(table_file, 'w') as f:
        f.write(table_md)
    print(f"✓ Data table saved: {table_file}")
    
    # Create main README for outputs
    create_output_readme(output_dir)
    
    print("\n" + "="*70)
    print("✓ OUTPUT FILES CREATED SUCCESSFULLY")
    print("="*70)
    print(f"\nView results in the OUTPUT folder:")
    print(f"  📄 OUTPUT/STATISTICS.md")
    print(f"  📄 OUTPUT/SUMMARY.md")
    print(f"  📄 OUTPUT/DATA_TABLE.md")
    print(f"  📄 OUTPUT/README.md")
    print("\n")


def generate_statistics_markdown(analyzer, stats):
    """Generate statistics as markdown"""
    
    md = """# 📊 Statistical Analysis Report

## Dataset Information
"""
    md += f"- **Total Rows:** {len(analyzer.data)}\n"
    md += f"- **Total Columns:** {len(analyzer.data.columns)}\n"
    md += f"- **Columns:** {', '.join(analyzer.data.columns)}\n"
    
    md += "\n## Statistical Summary\n\n"
    
    # Create statistics table
    md += "| Metric | "
    for col in analyzer.data.select_dtypes(include=[np.number]).columns:
        md += f"{col} | "
    md += "\n"
    
    md += "|--------|"
    for col in analyzer.data.select_dtypes(include=[np.number]).columns:
        md += "---------|"
    md += "\n"
    
    for stat_type, values in stats.items():
        md += f"| {stat_type.upper()} |"
        for col in analyzer.data.select_dtypes(include=[np.number]).columns:
            if col in values:
                val = values[col]
                md += f" {val:.2f} |" if pd.notna(val) else " - |"
            else:
                md += " - |"
        md += "\n"
    
    md += "\n## Detailed Breakdown\n\n"
    
    for stat_type, values in stats.items():
        md += f"### {stat_type.upper()}\n\n"
        md += "```\n"
        for col, val in values.items():
            if pd.notna(val):
                md += f"{col}: {val:.2f}\n"
        md += "```\n\n"
    
    return md


def generate_summary_markdown(analyzer):
    """Generate summary as markdown"""
    
    summary = analyzer.get_summary()
    
    md = """# 📈 Data Summary Report

## Summary Statistics

"""
    md += "```\n"
    md += str(summary)
    md += "\n```\n\n"
    
    md += "## Column Information\n\n"
    
    for col in analyzer.data.columns:
        md += f"### {col}\n\n"
        md += f"- **Data Type:** {analyzer.data[col].dtype}\n"
        md += f"- **Non-null Count:** {analyzer.data[col].notna().sum()}\n"
        md += f"- **Null Count:** {analyzer.data[col].isna().sum()}\n"
        md += f"- **Unique Values:** {analyzer.data[col].nunique()}\n"
        if analyzer.data[col].dtype in ['int64', 'float64']:
            md += f"- **Min:** {analyzer.data[col].min()}\n"
            md += f"- **Max:** {analyzer.data[col].max()}\n"
            md += f"- **Mean:** {analyzer.data[col].mean():.2f}\n"
        md += "\n"
    
    return md


def generate_data_table_markdown(data):
    """Generate data table as markdown"""
    
    md = """# 📋 Data Table

## Sample Dataset

"""
    md += data.to_markdown(index=False)
    md += "\n\n## Data Statistics\n\n"
    md += f"- **Total Records:** {len(data)}\n"
    md += f"- **Total Columns:** {len(data.columns)}\n"
    md += f"- **File Size:** {len(data)} rows × {len(data.columns)} columns\n"
    
    return md


def create_output_readme(output_dir):
    """Create main README for OUTPUT folder"""
    
    readme = """# 📊 Analysis Output

This folder contains all generated analysis reports and data tables.

## Files

### 1. **STATISTICS.md**
Detailed statistical analysis including:
- Mean, Median, Standard Deviation
- Min, Max values
- Count of records
- Statistical breakdown by column

### 2. **SUMMARY.md**
Comprehensive summary report including:
- Dataset information
- Summary statistics
- Column details
- Data type information

### 3. **DATA_TABLE.md**
The actual data table in readable format:
- All records displayed
- Data statistics
- Record count

### 4. **README.md** (this file)
Overview of all output files

## How to View

1. Click on any `.md` file above
2. GitHub will render it automatically
3. See the formatted analysis report

## Generated From

- **Project:** DataAnalyzer
- **Repository:** KeerthanKumar11/sample-python-project
- **Generated:** Automatically by Python script

## Data Used

Sample data created with:
- 12 months of data
- Sales, Profit, and Expenses columns
- Random but realistic values

---

**View these files directly on GitHub without any setup!** 🎉
"""
    
    readme_file = output_dir / 'README.md'
    with open(readme_file, 'w') as f:
        f.write(readme)


if __name__ == '__main__':
    try:
        generate_output_files()
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
