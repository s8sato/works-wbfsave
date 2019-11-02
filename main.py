from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import sys

# コマンドライン引数の設計
# python main.py scroll sleep whiteboard
scroll = sys.argv[1]  # 1回のスクロール量
sleep = sys.argv[2]  # 次のスクロールまでの休止時間（秒）
whiteboard = sys.argv[3]  # キャプチャ対象のホワイトボードID

driver = webdriver.Chrome()


def initialize():
    # 指定のホワイトボードを開く
    driver.get("https://whiteboardfox.com/{}".format(whiteboard))

    # 「移す」ボタンがクリックできる状態になるまで最大10秒待機
    move_button = "/html/body/div[2]/div[2]/div/div[2]/div/div[12]/div"
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, move_button)))

    # 「移す」ボタンをクリック
    element = driver.find_element_by_xpath(move_button)
    element.click()


def main():
    print("Prepare Screenpresso scroll mode.")
    if is_ready():
        print("Left-click during every sleep.")
        print("Right-click and press Ctrl+C at the end of your picture.")
        scroll_and_sleep()
    else:
        main()
    # driver.quit()


def is_ready():
    answer = input("Are you ready?\n: ")
    return answer[:1] in "Yy"


def scroll_and_sleep():
    actions = ActionChains(driver)
    element = driver.find_element_by_id("canvasId")
    actions.pause(int(sleep))
    actions.drag_and_drop_by_offset(element, 0, (-1) * int(scroll))
    actions.perform()
    scroll_and_sleep()


if __name__ == '__main__':
    initialize()
    main()
