from fastapi import APIRouter

from api.v1 import nodes

# Let's define some default responses
responses = {
    404: {"description": "Entity not found"},
    401: {"description": "Unauthorized"},
}


api_router = APIRouter(responses={**responses})
api_router.include_router(nodes.router, prefix="/nodes", tags=["nodes"])
