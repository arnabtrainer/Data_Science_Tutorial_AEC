# Formula and Interpretation Sheet

This sheet is a revision aid, not a substitute for assumptions and derivations.

## Descriptive statistics

- Mean: \(\bar{x}=\frac{1}{n}\sum_{i=1}^n x_i\)
- Sample variance: \(s^2=\frac{1}{n-1}\sum_i(x_i-\bar{x})^2\)
- Standard deviation: \(s=\sqrt{s^2}\)
- Interquartile range: \(IQR=Q_3-Q_1\)
- Z-score: \(z=(x-\mu)/\sigma\)

## Probability

- Complement: \(P(A^c)=1-P(A)\)
- Addition: \(P(A\cup B)=P(A)+P(B)-P(A\cap B)\)
- Conditional: \(P(A\mid B)=P(A\cap B)/P(B)\)
- Bayes: \(P(A\mid B)=P(B\mid A)P(A)/P(B)\)
- Total probability: \(P(B)=\sum_iP(B\mid A_i)P(A_i)\)

## Sampling and inference

- Standard error of a mean: \(SE(\bar{x})=s/\sqrt{n}\)
- Approximate interval: estimate ± critical value × standard error
- One-sample t statistic: \(t=(\bar{x}-\mu_0)/(s/\sqrt{n})\)
- Cohen's d for two independent groups: standardized difference in means
- Power depends on effect, variance, sample size, alpha, and design.

## Association

- Covariance: \(\mathrm{Cov}(X,Y)=E[(X-E[X])(Y-E[Y])]\)
- Pearson correlation: \(r=\mathrm{Cov}(X,Y)/(s_Xs_Y)\)
- Correlation measures linear association; it does not identify causal direction.

## Linear algebra

- Dot product: \(x^\top w=\sum_jx_jw_j\)
- Matrix multiplication: \((m\times k)(k\times n)\rightarrow(m\times n)\)
- Least squares objective: \(\min_\beta\|X\beta-y\|_2^2\)
- SVD: \(X=U\Sigma V^\top\)
- PCA directions are eigenvectors of a covariance/correlation matrix or right singular vectors of centred data.

## Regression

- Simple line: \(\hat{y}=\beta_0+\beta_1x\)
- OLS slope: \(\hat{\beta}_1=\sum(x_i-\bar{x})(y_i-\bar{y})/\sum(x_i-\bar{x})^2\)
- MAE: \(\frac{1}{n}\sum|y_i-\hat{y}_i|\)
- MSE: \(\frac{1}{n}\sum(y_i-\hat{y}_i)^2\)
- RMSE: \(\sqrt{MSE}\)
- \(R^2=1-\frac{\sum(y-\hat{y})^2}{\sum(y-\bar{y})^2}\)
- Ridge: SSE + \(\lambda\sum_j\beta_j^2\)
- Lasso: SSE + \(\lambda\sum_j|\beta_j|\)

## Classification

- Odds: \(p/(1-p)\)
- Logit: \(\log[p/(1-p)]\)
- Sigmoid: \(\sigma(z)=1/(1+e^{-z})\)
- Precision: \(TP/(TP+FP)\)
- Recall/sensitivity: \(TP/(TP+FN)\)
- Specificity: \(TN/(TN+FP)\)
- F1: \(2PR/(P+R)\)
- Log loss: negative mean log probability assigned to the observed class
- Brier score: mean squared probability error

## Trees and ensembles

- Gini impurity: \(1-\sum_k p_k^2\)
- Entropy: \(-\sum_kp_k\log p_k\)
- Bagging reduces variance through averaging diverse estimators.
- Boosting adds learners sequentially along loss gradients.

## Clustering and representation

- Euclidean distance: \(\sqrt{\sum_j(x_j-z_j)^2}\)
- K-means objective: \(\sum_i\|x_i-\mu_{c_i}\|^2\)
- Silhouette per point: \((b-a)/\max(a,b)\)
- GMM: \(p(x)=\sum_k\pi_k\mathcal N(x\mid\mu_k,\Sigma_k)\)
- PCA explained variance ratio: component eigenvalue / sum of eigenvalues
- Lift: \(P(B\mid A)/P(B)\)

## Optimization and neural networks

- Gradient descent: \(\theta_{t+1}=\theta_t-\eta\nabla_\theta L(\theta_t)\)
- Linear layer: \(z=Wx+b\)
- ReLU: \(\max(0,z)\)
- Softmax: \(\exp(z_k)/\sum_j\exp(z_j)\)
- Binary cross-entropy: \(-[y\log p+(1-y)\log(1-p)]\)
- Convolution output width: \(\lfloor(W+2P-K)/S\rfloor+1\)
- Attention: \(\mathrm{softmax}(QK^\top/\sqrt{d_k})V\)

## Monitoring

- Drift compares distributions; it is not automatically performance degradation.
- PSI is one binned diagnostic: \(\sum_i(a_i-e_i)\log(a_i/e_i)\)
- Monitor service, data, scores, calibration/outcomes, slices, decisions, overrides, and abstentions.

## Interpretation rules

1. State population, coverage, units, baseline, and uncertainty.
2. Separate descriptive, predictive, and causal claims.
3. A score is not a policy; thresholds encode costs and constraints.
4. A high validation score does not rule out leakage or train-serving skew.
5. Importance and explanation do not establish intervention effects.
