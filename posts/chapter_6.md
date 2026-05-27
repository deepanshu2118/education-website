# CHAPTER 5  
## Mathematical Groundwork  
*“Turn the knobs with confidence, not with hope.”*  

---

## 5.1 WHY THIS CHAPTER IS ILLUSTRATED FIRST  
Every machine-learning lecture that begins with a proof loses half the room; every lecture that begins with a picture does not.  
The pages that follow therefore introduce each concept twice: once as a sketch you can eyeball in three seconds, once as notation you can copy into code.  

---

## 5.2 LINEARITY IN ONE GLANCE  
**Fig. 5.1 – The seesaw diagram**  
![Fig 5.1](/static/images/fig5_1_seesaw.png)  

A straight line is a balanced lever:  
\[
y = mx + b
\]  
where *m* is slope (weights), *b* is intercept (bias).  

Take-away: If *m = 0* the lever is flat → the feature *x* is useless.  

---

## 5.3 DISTANCE: THE WORKHORSE METRIC  
**Fig. 5.2 – Flashlight grid (2D)**  
![Fig 5.2](/static/images/fig5_2_flashlight.png)  

The Euclidean norm measures the “cable length” between two points.  

**Table 5.1 – Distance zoo (1-line memory hook)**  

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Formula</th>
      <th>When to remember it</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Euclidean</td><td>√Σ(xᵢ − yᵢ)²</td><td>Default for continuous features</td></tr>
    <tr><td>Manhattan</td><td>Σ |xᵢ − yᵢ|</td><td>Grid cities, sparse counts</td></tr>
    <tr><td>Mahalanobis</td><td>√[(x−y)ᵀ Σ⁻¹ (x−y)]</td><td>Correlated features, elliptic clusters</td></tr>
    <tr><td>Cosine</td><td>1 − (x·y)/(‖x‖‖y‖)</td><td>Text / embedding similarity</td></tr>
    <tr><td>Edit (Levenshtein)</td><td>dynamic prog.</td><td>String matching</td></tr>
    <tr><td>Dynamic Time Warp</td><td>stretch-allowed</td><td>Time-series alignment</td></tr>
  </tbody>
</table>  

---

## 5.4 AVERAGES & SPREADS: THE CLASS PHOTO  
**Fig. 5.3 – 30 students lined up by height**  
![Fig 5.3](f/static/images/fig5_3_height_line.png)  

Mean = balancing point.  
Median = middle student.  
Mode = most frequent height.  

**Fig. 5.4 – Same photo with error bars ±1 SD**  
![Fig 5.4](/static/images/fig5_4_errorbar.png)  

Rule of thumb for bell-shaped data: 68–95–99.7 rule.  

---

## 5.5 PROBABILITY FOUNDATIONS  
**Fig. 5.5 – The raffle jar**  
![Fig 5.5](/static/images/fig5_5_raffle_strip.png)  

Probability rules:  
- Joint: P(A ∩ B)  
- Marginal: P(A)  
- Conditional: P(A|B)  

**Fig. 5.6 – Venn diagram of joint/marginal/conditional**  
![Fig 5.6](/static/images/fig5_6_venn.png)  

**Fig. 5.7 – Probability tree cartoon**  
![Fig 5.7](/static/images/fig5_7_bayes_tree.png)  

---

## 5.6 DISTRIBUTIONS: SHAPE → ALGORITHM CHOICE  
**Fig. 5.8 – Distribution cheat-sheet cards**  
![Fig 5.8](/static/images/fig5_8_dist_cards.png)  

**Chart 5.1 – Quick-picker flow**  
![Chart 5.1](/static/images/chart5_1_dist_picker.png)  

Gaussian → linear models  
Bernoulli → logistic regression  
Poisson → event counts  
Power-law → log-transform first  

---

## 5.7 INFORMATION THEORY IN ONE PICTURE  
**Fig. 5.9 – Surprise bars**  
![Fig 5.9](/static/images/fig5_9_surprise_bar.png)  

- Surprise = −log₂ p  
- Entropy = average surprise  
- Cross-entropy = distance between two distributions  

---

## 5.8 CALCULUS: THE SLOPE HUNT  
**Fig. 5.10 – Hill climbing in fog**  
![Fig 5.10](/static/images/fig5_10_hill_climb.png)  

- ∂L/∂w is gradient → steepest descent direction.  

**Fig. 5.11 – Chain rule diagram**  
![Fig 5.11](/static/images/fig5_11_chain_bowls.png)  

---

## 5.9 LINEAR ALGEBRA: THE LEGO BOX  
**Fig. 5.12 – Vector, matrix, tensor**  
![Fig 5.12](/static/images/fig5_12_lego_box.png)  

