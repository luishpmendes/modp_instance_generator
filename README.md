# Multi-Objective Districting Problem Instance Creator

This repository contains a Python script to generate instances for the Multi-Objective Districting Problem (MODP) using real-world map data obtained from OpenStreetMap via the OSMNX library.

## Description

The Python script included in this repository operates by reading place names from a CSV file. For each place name, the script fetches the corresponding road network graph via OSMNX, generates MODP instance files based on these graphs, and also plots and saves an image of each graph as a PNG file.

## Requirements

This script relies on the following Python libraries:

- `osmnx`
- `pandas`
- `matplotlib`

You can install these libraries using pip as follows:

```bash
pip install osmnx pandas matplotlib
```

## Usage
Follow these steps to use this script:
1. Clone this repository to your local machine.
2. Ensure that the required Python libraries mentioned above are installed.
3. Create a CSV file containing place names and put it in the root directory. This CSV file should have 'query' and 'name' columns. The script uses the 'query' column to generate the corresponding road network graphs with OSMNX, and the 'name' column to name the output instance files and images.
4. Run the Python script using the following command: `python instance_generator.py`

Upon successful execution, the script generates instance files, each containing graph data for a given place and district counts of 5, 10, and 20. Furthermore, the script will output PNG images, each depicting the road network graph of a place.

## Output Directory Structure
- Instance files: Located in the `./instance/` directory. Each file is named `{place_name}_{district_count}.txt`.
- Images: Located in the `./img/` directory. Each file is named `{place_name}.png`.

## Troubleshooting

If you encounter issues while running the script:
- Verify that your CSV file is formatted correctly with 'query' and 'name' columns.
- Check your Python environment to ensure that all required libraries are installed and up-to-date.

If the issue persists, please create a new issue detailing your problem, and we'll get back to you as soon as possible.
