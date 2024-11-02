from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any
from fastapi.middleware.cors import CORSMiddleware

from utils.graph import isDag

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}

class Node(BaseModel):
    id: str
    type: str
    position: Dict[str, float]
    data: Dict[str, Any]
    width: int
    height: int

class Edge(BaseModel):
    source: str
    sourceHandle: str
    target: str
    targetHandle: str
    type: str
    animated: bool
    markerEnd: Dict[str, str]
    id: str

class PipelineData(BaseModel):
    nodes: List[Node]
    edges: List[Edge]

@app.post('/pipelines/parse')
async def parse_pipeline(data: PipelineData):
    numNodes = len(data.nodes)
    numEdges = len(data.edges)
    dagCheck = isDag(data.nodes, data.edges)
    return {'num_nodes': numNodes, 'num_edges': numEdges, 'is_dag':  dagCheck }
