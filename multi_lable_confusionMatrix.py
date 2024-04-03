import math
import json
from sklearn.metrics import multilabel_confusion_matrix


# Read data from JSON file
with open('merged.json', 'r') as f:
    data = json.load(f)

# Accessing the "model1", "model2", "model3" key from the data
model1_data = data.get("model3", [])

# Extracting the values of the "marked_object" and "predicted_object" keys
y_true = [item.get("marked_object") for item in model1_data]
y_pred = [item.get("predicted_object") for item in model1_data]

# Define the labels, "no_object",
labels = ["armored_vehicle", "artillery", "radar_station", "warship", "air_defence_system"]

# Compute the multilabel confusion matrix
mcm = multilabel_confusion_matrix(y_true, y_pred, labels=labels)

print("Multilabel Confusion Matrix:")
for i, label in enumerate(labels):
    tp, fn = mcm[i][1][1], mcm[i][1][0]
    fp, tn = mcm[i][0][1], mcm[i][0][0]
    print(f"\nLabel: {label}")
    print(f"tp: {tp}, fp: {fp}, \n"
          f"fn: {fn}, tn: {tn}")

    # Calculate precision
    precision = tp / (tp + fp)
    # Print precision
    print("Precision:", precision)

    # Calculate recall
    recall = tp / (tp + fn)
    print("Recall:", recall)

    # Calculate F1 score
    f1_score = 2 * (precision * recall) / (precision + recall)
    print("F1 Score:", f1_score)

    # Calculate Matthews Correlation Coefficient (MCC)
    mcc = (tp * tn - fp * fn) / math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    print("Matthews Correlation Coefficient (MCC):", mcc)

# Aggregate counts from all confusion matrices
arg_tp = sum(mcm[i][1][1] for i in range(len(labels)))
arg_fn = sum(mcm[i][1][0] for i in range(len(labels)))
arg_fp = sum(mcm[i][0][1] for i in range(len(labels)))
arg_tn = sum(mcm[i][0][0] for i in range(len(labels)))

# Print aggregated counts
print("----------------------------")
print("Aggregated Confusion Matrix:")
print(f"Total True Positives (TP): {arg_tp}")
print(f"Total False Negatives (FN): {arg_fn}")
print(f"Total False Positives (FP): {arg_fp}")
print(f"Total True Negatives (TN): {arg_tn}")

# Calculate general precision
precision = arg_tp / (arg_tp + arg_fp)
print("Aggregated precision:", precision)

# Calculate recall
recall = arg_tp / (arg_tp + arg_fn)
print("Aggregated recall:", recall)

# Calculate F1 score
f1_score = 2 * (precision * recall) / (precision + recall)
print("Aggregated F1 Score:", f1_score)

# Calculate Matthews Correlation Coefficient (MCC)
mcc = (arg_tp * arg_tn - arg_fp * arg_fn) / math.sqrt((arg_tp + arg_fp)
                                                      * (arg_tp + arg_fn) * (arg_tn + arg_fp)
                                                      * (arg_tn + arg_fn))
print("Aggregated Matthews Correlation Coefficient (MCC):", mcc)
