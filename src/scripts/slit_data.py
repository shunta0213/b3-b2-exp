import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science', 'ieee'])
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams["font.size"] = 16

data = [
    "../data/B3_B2 - circle_data.csv",
    "../data/B3_B2 - ds1_data.csv",
    "../data/B3_B2 - ds2_data.csv",
    "../data/B3_B2 - ds3_data.csv",
    "../data/B3_B2 - ss1_data.csv",
    "../data/B3_B2 - ss2_data.csv",
    "../data/B3_B2 - ss3_data.csv",
]


for d in data:
    csv = pd.read_csv(d)

    dist = csv["Distance_(cm)"]
    gray_value = csv["Relative_Gray_Value"]

    plt.figure(figsize=(8, 6))
    title = d.split("/")[-1].split("-")[-1].strip(" ").split(".")[0]
    plt.plot(dist, gray_value)
    plt.xlabel("Distance / cm")
    plt.ylabel("Relative Gray Value")
    plt.savefig(f"../figures/result/{title}_amp.png")
    plt.close()
