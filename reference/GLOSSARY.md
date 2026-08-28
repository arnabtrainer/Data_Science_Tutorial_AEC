# Data Science, ML, DL, and MLOps Glossary

Definitions are operational learning definitions; always interpret them in the context of a specific design and decision.

## abstention

A policy allowing the system to decline uncertain or unsupported decisions.

## aliasing

Two names referring to the same mutable object, so mutation through either name is visible through both.

## autograd

Automatic differentiation of tensor operations.

## axis

A dimension along which indexing or reduction occurs.

## backbone

A reusable feature extractor, often pretrained before adding a task-specific head.

## bagging

Fitting learners on perturbed samples and averaging them to reduce variance.

## baseline

A simple reference procedure that establishes the minimum value of additional complexity.

## Bayes theorem

A rule for updating a prior probability with likelihood evidence.

## Boolean mask

An array of True/False values used to select matching elements or rows.

## boosting

Building an additive predictor sequentially so each learner corrects current error.

## broadcasting

NumPy's rule for virtually expanding compatible dimensions during element-wise operations.

## business decision

The action that analysis is intended to inform; it determines useful targets, metrics, and constraints.

## calibration

Agreement between predicted probability and empirical event frequency.

## CDF

The probability that a random variable is less than or equal to a threshold.

## centroid

The mean vector representing a K-means cluster.

## ColumnTransformer

A tool for applying different preprocessing pipelines to different feature subsets.

## composition

Building behaviour by combining objects with focused responsibilities rather than inheriting everything.

## computation graph

Recorded operations connecting inputs, parameters, and output for differentiation.

## concept drift

Change in the conditional relationship between inputs and outcome.

## conditional probability

The probability of an event after restricting attention to cases where another event occurred.

## confidence

Conditional frequency of a consequent among transactions containing an antecedent.

## confidence level

The long-run coverage rate of an interval-construction procedure under its assumptions.

## confounder

A common cause of an exposure and outcome that can distort their observed association.

## context manager

An abstraction that guarantees setup and cleanup around a block, including during exceptions.

## convolution

A spatially shared local weighted operation used to detect patterns across positions.

## copy

Creation of another container; shallow and deep copies differ in whether nested objects remain shared.

## covariance

A scale-dependent measure of how two variables vary together.

## cross-entropy

A probabilistic loss that penalizes low probability assigned to the observed class.

## data drift

Change in the distribution of model inputs or related data.

## DataFrame

A two-dimensional labelled collection of aligned Series.

## DBSCAN

A density-connectivity algorithm that can mark sparse points as noise.

## decision threshold

The probability or score cutoff that converts ranking into an action.

## dependency injection

Supplying collaborators from outside rather than constructing hidden dependencies internally.

## deserialization

Parsing stored data into in-memory objects under a defined schema.

## dictionary

A mutable mapping from unique hashable keys to values.

## dot product

A weighted sum measuring alignment and forming the basic operation of linear models.

## dropout

Random suppression of activations during training as a regularizer.

## dtype

The fixed representation used for every element in a NumPy array or Pandas column.

## dynamic typing

Types belong to runtime objects, while names may later refer to objects of other types.

## effect size

A magnitude measure that supports practical interpretation beyond statistical significance.

## epoch

One pass through the training dataset, subject to batching and sampling rules.

## Euclidean distance

Straight-line distance under a coordinate system.

## exception hierarchy

The inheritance tree used to classify and selectively handle errors.

## expected value

A probability-weighted long-run average of a random variable.

## explained variance

Variance captured by a component relative to total variance.

## expression

A piece of code that evaluates to a value; expressions can be combined into larger computations.

## feature parity

Use of equivalent feature definitions and transformations in training and inference.

## feedback loop

A path by which model decisions influence future observations, labels, or populations.

## function contract

The accepted inputs, guaranteed outputs, side effects, errors, and invariants of a function.

## generator

A resumable function that yields values lazily rather than materializing the full sequence.

## Gini impurity

Probability of class disagreement under two independent draws from a node's class distribution.

## gradient

The vector of partial derivatives of a scalar objective with respect to parameters.

## grain

The real-world entity and time period represented by one row.

## hidden state

A recurrent representation passed from one time step to the next.

## human oversight

Defined human authority, review, escalation, and override around automated decisions.

## hyperparameter

A learning-process setting chosen outside ordinary parameter fitting.

## identity versus equality

Equality compares values; identity checks whether two references point to the same object.

## immutability

An immutable object's value cannot be changed in place; an operation creates another object instead.

## immutable artifact

A release object identified by content/version and never modified in place.

## imputation

Replacing missing values according to a rule learned from appropriate training data.

## indexing

Selecting an element by position or label.

## invariant

A condition that must remain true for every valid object or system state.

## Isolation Forest

An anomaly method that uses short random-partition path length as evidence of isolation.

## Jupyter kernel

The long-running Python process that owns variables, imports, and execution state for a notebook.

## kernel trick

Computing inner products in an implicit feature space without materializing that space.

## key

A vector against which queries are compared.

## KPI

A metric tied to a specific decision, objective, owner, and review cadence.

## Lasso

Linear modelling with an L1 penalty that can set some coefficients exactly to zero.

## learning rate

The step-size multiplier applied to an optimization direction.

## least squares

Parameter estimation by minimizing the sum of squared residuals.

## lift

Rule confidence divided by the consequent's base rate.

## list

An ordered, mutable sequence that permits repeated values.

## logit

An unnormalized class score; logits become probabilities after an appropriate link such as sigmoid or softmax.

## MAE

Mean absolute error; an average error magnitude with linear penalty.

