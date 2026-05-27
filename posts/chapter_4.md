
# Chapter 4: Data – The Raw Clay of Machine Learning  

*"Garbage in, gospel out is not a thing."*  

---

## 4.1 ALCHEMY STARTS WITH DIRT  
A medieval alchemist needed pure mercury before he could dream of gold.  
Your mercury is **data**—row upon row of facts, measurements, clicks, pixels, vibrations, words.  

- Impure mercury exploded laboratories.  
- Impure data explodes budgets.  

This chapter turns the spotlight away from clever algorithms and onto the silent, unglamorous hero of every successful project: the dataset itself.  

---

## 4.2 THE DATA LIFECYCLE IN ONE GLANCE  
Think of data as moving along a **conveyor belt**:  

<div style="text-align:center; margin: 20px 0;">
<?xml version="1.0" encoding="UTF-8"?>
<svg width="600" height="140" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#4CAF50"/>
      <stop offset="100%" stop-color="#2E7D32"/>
    </linearGradient>
  </defs>
  <!-- boxes -->
  <rect x="0" y="40" width="75" height="40" fill="url(#grad)" rx="4"/>
  <rect x="85" y="40" width="75" height="40" fill="#FFC107" rx="4"/>
  <rect x="170" y="40" width="75" height="40" fill="#FF9800" rx="4"/>
  <rect x="255" y="40" width="75" height="40" fill="#F44336" rx="4"/>
  <rect x="340" y="40" width="75" height="40" fill="#9C27B0" rx="4"/>
  <rect x="425" y="40" width="75" height="40" fill="#3F51B5" rx="4"/>
  <rect x="510" y="40" width="75" height="40" fill="#607D8B" rx="4"/>
  <!-- arrows -->
  <path d="M75 60h10m5 0l-5-5 5 5-5 5" stroke="#333" fill="none"/>
  <path d="M160 60h10m5 0l-5-5 5 5-5 5" stroke="#333" fill="none"/>
  <!-- labels -->
  <text x="37.5" y="30" text-anchor="middle" font-size="12" fill="#333">RAW</text>
  <text x="122.5" y="30" text-anchor="middle" font-size="12" fill="#333">CLEAN</text>
  <text x="207.5" y="30" text-anchor="middle" font-size="12" fill="#333">ENRICH</text>
  <text x="292.5" y="30" text-anchor="middle" font-size="12" fill="#333">STORE</text>
  <text x="377.5" y="30" text-anchor="middle" font-size="12" fill="#333">SERVE</text>
  <text x="462.5" y="30" text-anchor="middle" font-size="12" fill="#333">MONITOR</text>
  <text x="547.5" y="30" text-anchor="middle" font-size="12" fill="#333">RETIRE</text>
  <!-- warning icons -->
  <polygon points="55,10 60,0 65,10" fill="#FF9800"/>
  <polygon points="140,10 145,0 150,10" fill="#FF9800"/>
</svg>
</div>
**RAW → CLEAN → ENRICH → STORE → SERVE → MONITOR → RETIRE**  

Skip a station—or visit them out of order—and the whole system risks collapse.  

---

## 4.3 SOURCE LANDSCAPE: WHERE EXAMPLES COME FROM  

Here’s a map of where training examples originate:  

<table border="1" cellspacing="0" cellpadding="5">
<tr>
  <th>Source Family</th>
  <th>Typical Formats</th>
  <th>Bright Side</th>
  <th>Shadow Side</th>
</tr>
<tr>
  <td>Operational DB</td>
  <td>SQL dumps, CSV</td>
  <td>High integrity, time-stamped</td>
  <td>Schema drift, access rights</td>
</tr>
<tr>
  <td>Event Streams</td>
  <td>JSON logs, Avro</td>
  <td>Millisecond granularity</td>
  <td>Volume tsunami, schema evolution</td>
</tr>
<tr>
  <td>Web & APIs</td>
  <td>REST/GraphQL, HTML</td>
  <td>Real-time, global</td>
  <td>Rate limits, legal scraping terms</td>
</tr>
<tr>
  <td>IoT / Sensors</td>
  <td>Binary blobs, PCAP</td>
  <td>High frequency</td>
  <td>Clock skew, sensor drift</td>
</tr>
<tr>
  <td>Open Repositories</td>
  <td>Kaggle, UCI, gov portals</td>
  <td>Free, well documented</td>
  <td>Label errors, licence landmines</td>
