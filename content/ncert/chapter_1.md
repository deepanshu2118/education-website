<!-- # Chapter 1: Relations and Functions

> *“There is no permanent place in the world for ugly mathematics...”* — G. H. Hardy  

---

# 1.1 Introduction
Relations and functions, along with the ideas of domain, co-domain, and range, were introduced in **Class XI**.  
A relation in mathematics represents a recognizable connection between elements of two sets.  

**Example:**  
Let  
- **A** = set of students of Class XII  
- **B** = set of students of Class XI  

Possible relations from A to B:  
- (a, b): a is the brother of b  
- (a, b): a is older than b  
- (a, b): a lives in the same locality as b  

Formally, a relation **R from A to B** is a subset of $\( A \times B \)$.  
If $\((a, b) \in R\)$, then we say **a R b**.

---

# 1.2 Types of Relations

### 🔹 Empty Relation
No element of \(A\) is related to any element of \(A\).  

$$
R = \varnothing \subseteq A \times A
$$

---

### 🔹 Universal Relation
Every element of \(A\) is related to every element of \(A\).  

$$
R = A \times A
$$

These are sometimes called *trivial relations*.

---

### 🔹 Reflexive, Symmetric, and Transitive Relations
- **Reflexive:**  

$$
(a,a) \in R \quad \forall a \in A
$$  

- **Symmetric:**  

$$
(a,b) \in R \implies (b,a) \in R
$$  

- **Transitive:**  

$$
(a,b), (b,c) \in R \implies (a,c) \in R
$$  

A relation that is **reflexive, symmetric, and transitive** is called an **equivalence relation**.

**Example:**  
- Congruence of triangles → equivalence relation.  
- "Perpendicular lines" → symmetric, but not reflexive or transitive.  

---

# 1.3 Types of Functions

- **One-One (Injective):** Distinct inputs → distinct outputs.  
- **Onto (Surjective):** Every element in the co-domain has a pre-image.  
- **Bijective:** Both one-one and onto.  

**Examples:**  
- $f(x) = 2x, f: \mathbb{R} \to \mathbb{R} $ → one-one and onto.  
-  $f(x) = x^2, f: \mathbb{R} \to \mathbb{R}$  → neither one-one nor onto.  

---

# 1.4 Composition of Functions
If  

$$
f: A \to B, \quad g: B \to C
$$  

then the composition is  

$$
g \circ f: A \to C, \quad (g \circ f)(x) = g(f(x))
$$

---

# 1.5 Invertible Functions
A function $\( f: X \to Y \)$ is invertible if there exists $\( g: Y \to X \)$ such that:  

$$
g \circ f = I_X \quad \text{and} \quad f \circ g = I_Y
$$

Invertible functions must be **bijective**.

---

# 📘 Examples
- Relation of integers with difference divisible by 2 → equivalence relation.  
- Function $\( f(x) = \sin x \)$, $\( g(x) = \cos x \)$ → both one-one, but $\( f+g \)$ not one-one.  

---

# 📝 Exercises

### Exercise 1.1 (Relations)
1. Determine whether the following are reflexive, symmetric, transitive:  
   -  

   $$
   R = \{(x,y): 3x - y = 0\}, \quad A = \{1,2,\dots,14\}
   $$  

   -  

   $$
   R = \{(x,y): y = x+5, \; x < 4\}, \quad x \in \mathbb{N}
   $$  

   -  

   $$
   R = \{(x,y): y \text{ divisible by } x\}, \quad A = \{1,2,\dots,6\}
   $$  

2. Prove/disprove:  

$$
R = \{(a,b): a \leq b^2\}, \quad a,b \in \mathbb{R}
$$  

is reflexive, symmetric, transitive.

---

### Exercise 1.2 (Functions)
1. Prove  

$$
f(x) = \frac{1}{x}, \quad x \neq 0
$$  

is bijective on $\(\mathbb{R}^*\)$.  

2. Check injectivity/surjectivity of:  
   - $ f(x) = x^2, f: \mathbb{N} \to \mathbb{N} $  
   - $f(x) = x^3, f: \mathbb{Z} \to \mathbb{Z}$  

3. Prove the **Greatest Integer Function**  

$$
f(x) = \lfloor x \rfloor
$$  

is neither one-one nor onto.  

---

# ✅ Summary
- Relations: empty, universal, reflexive, symmetric, transitive, equivalence.  
- Functions: one-one, onto, bijective.  
- Bijective functions are invertible.  
- Composition:  

$$
(g \circ f)(x) = g(f(x))
$$

---

# 📖 Historical Note
The concept of **function** evolved from **Descartes (1637)**, **Leibnitz (1673)**, **Euler (1734)** to **Dirichlet (1805–1859)**. Today, the set-theoretic definition by **Cantor (1845–1918)** is universally used.  

--- -->



# Chapter 1: Relations and Functions

> "There is no permanent place in the world for ugly mathematics ... . It may be very hard to define mathematical beauty but that is just as true of beauty of any kind, we may not know quite what we mean by a beautiful poem, but that does not prevent us from recognising one when we read it."
> — G. H. Hardy

# 1.1 Introduction

Recall that the notion of relations and functions, domain, co-domain and range have been introduced in earlier classes. The concept of relation in mathematics comes from the English meaning, i.e., two objects or quantities are related if there is a recognisable link between them.

Let $A$ be the set of students of Class XII and $B$ be the set of Class XI in a school. 

**Example relations from $A$ to $B$ are:**

