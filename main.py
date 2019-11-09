import gather as ga
import concat as co
import json
import sys
import os


def main(config):
    print("Hello!")
    # python main.py whiteboard output
    wtb = sys.argv[1]  # キャプチャ対象のホワイトボードID
    out = sys.argv[2]  # 出力ファイル名

    with open(config) as f:
        c = json.load(f)
    scr = c['gather']['scr']  # 1回のスクロール量
    slp = c['gather']['slp']  # 次のスクロールまでの休止時間（秒）
    rat = c['concat']['rat']  # スクロール量に対する、クリップ領域の縦幅の比率
    top = c['concat']['top']
    bot = int(top + scr * rat)
    lef = c['concat']['lef']
    rig = c['concat']['rig']

    drv = ga.webdriver.Chrome()

    try:
        ga.initialize(drv, wtb)
    except KeyboardInterrupt:
        print("Ctrl+C pressed.")
        print("Now terminating driver...")
        drv.quit()
        print("Bye!")
        sys.exit()
    try:
        ga.main(drv, scr, slp, 0)
    except KeyboardInterrupt:
        print("Ctrl+C pressed.")
        print("{} screenshots saved.".format("some"))
        print("Now terminating driver...")
    finally:
        drv.quit()

    image_name_pattern = os.path.join(c['temporary_shots_dir'], c['temporary_shot_prefix'] + '*.png')
    images = co.clip(image_name_pattern, top, bot, lef, rig)

    out_file = os.path.join(c['out_dir'], out)
    co.save(out_file,
            co.cv2.vconcat(images),
            c['temporary_img_for_pdf'])
    print("Successfully {} images are clipped and concatenated to: ".format(len(images)))
    print(out_file)
    print("See you!")


if __name__ == '__main__':
    main('config.json')