## matrix

A rectangular numerical transformation or collection of vectors.

## mean

The arithmetic average; a centre that is sensitive to extreme values.

## median

The middle ordered value; a robust centre for skewed data.

## method chaining

Expressing sequential transformations as one readable pipeline of operations.

## mini-batch

A subset used for one stochastic gradient update.

## missingness

The state and mechanism by which a value is absent; it can carry information and requires contextual treatment.

## model registry

A governed catalog of versioned model artifacts, lineage, metrics, and lifecycle status.

## multilayer perceptron

A feed-forward network composed of affine layers and nonlinear activations.

## ndarray

NumPy's homogeneous n-dimensional array with shape, dtype, and memory layout.

## numerical stability

Resistance of an algorithm to harmful amplification of floating-point rounding error.

## observation window

The period from which features may be calculated.

## one-hot encoding

Representing each category with indicator columns without imposing arbitrary numeric order.

## optimizer

A stateful algorithm that converts gradients into parameter updates.

## outcome window

The future period in which the target event is measured.

## overfitting

Learning sample-specific noise or quirks that do not generalize.

## overplotting

Loss of information when many graphical marks overlap.

## p-value

Under a specified null model, the probability of a result at least as incompatible with that model as the observed result.

## Path

An operating-system-independent object for constructing and manipulating filesystem paths.

## PDF

A nonnegative continuous density whose integral over a range gives probability.

## Pearson correlation

Standardized linear association between two numeric variables.

## permutation importance

Held-out performance loss after breaking one feature's association with the target.

## Pipeline

An ordered composite estimator that learns and applies transformations with a model as one unit.

## PMF

A function assigning probability mass to each discrete value.

## population

The full set of entities or events about which an inference is intended.

## power

Probability that a test rejects the null under a specified alternative.

## PR-AUC

Summary of precision-recall trade-offs, especially informative when positives are rare.

## precision

Among positive predictions, the fraction that are truly positive.

## principal component

An orthogonal direction along which projected variance is maximized.

## projection

The closest representation of a vector within a subspace under a chosen geometry.

## pure function

A function whose result depends only on explicit inputs and which has no externally visible side effects.

## query

A vector representing what a token or position is seeking.

## R-squared

Fraction of target variance reduced relative to predicting the target mean on the same evaluation set.

## random generator

An explicit pseudorandom state object that makes simulation reproducible and avoids hidden global state.

## recall

Among true positives, the fraction detected.

## receptive field

The region of input capable of influencing a particular activation.

## recursive partition

Repeatedly splitting feature space into regions with simpler target behaviour.

## regularization

Constraining a learner to reduce variance or encode preferences for simpler solutions.

## resample

Aggregate or align time-indexed data to a new frequency.

## residual

Observed target minus model prediction.

## responsibility

Posterior probability that a mixture component generated an observation.

## Ridge

Linear modelling with an L2 coefficient penalty.

## RMSE

Root mean squared error; a measure that emphasizes larger errors.

## ROC-AUC

Probability that a randomly chosen positive is ranked above a randomly chosen negative.

## rolling window

A statistic computed repeatedly over a moving trailing or centred subset.

## sample

The observed subset used to estimate properties of a population.

## sampling distribution

The distribution an estimator would have over repeated samples from the same process.

## schema

The expected columns, types, ranges, nullability, keys, and semantic constraints of data.

## selection bias

A mismatch created when inclusion in the observed data is related to variables relevant to the conclusion.

## serialization

Conversion of in-memory state into a stored or transferable representation.

## Series

A one-dimensional labelled array, typically one DataFrame column.

## set

An unordered collection of unique hashable values with fast membership operations.

## shape

The length of each array dimension.

## silhouette score

Comparison of average within-cluster distance to nearest-other-cluster distance.

## slicing

Selecting a range using start, stop, and step boundaries.

## split-apply-combine

Partition rows into groups, calculate within groups, and combine group results.

## standard deviation

The square root of variance, expressed in the original unit.

## standard error

The standard deviation of an estimator's sampling distribution.

## standardization

Centering and scaling a feature using a mean and standard deviation.

## stratification

Preserving important class proportions across splits or folds.

## string

An immutable Unicode sequence used for text.

## structured context

Named diagnostic fields—such as request, file, or record identifiers—attached to a log event.

## support

Fraction of transactions containing an itemset.

## support vector

A training point that defines or violates the maximum-margin boundary.

## SVD

A factorization into orthogonal input directions, singular values, and orthogonal output directions.

## target leakage

Use of information unavailable at real decision time or derived from the outcome.

## tensor

A multidimensional numerical array used by deep-learning frameworks.

## test set

Held-out data used for a final deployment-like estimate after design choices are frozen.

## training set

Data used to estimate model parameters.

## Transformer encoder

A stack of self-attention and feed-forward blocks producing contextual token representations.

## truthiness

Python's rule for interpreting an object in a Boolean context, including empty collections and zero.

## tuple

An ordered, immutable sequence useful for fixed records or hashable groupings.

## unit test

A fast, isolated check of one observable behaviour.

## validation set

Data used for design, tuning, and model selection.

## value

The content vectors combined according to attention weights.

## variable binding

Association of a name with an object. Python variables are labels, not fixed typed boxes.

## variance

Average squared deviation from the mean, with a degrees-of-freedom adjustment for a sample estimator.

## vector

An ordered numerical representation of magnitude, direction, or a set of features.

## vectorization

Expressing element-wise work as compiled array operations rather than Python-level loops.

## view

An array object that shares underlying data with another array.

## visual encoding

A mapping from a data field to position, length, shape, size, angle, or colour.
