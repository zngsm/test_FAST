# 환경별 변수
# 서버는 운영 서버/ 개발 서버 / qa 수행하는 스테이징 서버도 있고, 로컬 환경도 있다.
# 그때마다 다른 방법으로 설정파일 넣는 것으로 config.py에 하고 consts.py는 어떤 환경에도 변하지 않는 것

from dataclasses import dataclass, asdict
from os import path, environ

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))

@dataclass
class Config:

    BASE_DIR = base_dir

    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True