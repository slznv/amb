from typing import Optional

from pydantic import BaseModel


class NodeCreate(BaseModel):
    name: str
    attr: Optional[str] = None


class Node(NodeCreate):
    id: str
