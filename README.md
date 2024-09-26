# Search Engine for Directory Traversal and Indexing

## Introduction

This project implements a search engine in Python for traversing directories and indexing files. It features efficient search algorithms and data structures for managing and querying file content.

## Features

- **Search Algorithms**: Implements various search algorithms for finding words in files. Includes support for both exact and partial matches.
- **Sorting Algorithms**: Uses sorting algorithms to rank and order search results based on relevance.
- **Data Structures**:
  - **Lists**: Used for managing file paths, search results, and other collections of data.
  - **Trie**: Implements a Trie data structure for efficient storage and retrieval of words.
  - **Dictionary**: Utilizes Python's dictionary for fast lookups and indexing.
  - **Array**: Employs arrays for storing and manipulating data during searches and sorting.
  - **Tuple**: Uses tuples to hold and manipulate pairs of data, such as file paths and their relevance scores.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:

    ```bash
    git clone git@github.com:marijazhiv/Search-engine.git
    ```

2. Navigate to the project directory:

    ```bash
    cd search-engine
    ```

3. Install any required dependencies (if applicable):

    ```bash
    pip install -r requirements.txt
    ```

## Usage

- **Directory Traversal and Indexing**: Use the `prolazak_kroz_direktorijume` function to analyze directories and index HTML files.

- **Search and Rank**: Use `trazenje_reci` or `trazenje_reci_sa_izbacivanjem` functions to search for specific words and rank files based on word occurrences and links.

- **Sorting Results**: Use the `sortiranje` function to sort and rank search results based on custom metrics.

## Code Structure

- **`graph.py`**: Implements the `Graph` class for managing file links.
- **`parser.py`**: Contains the `Parser` class for parsing HTML files and extracting content.
- **`trie.py`**: Provides the `Trie` class for efficient word storage and search.
- **`quicksort.py`**: Implements the `quick_sort` function for sorting and ranking data.
- **`main.py`**: The main script to perform file analysis and search operations.

## Example Usage

### Example 1: Analyzing Files

```python
from main import prolazak_kroz_direktorijume, trazenje_reci, sortiranje

# Specify the root directory for traversal
root_directory = 'path/to/directory'

# Perform directory traversal
nodes, tries, graph = prolazak_kroz_direktorijume(root_directory)

# Search for a specific word
word_to_search = 'example'
results = trazenje_reci(nodes, tries, graph, word_to_search)

# Sort and rank the results
sorted_results = sortiranje(results)
