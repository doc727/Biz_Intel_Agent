import os
import pandas as pd
from dotenv import load_dotenv
import google.generativeai as genai

# Load your .env key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load CSV
df = pd.read_csv("data/jobs.csv")

# Prepare prompt
job_titles = df["title"].head(10).tolist()
prompt = "Summarize the following job titles:\n" + "\n".join(job_titles)

# Use correct model and method
model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content(prompt)

print("🧠 Summary:")
print(response.text)