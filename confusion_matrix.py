import json
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from multi_lable_confusionMatrix import labels

# Read data from JSON file
with open('merged.json', 'r') as f:
    data = json.load(f)

# Accessing the "model1", "model2", "model3" key from the data
model1_data = data.get("model1", [])

# Extracting the values of the "marked_object" and "predicted_object" keys
y_true = [item.get("marked_object") for item in model1_data]
y_pred = [item.get("predicted_object") for item in model1_data]

# Define the classes (unique labels)
classes = sorted(set(y_true + y_pred))

# Compute the confusion matrix
cm = confusion_matrix(y_true, y_pred, labels=classes)

# Print the confusion matrix
print("Confusion Matrix:")
print(cm)

# Compute confusion matrix
cm = confusion_matrix(y_true, y_pred, labels=labels)

# Plot confusion matrix
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')
plt.show()
