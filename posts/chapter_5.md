# Chapter 5: Mathematical Groundwork  
---
## WHY THIS CHAPTER IS ILLUSTRATED FIRST  

Every machine-learning lecture that begins with a proof loses half the room; every lecture that begins with a picture does not.  

The pages that follow therefore introduce each concept twice:  
- once as a sketch you can eyeball in three seconds,  
- once as notation you can copy into code.  

Feel free to linger on whichever version feels real and skip the other without guilt.  

---

## LINEARITY IN ONE GLANCE  

**Fig. 5.1 The seesaw diagram**  
<figure>
  <img src="/static/images/fig5_1_seesaw.png" 
       alt=" The seesaw diagram(figure 5.1)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

A straight line is a balanced lever: move 1 unit on x, move *m* units on y. The number *m* is the only knob the learner can turn.  

Mathematically:  

\[
y = m x + b
\]  

where:  

- \(x ∈ ℝ^d\) (often d = 1 for drawings)  
- \(m ∈ ℝ^d\) (weights, coefficients, slopes)  
- \(b ∈ ℝ\) (bias, intercept, offset)  

**Take-away**: If *m = 0* the lever is flat → the feature *x* is useless for predicting *y*.  

---

##  DISTANCE: THE WORKHORSE METRIC  

**Fig. 5.2 Flashlight grid (2-D)**  
<figure>
  <img src="/static/images/fig5_2_flashlight.png" 
       alt=" Flashlight grid (2-D)(figure 5.2)" 
       style="max-width:40%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

Shine two torches on the floor; the cable length between them is the Euclidean norm.  

Add a third dimension (ceiling) and the cable still obeys Pythagoras:  

\[
‖x − x′‖₂ = \sqrt{(x₁ − x′₁)² + … + (x_d − x′_d)²}
\]  

<div class="table-container">
  <h3>Table 5.1 Distance zoo (1-line memory hook)</h3>
  <table>
    <thead>
      <tr>
        <th>Name</th>
        <th>Formula</th>
        <th>When to remember it</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Euclidean</td>
        <td>√Σ(xᵢ − yᵢ)²</td>
        <td>Default for continuous features</td>
      </tr>
      <tr>
        <td>Manhattan</td>
        <td>Σ |xᵢ − yᵢ|</td>
        <td>Grid cities, sparse counts</td>
      </tr>
      <tr>
        <td>Mahalanobis</td>
        <td>√[(x−y)ᵀ Σ⁻¹ (x−y)]</td>
        <td>Correlated features, elliptic clusters</td>
      </tr>
      <tr>
        <td>Cosine</td>
        <td>1 − (x·y)/(‖x‖‖y‖)</td>
        <td>Text / embedding similarity</td>
      </tr>
      <tr>
        <td>Edit (Levenshtein)</td>
        <td>dynamic prog.</td>
        <td>String matching</td>
      </tr>
      <tr>
        <td>Dynamic Time Warp</td>
        <td>stretch-allowed</td>
        <td>Time-series alignment</td>
      </tr>
    </tbody>
  </table>
</div>

<style>
  .table-container {
    margin: 20px 0;
    font-family: Arial, sans-serif;
  }
  .table-container h3 {
    margin-bottom: 10px;
    color: #333;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    border: 1px solid #ddd;
  }
  th, td {
    border: 1px solid #ddd;
    padding: 10px 14px;
    text-align: left;
    font-size: 15px;
  }
  th {
    background-color: #f5f5f5;
    font-weight: bold;
  }
  tr:nth-child(even) {
    background-color: #fafafa;
  }
  tr:hover {
    background-color: #f1f1f1;
  }
</style>

<figure>
  <img src="/static/images/chart5_2_distance_table.png" 
       alt=" Distance-metrics cheat-sheet (chart 5.1)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>


---

## AVERAGES & SPREADS: THE CLASS PHOTO  

**Fig. 5.3 30 students lined up by height**  

<figure>
  <img src="/static/images/fig5_3_height_line.png" 
       alt=" 30 students lined up by height(figure 5.3)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>


- Mean = balancing point of the seesaw.  
- Median = the 15th student (robust to a giant on stilts).  
- Mode = the most frequent height.  
- Variance = average squared distance from the mean.  
- Standard deviation = √variance (same units as data).  

