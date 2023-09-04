from fastapi import FastAPI
import uvicorn
import requests

app = FastAPI()

@app.get("/")
def norma_root():
    return { "Message": "Welcome to python" }

@app.get("/express")
def express():
    resp = requests.get('http://k8s-web-hello:3000/fastapi')
    return {'res':resp.text}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
