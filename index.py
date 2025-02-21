from app import app

def handler(request):
    """
    Vercel serverless function handler
    """
    return app(request)

# This is for Vercel serverless deployment 