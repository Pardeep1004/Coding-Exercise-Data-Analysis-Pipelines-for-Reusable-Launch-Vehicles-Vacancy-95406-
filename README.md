## Functions

### 1. `mean_confidence_interval`

This function calculates the mean and confidence interval for each x value in the given dataset.

#### Parameters:
- `data` (pandas.DataFrame): A DataFrame where each row represents a set of observations corresponding to an x value.
- `confidence` (float, optional): The confidence level for the interval. Default is 0.80 (80%).

#### Returns:
- `result` (pandas.DataFrame): A DataFrame containing the x values, means, lower bounds, and upper bounds of the confidence intervals.

### 2. plot_data_with_intervals
This function visualizes the data along with the calculated mean and confidence intervals.

#### Parameters:
- `data` (pandas.DataFrame): A DataFrame where each row represents a set of observations corresponding to an x value.
- `mean_conf_intervals` (pandas.DataFrame, optional): A DataFrame containing the mean and confidence intervals, as returned by mean_confidence_interval. Default is None.


### DockerFile
- It is easy to manage and even efficient with better working environment.
- Below mention are the code to build docker image and container.


For building a docker image
```docker build -t dlr:v1 . ```

for creating a docker container out of docker image
```docker run dlr:v1 -p 8501:8501```

