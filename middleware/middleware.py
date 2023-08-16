from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from redis import Redis
from datetime import datetime


class CollectMiddleware(BaseHTTPMiddleware):
    def __init__(self,app,redis_host: str, redis_port: str):
        
        super().__init__(app)
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.redis = Redis(self.redis_port, redis_host)

    async def dispatch(self, request: Request, call_next):
        # do something with the request object, for example
        # i want to collect data from Request object to redisTimeseris with this midddleware

        client_host = request.client.host
        request_path = request.url.path
        request_methode = request.method
        schema_request = request.url.scheme
        content_type = request.headers.get('Content-Type')
        user_agent = request.headers.get("user-agent")
        host = request.headers.get("host")
        connection = request.headers.get("connection")
        content_length = request.headers.get("content-length")
        referer = request.headers.get("referer")
        accept_encoding = request.headers.get("accept-encoding")
        origin = request.headers.ge("origin")
        header_request = request.headers
        request_port = request.url.port
        query_parametre_request = request.query_params
        path_parametre_request = request.path_params
        cokies_request = request.cookies
        # boby_request = await request.json()

        time = datetime.now()

        content_type = request.headers.get('Content-Type')
        print(f"content_type: {content_type}, client_host: {client_host}, request_path : {request_path}, request_methode: {request_methode }, schema_request : {schema_request}, header_request : {header_request}, request_port : {request_port}, query_parametre_request : {query_parametre_request} path_parametre_request : {path_parametre_request}, cokies_request : {cokies_request}, user_agent: {user_agent}, host : {host}, connection : {connection}, referer : {referer}, content_length : {content_length} accept-encoding : {accept_encoding} origin: {origin}")
        
        # process the request and get the response    
        response = await call_next(request)
        
        return response
