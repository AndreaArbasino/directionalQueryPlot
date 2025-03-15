# Directional Query Plotter

## Overview
This Python project is designed to visualize the effects of a directional query on a 2D space using contour plots. It allows users to interactively adjust parameters and observe how they influence the plotted data. The project was developed as part of an academic research study.

## Features
- Generates contour plots representing the effect of a query function.
- Interactive sliders to adjust the `alpha` and `beta` parameters dynamically.
- Supports multiple colormaps for better visualization.
- Saves the generated plot as an image file.

## Requirements
Ensure you have the following dependencies installed before running the script:

```sh
pip install numpy matplotlib
```

## Usage
Run the script using:

```sh
python plot_query.py
```

### Interactive Controls
- **Beta Slider**: Adjusts the `beta` parameter.
- **Alpha Slider**: Modifies the `alpha` parameter.
- **Reset Button**: Resets sliders to default values.

## Explanation of Core Functions
- `score_lin(point, query)`: Computes a linear score based on a given query.
- `dist_line_point(point, query)`: Calculates the Euclidean distance between a set of points and a line defined by the query.
- `score(q, alpha)`: Computes a weighted combination of various distance and score metrics.

## Output
The script generates:
- A contour plot displayed in a Matplotlib figure.
- A PNG image file saved in the working directory with a name format:
  
  ```
  q_plot_alpha_<alpha>_beta_<beta>_<colormap>.png
  ```

## Example Output
After execution, the program will generate a graphical visualization like the one below:

![Example Plot](example_output.png)

## License
This project is open-source and available under the MIT License.

