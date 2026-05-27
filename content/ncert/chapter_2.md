# Chapter 2: Inverse Trigonometric Functions

> "Mathematics, in general, is fundamentally the science of self-evident things."  
> — Felix Klein

---

# 2.1 Introduction

- The inverse of a function $f$, denoted $f^{-1}$, exists if $f$ is both one-one and onto.
- Many functions (including trigonometric) are not one-one and onto over their natural domains/ranges, so their inverses do not exist.
- This chapter discusses how restricting domain/range allows us to define inverses for trigonometric functions and explores their graphs and properties.
- Inverse trigonometric functions are essential in calculus, science, and engineering.

---

# 2.2 Basic Concepts

Recall the main trigonometric functions and their domains/ranges:

1. $ \sin: \mathbb{R} \to [-1, 1] $

2. $ \cos: \mathbb{R} \to [-1, 1] $

3. $ \tan: \mathbb{R} \setminus \lbrace x = (2n+1)\frac{\pi}{2}, n \in \mathbb{Z}\rbrace \to \mathbb{R} $

4. $ \cot: \mathbb{R} \setminus \lbrace x = n\pi, n \in \mathbb{Z}\rbrace \to \mathbb{R} $

5. $ \sec: \mathbb{R} \setminus \lbrace x = (2n+1)\frac{\pi}{2}, n \in \mathbb{Z}\rbrace \to \mathbb{R} \setminus (-1, 1) $

6. $ \csc: \mathbb{R} \setminus \lbrace x = n\pi, n \in \mathbb{Z}\rbrace \to \mathbb{R} \setminus (-1, 1) $

For a function $f: X \to Y$ invertible (one-one, onto), its inverse $g: Y \to X$ satisfies:
$$
g(f(x)) = x \qquad \text{and} \qquad f(g(y)) = y
$$

To make $\sin$, $\cos$, etc., invertible, restrict their domains:

### Sine Function
- Restrict $x$ to $[-\frac{\pi}{2}, \frac{\pi}{2}]$ so it’s bijective onto $[-1, 1]$.
- Inverse (arc sine) is
  $$
  \sin^{-1}: [-1, 1] \to \left[ -\frac{\pi}{2}, \frac{\pi}{2} \right ]
  $$
- If $y = \sin^{-1} x$, then $x = \sin y$, $y \in [-\frac{\pi}{2}, \frac{\pi}{2}]$

### Cosine Function
- Restrict $x$ to $[0, \pi]$.
- Inverse:
  $$
  \cos^{-1}: [-1, 1] \to [0, \pi]
  $$

### Tangent, Cotangent, Secant, Cosecant
- $$
  \tan^{-1}: \mathbb{R} \to \left( -\frac{\pi}{2}, \frac{\pi}{2} \right )
  $$
- $$
  \cot^{-1}: \mathbb{R} \to (0, \pi)
  $$
- $$
\sec^{-1}: \mathbb{R} \setminus (-1, 1) \to [0, \pi] \setminus \{ \frac{\pi}{2} \}
  $$
- $$
  \csc^{-1}: \mathbb{R} \setminus (-1, 1) \to \left[ -\frac{\pi}{2}, \frac{\pi}{2} \right] \setminus \{0\}
  $$

---

# 2.3 Properties

- If $y = \sin^{-1}x$, then $x = \sin y$ and $y \in \left[ -\frac{\pi}{2}, \frac{\pi}{2} \right]$
- $ \sin(\sin^{-1} x) = x $, for $x \in [-1, 1]$
- $ \sin^{-1}(\sin x) = x $, for $x \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right] $
- Graphs of $y = f(x)$ and $y = f^{-1}(x)$ are mirror images along $y = x$

---

# 2.4 Graphs
### 2.4.1 Trigonometric Functions

Here are the graphs of sine and cosine:

<!-- ![Trig Graph](/static/images/trig_graph.png) -->

<figure>
  <img src="/static/images/trig_graph.png" 
       alt=" sin & cos graph" 
       style="max-width:70%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

Here the graph of tangenet (tanx):