</tr>
<tr>
  <td>Synthetic</td>
  <td>Simulators, GANs</td>
  <td>Infinite, balanced</td>
  <td>Reality gap, bias xerox</td>
</tr>
</table>  


Here’s the "Shadow Side" risk heat-map:

<div style="text-align:center; margin: 20px 0;">
<svg width="500" height="180" xmlns="http://www.w3.org/2000/svg">
  <!-- gradient red -->
  <linearGradient id="redgrad" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#ffffff"/>
    <stop offset="100%" stop-color="#d32f2f"/>
  </linearGradient>
  <!-- bars -->
  <rect x="40" y="20" width="60" height="20" fill="url(#redgrad)" opacity="0.9"/>
  <rect x="40" y="45" width="60" height="20" fill="url(#redgrad)" opacity="0.7"/>
  <rect x="40" y="70" width="60" height="20" fill="url(#redgrad)" opacity="0.5"/>
  <rect x="40" y="95" width="60" height="20" fill="url(#redgrad)" opacity="0.3"/>
  <rect x="40" y="120" width="60" height="20" fill="url(#redgrad)" opacity="0.2"/>
  <!-- y-labels -->
  <text x="5" y="35" font-size="10" fill="#333">Operational DB</text>
  <text x="5" y="60" font-size="10" fill="#333">Event Streams</text>
  <text x="5" y="85" font-size="10" fill="#333">Web / APIs</text>
  <text x="5" y="110" font-size="10" fill="#333">IoT Sensors</text>
  <text x="5" y="135" font-size="10" fill="#333">Open Repos</text>
  <!-- x-axis -->
  <line x1="40" y1="150" x2="110" y2="150" stroke="#333"/>
  <text x="25" y="165" font-size="9" fill="#333">Low risk</text>
  <text x="95" y="165" font-size="9" fill="#333">High risk</text>
</svg>
</div>
---

## 4.4 SAMPLING: HOW TO SIP FROM A FIREHOSE  

Data is often too big. Sampling makes it manageable.  

**Rule of 30:** For many datasets, once you have  
30 × (features²) rows → more rows give diminishing returns.  

<table border="1" cellspacing="0" cellpadding="5">
<tr>
  <th>Strategy</th>
  <th>When to Use</th>
  <th>Pro / Con</th>
</tr>
<tr>
  <td>Simple random</td>
  <td>Homogeneous population</td>
  <td>Easy / can miss minorities</td>
</tr>
<tr>
  <td>Stratified</td>
  <td>Imbalanced classes</td>
  <td>Preserves proportions / needs class labels</td>
</tr>
<tr>
  <td>Cluster</td>
  <td>Natural groups (stores, schools)</td>
  <td>Cheap collection / extra variance</td>
</tr>
<tr>
  <td>Reservoir stream</td>
  <td>Infinite feed, memory cap</td>
  <td>O(1) memory / randomness only</td>
</tr>
<tr>
  <td>Importance</td>
  <td>Rare-event simulation</td>
  <td>Focuses on tails / needs density estimate</td>
</tr>
</table>  



<figure>
  <img src="/static/images/fig4_3_sampling.png" 
       alt="Simple vs Stratified sampling (figure 4.3)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
    Figure 4.3 — Left: simple random sample. Right: stratified sample by income quartile (each colour = an income quartile).
  </figcaption>
</figure>

---

## 4.5 DATA QUALITY: THE SEVEN DIMENSIONS  

Good datasets satisfy seven tests:  

1. Accuracy  
2. Completeness  
3. Consistency  
4. Timeliness  
5. Validity  
6. Uniqueness  
7. Representativeness  

(A radar chart often visualises these dimensions.)  

<figure>
  <img src="/static/images/fig4_4_radar.png" 
       alt="Seven-axis quality comparison(figure 4.4)" 
       style="max-width:25%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

---

## 4.6 MISSINGNESS PATTERNS & FIXES  

<figure>
  <img src="/static/images/fig4_5_missingness.png" 
       alt="Missingness heat-map(figure 4.5)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

Rows = patients, columns = lab tests; black = observed, grey = missing.
A vertical grey stripe signals a dropped lab machine; a horizontal block suggests patient dropout.

Missing data is more revealing than it looks.  

<table border="1" cellspacing="0" cellpadding="5">
<tr>
  <th>Pattern</th>
  <th>Quick Fix</th>
  <th>Sophisticated Fix</th>