**Fig. 5.13 – Dot product projection**  
![Fig 5.13](/static/images/fig5_13_dot_projection.png)  

**Fig. 5.14 – Matrix multiplication (row × column pipes)**  
![Fig 5.14](/static/images/fig5_14_mat_pipes.png)  

**Fig. 5.15 – Eigenvector**  
![Fig 5.15](/static/images/fig5_15_eigen_arrow.png)  

**Fig. 5.16 – SVD rotate-stretch-rotate**  
![Fig 5.16](/static/images/fig5_16_svd_cartoon.png)  

**Table 5.2 – Memory matrix**  

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th>Geometric feel</th>
      <th>ML use</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Ax = b</td><td>transform x</td><td>linear regression</td></tr>
    <tr><td>A⁻¹</td><td>undo transform</td><td>solve equations</td></tr>
    <tr><td>det(A)</td><td>volume scaler</td><td>invertibility test</td></tr>
    <tr><td>eigen(A)</td><td>principal directions</td><td>PCA, spectral clustering</td></tr>
    <tr><td>SVD</td><td>best low-rank approx</td><td>semantic analysis, compression</td></tr>
  </tbody>
</table>  

---

## 5.10 OPTIMISATION LANDSCAPE  
**Fig. 5.17 – 3D contour map**  
![Fig 5.17](/static/images/fig5_17_landscapes.png)  

Convex = single valley  
Non-convex = multiple valleys  

**Chart 5.2 – Optimiser cheat-card**  
![Chart 5.2](/static/images/chart5_2_distance_table.png)  

---

## 5.11 GRAPH THEORY PRIMER  
**Fig. 5.18 – Nodes and edges**  
![Fig 5.18](/static/images/fig5_18_graph_intro.png)  

**Fig. 5.19 – Laplacian spectral embedding**  
![Fig 5.19](/static/images/fig5_19_spectral_embed.png)  

---

## 5.12 CAPACITY MEASURES AT A GLANCE  
**Fig. 5.20 – VC-dimension ruler**  
![Fig 5.20](/static/images/fig5_20_vc_ruler.png)  

Rule of thumb: training samples > 10 × VC.  

---

## 5.13 BIAS–VARIANCE BREAK-DOWN VISUALISED  
**Fig. 5.21 – Four dartboards**  
![Fig 5.21](/static/images/fig5_21_dartboards.png)  

Low bias + low variance = bull’s-eye  
High bias = systematic error  
High variance = noisy scatter  

---

## 5.14 RANDOM VARIABLES & LAW OF LARGE NUMBERS  
**Fig. 5.22 – Simulation of convergence**  
![Fig 5.22](/static/images/fig5_22_lln_demo.png)  

As N grows, sample mean converges to expectation.  

---

## 5.15 BOOTSTRAP & CONFIDENCE INTERVALS  
**Fig. 5.23 – Resampling histogram**  
![Fig 5.23](/static/images/fig5_23_bootstrap_bar.png)  

Vertical band = 95% CI.  

---

## 5.16 FROM PICTURE TO CODE: CHEAT-SHEET SUMMARY  
**Table 5.3 – One-sentence translation**  

<table>
  <thead>
    <tr>
      <th>Concept</th>
      <th>Picture meaning</th>
      <th>NumPy one-liner</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Mean</td><td>balance point</td><td>x.mean()</td></tr>
    <tr><td>Dot product</td><td>projection length</td><td>x @ y</td></tr>
    <tr><td>Matrix multiply</td><td>linear map</td><td>A @ x</td></tr>
    <tr><td>Euclidean distance</td><td>straight-line</td><td>np.linalg.norm(x-y)</td></tr>
    <tr><td>Covariance matrix</td><td>ellipse shape</td><td>np.cov(X.T)</td></tr>
    <tr><td>Eigenvalues</td><td>stretch factors</td><td>np.linalg.eigvals(S)</td></tr>
    <tr><td>SVD</td><td>best rank-k approx</td><td>U, s, Vt = np.linalg.svd(A)</td></tr>
    <tr><td>Gradient</td><td>steepest rise</td><td>np.gradient(f)</td></tr>
    <tr><td>Softmax</td><td>turn scores into probs</td><td>np.exp(z)/np.sum(np.exp(z))</td></tr>
  </tbody>
</table>  

---

## 5.17 CHECKLIST BEFORE TURNING THE PAGE  
Before you proceed, ensure you can:  

- Sketch the bias–variance dartboard and label quadrants.  
- Explain the chain rule.  
- Translate mean, dot product, eigenvector into NumPy.  
- Recognise distributions and their matching algorithms.  

✅ Once all boxes are ticked, your mathematical foundation is ready.  

