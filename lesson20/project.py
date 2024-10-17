from typing import Literal
import dotenv
import pydantic
from appium.options.android import UiAutomator2Options
from utils import file


class Config(pydantic.BaseSettings):
    context: Literal['bstack', 'emulator', 'real'] = 'emulator'

    url: str = None
    deviceName: str = None
    udid: str = None
    ignoreHiddenApiPolicyError: bool = None
    appWaitActivity: str = None
    app: str = None
    timeout: float = None
    userName: str = pydantic.Field(None, env=['bs.userName', 'userName'])
    accessKey: str = pydantic.Field(None, env=['bs.accessKey', 'accessKey'])

    def to_driver_options(self):
        options = UiAutomator2Options()

        if self.deviceName:
            options.set_capability('deviceName', self.deviceName)

        if self.udid:
            options.set_capability('udid', self.udid)

        if self.ignoreHiddenApiPolicyError:
            options.set_capability('ignoreHiddenApiPolicyError', self.ignoreHiddenApiPolicyError)

        if self.appWaitActivity:
            options.set_capability('appWaitActivity', self.appWaitActivity)

        options.set_capability('app', (
            self.app if (self.app.startswith('С:\\') or self.app.startswith('bs://'))
            else file.abs_path_from_project(self.app)
        ))

        if self.context == 'bstack':
            options.set_capability('platformVersion', '9.0')
            options.set_capability(
                'bstack:options', {
                    'projectName': 'First Python project',
                    'buildName': 'browserstack-build-1',
                    'sessionName': 'BStack first_test',

                    'userName': self.userName,
                    'accessKey': self.accessKey,
                },
            )

        return options


dotenv.load_dotenv()
config = Config(dotenv.find_dotenv(f'.env.{Config().context}'))
