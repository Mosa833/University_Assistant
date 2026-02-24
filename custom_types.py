import pydantic 


class RAGChunkAndSRC(pydantic.BaseModel): # results after we chunked the docs
    chunks: list[str]
    source_id: str = None


class RAGUpsertResult(pydantic.BaseModel): #result after we upsert the docs
    ingested: int # how many texts we have ingested


class RAGSearchResult(pydantic.BaseModel): # searching for some texts
    contexts: list[str]
    sources: list[str]


class RAGQueryResult(pydantic.BaseModel): #quesry that the users will send to the endpoint
    answer: str
    sources: list[str]
    num_contexts: int
