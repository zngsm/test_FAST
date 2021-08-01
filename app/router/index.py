from datetime import datetime
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import Response
from app.database.conn import db
from app.database.schema import Users

router = APIRouter()

@router.get("/")
async def index(session: Session = Depends(db.session),):
    """
    ELB 상태 체크용 API
    :return:
    """

    """
    유저 생성시
    user = Users(status="active")
    session.add(user)
    session.commit()
    이와 같이 생성할 수 있으나.. 
    번거롭기 때문에 schema 의 create 함수를 선언하여 사용하겠다!
    """

    Users().create(session, auto_commit=True, name="코알라")
    current_time = datetime.utcnow()
    return Response(f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')}")