<figure>
  <img src="/static/images/tan_graph.png" 
       alt="tan graph" 
       style="max-width:70%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>


Here the graph of cotangenet (cotx):

<figure>
  <img src="/static/images/cot_graph.png" 
       alt="cot graph" 
       style="max-width:70%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

Here the graph of secant (secx):

<figure>
  <img src="/static/images/sec_graph.png" 
       alt="tan graph" 
       style="max-width:70%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>


Here the graph of cosecant (cosecx):

<figure>
  <img src="/static/images/cosec_graph.png" 
       alt="tan graph" 
       style="max-width:70%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>
---


### 2.4.2 Inverse Trigonometric Functions

Here the graph of Arcsin ($\sin^{-1}x$)

<figure>
  <img src="/static/images/arcsin.png" 
       alt=" $\sin^{-1}x$ graph" 
       style="max-width:70%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

Here the graph of Arccos ($\cos^{-1}x$)

<figure>
  <img src="/static/images/arccos.png" 
       alt=" $\cos^{-1}x$ graph" 
       style="max-width:70%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

Here the graph of Arctan ($\tan^{-1}x$)

<figure>
  <img src="/static/images/arctan.png" 
       alt=" $\tan^{-1}x$ graph" 
       style="max-width:70%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

Here the graph of Arccot ($\cot^{-1}x$)

<figure>
  <img src="/static/images/arccot.png" 
       alt=" $\cot^{-1}x$ graph" 
       style="max-width:70%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>


Here the graph of Arcsec ($\sec^{-1}x$)

<figure>
  <img src="/static/images/arcsec.png" 
       alt=" $\sec^{-1}x$ graph" 
       style="max-width:70%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>


Here the graph of Arccosec ($\csc^{-1}x$)

<figure>
  <img src="/static/images/arccosec.png" 
       alt=" $\cosec^{-1}x$ graph" 
       style="max-width:70%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>


# 2.5 Principal Value Branches Table

| Function | Domain | Range (Principal Value Branch) |
|----------|--------|-------------------------------|
| $y = \sin^{-1} x$ | $[-1, 1]$ | $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ |
| $y = \cos^{-1} x$ | $[-1, 1]$ | $[0, \pi]$ |
| $y = \csc^{-1} x$ | $\mathbb{R}\setminus(-1, 1)$ | $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]\setminus\{0\}$ |
| $y = \sec^{-1} x$ | $\mathbb{R}\setminus(-1, 1)$ | $[0,\pi]\setminus\{\frac{\pi}{2}\}$ |
| $y = \tan^{-1} x$ | $\mathbb{R}$ | $\left(-\frac{\pi}{2},\frac{\pi}{2}\right)$ |
| $y = \cot^{-1} x$ | $\mathbb{R}$ | $(0,\pi)$ |

The value of an inverse trigonometry functions which lies in the range of principal branch is called the principal value of that inverse trigonometry functions.


---

# Examples

**Example 1:**  
Find the principal value of $ \sin^{-1}\left(\frac{1}{\sqrt{2}}\right) $

Solution:  
Let $y = \sin^{-1}\left(\frac{1}{\sqrt{2}}\right)$.  
$ \sin y = \frac{1}{\sqrt{2}} $.  
Principal value is:
$$
y = \frac{\pi}{4}
$$

**Example 2:**  
Find the principal value of $ \cot^{-1}\frac{-1}{\sqrt{3}} $

Solution:  
Let $y = \cot^{-1}\frac{-1}{\sqrt{3}}$  
So $\cot y = \frac{-1}{\sqrt{3}}$  
Principal value is:
$$
y = \frac{2\pi}{3}
$$

---

# 2.6 Important Properties

- $ \sin^{-1}(\sin x) = x $, for $x \in \left[ -\frac{\pi}{2}, \frac{\pi}{2} \right]$
- $ \cos^{-1}(\cos x) = x $, for $x \in [0, \pi]$
- $ \tan^{-1}(\tan x) = x $, for $x \in \left( -\frac{\pi}{2}, \frac{\pi}{2} \right ) $
- For $x \in [-1,1]$, $ \sin[\cos^{-1}x] = \sqrt{1-x^2} $


