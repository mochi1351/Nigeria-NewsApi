from uuid import UUID
from typing import Optional, Any
from pydantic import BaseModel


class NewsSchema(BaseModel):
    uuid : UUID
    source: Optional[str]




class NewsArticleScrapeEventDetailSchema(BaseModel):
    title: Optional[str]
    author_name: Optional[str]
    description: Optional[str]
    url: Optional[str]
    urlImage: Optional[str]
    published: Optional[Any] = None
    content: Optional[str]


    
    


   