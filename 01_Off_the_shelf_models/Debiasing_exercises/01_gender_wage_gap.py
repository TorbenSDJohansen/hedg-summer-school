# %% Setup
import numpy as np
import pandas as pd

URL = (
    "https://raw.githubusercontent.com/TorbenSDJohansen/hedg-summer-school/"
    "debiasing/01_Off_the_shelf_models/Debiasing_exercises/Stockholm1920.csv"
)

d = pd.read_csv(URL)
lab = d[d["R"] == 1]


def ols(y, x):
    x, y = np.asarray(x, float), np.asarray(y, float)
    b = np.cov(x, y, ddof=1)[0, 1] / x.var(ddof=1)
    e = y - (y.mean() - b * x.mean()) - b * x
    se = np.sqrt((e**2).sum() / (len(x) - 2) / ((x - x.mean()) ** 2).sum())
    return b, se


# %% 1. Accuracy, precision, recall and F1 on the labelled rows
tp = ((lab["female_pred_binary"] == 1) & (lab["female"] == 1)).sum()
fp = ((lab["female_pred_binary"] == 1) & (lab["female"] == 0)).sum()
fn = ((lab["female_pred_binary"] == 0) & (lab["female"] == 1)).sum()
tn = ((lab["female_pred_binary"] == 0) & (lab["female"] == 0)).sum()

print(f"accuracy  {(tp + tn) / len(lab):.3f}")
print(f"precision {tp / (tp + fp):.3f}")
print(f"recall    {tp / (tp + fn):.3f}")
print(f"f1        {2 * tp / (2 * tp + fp + fn):.3f}")

# %% 2. Naive: predicted sex, all observations
b, se = ols(d["log_labor_income"], d["female_pred_binary"])
print(f"naive    {b:.3f}  95% CI [{b - 1.96 * se:.3f}, {b + 1.96 * se:.3f}]")

# %% 3. Labelled only: observed sex, the 330 rows where we have it
b, se = ols(lab["log_labor_income"], lab["female"])
print(f"labelled {b:.3f}  95% CI [{b - 1.96 * se:.3f}, {b + 1.96 * se:.3f}]")

# %% 4. Which do you trust?
# Naive is precise but biased, labelled-only is unbiased but noisy.
# The true gap is -0.822.
