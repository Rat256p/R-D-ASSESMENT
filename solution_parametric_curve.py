import numpy as np
import pandas as pd
from scipy.optimize import least_squares

df = pd.read_csv("xy_data.csv")

x = df["x"].to_numpy()
y = df["y"].to_numpy()


def residual(params):
    theta, M, X = params

    c = np.cos(theta)
    s = np.sin(theta)

    # Since 6 < t < 60, |t| = t
    t = (x - X) * c + (y - 42) * s

    perpendicular = (
        -(x - X) * s
        + (y - 42) * c
    )

    predicted = np.exp(M * t) * np.sin(0.3 * t)

    return perpendicular - predicted


lower = [
    0,
    -0.05,
    0
]

upper = [
    np.deg2rad(50),
    0.05,
    100
]

initial = [
    np.deg2rad(25),
    0.0,
    50
]

result = least_squares(
    residual,
    initial,
    bounds=(lower, upper),
    max_nfev=10000
)

theta, M, X = result.x

print("theta (degrees):", np.rad2deg(theta))
print("M:", M)
print("X:", X)
print("RMSE:", np.sqrt(np.mean(result.fun ** 2)))