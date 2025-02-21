from app import app

def handler(request):
    return app(request)

# This is for Vercel serverless deployment 