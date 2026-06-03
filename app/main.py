from fastapi import FastAPI

app = FastAPI(title='Raghav Jarvis AI')

@app.get('/')
def root():
    return {'assistant':'Raghav Jarvis AI','status':'online'}

@app.get('/health')
def health():
    return {'status':'healthy'}
