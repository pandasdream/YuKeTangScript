import json
import os
import time

import pyautogui
import requests

config = json.loads(open("./conf.txt", "r", encoding="utf-8").read())
wp = open("./log.txt", "w", encoding="utf-8")

'''get_page_status function returns a dic:
{
    "index": {
        "first_point": float,
        "last_point": float,
        "completed": int,
        "watch_length": int,
        "ult": float,
        "rate": float,
        "video_length": float
    }
}'''
def get_video_status(index):
    url_upper = "https://buaa.yuketang.cn/video-log/get_video_watch_progress/?cid=" + config.get(
        "cid") + "&user_id=" + config.get("user_id") + "&classroom_id=" + config.get(
        "classroom_id") + "&video_type=video&vtype=rate&video_id="
    url_latter = "&snapshot=1&term=latest&uv_id=" + config.get("uv_id")
    url = url_upper + str(index) + url_latter
    header = {
        "User-Agent": config.get("user_agent"),
        "Cookie": config.get("cookie")}
    response = requests.request("GET", url=url, headers=header)
    log(response.text)
    js_res = json.loads(response.text)
    return js_res.get('data')


'''
get_page_type function returns a dic:
{
    "msg": "",
    "data": {
        "leaf_type": int value: 0-video, 3-pdf, 4-discussion, 6-quiz
    }
}
'''
def get_page_type(index):
    url = config.get("get_page_type_upper") + str(index) + config.get("get_page_type_latter")
    header = {
        "User-Agent": config.get("user_agent"),
        "Cookie": config.get("cookie"),
        "Xtbz": "cloud"
    }
    response = requests.request('GET', url=url, headers=header)
    log(response.text)
    return response.json().get('data').get('leaf_type')


def ctrl_w():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('w')
    pyautogui.keyUp('w')
    pyautogui.keyUp('ctrl')


def ctrl_t():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('t')
    pyautogui.keyUp('t')
    pyautogui.keyUp('ctrl')


def log(info):
    print(time.strftime("%Y-%m-%d %H:%M:%S----", time.localtime()) + info)
    wp.write(time.strftime("%Y-%m-%d %H:%M:%S----", time.localtime()) + info + "\n")


def auto_study(start):
    def play():
        # TODO async video play check
        pyautogui.keyDown('space')
        pyautogui.keyUp('space')
        log("video starts to play")

    video_index = start
    error_counting = 0
    while error_counting < 10 and video_index < 38132693:
        page_type = get_page_type(video_index)
        log(str(video_index) + " type:" + str(page_type))
        if page_type == 0:
            os.system("start " + config.get("start_url") + str(video_index))
            time.sleep(6)
            ctrl_t()
            time.sleep(1.5)
            ctrl_w()
            time.sleep(0.5)
            play()
            data = get_video_status(video_index)
            if str(video_index) not in data:
                error_counting = error_counting + 1
                ctrl_w()
                log("exception occurs " + str(error_counting))
                continue
            error_counting = 0
            video_length = data.get(str(video_index)).get('video_length')
            log('时长：' + str(video_length) + 's')
            time.sleep(video_length / 2)
            ctrl_w()
        video_index = video_index + 1
        time.sleep(1)


# 38132375 第一章
start = config.get("start_video_id")
auto_study(start=start)
