# %% Setup
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

N, pi = 1000, 0.1

# %% 1. One sample from the DGP, with Y removed for 90% of it
def draw(N, pi, rng):
    X = rng.uniform(size=N)
    Y = 2 * X                        # the true mean of Y is 1
    R = rng.binomial(1, pi, size=N)  # 1 where we still observe Y
    f = 2.1 * X - 0.5 * X**2         # the deliberately imperfect predictor
    return Y, f, R


Y, f, R = draw(N, pi, rng)

# %% 2. The three estimators
def estimators(Y, f, R):
    gold = Y[R == 1].mean()                                       # option 1
    ml = f.mean()                                                 # option 2
    debiased = f[R == 0].mean() - (f[R == 1] - Y[R == 1]).mean()  # option 3
    return gold, ml, debiased


print(estimators(Y, f, R))

# %% 3. Repeat 1,000 times and plot
sims = np.array([estimators(*draw(N, pi, rng)) for _ in range(1000)])

for i, name in enumerate(["Gold standard", "Naive ML", "Debiased"]):
    plt.hist(sims[:, i], bins=40, alpha=0.5, label=name)

plt.axvline(1, color="black", linestyle="--")
plt.xlabel("Estimate")
plt.legend()
plt.show()

print(sims.mean(axis=0))
print(sims.std(axis=0))