1. $$ 
R= \lbrace (a, b) \in A \times B \mid a \text{ is brother of } b \rbrace
 $$
2. $$ R= \lbrace (a, b) \in A \times B \mid a \text{ is sister of } b \rbrace $$
3. $$ R= \lbrace (a, b) \in A \times B \mid \text{age of } a > \text{age of } b \rbrace $$
4. $$ R= \lbrace (a, b) \in A \times B \mid \text{marks of } a < \text{marks of } b \rbrace $$
5. $$ R= \lbrace (a, b) \in A \times B \mid \text{same locality} \rbrace $$

Mathematically, a relation $R$ from $A$ to $B$ is an arbitrary subset of $A \times B$. If $(a, b) \in R$, we say $a$ is related to $b$ under $R$.

---

# 1.2 Types of Relations

A relation in set $A$ is a subset of $A \times A$. The empty set $(\varnothing)$ and $A \times A$ are two extreme relations.

**Definition 1** (Empty Relation): A relation R in a set A is called empty relation, if no element of A is related to any element of A.  

$$
R = \varnothing \subseteq A \times A
$$

**Definition 2** (Universal Relation): A relation R in a set A is called universal relation, if each element of A is related to every element of A.

$$
R = A \times A
$$

Empty and universal relations are sometimes called trivial relations.

**Example:** If $A$ is all students in a boys' school, the relation $R = \lbrace(a, b) : a \text{ is sister of } b\rbrace$ is empty, as no student is sister of any other; $R' = \lbrace(a, b) : |\text{height}(a) - \text{height}(b)| < 3\rbrace$ is universal for all heights differing by less than $3$ meters.

### Types and Properties

A relation R in a set A is called

- Reflexive: $(a, a) \in R,  ~\forall~ a \in A$
- Symmetric: $(a_1, a_2) \in R \implies (a_2, a_1) \in R$
- Transitive: $(a_1, a_2) \in R$ and $(a_2, a_3) \in R \implies (a_1, a_3) \in R$

**Equivalence Relation:** Reflexive, symmetric, and transitive.

**Equivalence Classes:** An equivalence relation partitions a set into mutually disjoint subsets $A_i$ (classes).

(i) all elements of $A_i$ are related to each other, for all i.

(ii) no element of $A_i$ is related to any element of $A_j$, $i \neq j$

(iii) $\cup A_j$ = X and $A_i \cap A_j = \varnothing $, $ i \neq j$

---

# 1.3 Types of Functions

A function $f : X \rightarrow Y$ is:

**One-One (Injective):**  defined to be one-one, if the images of distinct elements of X under f are distinct. i.e.

$$
f(x_1) = f(x_2) \implies x_1 = x_2 ~\forall~ x_1, x_2 \in X
$$

**Onto (Surjective):** said to be onto, if every element of Y is the images of some element of X under f, i.e.

$$
\forall\, y \in Y,\ \exists\, x \in X : f(x) = y
$$

**Bijective:** A function $f : X \rightarrow Y$ is said to be one-one and onto (or bijective),if f is both one-one and onto.

**Examples:**

1. $f : \mathbb{N} \rightarrow \mathbb{N},\ f(x) = 2x$ is one-one but not onto.
2. $f : \mathbb{R} \rightarrow \mathbb{R},\ f(x) = 2x$ is bijective.

For finite sets, injectivity and surjectivity are equivalent; for infinite sets, this may not be true.

---

# 1.4 Composition and Invertible Functions

**Composition:** If $f : A \rightarrow B$ and  $g : B \rightarrow C$ be two functions. Then the composition of f and g denoted by $g \circ f$, is defined as the function $g \circ f : A \rightarrow C $ given by

$$
(g \circ f)(x) = g(f(x)),\quad \forall~x \in A
$$

**Invertible:** $f : X \rightarrow Y$ is invertible if there exists $g : Y \rightarrow X$ such that

$$
g \circ f = I_X \quad\text{and}\quad f \circ g = I_Y
$$

The function g is called the inverse of f and is denoted by $f^{-1}$.

where $I_X$ and $I_Y$ are the identity functions on $X$ and $Y$.

---

# Chapter Summary

- **Empty relation:**
  $$
  R = \varnothing \subseteq X \times X
  $$
- **Universal relation:**
  $$
  R = X \times X
  $$
- **Reflexive:** $(a, a) \in R,~ \forall a \in X$
- **Symmetric:** $(a, b) \in R \implies (b, a) \in R$
- **Transitive:** $(a, b) \in R$ and $(b, c) \in R \implies (a, c) \in R$
- **Equivalence class:** $[a]$ containing $a$ is all $b$ related to $a$
- **Injective function:** $f : X \rightarrow Y$ is injective if
  $$
  f(x_1) = f(x_2) \implies x_1 = x_2
  $$
- **Surjective function:** $f : X \rightarrow Y$ is surjective if
  $$
  \forall y \in Y,~~ \exists x \in X:~ f(x) = y
  $$
- **Bijective function:** $f$ is both injective and surjective.
- For finite $X$, one-one implies onto and vice versa.

---
# Exercise: 1.1


---

# Excercise: 1.2



---


# Miscellaneous Excercise: 



---

# Historical Note

The concept of function evolved from Descartes (1637) to Dirichlet, and the set-theoretic definition was completed by Cantor. The word 'function' and related notations developed over centuries, with contributions from Leibnitz, Euler, Lagrange, and others.

