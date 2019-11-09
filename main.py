import gather as ga
import concat as co
import json
import sys


def main(config, wtb, out):

    with open(config) as f:
        cfg = json.load(f)

    scr = cfg['gather']['scr']  # 1回のスクロール量
    slp = cfg['gather']['slp']  # 次のスクロールまでの休止時間（秒）
    rat = cfg['concat']['rat']  # スクロール量に対する、クリップ領域の縦幅の比率
    top = cfg['concat']['top']
    lef = cfg['concat']['lef']
    rig = cfg['concat']['rig']

    ga.main(config, scr, slp, wtb, 0)
    co.main(config, rat, top, lef, rig, out)


if __name__ == '__main__':
    print("Hello!")

    # python main.py whiteboard output
    wtb = sys.argv[1]  # キャプチャ対象のホワイトボードID
    out = sys.argv[2]  # 出力ファイル名

    main('config.json', wtb, out)
    print("See you!")
