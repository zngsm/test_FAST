# 환경별 변수 django의 settings.py ..!!
# 서버는 운영 서버/ 개발 서버 / qa 수행하는 스테이징 서버도 있고, 로컬 환경도 있다.
# 그때마다 다른 방법으로 설정파일 넣는 것으로 config.py에 하고 consts.py는 어떤 환경에도 변하지 않는 것


from dataclasses import dataclass, asdict
from os import path, environ

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))

# dataclass 데코레이터 달고 있을 경우 해당 클래스를 dict 형태로 추추해서 쓸 수 있다.
@dataclass
class Config:
    """
    기본 configuration
    """
    BASE_DIR = base_dir

    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True


@dataclass
class LocalConfig(Config):
    PROJ_RELOAD: bool = True

@dataclass
class ProdConfig(Config):
    PROJ_RELOAD: bool = False
    DB_URL: str="mysql+pymysql://root:zngsm05051629315^^@localhost:3306/test_fast?charset=utf8"

# print(LocalConfig().DB_ECHO)
# True 출력

def abc(DB_ECHO=None, DB_POOL_RECYCLE=None, **kwargs):
    print(DB_ECHO, DB_POOL_RECYCLE)

abc(LocalConfig())
# LocalConfig(DB_POOL_RECYCLE=900, DB_ECHO=True, PROJ_RELOAD=True) None 출력

print(asdict(LocalConfig()))
# {'DB_POOL_RECYCLE': 900, 'DB_ECHO': True, 'PROJ_RELOAD': True}
# 위의 abc를 이용해 출력했을 경우는 객체형태로 출력되지만, asdict로 출력하면 데코레이터를 붙여줬기 때문에 dict 형태로 출력할 수 있다.
arg = asdict(LocalConfig())
abc(arg)
# {'DB_POOL_RECYCLE': 900, 'DB_ECHO': True, 'PROJ_RELOAD': True} None
abc(**arg)
# True 900

def conf():
    """
    환경 불러오기
    :return:
    """
    config = dict(prod=ProdConfig(), local=LocalConfig())
    return config.get(environ.get("API_ENV", "local"))
