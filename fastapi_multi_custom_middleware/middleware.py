from traceback import print_exception
from typing import Any, Coroutine
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint


class SignatureException(HTTPException):
    def __init__(self, status_code: int, detail: Any = None) -> None:
        super().__init__(status_code, detail)

class ExceptionHanlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(
            self,
            request: Request,
            call_next: RequestResponseEndpoint
        ) -> Coroutine[Any, Any, Response]:
        try:
            return await call_next(request)
        except SignatureException as e:
            print_exception(e)
            return JSONResponse(status_code=e.status_code, content={'error': e.detail})
        except HTTPException as http_exception:
            return JSONResponse(
                status_code=http_exception.status_code,
                content={'error': 'Client Error', 'message': str(http_exception.detail)},
            )
        except Exception as e:
            print_exception(e)
            return JSONResponse(
                status_code=500,
                content={
                    'error': e.__class__.__name__,
                    'messages': e.args
                }
            )


class SignatureMiddleware(BaseHTTPMiddleware):
    async def dispatch(
            self,
            request: Request,
            call_next: RequestResponseEndpoint
        ) -> Coroutine[Any, Any, Response]:
        if request.scope['path'] in ['/norma/api/docs', '/norma/api/v1/openapi.json']:
            return await call_next(request)
        if request.scope['path'] == '/norma/with_extra_heasers':
            required_headers = ['X-Signature', 'X-identifier']
            headers = [True for x in required_headers if x in request.headers]
            if len(headers) < len(required_headers):
                return JSONResponse(
                    status_code=409,
                    content={'error': f'Header {required_headers} is missing'}
                )
            encrypted_message = request.headers['X-identifier']
            signature = request.headers['X-signature']
            # you can add any logic to validate encrypted message and signature
            print(encrypted_message, signature)
        response = await call_next(request)
        return response