**Fig. 5.4 Same photo with error bars ±1 SD**  

<figure>
  <img src="/static/images/fig5_4_errorbar.png" 
       alt=" Same photo with error bars ±1 SD (figure 5.4)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

Rule-of-thumb for bell-shaped data:  
- ≈ 68 % inside 1 SD,  
- 95 % inside 2 SD,  
- 99.7 % inside 3 SD.  

---

## 5.5 PROBABILITY FOUNDATIONS  

**Fig. 5.5 The raffle jar: 100 tickets, 3 winners**  

<figure>
  <img src="/static/images/fig5_5_raffle_strip.png" 
       alt=" The raffle jar (figure 5.5)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

\[
P(win) = \frac{3}{100} = 0.03
\]  

**Joint, marginal, conditional in one Venn (Fig. 5.6)**  
<figure>
  <img src="/static/images/fig5_6_venn.png" 
       alt=" Joint, marginal, conditional in one Venn (figure 5.6)" 
       style="max-width:40%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

- \(P(A ∩ B) =\) joint  
- \(P(A) =\) marginal  
- \(P(A|B) = \frac{joint}{P(B)}\)  (Bayes’ door-opener)  

Bayes re-arranged:  

\[
P(B|A) = \frac{P(A|B) \cdot P(B)}{P(A)}
\]  

**Memorise**: the tree cartoon (Fig. 5.7) – branches multiply, leaves add.  
<figure>
  <img src="/static/images/fig5_7_bayes_tree.png" 
       alt=" Memorise the tree cartoon (figure 5.7)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

---

## 5.6 DISTRIBUTIONS: SHAPE → ALGORITHM CHOICE  

**Fig. 5.8 Distribution cheat-sheet cards**  

<figure>
  <img src="/static/images/fig5_8_dist_cards.png" 
       alt=" Distribution cheat-sheet cards (figure 5.8)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

- Gaussian → linear models, least-squares, Central Limit Theorem  
- Bernoulli → logistic regression, cross-entropy  
- Multinomial → naive Bayes text classifiers  
- Poisson → event counts, arrival rates  
- Exponential → time-between-events  
- Power-law → long-tail, log-transform first  

**Chart 5.1 Quick-picker flow**  

<figure>
  <img src="/static/images/chart5_1_dist_picker.png" 
       alt=" Quick-picker flow (chart 5.1)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

- start → continuous? → symmetric? → Gaussian  
- ↓ no → skewed → log-normal / Box-Cox  
- count → Poisson / negative-binomial  
- binary → Bernoulli  

---

## 5.7 INFORMATION THEORY IN ONE PICTURE  

**Fig. 5.9 Surprise bars: event probability vs. “wow” length**  

<figure>
  <img src="/static/images/fig5_9_Surprise_bar.png" 
       alt=" Surprise bars: event probability vs. “wow” length (figure 5.9)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

- Surprise = −log₂ p (bits)  
- Entropy = average surprise = \(H = −Σ p log₂ p\)  
- Cross-entropy = distance between two surprise tables → loss function for classifiers.  

---

## 5.8 CALCULUS: THE SLOPE HUNT  

**Fig. 5.10 Hill-climbing in fog**  
<figure>
  <img src="/static/images/fig5_10_hill_climb.png" 
       alt=" Hill-climbing in fog (figure 5.10)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

- \(\partial L / \partial w\) = compass direction that lowers loss fastest.  
- Chain rule = read-map-compass in multi-layer terrain .

<figure>
  <img src="/static/images/fig5_11_chain_bowls.png" 
       alt=" Hill-climbing in fog (figure 5.11)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

- Hessian = curvature → bowl vs. saddle.  

---

## 5.9 LINEAR ALGEBRA: THE LEGO BOX  

**Fig. 5.12 Vector as arrow, matrix as grid, tensor as Rubik cube**  
<figure>
  <img src="/static/images/fig5_12_lego_box.png" 
       alt="Vector as arrow, matrix as grid, tensor as Rubik cube (figure 5.12)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

Key pictures:  
- Dot-product = projection length 

