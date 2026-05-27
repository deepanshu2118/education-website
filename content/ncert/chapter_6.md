<h1> Chapter 6 : Application of Derivatives </h1>

> "With the Calculus as a key, Mathematics can be successfully applied to the explanation of the course of Natue." - WHITEHEAD

## Introduction

Building on Chapter 5 (derivatives of composite, inverse trig, implicit, exponential, and log functions), this chapter explores real-world uses in engineering, science, and social sciences. Key applications include:

- Rate of change of quantities

- Tangent/normal equations at curve points

- Turning points for max/min values

- Increasing/decreasing intervals

- Approximating values

## Rate of Change of Quantities

The derivative $\frac{dy}{dx}$ gives the rate of change of y with respect to x (like $\frac{ds}{dt}$ for distance over time). 

- $f^{'}(x)$ represents the rate of change of y with resepect to x and
 <p>
\[
\left.\frac{dy}{dx}\right|_{x=0}
\]
</p>
(or $f^{'}(x_0)$) represents the rate of change of y with respect to x at $x = x_{0}$.

- When x = f(t) and y = g(t) vary with time t, use the chain rule :
<p>
\[
\frac{dy}{dx} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}}   , (if \frac{dx}{dt}\neq 0)
\]
</p>

Thus, the rate of change of y with respect to x can be calculated using the rate of
change of y and that of x both with respect to t.

**Example 1** Find the rate of change of the area of a circle per second with respect to
its radius r when r = 5 cm.

**Example 2** The volume of a cube is increasing at a rate of 9 cubic centimetres per
second. How fast is the surface area increasing when the length of an edge is 10
centimetres ?

**Example 3** A stone is dropped into a quiet lake and waves move in circles at a speed
of 4cm per second. At the instant, when the radius of the circular wave is 10 cm, how
fast is the enclosed area increasing?

**Note:** $\frac{dy}{dx}$ is positive if y increases as x increases and is negative if y decreases
as x increases.

**Example 4** The length x of a rectangle is decreasing at the rate of 3 cm/minute and
the width y is increasing at the rate of 2cm/minute. When x =10cm and y = 6cm, find
the rates of change of (a) the perimeter and (b) the area of the rectangle.

**Example 5** The total cost C(x) in Rupees, associated with the production of x units of
an item is given by

$C(x) = 0.005 x^3 - 0.02 x^2 + 30x + 500
$
Find the marginal cost when 3 units are produced, where by marginal cost we
mean the instantaneous rate of change of total cost at any level of output.

**Example 6** The total revenue in Rupees received from the sale of x units of a product
is given by $R(x) = 3x^2 + 36x + 5$. Find the marginal revenue, when x = 5, where by
marginal revenue we mean the rate of change of total revenue with respect to the
number of items sold at an instant.

### Exercise 6.1

## Increasing and Decreasing Functions

**Defintion 1**  Let $I$ be an interval contained in the domain of a real valued function f.
Then f is said to be

(i) increasing on $I$ if $x_1 < x_2 $ in I $ \implies f(x_1) \leq f(x_2)$ for all $x_1, x_2 \in I$

(ii) decreasing on $I$ if $x_1 < x_2 $ in I $ \implies f(x_1) \geq f(x_2)$ for all $x_1, x_2 \in I$

(iii) constant on I, if f(x) = c for all $x \implies I$, where c is a constant.

(iv) strictly increasing on $I$ if $x_1 < x_2 $ in I $ \implies f(x_1) \le f(x_2)$ for all $x_1, x_2 \in I$

(v) strictly decreasing on $I$ if $x_1 < x_2 $ in I $ \implies f(x_1) \ge f(x_2)$ for all $x_1, x_2 \in I$

<figure>
  <img src="/static/images/in_dec.png" 
       alt="tan graph" 
       style="max-width:70%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

**Definition 2**  Let $x_0$ be a point in the domain of definition of a real valued function  f. Then  f  is said to be increasing, decreasing at $x_0$, if  there exists an open interval I containing $x_0$ such that f is increasing, decreasing, respectively, in I.

**Example 7** Show that the function given by f(x) 7x-3 is increasing on $\mathbb{R}$.

**Theorem 1** Let  f  be continuous on [a, b] and differentiable on the open interval (a,b). The

(a)  f is increasing in [a,b] if $f^{'}(x) \geq 0$ for each $x \implies (a,b)$

(b) f is decreasing in [a,b] if $f^{'}(x) \leq 0$ for each $x \implies (a,b)$

(c) f is content function in [a,b] if $f^{'}(x) =0$ for each $x \implies (a,b)$