# Parametric Curve Parameter Estimation

## 1. Problem Statement

The objective of this assignment is to determine the unknown parameters
$\theta$, $M$, and $X$ from the given set of points in `xy_data.csv`.

The parametric equations of the curve are:

$$
x =
t\cos(\theta)
-
e^{M|t|}\sin(0.3t)\sin(\theta)
+
X
$$

$$
y =
42
+
t\sin(\theta)
+
e^{M|t|}\sin(0.3t)\cos(\theta)
$$

The parameter $t$ is constrained to:

$$
6 < t < 60
$$

The unknown parameters have the following ranges:

$$
0^\circ < \theta < 50^\circ
$$

$$
-0.05 < M < 0.05
$$

$$
0 < X < 100
$$

The supplied `xy_data.csv` contains points that lie on the target curve.
The objective is to estimate the values of $\theta$, $M$, and $X$ such that
the generated curve matches these points as closely as possible.


## 2. Approach

The points from `xy_data.csv` are loaded and used as the observed $(x,y)$
coordinates.

Since the given range satisfies $t > 6$, we have:

$$
|t| = t
$$

Therefore, the equations can be written as:

$$
x =
t\cos(\theta)
-
e^{Mt}\sin(0.3t)\sin(\theta)
+
X
$$

$$
y =
42
+
t\sin(\theta)
+
e^{Mt}\sin(0.3t)\cos(\theta)
$$

To estimate the unknown parameters, the equations can be viewed as a rotated
coordinate system.

For a candidate value of $\theta$, the component of a point along the
direction $(\cos\theta,\sin\theta)$ gives an estimate of $t$:

$$
t =
(x-X)\cos(\theta)
+
(y-42)\sin(\theta)
$$

The perpendicular component is:

$$
-(x-X)\sin(\theta)
+
(y-42)\cos(\theta)
$$

According to the original curve equation, this component should satisfy:

$$
-(x-X)\sin(\theta)
+
(y-42)\cos(\theta)
=
e^{Mt}\sin(0.3t)
$$

This relationship allows the unknown parameters $\theta$, $M$, and $X$ to
be estimated directly from the observed points.


## 3. Optimization Method

The parameters were estimated using numerical least-squares optimization.

For every candidate parameter set

$$
(\theta,M,X)
$$

the corresponding value of $t$ was calculated as:

$$
t =
(x-X)\cos(\theta)
+
(y-42)\sin(\theta)
$$

The perpendicular-coordinate residual was then calculated as:

$$
r_i =
-(x_i-X)\sin(\theta)
+
(y_i-42)\cos(\theta)
-
e^{Mt_i}\sin(0.3t_i)
$$

The objective was to minimize the sum of squared residuals:

$$
\min_{\theta,M,X}
\sum_{i=1}^{N} r_i^2
$$

subject to the parameter constraints:

$$
0 < \theta < 50^\circ
$$

$$
-0.05 < M < 0.05
$$

$$
0 < X < 100
$$

The optimization was performed with $\theta$ represented internally in radians
and converted to degrees when reporting the final result.


## 4. Final Values

The optimization converged to the following parameter values:

$$
\boxed{\theta \approx 30^\circ}
$$

$$
\boxed{M \approx 0.03}
$$

$$
\boxed{X \approx 55}
$$

Therefore, the final estimated parameters are:

| Parameter | Estimated Value |
|-----------|-----------------|
| $\theta$ | $30^\circ$ |
| $M$ | $0.03$ |
| $X$ | $55$ |

Substituting these values into the original equations gives the fitted
parametric curve:

$$
x =
t\cos(30^\circ)
-
e^{0.03|t|}
\sin(0.3t)
\sin(30^\circ)
+
55
$$

$$
y =
42
+
t\sin(30^\circ)
+
e^{0.03|t|}
\sin(0.3t)
\cos(30^\circ)
$$


## 5. Verification

The estimated parameters were substituted back into the original parametric
equations and compared against the points supplied in `xy_data.csv`.

Using the fitted numerical parameters, the mean coordinate-wise L1 error was
approximately:

$$
\boxed{3.50\times10^{-6}}
$$

Using the rounded parameters

$$
\theta=30^\circ,\qquad M=0.03,\qquad X=55
$$

the mean coordinate-wise L1 error was approximately:

$$
\boxed{2.06\times10^{-5}}
$$

The very small error indicates that the recovered parameters reproduce the
given curve to high numerical accuracy.

The recovered values of $t$ also remain within the required range:

$$
6 < t < 60
$$

This provides an additional check that the estimated parameters are consistent
with the constraints specified in the assignment.


## 6. How to Run

### Requirements

Python 3.9 or later is recommended.

Install the required packages using:

```bash
pip install numpy pandas scipy
