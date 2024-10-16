import pydantic
import dotenv


class Config(pydantic.BaseSettings):
    userName: str = pydantic.Field(None, env=['BSTACK_USERNAME', 'userName'])
    accessKey: str = pydantic.Field(None, env=['BSTACK_ACCESSKEY', 'accessKey'])
    remote_url: str = pydantic.Field(None, env=['BSTACK_URL', 'remoteUrl'])


config = Config(dotenv.find_dotenv('.env'))
