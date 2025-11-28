def handler(request):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": {"message": "Hola desde Python en Vercel"}
    }