import allure
import requests
from selene import browser

import project


def allure_png():
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )


def allure_xml():
    allure.attach(
        browser.driver.page_source,
        name='screen xml dump',
        attachment_type=allure.attachment_type.XML
    )


def allure_video(session_id):
    response = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(project.config.userName, project.config.accessKey),
    ).json()

    video_url = response['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )
