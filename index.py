# filepath: /c:/Users/Acer/Desktop/React Projects/Qualifier 1/my-backend-app/index.py
from app import create_app

app = create_app()

# This is for Vercel serverless deployment
handler = app