<figure>
  <img src="/static/images/fig5_13_dot_projection.png" 
       alt=" (figure 5.13)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

- Matrix multiplication = row-times-column pipes (Fig. 5.14)  

<figure>
  <img src="/static/images/fig5_14_mat_pipes.png" 
       alt=" (figure 5.14)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

- Eigenvector = direction untouched by transformation (Fig. 5.15)  

<figure>
  <img src="/static/images/fig5_15_eigen_arrow.png" 
       alt=" (figure 5.15)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

- SVD = rotate-stretch-rotate (Fig. 5.16)  

<figure>
  <img src="/static/images/fig5_16_svd_cartoon.png" 
       alt=" (figure 5.16)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

<div class="table-container">
  <h3>Table 5.2 Memory matrix</h3>
  <table>
    <thead>
      <tr>
        <th>Operation</th>
        <th>Geometric feel</th>
        <th>ML use</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Ax = b</td>
        <td>transform x</td>
        <td>linear regression</td>
      </tr>
      <tr>
        <td>A⁻¹</td>
        <td>undo transform</td>
        <td>solve normal equations</td>
      </tr>
      <tr>
        <td>det(A)</td>
        <td>volume scaler</td>
        <td>decide if invertible</td>
      </tr>
      <tr>
        <td>eigen(A)</td>
        <td>principal directions</td>
        <td>PCA, spectral clustering</td>
      </tr>
      <tr>
        <td>SVD</td>
        <td>best low-rank approx</td>
        <td>semantic analysis, compression</td>
      </tr>
    </tbody>
  </table>
</div>

<style>
  .table-container {
    margin: 20px 0;
    font-family: Arial, sans-serif;
  }
  .table-container h3 {
    margin-bottom: 10px;
    color: #333;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    border: 1px solid #ddd;
  }
  th, td {
    border: 1px solid #ddd;
    padding: 10px 14px;
    text-align: left;
    font-size: 15px;
  }
  th {
    background-color: #f5f5f5;
    font-weight: bold;
  }
  tr:nth-child(even) {
    background-color: #fafafa;
  }
  tr:hover {
    background-color: #f1f1f1;
  }
</style>

---

## 5.10 OPTIMISATION LANDSCAPE  

**Fig. 5.17 3-D contour map: loss vs. two weights**  

<figure>
  <img src="/static/images/fig5_17_landscapes.png" 
       alt=" 3-D contour map: loss vs. two weights(figure 5.17)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

- Convex = single valley → any downhill path reaches bottom.  
- Non-convex = multiple valleys → algorithm may stop in sub-optimal crater.  

**Chart 5.3 Optimiser cheat-card**  

<figure>
  <img src="/static/images/chart5_3_optimiser_card.png" 
       alt=" 3-D contour map: loss vs. two weights(figure 5.17)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

- Batch GD – smooth, slow  
- SGD – noisy, fast  
- Momentum – heavy ball rolls past potholes  
- AdaGrad – per-feature learning rate (good for sparse text)  
- RMSprop – decaying average of squared grads  
- Adam – momentum + RMSprop (default in labs)  
- L-BFGS – second-order approximation; batch only  

---

## 5.11 GRAPH THEORY PRIMER  

**Fig. 5.18 Nodes = entities, edges = relations**  

<figure>
  <img src="/static/images/fig5_18_graph_intro.png" 
       alt=" (figure 5.18)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

- Adjacency matrix = square 0/1 table; degree = row sum.  
- Walk = sequence of edges; path = no repeated nodes.  
- Spectral clustering = embed nodes via eigenvectors of Laplacian (Fig. 5.19).  

<figure>
  <img src="/static/images/fig5_19_spectral_embed.png" 
       alt=" (figure 5.19)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

---

## 5.12 CAPACITY MEASURES AT A GLANCE  

**Fig. 5.20 VC-dimension ruler**  

<figure>
  <img src="/static/images/fig5_20_vc_ruler.png" 
       alt=" VC-dimension ruler(figure 5.20)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

- 2-D linear classifier → VC = 3  
- Depth-d decision tree → VC ≈ 2^d  
- Neural net with W weights → VC ≈ W log W  

