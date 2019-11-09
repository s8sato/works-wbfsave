from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import sys
import os
import json
import glob

with open('config.json') as f:
    c = json.load(f)


def initialize(driver, whiteboard):
    # 指定のホワイトボードを開く
    driver.get('https://whiteboardfox.com/{}'.format(whiteboard))
    # 「移す」ボタンがクリックできる状態になるまで最大10秒待機
    move_button = '/html/body/div[2]/div[2]/div/div[2]/div/div[12]/div'
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, move_button)))
    # 「移す」ボタンをクリック
    element = driver.find_element_by_xpath(move_button)
    element.click()


def main(driver, scroll, sleep, count):
    if is_ready():
        print("Ctrl+C at the end of your picture.")
        shot_and_scroll(driver, scroll, sleep, count)
    else:
        main(driver, scroll, sleep, count)


def is_ready():
    answer = input("Are you ready?\n: ")
    return answer[:1] in 'Yy'


def shot_and_scroll(driver, scroll, sleep, count):
    if count == 0:
        sweep_tempshots()
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            c['temporary_shots_dir'],
                            c['temporary_shot_prefix'] + '{:03}.png'.format(count))
    driver.save_screenshot(filename)
    actions = ActionChains(driver)
    element = driver.find_element_by_id('canvasId')
    actions.drag_and_drop_by_offset(element, 0, (-1) * scroll)
    actions.pause(sleep)
    actions.perform()
    shot_and_scroll(driver, scroll, sleep, count + 1)


def sweep_tempshots():
    name_pattern = os.path.join(c['temporary_shots_dir'],
                                c['temporary_shot_prefix'] + '*.png')
    tempshots = glob.glob(name_pattern)
    for tempshot in tempshots:
        os.remove(tempshot)


if __name__ == '__main__':
    """直接に実行されたときの処理"""
    print("Hello!")
    # コマンドライン引数の設計
    # python gather.py scroll sleep whiteboard count
    scr = int(sys.argv[1])  # 1回のスクロール量
    slp = int(sys.argv[2])  # 次のスクロールまでの休止時間（秒）
    wtb = sys.argv[3]  # キャプチャ対象のホワイトボードID
    cnt = int(sys.argv[4])  # 一時保存ファイル名の連番の開始位置

    drv = webdriver.Chrome()

    try:
        initialize(drv, wtb)
    except KeyboardInterrupt:
        print("Ctrl+C pressed.")
        print("Now terminating driver...")
        drv.quit()
        print("Bye!")
        sys.exit()
    try:
        main(drv, scr, slp, cnt)
    except KeyboardInterrupt:
        print("Ctrl+C pressed.")
        print("{} screenshots saved.".format("some"))
        print("Now terminating driver...")
    finally:
        drv.quit()
        print("Bye!")

