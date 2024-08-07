from enum import Enum
from typing import Optional
from fastapi import FastAPI, status, Response, APIRouter

router = APIRouter(prefix='/blog', tags=['blog'])


class TypeBlog(str, Enum):
    m1 = 'mesal1'
    m2 = 'mesal2'
    m3 = 'mesal3'


@router.get("/type/{type}", summary='dryaft blog ha !', )
def get_type(type: TypeBlog):
    """
    api baray daryaft api hastesh

    **id**  baray daryaft id blog
    """

    return {'message': f'blog type is {type}'}


@router.get("/{id}/comments/{comment_id}/", tags=['comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {"messages": f"blog id {id} comment id {comment_id} {valid=} {username=}"}


@router.get('/t/{id}/', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message': f'blog id {id} not found ! '}
    return {'message': f'blog id {id} found'}