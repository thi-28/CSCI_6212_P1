# Asymptotic Analysis of Nested Loop Algorithm

This repository contains an analysis of the time complexity of a nested loop algorithm, demonstrating how constraints can significantly reduce computational complexity.

## Files

- `Asymptotic_analysis.py` - Main analysis script with experimental setup and visualization

## Running Instructions

### Prerequisites
- Python 3.6 or higher
- Required packages: `matplotlib`

### Installation
```bash
pip install matplotlib
```

### Running the Analysis
```bash
python Asymptotic_analysis.py
```

### What the Script Does
1. **Executes the algorithm** for input sizes: [20, 300, 650, 1000, 2500, 4900, 8000, 12500, 17500, 23900, 30000]
2. **Measures execution times** using high-precision nanosecond timing
3. **Calculates theoretical O(n²) predictions** with scaling constants
4. **Displays results** in a comparison table showing:
   - Input size (n)
   - Experimental runtime (ns)
   - Theoretical n² values
   - Adjusted theoretical times
   - Ratio between experimental and theoretical
5. **Generates a log-log plot** comparing experimental vs theoretical results

### Expected Output
- Console output showing timing data and ratios
- A matplotlib window displaying the log-log plot
- Scaling constant for O(n²) complexity

### Note
The script may take several minutes to complete due to the large input sizes. The plot window will remain open until manually closed.

## Key Findings

This analysis demonstrates how algorithmic constraints can significantly reduce computational complexity from the naive O(n³) that three nested loops would suggest to O(n²), highlighting the importance of considering loop constraints in complexity analysis.

## Course Information

**Course:** CSCI 6212 - Design and Analysis of Algorithms  
**Assignment:** Project 1 - Asymptotic Analysis  
