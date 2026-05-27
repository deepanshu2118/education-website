# Chapter 5: Continuity and Differentiability

> “The whole of science is nothing more than a refinement of everyday thinking.” — Albert Einstein 

## Introduction
This chapter extends differentiation from Class XI to the formal study of continuity, differentiability, their relationships, derivatives of inverse trigonometric functions, and introduces exponential and logarithmic functions with powerful differentiation techniques and foundational theorems. 

In the last class we learned how to pull out the “slope” of easy curves like x² or sin x; now we push the idea one step further. First we ask a simple question—does the graph have any sudden breaks?—and give that break-free property the name continuity. Next we check whether every point on the curve actually allows a neat tangent; this sharper test is called differentiability and, surprisingly, a graph can be continuous yet fail it. Once these two ideas are clear we add three new friends to our function list: inverse-trigonometric, exponential and logarithmic; each brings its own quick differentiation rule that saves precious minutes in the exam. Finally we meet two “every-time-true” theorems—Rolle and Lagrange—which turn vague geometric feelings into exact formulas and are favourite 4-mark questions every year. Master this small kit and every derivative problem in the board paper becomes a 30-second job.

## Continuity
We begin with examples to build intuition for continuity. For piecewise functions with different left and right limits at a point, the function is not continuous there; if the common limit exists but differs from the function value, it is also discontinuous.
example:
<p>
    \[
      f(x)=
      \begin{cases}
        1, & \text{if } x\neq 0\\
        2, & \text{if } x=0.
      \end{cases}
    \]
  </p>

**Note:** We may say that a function is continuous at a fixed point if we can draw the graph of the function around that point without lifting the pen from the plane of the paper.  

**Definition 1** (Continuity at a point): Suppose f is a real function on a subset of the real number and c be a point in the domain of f. Then f is continuous at c if
$$\lim_{x\to c} f(x)=f(c)$$

More elaborately, if the left hand limit, right hand limit and the value of the function at x = c exist and equal to each other, then f is said to be contiuous at x = c. Recall that if the right hand and left hand limits at x = c coincide, then we say that the common value is the limit of the function at x = c. Hence we may also repharse the definition of continuity as follows: a function is continuous at x = c if the function is defined at x = c and if the value of the function at x = c equals the limit of the function at  x = c. If f is not continuous at c, we say f is discontinuous at c and c is called  a point of discontinuity of f.

**Examples 1** Check the function f(x)=2x+3 is continuous at x=1 ?

**Examples 2** Examine the function f(x)=x^2 is continuous at x=0. 

**Example 3** Discuss the function f(x)=|x| is continuous at x=0.

**Example 4** Show that the function f is given by
<p>
    \[
      f(x)=
      \begin{cases}
        x^3 + 3, & \text{if } x\neq 0\\
        1, & \text{if } x=0.
      \end{cases}
    \]
  </p>
is not continuous at x = 0. 

**Example 5** Check the points where the constant function f(x) = k is continuous.

**Example 6** Prove that the identity function on real numbers given by f(x) = x is continuous at every real number.

**Definition 2** (continuity on interval) A real function f is said to be continuous if it is continuous at every point in the domain of f.

This definition requires a bit of elaboration. Suppose f is a function defined on a closed interval [a,b], then for f to be continuous, it needs to be continuous at every point in [a,b] including the end points a and b. Continuity of f at a means
$$\lim_{x\to a^+} f(x)=f(a)$$
and Continuity of f at b means
$$\lim_{x\to b^-} f(x)=f(b)$$


Observe that $\lim_{x\to a^-} f(x)=f(a)$ and $\lim_{x\to b^+} f(x)=f(b)$ do not make sense. As a consequence of this definition, if f is defined only at one point, it is continuous there, i.e., if the domain of f is a singleton, f is a continuous function.

**Example 7** Is the function be f(x) = |x|, a continuous function ?

