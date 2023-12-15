import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

items = pd.read_csv("data/e2a_sine_waves_pairs_items.csv")
questions = pd.read_csv("data/e2a_sine_waves_pairs_questions.csv")
data = pd.merge(items, questions, on='question_id')

metrics = ["pleasant", "stimulating", "complex"]
colors = ["y", "r", "b"]
key = "user_id"
dimensions = ["spatial_waveform_2", "temporal_waveform_2"]

data = data[[key] + dimensions + metrics]
data_long = data.melt(
    id_vars=[key] + dimensions,
    value_vars=metrics,
    var_name="metric",
    value_name="value",
)
data_long["value"] = data_long.groupby([key, "metric"])["value"].transform(
    lambda x: (x - x.mean()) / x.std() if x.std() != 0 else np.nan
)
stats = (
    data_long.groupby(dimensions + ["metric"])["value"]
    .agg(["mean", "sem"])
    .reset_index()
)

for d in dimensions:
    criteria = (
        (stats["spatial_waveform_2"] == 35)
        if d == "temporal_waveform_2"
        else (stats["temporal_waveform_2"] == 4)
    )
    fig, axs = plt.subplots(len(metrics), 1)
    fig.set_size_inches(5, 7)
    for ax, metric, color in zip(axs.flat, metrics, colors):
        dm = stats[(stats["metric"] == metric) & criteria][
            ["mean", "sem"] + dimensions
        ].sort_values(by=d)
        ax.plot(dm[d], dm["mean"], c=color)
        ax.plot(dm[d], dm["mean"] + dm["sem"], lw=0.5, ls="--", c=color)
        ax.plot(dm[d], dm["mean"] - dm["sem"], lw=0.5, ls="--", c=color)
        ax.set_title(metric)
        ax.set_ylim(-1, 1)
        ax.set_xticks(dm[d], [])
        ax.grid(True)
    ax.set_xticks(dm[d], dm[d])
    ax.set_xlabel(d.replace("_", " ").replace("2", "").capitalize())
    fig.savefig(f"analysis/figures/e2a_{d.replace('_2', '')}.png")
