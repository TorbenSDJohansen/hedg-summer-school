# %% Setup
import numpy as np
import pandas as pd

URL = (
    "https://raw.githubusercontent.com/TorbenSDJohansen/hedg-summer-school/"
    "debiasing/01_Off_the_shelf_models/Debiasing_exercises/Stockholm1920.csv"
)

d = pd.read_csv(URL)

pi = 0.10  # the gold standard was drawn with 10% probability, known by design

# %% 1. DSL estimate of the gender wage gap
Y = d["log_labor_income"].to_numpy(float)
Z_pred = d["female_pred"].to_numpy(float)       # the probability, not the label
R = d["R"].to_numpy(float)
Z = d["female"].fillna(0).to_numpy(float)       # 0 * NaN is NaN, so fill first

Z_aug = Z_pred + R / pi * (Z - Z_pred)
Z2_aug = Z_pred**2 + R / pi * (Z**2 - Z_pred**2)
ZY_aug = Z_pred * Y + R / pi * (Z * Y - Z_pred * Y)

mu_Y, mu_Z = Y.mean(), Z_aug.mean()
mu_Z2, mu_ZY = Z2_aug.mean(), ZY_aug.mean()

denom = mu_Z2 - mu_Z**2
beta = (mu_ZY - mu_Z * mu_Y) / denom

IF_A = (ZY_aug - mu_ZY) - mu_Y * (Z_aug - mu_Z) - mu_Z * (Y - mu_Y)
IF_B = (Z2_aug - mu_Z2) - 2 * mu_Z * (Z_aug - mu_Z)
psi = IF_A - beta * IF_B
se = np.sqrt(psi.var(ddof=1) / (len(Y) * denom**2))

print(f"dsl      {beta:.3f}  95% CI [{beta - 1.96 * se:.3f}, {beta + 1.96 * se:.3f}]")

# %% 2. Compare with the previous exercise
lab = d[d["R"] == 1]

print(f"naive    {np.polyfit(d['female_pred_binary'], d['log_labor_income'], 1)[0]:.3f}")
print(f"labelled {np.polyfit(lab['female'], lab['log_labor_income'], 1)[0]:.3f}")
print(f"dsl      {beta:.3f}")
print("oracle   -0.822")
