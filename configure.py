import json
import sys


def main(config):
    with open(config) as f:
        c = json.load(f)
    if sys.argv[1] == 'gather':
        c['gather']['scr'] = int(sys.argv[2])  # 1回のスクロール量
        c['gather']['slp'] = int(sys.argv[3])  # 次のスクロールまでの休止時間（秒）
        with open(config, 'w') as f:
            json.dump(c, f, indent=2)
        print("Config has been modified:")
        print(json.dumps(c['gather']))
    elif sys.argv[1] == 'concat':
        c['concat']['rat'] = float(sys.argv[2])  # スクロール量に対する、クリップ領域の縦幅の比率
        c['concat']['top'] = int(sys.argv[3])
        c['concat']['lef'] = int(sys.argv[4])
        c['concat']['rig'] = int(sys.argv[5])
        with open(config, 'w') as f:
            json.dump(c, f, indent=2)
        print("Config has been modified:")
        print(json.dumps(c['concat']))
    else:
        print("Wrong argument: {}".format(sys.argv[1]))
        main(config)
    print("See you!")


if __name__ == '__main__':
    main('config.json')