</tr>
<tr>
  <td>MCAR 5%</td>
  <td>Drop rows</td>
  <td>Multiple imputation (MICE)</td>
</tr>
<tr>
  <td>MAR income</td>
  <td>Mean within group</td>
  <td>Bayesian regression impute</td>
</tr>
<tr>
  <td>MNAR sensor</td>
  <td>Flag + dummy</td>
  <td>Joint model + instrument</td>
</tr>
</table>  

👉 Always add a “was_missing” flag—absence itself can be predictive.  
Pro tip: Always add a "was_missing" binary flag; the absence itself can be predictive.

---

## 4.7 OUTLIERS: TO CAP, TO TRANSFORM, OR TO CELEBRATE?  

<figure>
  <img src="/static/images/fig4_6_box.png" 
       alt="Box-plot gallery(figure 4.5)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>

- Faulty sensor? → Remove.  
- Fraud signal? → Keep and investigate.  
- Natural extreme? → Winsorise or transform.  

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Outlier Handling Flowchart</title>
  <style>
    svg { font-family: Arial, sans-serif; font-size: 12px; }
    .diamond { fill: #fdf6e3; stroke: #333; stroke-width: 1.5; }
    .box { fill: #e3f2fd; stroke: #333; stroke-width: 1.5; rx: 6; ry: 6; }
    text { fill: #000; }
  </style>
</head>
<body>
  <svg width="600" height="450">

    <!-- Outlier detected? -->
    <polygon class="diamond" points="260,20 320,50 260,80 200,50"/>
    <text x="260" y="55" text-anchor="middle">Outlier detected?</text>

    <!-- Business critical? -->
    <polygon class="diamond" points="260,120 320,150 260,180 200,150"/>
    <text x="260" y="155" text-anchor="middle">Business critical?</text>

    <!-- Keep & flag -->
    <rect class="box" x="360" y="130" width="100" height="40"/>
    <text x="410" y="155" text-anchor="middle">Keep &amp; flag</text>

    <!-- Domain plausible? -->
    <polygon class="diamond" points="260,220 320,250 260,280 200,250"/>
    <text x="260" y="255" text-anchor="middle">Domain plausible?</text>

    <!-- Remove / impute -->
    <rect class="box" x="360" y="230" width="100" height="40"/>
    <text x="410" y="255" text-anchor="middle">Remove / impute</text>

    <!-- Winsorise / transform -->
    <rect class="box" x="360" y="320" width="120" height="40"/>
    <text x="420" y="345" text-anchor="middle">Winsorise / transform</text>

    <!-- Connectors -->
    <line x1="260" y1="80" x2="260" y2="120" stroke="#333" marker-end="url(#arrow)"/>
    <line x1="320" y1="150" x2="360" y2="150" stroke="#333" marker-end="url(#arrow)"/>
    <line x1="260" y1="180" x2="260" y2="220" stroke="#333" marker-end="url(#arrow)"/>
    <line x1="320" y1="250" x2="360" y2="250" stroke="#333" marker-end="url(#arrow)"/>
    <line x1="260" y1="280" x2="260" y2="320" stroke="#333" marker-end="url(#arrow)"/>
    <line x1="260" y1="60" x2="200" y2="60" stroke="transparent"/>

    <!-- Labels -->
    <text x="190" y="145">No</text>
    <text x="340" y="145">Yes</text>

    <!-- Arrowhead marker -->
    <defs>
      <marker id="arrow" markerWidth="10" markerHeight="10" refX="6" refY="3"
              orient="auto" markerUnits="strokeWidth">
        <path d="M0,0 L0,6 L6,3 z" fill="#333"/>
      </marker>
    </defs>
  </svg>
</body>
</html>


Outlier handling is a **business decision**, not just statistics.  
Outlier detected → Business critical? → Yes → Keep & flag → No → Domain plausible? → No → Remove / impute → Yes → Winsorise / transfor
---

## 4.8 LABEL ENGINEERING: THE £100-MILLION TYPO  

One typo can cost fortunes. Example: hedge fund labels inverted → fake profits.  

**Checklist:**  

<table border="1" cellspacing="0" cellpadding="5">
<tr><td>[ ] Time-zone alignment</td></tr>
<tr><td>[ ] Look-ahead embargo (no future info)</td></tr>
<tr><td>[ ] Class imbalance ratio documented</td></tr>
<tr><td>[ ] Negative class definition reviewed</td></tr>
<tr><td>[ ] Random sample re-labelled (κ ≥ 0.75)</td></tr>
</table>  

---

## 4.9 FEATURE LEAKAGE MATRIX 

<figure>
  <img src="/static/images/fig4_8_leakage.png" 
       alt=" Leakage matrix heat-map(figure 4.8)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>
Fig. 4.8 Dark red bars warn of possible target leakage.
Dark cell = correlation = 0.95 → investigate; probably a proxy for the target.
Leakage = hidden cheating.  
- High correlation between feature & target → red flag.  
- Always ask: “Would this feature exist at prediction time?”  

---

## 4.10 AUGMENTATION & SYNTHESIS  
Ways to create *more* data:  

- Images → flip, rotate, jitter. 

<figure>
  <img src="/static/images/fig4_9_aug.png" 
       alt=" Classic flip / rotate / colour-jitter montage(figure 4.9)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>
 
- Text → synonym swap, back-translation.  
<figure>
  <img src="/static/images/fig4_10_text_aug.png" 
       alt=" Text-augmentation montage (figure 4.10)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>


- Tables → SMOTE, ADASYN, VAEs.  

<table border="1" cellspacing="0" cellpadding="6">
  <thead>
    <tr>
      <th>Technique</th>
      <th>Core Idea</th>
      <th>When to Use</th>
      <th>Pro</th>
      <th>Con</th>
      <th>Python Snippet (high-level)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>SMOTE</td>
      <td>Creates synthetic minority samples by interpolating k-nearest neighbours</td>
      <td>Class imbalance &lt; ~20%</td>
      <td>Keeps feature space continuous</td>
      <td>Can blur decision boundary</td>
      <td><code>from imblearn.over_sampling import SMOTE; sm = SMOTE(); X_sm, y_sm = sm.fit_resample(X, y)</code></td>
    </tr>
    <tr>
      <td>ADASYN</td>
      <td>Adaptive synthetic sampling: generates <i>more</i> samples in "hard-to-learn" regions</td>
      <td>Borderline cases are important</td>
      <td>Focuses on informative regions</td>
      <td>Still sensitive to noise</td>
      <td><code>from imblearn.over_sampling import ADASYN; ad = ADASYN(); X_ad, y_ad = ad.fit_resample(X, y)</code></td>
    </tr>
    <tr>
      <td>RandomUnder-sampling</td>
      <td>Randomly drops majority-class rows</td>
      <td>Very large majority set, fast prototype</td>
      <td>Trains on smaller set → faster</td>
      <td>Loses real information</td>
      <td><code>from imblearn.under_sampling import RandomUnderSampler; rus = RandomUnderSampler(); X_r, y_r = rus.fit_resample(X, y)</code></td>
    </tr>
    <tr>
      <td>Gaussian Noise Injection</td>
      <td>Add N(0, σ) to numerical columns</td>
      <td>Low noise, robust model needed</td>
      <td>Simple, fast</td>
      <td>Distorts correlations</td>
      <td><code>X_aug = X + np.random.normal(0, 0.02, X.shape)</code></td>
    </tr>
    <tr>
      <td>Conditional Tabular GAN (CTGAN)</td>
      <td>Train GAN to generate synthetic rows that preserve column marginals &amp; correlations</td>
      <td>Need lots of realistic fake data</td>
      <td>Captures multivariate structure</td>
      <td>Training-heavy, GPU RAM</td>
      <td><code>from ctgan import CTGAN; model = CTGAN(); model.fit(data); synthetic = model.sample(1000)</code></td>
    </tr>
    <tr>
      <td>Mixup (numerical)</td>
      <td>Convex combo of two random samples: λx₁ + (1-λ)x₂</td>
      <td>Small tabular DL models</td>
      <td>Acts like regulariser</td>
      <td>Produces <i>implausible</i> rows (e.g., 0.3×Dog + 0.7×Cat)</td>
      <td><code>lamb = np.random.beta(0.2, 0.2); x_mix = lamb * x1 + (1-lamb) * x2</code></td>
    </tr>
    <tr>
      <td>Feature-cross / polynomial</td>
      <td>Create interaction terms (x₁×x₂) or powers</td>
      <td>Domain suspects non-linear relations</td>
      <td>Model-free</td>
      <td>Explodes dimensionality</td>
      <td><code>from sklearn.preprocessing import PolynomialFeatures; poly = PolynomialFeatures(2)</code></td>
    </tr>
    <tr>
      <td>Time-window slice &amp; shuffle</td>
      <td>Cut time-series into windows &amp; re-order</td>
      <td>Robustness to temporal drift</td>
      <td>Keeps local dynamics</td>
      <td>Breaks long-term trend</td>
      <td><code>Custom slicing with np.array_split + np.random.shuffle</code></td>
    </tr>
    <tr>
      <td>Marginal resample (bootstrap)</td>
      <td>Sample <i>each</i> column independently from its marginal</td>
      <td>Quick sanity / stress test</td>
      <td>Trivial to code</td>
      <td>Destroys joint distribution</td>
      <td><code>boot = df.copy(); for col in df: boot[col] = df[col].sample(frac=1, random_state=42).reset_index(drop=True)</code></td>
    </tr>
  </tbody>
</table>



Golden rule: **Augment training only; keep validation & test pristine**  

---

## 4.11 STORAGE, VERSIONING & LINEAGE  

<div style="text-align:center; margin:20px 0;">
  <svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
    <!-- Triangle -->
    <polygon points="200,20 380,280 20,280" fill="#e3f2fd" stroke="#0288d1" stroke-width="2"/>
    
    <!-- Labels -->
    <text x="200" y="50" text-anchor="middle" font-size="14" fill="#0277bd">Git (code)</text>
    <text x="100" y="250" text-anchor="middle" font-size="14" fill="#0277bd">DVC (data)</text>
    <text x="300" y="250" text-anchor="middle" font-size="14" fill="#0277bd">MLflow (model)</text>
    
    <!-- Circle in center -->
    <circle cx="200" cy="150" r="35" fill="#ffffff" stroke="#0288d1"/>
    <text x="200" y="155" text-anchor="middle" font-size="12" fill="#0277bd">Hash link</text>
  </svg>
</div>


- Git for code  
- DVC for data  
- MLflow for models  

Together they guarantee **traceability**.  

---

## 4.12 PRIVACY, ETHICS & COMPLIANCE QUICK-SCAN  

<table border="1" cellspacing="0" cellpadding="5">
<tr>
  <th>Technique</th>
  <th>GDPR</th>
  <th>CCPA</th>
  <th>HIPAA</th>
  <th>Notes</th>
</tr>
<tr>
  <td>Pseudonymisation</td>
  <td>✔</td><td>✔</td><td>✔</td>
  <td>Still personal if re-linkable</td>
</tr>
<tr>
  <td>Differential Privacy</td>
  <td>✔</td><td>?</td><td>✔</td>
  <td>ε-setting is art</td>
</tr>
<tr>
  <td>Synthetic Data</td>
  <td>?</td><td>?</td><td>?</td>
  <td>Needs de-identification review</td>
</tr>
<tr>
  <td>Right to Deletion</td>
  <td>✔</td><td>✔</td><td>✔</td>
  <td>Backup purge required</td>
</tr>
</table>  


<figure>
  <img src="/static/images/fig4_12_eps.png" 
       alt=" ε-differential privacy noise scale(figure 4.12)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>


---

## 4.13 AUTOMATED DATA-CARD TEMPLATE  

Every dataset should come with a **1-page card**:  

- Name, version, owner  
- Size, schema, collection dates  
- Known biases  
- Licence restrictions  
- QA sign-off  


<figure>
  <img src="/static/images/fig4_13_datacard.jpg" 
       alt=" ε-differential privacy noise scale(figure 4.13)" 
       style="max-width:50%;height:auto;border:1px solid #ddd;
              border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08);" />
  <figcaption style="font-size:0.95rem;color:#555;margin-top:8px;">
  </figcaption>
</figure>
---

## 4.14 10 COMMANDMENTS FOR DATA PRACTITIONERS  

1. Log every query.  
2. Never edit raw files.  
3. Keep a time-based hold-out.  
4. Label at smallest grain.  
5. Visualise before sanitise.  
6. Version-lock seeds.  
7. Document null semantics.  
8. Reuse preprocessing in training & inference.  
9. Treat privacy as a feature.  
10. Assume subpoena readiness.  

---

## 4.15 BRIDGE TO CHAPTER 5  

Clean, well-documented data is still inert clay.  
Next, we sculpt it into **features**—representations that amplify signal and bury noise.  
