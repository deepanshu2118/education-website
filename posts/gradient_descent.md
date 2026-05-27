# Gradient Descent in Machine Learning

Gradient Descent is an optimization algorithm used to minimize the cost function in machine learning models.

## How It Works
1. Start with random values of parameters (weights).
2. Compute the gradient of the cost function with respect to the parameters.
3. Update the parameters by moving them in the opposite direction of the gradient:
   
   $$
   \theta = \theta - \alpha \cdot \nabla J(\theta)
   $$
   where
   - $\theta$ = parameters
   - $\alpha$ = learning rate
   - $\nabla J(\theta)$ = gradient of the cost function

## Types of Gradient Descent
- **Batch Gradient Descent** – uses the whole dataset to compute the gradient.
- **Stochastic Gradient Descent (SGD)** – updates parameters for each training example.
- **Mini-Batch Gradient Descent** – compromise between batch and SGD.

## Key Intuition
Gradient Descent is like **rolling downhill** to find the lowest point in a valley — the minimum of the function.

---

### References
- Andrew Ng’s ML Course
- Deep Learning Book (Goodfellow et al.)