### Formulas:
- $\sin^{-1}x + \cos^{-1}x =\frac{\pi}{2}, \quad x \in [-1,1]$
- $\tan^{-1}x + \cot^{-1}x =\frac{\pi}{2}, \quad x \in \mathbb{R}$
- $\sec^{-1}x + \csc^{-1}x =\frac{\pi}{2}, \quad |x| \geq 1$
- $\sin^{-1}(-x) = -\sin^{-1}x$
- $\cos^{-1}(-x) = \pi - \cos^{-1}x$
- $\tan^{-1}(-x) = -\tan^{-1}x$
- $\cot^{-1}(-x) = \pi - \cot^{-1}x$
- $\sec^{-1}(-x) = \pi - \sec^{-1}x$
- $\csc^{-1}(-x) = -\csc^{-1}x$
- $\tan^{-1}x + \tan^{-1}y =\tan^{-1}\left(\frac{x+y}{1-xy}\right),  xy < 1$
- $\tan^{-1}x - \tan^{-1}y = \tan^{-1}\left(\dfrac{x-y}{1+xy}\right), \quad xy > -1$
- $\cot^{-1}x + \cot^{-1}y = \cot^{-1}\left(\dfrac{xy-1}{x+y}\right)$
- $\cot^{-1}x = \tan^{-1}\left(\dfrac{1}{x}\right), \quad x>0$
- $\sec^{-1}x = \cos^{-1}\left(\dfrac{1}{x}\right), \quad |x|\ge 1$
- $\csc^{-1}x = \sin^{-1}\left(\dfrac{1}{x}\right), \quad |x|\ge 1$
- $2\tan^{-1}x = \sin^{-1}\left(\dfrac{2x}{1+x^2}\right), \quad x \in \mathbb{R}$
- $2\tan^{-1}x = \cos^{-1}\left(\dfrac{1-x^2}{1+x^2}\right)$
- $2\tan^{-1}x = \tan^{-1}\left(\dfrac{2x}{1-x^2}\right), \quad |x|<1$



---

# Miscellaneous Examples

**Example 3:**  
Show: $ \sin^{-1}(2x\sqrt{1-x^2}) = 2\sin^{-1} x $, for $ -\frac{1}{\sqrt{2}} \leq x \leq \frac{1}{\sqrt{2}} $

Solution:  
Let $x = \sin \theta$.  
$\sin^{-1}(2x\sqrt{1-x^2}) = \sin^{-1}(2\sin\theta\cos\theta) = \sin^{-1}(\sin 2\theta) = 2\theta = 2\sin^{-1}x$

**Example 4:**  
Express $ \tan^{-1} \left( \frac{\cos x}{1-\sin x} \right) $ in simplest form.

Solution:  
$\tan^{-1} \left( \frac{\cos x}{1-\sin x} \right) = \frac{x}{2} - \frac{\pi}{4}$

---

# Exercise 

### exercise 2.1

Find the principal values:
1. $ \sin^{-1}\left(\frac{\sqrt{3}}{2}\right) $
2. $ \cos^{-1}\left(\frac{1}{2}\right) $
3. $ \csc^{-1}(2) $

Write in the simplest form:
- $ \tan^{-1}\left( \frac{\cos x}{1-\sin x} \right) $

Prove:
- $ 3\sin^{-1}x = \sin^{-1}(3x-4x^3),\quad x \in \left[-\frac{1}{2},\frac{1}{2}\right] $


### exercise 2.2



### miscellaneous exercise
---

# Summary

- Domains and principal value branches for inverse trigonometric functions are shown above.
- $ \sin^{-1}x $ is not the same as $ (\sin x)^{-1} = \frac{1}{\sin x} $
- Principal value means value in the main branch.

---

# Historical Note

- The study of trigonometry originated in India with Aryabhata, Brahmagupta, Bhaskara I and II.
- Approaches from India spread to Arabia and later Europe.
- Symbols $ \sin^{-1} x, \cos^{-1} x $ were introduced by John F.W. Herschel (1813).
- Thales (Greek, c.600 BC) tackled height/distance using shadows and ratios.