**Example 8** Discuss the continuity of the function f given by $f(x) = x^3 + x^2 -1$.

**Example 9** Discuss the continuity of the function f defined by $f(x) = \frac{1}{x}, x \neq 0.$

**Example 10** Discuss the continuity of the function f defined by 
<p>
    \[
      f(x)=
      \begin{cases}
        x + 2, & \text{if } x\leq 0\\
        x - 2, & \text{if } x > 0.
      \end{cases}
    \]
  </p>

**Example 11** Find all points of discontinuity of the function f defined by 
<p>
    \[
      f(x)=
      \begin{cases}
        x + 2, & \text{if } x < 1\\
        0 , & \text{if} x = 0 \\
        x - 2, & \text{if } x > 0.
      \end{cases}
    \]
  </p>

**Example 12** Discuss the continuity of the function defined by
<p>
    \[
      f(x)=
      \begin{cases}
        x + 2, & \text{if } x < 0\\
       -x + 2, & \text{if } x > 0.
      \end{cases}
    \]
  </p>

**Example 13** Discuss the continuity of the function f given by
<p>
    \[
      f(x)=
      \begin{cases}
        x , & \text{if } x \geq 0\\
       x^2, & \text{if } x < 0.
      \end{cases}
    \]
  </p>

**Example 14** Show that every polynomial function is continuous.

**Example 15** Find all the points of discontinuity of the greatest integer function defined by f(x) = [x], where [x] denotes the greatest integer less than or equal to x.

### 5.2.1 Algebra of continuous functions

**Theorem 1** Suppose f and g be two real functions continuous at a real number c. Then

(1) f + g is continuous at x = c.

(2) f -g is continuous at x = c.

(3) f.g is continous at x = c.

(4) $\frac{f}{g}$ is continous at x = c. (provided g(c)$\neq$ 0) 

**Example 16** Prove that every rational function is continuous.

**Example 17** Discuss the continuity of sine function.

**Example 18** Prove that the function defined by f(x) = tanx is a continuous function.

**Theorem 2** Suppose f and g are real valued functions such that (fog) is defined at c. If g is continuous at c and if f is continuous at g(c), then (fog) is continuous at c.

**Example 19** Show that the function defined by f(x) =sin($x^2$) is a continuous  function. 

**Example 20** Show that the function f defined by

<p>
 \[
        f(x) = \lvert 1 - x + \lvert x \rvert \rvert,
\]
</p>
Where x is any real number is a continuous function. 


