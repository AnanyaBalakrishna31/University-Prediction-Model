import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import joblib

# Load the data (make sure you replace 'data.csv' with the correct path to your dataset)
df = pd.read_csv('data.csv')

# Preprocessing (this should match what you've already done)
df_with_dummies = pd.get_dummies(df['rank'])
df_new = pd.concat([df, df_with_dummies], axis=1)
df_new = df_new.drop('rank', axis=1)

gre_mean, gre_std = df_new['gre'].mean(), df_new['gre'].std()
gpa_mean, gpa_std = df_new['gpa'].mean(), df_new['gpa'].std()

df_new['gre'] = (df_new['gre'] - gre_mean) / gre_std
df_new['gpa'] = (df_new['gpa'] - gpa_mean) / gpa_std

# Convert column names to strings to avoid the error
df_new.columns = df_new.columns.astype(str)

# Split the data into features and target
features = df_new.drop('admit', axis=1)
target = df_new['admit']

# Train the LDA model
model = LinearDiscriminantAnalysis()
model.fit(features, target)

# Save the model to a file
joblib.dump(model, 'lda_model.pkl')

print("Model saved to lda_model.pkl")
