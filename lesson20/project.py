from typing import Literal
import dotenv
import pydantic
from appium.options.android import UiAutomator2Options
from utils import file


class Config(pydantic.BaseSettings):
    context: Literal['bstack', 'emulator', 'real'] = 'emulator'

    url: str = None
    device_name: str = None
    udid: str = None
    ignore_hidden_api_policy_error: bool = None
    app_wait_activity: str = None
    app: str = None
    timeout: float = None
    user_name: str = pydantic.Field(None, env=['bs.userName', 'userName'])
    access_key: str = pydantic.Field(None, env=['bs.accessKey', 'accessKey'])

    def to_driver_options(self):
        options = UiAutomator2Options()

        if self.device_name:
            options.set_capability('deviceName', self.device_name)

        if self.udid:
            options.set_capability('udid', self.udid)

        if self.ignore_hidden_api_policy_error:
            options.set_capability('ignoreHiddenApiPolicyError', self.ignore_hidden_api_policy_error)

        if self.app_wait_activity:
            options.set_capability('appWaitActivity', self.app_wait_activity)

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

                    'userName': self.user_name,
                    'accessKey': self.access_key,
                },
            )

        return options


dotenv.load_dotenv()
config = Config(dotenv.find_dotenv(f'.env.{Config().context}'))
