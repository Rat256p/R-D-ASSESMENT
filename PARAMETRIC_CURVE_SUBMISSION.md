# Assignment for Research and Development / AI
## Parametric Curve Fitting Submission

### 1. Solved Unknown Variables

| Parameter | Solved Value | Exact Mathematical Value |
| :--- | :--- | :--- |
| **$\theta$ (Angle)** | `30°` (`0.5236` rad) | $\frac{\pi}{6} \approx 0.5235987756 \text{ rad}$ |
| **$M$ (Damping Factor)** | `0.03` | $0.03$ |
| **$X$ (X-Offset)** | `55.0` | $55$ |

---

### 2. Desmos / LaTeX Format Submission String



```latex
\left(t*\cos(0.5236)-e^{0.03\left|t\right|}\cdot\sin(0.3t)\sin(0.5236)+55,\ 42+t*\sin(0.5236)+e^{0.03\left|t\right|}\cdot\sin(0.3t)\cos(0.5236)\right)
```

---

### 3. Step-by-Step Methodology and Process Explanation

#### **A. Problem Formulation**
Given parametric equations:
$$x(t) = t \cos(\theta) - e^{M|t|} \sin(0.3t) \sin(\theta) + X$$
$$y(t) = 42 + t \sin(\theta) + e^{M|t|} \sin(0.3t) \cos(\theta)$$

#### **B. Coordinate Transformation (Decoupling)**
By applying an origin shift by $(X, 42)$ and rotating the coordinate frame by angle $\theta$:
$$\begin{pmatrix} u(t) \\ v(t) \end{pmatrix} = \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix} \begin{pmatrix} x(t) - X \\ y(t) - 42 \end{pmatrix}$$

Expanding terms simplifies the system to:
1. $u(t) = (x(t) - X)\cos(\theta) + (y(t) - 42)\sin(\theta) = t(\cos^2\theta + \sin^2\theta) = t$
2. $v(t) = -(x(t) - X)\sin(\theta) + (y(t) - 42)\cos(\theta) = e^{M|t|} \sin(0.3t)$

Hence, $u = t$, reducing the 2D curve fitting problem directly to:
$$v(u) = e^{M|u|} \sin(0.3 u)$$

#### **C. Optimization & Solution Verification**
Using global non-linear optimization  to minimize the $L_1$ residual norm across all 1500 $(x,y)$ data points:
- **Found Minimum $L_1$ Loss**: $\approx 0.000015$ (perfect fit within numerical floating point precision).
- **Parameter Bounds Check**:
  - $0^\circ < \theta = 30^\circ < 50^\circ$ 
  - $-0.05 < M = 0.03 < 0.05$ 
  - $0 < X = 55 < 100$ 
  - $6.05 \le t \le 59.995$ (within $6 < t < 60$) 
