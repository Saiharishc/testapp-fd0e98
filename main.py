from fastapi import FastAPI

app = FastAPI()

@app.get('/api/test')
def test_endpoint():
    return {'message': 'Backend is running!'}

@app.get('/')
def root():
    return {'message': 'Welcome to the API!'}