## Differentiability
Suppose f is a real function and c is a point in its domain. The derivative of f at c is defined by 
<p>
\[
\lim_{h \to 0} \frac{f(c+h) - f(c)}{h}
\]
</p>
<p>
provided this limit exists. Derivative of <i>f</i> at <i>c</i> is denoted by
\( f'(c) \) or
\( \left.\dfrac{d}{dx}(f(x))\right|_{c} \).
The function defined by
</p>

<p>
\[
f'(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}
\]
</p>

<p>
wherever the limit exists is defined to be the derivative of <i>f</i>.
The derivative of <i>f</i> is denoted by \( f'(x) \) or
\( \dfrac{d}{dx}(f(x)) \) or if \( y=f(x) \) by
\( \dfrac{dy}{dx} \) or \( y' \).
The process of finding derivative of a function is called
<i>differentiation</i>.
We also use the phrase <i>differentiate</i> \( f(x) \)
<i>with respect to</i> \( x \) to mean find \( f'(x) \).
</p>
The following rules were established as a part of algebra of derivatives:
<p>
\[
(1)  (u \pm v)' =  u' \pm v' 
\]
</p>
<p>
\[
(2) (uv)' = u'v + uv'
\]
</p>
<p>
\[
(3) \frac{u}{v} = \frac{u'v-uv'}{v^2}
\]
</p>
Whenever we defined derivative we had put a caution provided the limit exists. If $\lim_{h\to 0}\frac{f(c+h)-f(c)}{h}$ does not exist, we say that f is not differentiable at c. In other words, we say that a function f is differentiable at a point c in its domain if both $\lim_{h\to 0^-}\frac{f(c+h)-f(c)}{h}$ and $\lim_{h\to 0^+}\frac{f(c+h)-f(c)}{h}$ are finite and equal.

A function is said to be differentiable in an interval [a,b] if it is differentiable at every point of [a,b]. As in case of continuity at the end points a and b, we take the right hand limit and left hand limit, which are nothing but left hand derivative and right hand derivative of the function at a and b respectively. Similarly, a function is said to be differentiable in an interval (a, b) if it is differentiable at every point of (a, b).

**Theorem 3** If a function f is differentiable at a point c, then it is also contiuous at that point.

**Corollary 1** Every differentiable function is continuous.



### 5.3.1 Derivatives of composite function 

**Theorem 4 (chain rule)**  Let f be a real valued function which is a composite of two functions u and v; i.e., f = v o u. Suppose t = u(x) and if both $\frac{dt}{dx}$ and $\frac{dv}{dt}$ exist, we have 
<p>
\[ 
  \frac{df}{dx} = \frac{dv}{dt}.\frac{dt}{dx}
  \]
</p>
Suppose f is a real valued function which is a composite of three functions u, v and w ; i.e.

f = (w o u) o v. If t = v(x) and s = u(t)
<p>
\[ 
  \frac{df}{dx} = \frac{d(w o u)}{dt}.\frac{dt}{dx} = \frac{dw}{ds}.\frac{ds}{dt}.\frac{dt}{dx}
  \]
</p>

**Example 21**  Find the derivative of the function given by f(x) = sin($x^2$)


### 5.3.2 Implicit differentiation
**Example 22** Find $\frac{dy}{dx}$ if x - y = $\pi$

**Example 23** Find  $\frac{dy}{dx}$ if y + siny = cosx

### 5.3.3 Inverse trigonometric derivatives
**Example 24** Find the derivative of f given by f(x) =$sin^{-1}x$ assuming it exists. 

##  Exponential and Logarithmic Functions

**Defintion 3** The exponential function with positive base b > 1 is the function
<p>
\[ 
  y = f(x) = b^x
  \]
</p>
Following are some of the salient features of the exponential functions.

(1) Domain of the exponential function is R, the set of all real numbers

(2)  Range of the exponential function is the set of all positive real numbers.

(3) The point (0, 1) is always on the graph of the exponential function (this is a
restatement of the fact that b0 = 1 for any real b > 1).

(4) Exponential function is ever increasing; i.e., as we move from left to right, the
graph rises above.

(5)  For very large negative values of x, the exponential function is very close to 0. In
other words, in the second quadrant, the graph approaches x-axis (but never
meets it).

Exponential function with base 10 is called the $\textbf{common exponential function}$.

Using this e as the base we obtain an extremely important exponential function y = $e^x$.
This is called $\textbf {natural exponential function}.$

**Definition 4** Let b > 1 be a real number. Then we say logarithm of a to base b is x if
$b^x$ = a.

Logarithm of a to base b is denoted by $log_b(a)$. Thus $log_b(a) = x$ if $b^x$ = a.

Fixing a base b > 1, we may look at logarithm as a function from positive real numbers to all real numbers. This function called the logarithmic function, is denoted by
<p>
\[
\log_b : \mathbb{R}^{+} \longrightarrow \mathbb{R}
\]
</p>
<p>
\[
x \longmapsto \log_b x = y \quad \text{if } b^{y} = x
\]
</p>

As before if the base b = 10, we say it
is $\textbf{common logarithms}$ and if b = e, then
we say it is $\textbf{natural logarithms}$. Often
natural logarithm is denoted by ln.

Some observations about the logarithm function

(1) We cannot make a meaningful definition of logarithm of non-positive numbers
and hence the domain of log function is $\mathbb{R}^{+}$.

(2) The range of log function is the set of all real numbers.

(3) The point (1, 0) is always on the graph of the log function.

(4) The log function is ever increasing, i.e., as we move from left to right the graph rises above.

(5) For x very near to zero, the value of log x can be made lesser than any given real number. In other words in the fourth quadrant the graph approaches y-axis (but never meets it).

<figure>
  <img src="/static/images/exp_log_graph.png" 
       alt="tan graph" 
       style="max-width:70%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

(6) Above Plot of $y = e^{x}$ and $y = lnx$. It is of interest to observe that the two curves are the mirror images of each other reflected in the line y = x. 

Some Properties of "log" function are below: 
<p>
\[
(i) \hspace{0.5cm} log_a(p) = \frac{log_b(p)}{log_b(a)}
\]
</p>

<p>
\[
(ii) \hspace{0.5cm}  log_b(pq) = log_b(p)+log_b(q)
\]
</p>

<p>
\[
(iii) \hspace{0.5cm}  log_b(p^2) = log_b(p)+log_b(p) = 2 log(p)
\]
</p>

<p>
\[
(iv) \hspace{0.5cm}  log_b(p^n) =  n log(p)
\]
</p>

<p>
\[
(v) \hspace{0.5cm}  log_b(\frac{x}{y}) = log_b(x)-log_b(y)
\]
</p>

**Example 25** Is it true that $ x = e^{log x}$ for all real x ?

(1) The derivative of $e^{x}$ w.r.t., x is e^{x} ; i.e., $\frac{d}{dx}(e^x) = e^x$

(2) The derivative of log x w.r.t., x is $\frac{1}{x}$ ; i.e. $\frac{d}{dx}(log x) = \frac{1}{x}$

**Example 26** Differentiate the following w.r.t. x:
<p>
\[
(i) \hspace{0.5cm} e^{-x} \hspace{0.5cm} (ii) \hspace{0.5cm} sin(logx) , x > 0 \hspace{0.5cm} (iii) \hspace{0.5cm} cos^{-1}(e^{x}) \hspace{0.5cm} (iv) \hspace{0.5cm} e^{cosx}
\]
</p>
### Exercise 5.4


## Logarithmic Differentiation

**Example 27**
<p>
Differentiate
\[  \sqrt\frac{(x-3)(x^2 + 4 )}{3x^2 + 4x + 5}
\]
with respect to the x.
</p>

**Example 28** Differentiate $a^{x}$ with respect to the x, where a is a positive constant.

**Example 29**  Differentiate $x^{sinx}$, x > 0 with respect to the x.

**Example 30** Find $\frac{dy}{dx}$, if $y^{x} + x^{y} + x^{x} = a^{b}$.


### Exercise 5.5
Differentiate products with multiple factors, nested logs and powers, verify multi‑factor product rule via logs, and related identities. 

## Derivatives in Parametric Form
A relation expressed between two variables x and y in the form x = f(t), y = g(t) is said to be parametric form with t as a parameter.

In  order to find derivative of function in such form, we have by chain rule.
<!-- <p>
\[
\frac{dy}{dt} &= \frac{dy}{dx}.\frac{dx}{dt} \\

\frac{dy}{dx} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}} 

\frac{dy}{dx} = \frac{g'(t)}{f'(t)} 


\]
</p> -->
<p>
\[
\begin{aligned}
\frac{dy}{dt} &= \frac{dy}{dx}\cdot\frac{dx}{dt} \\
\frac{dy}{dx} &= \frac{\frac{dy}{dt}}{\frac{dx}{dt}} (whenever  \frac{dy}{dx} \neq 0) \\
\frac{dy}{dx} &= \frac{g'(t)}{f'(t)}
\end{aligned}
\]
</p>
Where $\frac{dy}{dt} = g'(t)$ and $\frac{dx}{dt} = f'(t)$ provided $f'(t) \neq 0$

**Example 31** Find $\frac{dy}{dx}$, if $x = acos(\theta)$ , $y = asin(\theta)$

**Example 32** Find $\frac{dy}{dx}$, if $x = at^2$ and y = 2at.

**Example 33** Find $\frac{dy}{dx}$, if $x = a(\theta + sin\theta)$  and $y = a(1-cos\theta)$

**Example 34** Find $\frac{dy}{dx}$, if $x^{\frac{2}{3}} + y^{\frac{2}{3}} = a^{\frac{2}{3}}$

### Exercise 5.6


## Second Order Derivative
Let y = f(x). Then
<p>
\[
\frac{dy}{dx} = f'(x) --------(1)
\]
</p>

If f'(x) is differentiable, differentiate again w.r.t. x:
<p>
\[
\frac{d}{dx}\left(\frac{dy}{dx}\right)=\frac{d^2y}{dx^2}=f''(x)
\]
</p>
Which is called the second order derivative of y w.r.t. x 

The second order derivative is also written as $D^{2}y$ or  y'', or $y_2$ (when y=f(x)).

**Example 35** Find $\frac{d^2y}{dx^2}$ , if y = $x^3 $+ tanx.

**Example 36** If y = Asinx + Bcosx, then prove that $\frac{d^2y}{dx^2} + y = 0.$

**Example 37** If $y = 3e^{2x} + 2e^{3x}$, Prove that $\frac{d^2y}{dx^2} - 5\frac{dy}{dx}+ 6y = 0.$

**Example 38** If $y = sin^{-1}x$, show that $(1-x^2)\frac{d^2y}{dx^2} - x\frac{dy}{dx} = 0.$

### Exercise 5.7
Find second derivatives of standard/composite/inverse‑trig functions and prove simple differential equations satisfied by given forms. 

## Miscellaneous Examples and Exercise

**Example 39** Differentiate w.r.t.x, the following function:

(i) $\sqrt{3x+2} + \frac{1}{\sqrt{2x^2+4}}$

(ii) $log_7(logx)$

**Example 40** Differentiate the following w.r.t. x.

(i) $cos^{-1}(sinx)$

(ii) $tan^{-1}(\frac{sinx}{1+cosx})$

(iii) $sin^{-1}(\frac{2^{x+1}}{1+4^x})$

**Exmaple 41** Find $f^{'}(x)$ if f(x) = $(sinx)^{sinx}$ for all $0 < x < \pi$

**Example 42** For a positive constant a find $\frac{dy}{dx}$, where
<p>
$y = a^{t+\frac{1}{t}}$  and $x = (t + \frac{1}{t})^a$

</p>

**Example 43** Differentiate $sin^{2}x$ w.r.t $e^{cosx}$.

### Miscellaneous Exercise on Chapter 5

## Summary

### Key Topics

**Continuity :**

- A function f is continuous at x = c if $lim_{x \to c} f(x) = f(c)$.

- Sum, difference, product, and quotient of continuous functions remain continuous.

**Differentiability :**

- A function is differentiable if it has a derivative.

- Differentiability implies continuity, but not vice versa (e.g., sharp corners prevent differentiability).

**Derivative Rules :**

- Chain rule, product rule, quotient rule.

- Derivatives of exponential, logarithmic, trigonometric, and parametric functions.

### Theorems and Applications

**Rolle's Theorem :**
<p>
If \(f\) is continuous on \([a, b]\), differentiable on \((a, b)\), and \(f(a) = f(b)\), then \(\exists c \in (a, b)\) such that \(f'(c) = 0\).
</p>

**Mean Value Theorem :**
<p>
Extends Rolle's; \(\exists c\) where \(f'(c) = \frac{f(b) - f(a)}{b - a}\).
</p>

### Other Techniques

- Logarithmic differentiation.

- Second-order derivatives.

- Implicit differentiation.
