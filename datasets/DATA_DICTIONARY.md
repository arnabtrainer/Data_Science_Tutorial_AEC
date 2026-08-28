# Bundled Dataset Dictionary

> All datasets are synthetic and intended only for education. They do not represent real people, businesses, medical cases, financial decisions, or production systems.

## `student_scores.csv`

**Grain:** One synthetic student record  
**Purpose:** Python/Pandas, regression, classification, and tabular neural-network examples  
**Target(s):** final_score, passed

| Field | Meaning |
|---|---|
| `student_id` | Synthetic unique identifier; never use as a predictive feature. |
| `study_hours_per_week` | Reported weekly study hours. |
| `attendance_pct` | Attendance percentage. |
| `sleep_hours` | Average sleep hours. |
| `prior_score` | Prior assessment score. |
| `final_score` | Synthetic continuous outcome. |
| `passed` | 1 when final_score >= 60, otherwise 0. |

## `retail_sales.csv`

**Grain:** One synthetic order  
**Purpose:** Pandas, visualization, EDA, aggregation, and business storytelling  
**Target(s):** None

| Field | Meaning |
|---|---|
| `order_id` | Synthetic unique order identifier. |
| `order_date` | Order date. |
| `region` | North, South, East, or West. |
| `category` | Product category. |
| `units` | Units purchased. |
| `unit_price` | Price per unit before discount. |
| `discount_pct` | Fractional discount from 0 to 1. |
| `revenue` | Synthetic net revenue. |
| `cost` | Synthetic attributed cost. |
| `profit` | Revenue minus cost. |

## `messy_retail_sales.csv`

**Grain:** One raw synthetic order extract, including deliberate defects  
**Purpose:** Data-quality auditing and cleaning exercises  
**Target(s):** None

| Field | Meaning |
|---|---|
| `all retail columns` | Contains duplicate rows, missing values, inconsistent text, invalid dates, nonpositive units, and impossible discounts by design. |

## `house_prices.csv`

**Grain:** One synthetic residential property  
**Purpose:** Regression, preprocessing, regularization, tree ensembles, residual analysis  
**Target(s):** price

| Field | Meaning |
|---|---|
| `area_sqft` | Property area. |
| `bedrooms` | Bedroom count. |
| `bathrooms` | Bathroom count. |
| `age_years` | Property age. |
| `distance_to_city_km` | Distance to city centre; some values missing. |
| `school_rating` | Synthetic neighbourhood school rating; some values missing. |
| `neighborhood` | Urban, Suburban, or Rural; some values missing. |
| `garage_spaces` | Garage capacity. |
| `price` | Synthetic target price. |

## `customer_churn.csv`

**Grain:** One synthetic customer at an observation cutoff  
**Purpose:** EDA, imbalanced classification, thresholding, calibration, and production serving  
**Target(s):** churn

| Field | Meaning |
|---|---|
| `customer_id` | Synthetic identifier; exclude from modelling. |
| `tenure_months` | Months as a customer. |
| `monthly_charges` | Current monthly charge. |
| `support_tickets_90d` | Tickets in the trailing 90 days. |
| `weekly_usage_hours` | Usage estimate; some values missing. |
| `contract_type` | Month-to-month, One year, or Two year. |
| `internet_service` | Fiber, DSL, or None. |
| `autopay` | Binary indicator. |
| `senior_citizen` | Synthetic binary segment indicator. |
| `churn` | Synthetic future outcome label. |

## `customer_segments.csv`

**Grain:** One synthetic customer  
**Purpose:** Clustering, mixture models, PCA, and profiling  
**Target(s):** None

| Field | Meaning |
|---|---|
| `customer_id` | Synthetic identifier; exclude from clustering. |
| `age` | Age. |
| `annual_income` | Synthetic annual income. |
| `purchase_frequency` | Purchases in an illustrative period. |
| `avg_order_value` | Average order value. |
| `satisfaction` | Synthetic 1–5 satisfaction measure. |

## `operations_anomalies.csv`

**Grain:** One synthetic 15-minute service interval  
**Purpose:** Anomaly detection, ranking, alert thresholds, and monitoring  
**Target(s):** is_anomaly (evaluation only)

| Field | Meaning |
|---|---|
| `timestamp` | Interval start time. |
| `latency_ms` | Synthetic latency. |
| `error_rate` | Synthetic fractional error rate. |
| `throughput_rpm` | Requests per minute. |
| `cpu_pct` | CPU utilization. |
| `memory_pct` | Memory utilization. |
| `is_anomaly` | Injected synthetic anomaly label, intended only for evaluation. |

## `demand_timeseries.csv`

**Grain:** One synthetic calendar day  
**Purpose:** Time-series visualization and leakage-safe forecasting  
**Target(s):** demand

| Field | Meaning |
|---|---|
| `date` | Calendar date. |
| `demand` | Synthetic daily demand. |
| `promotion` | Known promotion indicator. |
| `holiday` | Illustrative holiday indicator. |

## `text_reviews.csv`

**Grain:** One synthetic product review  
**Purpose:** Text preprocessing and sentiment classification  
**Target(s):** positive

| Field | Meaning |
|---|---|
| `review_id` | Synthetic identifier. |
| `review_text` | Template-generated review text. |
| `positive` | Binary sentiment label. |

## `images/simple_shapes_X.npy`

**Grain:** One 1×16×16 synthetic grayscale image  
**Purpose:** CNN training without external downloads  
**Target(s):** paired simple_shapes_y.npy

| Field | Meaning |
|---|---|
| `tensor` | Values between 0 and 1 representing vertical, horizontal, or diagonal patterns. |
