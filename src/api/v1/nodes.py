from fastapi import APIRouter, Depends, HTTPException, Query

from api.authentication import authenticate
from models.node import Node, NodeCreate
from storage.base import AbstractStorage
from storage.main import get_storage


router = APIRouter()


@router.get("")
def read_nodes(
        *,
        storage: AbstractStorage = Depends(get_storage),
        is_user_authorized: str = Depends(authenticate),
):
    """
    Retrieve all nodes
    """

    return storage.get_nodes()


@router.post(
    "",
    response_model=Node
)
def add_node(
        *,
        node: NodeCreate,
        storage: AbstractStorage = Depends(get_storage),
        is_user_authorized: str = Depends(authenticate)
):
    """
    Add new node.
    """
    new_node = storage.add_node(node)

    return new_node


@router.get(
    "/{node_id}",
    response_model=Node
)
def read_node(
        *,
        storage: AbstractStorage = Depends(get_storage),
        node_id: str = Query(
            "",
            title="Node unique identifier",
            description="The node's ID."
        ),
        is_user_authorized: str = Depends(authenticate)
):
    """
    Retrieve a single node by ID.
    Return 404 NOT FOUND if the node does not exist.
    """
    node = storage.get_node(node_id)

    if not node:
        raise HTTPException(status_code=404, detail="Node not found")

    return node
