from fastapi import FastAPI
from middleware import ExceptionHanlerMiddleware, SignatureMiddleware
import uvicorn

app = FastAPI(
        openapi_url='/norma/api/v1/openapi.json', docs_url='/norma/api/docs'
    )

app.add_middleware(SignatureMiddleware)
app.add_middleware(ExceptionHanlerMiddleware)

@app.get('/')
def contact_norma_for_more_details():
    return { 'Message': 'Join Norm and learn more' }


@app.get('/norma/with_extra_heasers')
def norma_login():
    return { 'Message': 'Join Norm and learn more' }

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)
