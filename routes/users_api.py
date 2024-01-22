# - document class : models.users.py
# - 회원가입(post : /), 로그인(get : /{id}/{pswd}), 회원탈퇴(delete : /{id})
# - option : 회원 수정(put : /{id})

from typing import List

from beanie import PydanticObjectId
from databases.connections import Database
from fastapi import APIRouter, Depends, HTTPException, status
from models.users import User

router = APIRouter(
    tags=["users"]
)

user_database = Database(User)

# 회원가입(post : /) = 새로운 레코드(row) 생성
@router.post("/new")
async def create_event(body: User) -> dict:
    document = await user_database.save(body)
    return {
        "message": "User created successfully"
        ,"datas": document
    }
    
# 로그인(get : /{id}/{pswd}) = id 기준으로 한 경우 row 확인하기
@router.get("/{id}", response_model=User)
async def retrieve_user_id(id: PydanticObjectId) -> User:
    user_id = await user_database.get(id)
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Uesr with supplied ID does not exist"
        )
    return user_id

@router.get("/{pswd}", response_model=User)
async def retrieve_user_pswd(id: PydanticObjectId) -> User:
    user_pswd = await user_database.get(id)
    if not user_pswd:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Uesr with supplied pswd does not exist"
        )
    return user_pswd

    
# 회원탈퇴(delete : /{id}) = id에 따른 row 삭제
@router.delete("/{id}")
async def delete_User(id: PydanticObjectId) -> dict:
    user_del = await user_database.get(id)
    if not user_del:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    user_del = await user_database.delete(id)

    return {
        "message": "User deleted successfully."
        ,"datas": user_del
    }

# 회원 수정(put : /{id}) = row 업데이트
from fastapi import Request
@router.put("/{id}", response_model=User)
async def update_user_withjson(id: PydanticObjectId, request:Request) -> User:
    user_update = await user_database.get(id)
    if not user_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    body = await request.json()
    user_update = await user_database.update_withjson(id, body)
    if not user_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with supplied ID does not exist"
        )
    return user_update

# 전체 내용 가져오기(mongoDB에 있는 모든정보를 postman으로 보여줘)
@router.get("/")
async def retrieve_all_users() -> dict:
    user = await user_database.get_all()
    return {"total_count" : len(user)
            , 'datas' : user}