**Rule of thumb**:  
“Keep training samples > 10 × VC for over-fit risk < 5 %.”  

---

## 5.13 BIAS–VARIANCE BREAK-DOWN VISUALISED  

**Fig. 5.21 Four dartboards**  

<figure>
  <img src="/static/images/fig5_21_dartboards.png" 
       alt=" Four dartboards(figure 5.21)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

- Low bias / low variance – bull’s-eye  
- High bias – tight cluster off-centre  
- High variance – scattered around centre  
- High bias + high variance – scattered off-centre  

**Take-away**: you can’t reduce both to zero; noise is irreducible.  

---

## 5.14 RANDOM VARIABLES & THE LAW OF LARGE NUMBERS  

**Simulation Fig. 5.22**  

<figure>
  <img src="/static/images/fig5_22_lln_demo.png" 
       alt=" (figure 5.22)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

- Flip a coin 10 000 times → running mean converges to 0.5.  
- Same chart for die rolls, Gaussian draws, Poisson arrivals.  

**Message**: expect simulation stability only after “large” N.  

---

## 5.15 BOOTSTRAP & CONFIDENCE INTERVALS  

**Fig. 5.23 Resample-with-replacement**  

<figure>
  <img src="/static/images/fig5_23_bootstrap_bar.png" 
       alt=" (figure 5.23)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

- Resample 1000 times → histogram of any statistic.  
- Vertical band = 95 % confidence interval (percentile method).  
- No maths required beyond sorting a list.  

---

## 5.16 FROM PICTURE TO CODE: CHEAT-SHEET SUMMARY  

<div class="table-container">
  <h3>Table 5.3 One-sentence translation</h3>
  <table>
    <thead>
      <tr>
        <th>Concept</th>
        <th>Picture meaning</th>
        <th>NumPy one-liner</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Mean</td>
        <td>balance point</td>
        <td>x.mean()</td>
      </tr>
      <tr>
        <td>Dot product</td>
        <td>projection length</td>
        <td>x @ y</td>
      </tr>
      <tr>
        <td>Matrix multiply</td>
        <td>linear map</td>
        <td>A @ x</td>
      </tr>
      <tr>
        <td>Euclidean distance</td>
        <td>straight-line</td>
        <td>np.linalg.norm(x-y)</td>
      </tr>
      <tr>
        <td>Covariance matrix</td>
        <td>ellipse shape</td>
        <td>np.cov(X.T)</td>
      </tr>
      <tr>
        <td>Eigenvalues</td>
        <td>stretch factors</td>
        <td>np.linalg.eigvals(S)</td>
      </tr>
      <tr>
        <td>SVD</td>
        <td>best rank-k approx</td>
        <td>U, s, Vt = np.linalg.svd(A)</td>
      </tr>
      <tr>
        <td>Gradient</td>
        <td>steepest rise</td>
        <td>np.gradient(f)</td>
      </tr>
      <tr>
        <td>Softmax</td>
        <td>turn scores into probs</td>
        <td>np.exp(z)/np.sum(np.exp(z))</td>
      </tr>
    </tbody>
  </table>
</div>

<style>
  .table-container {
    margin: 20px 0;
    font-family: Arial, sans-serif;
  }
  .table-container h3 {
    margin-bottom: 10px;
    color: #333;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    border: 1px solid #ddd;
  }
  th, td {
    border: 1px solid #ddd;
    padding: 10px 14px;
    text-align: left;
    font-size: 15px;
  }
  th {
    background-color: #f5f5f5;
    font-weight: bold;
  }
  tr:nth-child(even) {
    background-color: #fafafa;
  }
  tr:hover {
    background-color: #f1f1f1;
  }
</style>
---

## 5.17 CHECKLIST BEFORE TURNING THE PAGE  

Before you proceed, ensure you can:  
- Sketch the bias–variance dartboard and label each quadrant.  
- Explain why the chain rule is needed when a loss function is nested.  
- Translate “mean”, “dot product”, and “eigenvector” into one NumPy call each.  
- Look at a distribution plot and name the algorithm family that usually assumes it.  

✅ Once every box is ticked, the mathematical groundwork is solid; we can now turn the knobs with confidence, not with hope.  

