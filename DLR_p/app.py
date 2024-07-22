import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def mean_confidence_interval(data, confidence=0.80):
    """
    Calculate the mean and confidence interval for each x .

    """
    means = data.mean(axis=1)
    sems = data.apply(lambda row: stats.sem(row.dropna()), axis=1)
    h = sems * stats.t.ppf((1 + confidence) / 2., data.shape[1] - 1)

    result = pd.DataFrame({
        'x': data.iloc[:, 0],
        'mean': means,
        'lower_bound': means - h,
        'upper_bound': means + h
    })

    st.write(result)
    return result


def plot_data_with_intervals(data, mean_conf_intervals=None):
    plt.figure(figsize=(10, 6))

    # Plot each y sample
    for col in data.columns[1:]:
        plt.plot(data.iloc[:, 0], data[col], marker='o', linestyle='-', alpha=0.5, label=col)

    if mean_conf_intervals is not None:
        # Plot mean
        plt.plot(mean_conf_intervals['x'], mean_conf_intervals['mean'], color='red', marker='o', linestyle='-', label='Mean')

        # Plot confidence intervals
        plt.fill_between(mean_conf_intervals['x'], mean_conf_intervals['lower_bound'], mean_conf_intervals['upper_bound'], color='gray', alpha=0.2, label='Confidence Interval')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Data with Mean and Confidence Intervals')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)





upload_file = st.file_uploader("Choose csv file",type="csv")
confidence = st.number_input("Cofidence value",max_value=1.0,min_value=0.0,value=0.8)

if st.button("Submit data"):
    if upload_file is not None:
        
        data = pd.read_csv(upload_file)

        # Fill NaN values with the mean of their respective columns
        data_filled = data.apply(lambda col: col.fillna(col.mean()), axis=0)

        plot_data_with_intervals(data,mean_confidence_interval(data_filled,confidence=confidence))
    else:
        st.write("Please upload the dataset")
    