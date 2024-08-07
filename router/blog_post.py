from typing import Optional, List, Dict

from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel

router = APIRouter(prefix='/blog', tags=['blog'])


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]
    tags : List[str]
    metadata : Dict[str, str] = {'key1': 'value1'}
    image: Image


@router.post('/new/')
def create_post(blog: BlogModel):
    return {'message': 'OK', 'data': blog}


@router.post('/new/{id}/comment/{comment_id}')
def create_comment(id: int, blog: BlogModel,
                   comment_title:int = Query(None,
                          title= 'title text',
                          description = 'description text !',
                          alias='CommentTitle',
                          deprecated=True),
                   content:str = Body(...,  # str validator
                                      min_length=8,
                                      max_length=20,
                                      regex='^[A-Z].*'),
                   v:Optional[List[str]]= Query(None),
                   comment_id:int = Path(..., gt=5)
                   ):
    return {
        'blog': blog,
        'comment_id': comment_id,
        'id': id,
        'content':content,
        'version':v,
        'comment_title':comment_title,
    }