import numpy as np

# -----------------------------
# Assume structured array:
data = np.genfromtxt("numpy/5_numpy_project/nyc_taxis.csv", delimiter=",", names=True, dtype=None, encoding="utf-8")
# -----------------------------

# 1️⃣ Prepare data arrays
distance = data['trip_distance']   # independent variable
fare = data['fare_amount']         # dependent variable
pickup_hour = data['pickup_time']  # 0-23
pickup_day = data['pickup_day']    # 1-31
pickup_month = data['pickup_month']  # 1-12
pickup_dow = data['pickup_dayofweek']  # 0-6

# Clean: remove trips with zero or negative distance
mask = distance > 0
distance = distance[mask]
fare = fare[mask]
pickup_hour = pickup_hour[mask]
pickup_day = pickup_day[mask]
pickup_month = pickup_month[mask]
pickup_dow = pickup_dow[mask]

# -----------------------------
# 2️⃣ Linear Regression: fare = a * distance + b
# -----------------------------
# X matrix: [distance, 1] for intercept
X = np.vstack([distance, np.ones_like(distance)]).T
# Solve least squares: [a, b]
a, b = np.linalg.lstsq(X, fare, rcond=None)[0]

# Predict fares
fare_pred = a * distance + b

# Compute RMSE
rmse = np.sqrt(np.mean((fare - fare_pred)**2))

print("Linear Regression Fare Prediction")
print(f"Slope (a): {a:.2f}, Intercept (b): {b:.2f}")
print(f"RMSE: {rmse:.2f}")

# -----------------------------
# 3️⃣ Analyze peak taxi usage times
# -----------------------------
# Trips per hour
hour_counts = np.bincount(pickup_hour.astype(int))
peak_hour = np.argmax(hour_counts)

# Trips per day of week
dow_counts = np.bincount(pickup_dow.astype(int))
peak_dow = np.argmax(dow_counts)

# Trips per month
month_counts = np.bincount(pickup_month.astype(int))
peak_month = np.argmax(month_counts)

print("\nPeak Taxi Usage")
print(f"Hour with most trips: {peak_hour}")
print(f"Day of week with most trips (0=Mon): {peak_dow}")
print(f"Month with most trips: {peak_month}")

# -----------------------------
# 4️⃣ Detect outliers using z-scores
# -----------------------------
def detect_outliers(arr, threshold=3):
    z = (arr - arr.mean()) / arr.std()
    return np.where(np.abs(z) > threshold)[0]

# Distance outliers
distance_outliers = detect_outliers(distance)

# Fare outliers
fare_outliers = detect_outliers(fare)

# Negative or zero distance (already removed)
zero_distance = np.where(distance <= 0)[0]

print("\nOutlier Detection")
print(f"Number of distance outliers: {len(distance_outliers)}")
print(f"Number of fare outliers: {len(fare_outliers)}")
print(f"Number of zero or negative distances: {len(zero_distance)}")
