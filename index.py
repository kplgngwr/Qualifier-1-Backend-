from app import app

# This is for Vercel serverless deployment
handler = app

def handler(request):
    """
    Vercel serverless function handler
    """
    return app(request) 