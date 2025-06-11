import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.neighbors import NearestNeighbors
import joblib
import os


# Create models directory if it doesn't exist
os.makedirs('models', exist_ok=True)


print("📥 Loading dataset...")
# Load updated dataset
df = pd.read_csv('data/job_dataset.csv')


# Validate required columns
required_columns = ['job_title', 'skills', 'description', 'salary']
missing_cols = [col for col in required_columns if col not in df.columns]
if missing_cols:
    raise ValueError(f"Missing required columns in dataset: {missing_cols}")


# Clean and prepare skills text for embedding
df['skills_str'] = df['skills'].str.replace(';', ' ', regex=False)


print("🤖 Loading Sentence Transformer model...")
# Load pre-trained Sentence-BERT model
bert_model = SentenceTransformer('all-MiniLM-L6-v2')


print("🧠 Encoding job skill sets into embeddings...")
# Generate sentence embeddings for each job's skill list
X = bert_model.encode(df['skills_str'].tolist(), show_progress_bar=True)


print("🔧 Training Nearest Neighbors model...")
# Train Nearest Neighbors model using cosine similarity
nn_model = NearestNeighbors(n_neighbors=5, metric='cosine')
nn_model.fit(X)


print("💾 Saving trained models and data...")
# Save the trained models and dataset
joblib.dump(nn_model, 'models/job_recommender.pkl')
joblib.dump(bert_model, 'models/bert_model.pkl')
joblib.dump(df, 'models/job_data.pkl')


print("✅ Training complete. All models saved to /models.")
