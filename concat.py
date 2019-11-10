import cv2
import os
import sys
import glob
import img2pdf
import json


def clip(name_pattern, top, bot, lef, rig):
    """:return [image]"""
    images = glob.glob(name_pattern)
    return [cv2.imread(image)[top:bot, lef:rig] for image in images]


def save(filename, image, tmp_img_for_pdf):
    ext = filename[-4:]
    if ext in ['.png', '.jpg']:
        cv2.imwrite(filename, image)
        return True
    elif ext == '.pdf':
        cv2.imwrite(tmp_img_for_pdf, image)
        with open(filename, 'wb') as f:
            f.write(img2pdf.convert(tmp_img_for_pdf))
            os.remove(tmp_img_for_pdf)
        return True
    else:
        print("Wrong output extension name: {}".format(ext))
        return False


def main(config, rat, top, lef, rig, out):
    with open(config) as f:
        cfg = json.load(f)
    bot = int(top + cfg['gather']['scr'] * rat)
    name_pattern = os.path.join(cfg['temporary_shots_dir'],
                                cfg['temporary_shot_prefix'] + '*.png')
    images = clip(name_pattern, top, bot, lef, rig)
    out_file = os.path.join(cfg['out_dir'], out)
    if save(out_file,
            cv2.vconcat(images),
            cfg['temporary_img_for_pdf']):
        print("Successfully {} images are clipped and concatenated to: ".format(len(images)))
        print(out_file)
    else:
        print("Failed to create image.")


if __name__ == '__main__':
    print("Hello!")

    # python concat.py ratio top left right output
    rat = float(sys.argv[1])  # スクロール量に対する、クリップ領域の縦幅の比率
    top = int(sys.argv[2])
    lef = int(sys.argv[3])
    rig = int(sys.argv[4])
    out = sys.argv[5]  # 出力ファイル名

    main('config.json', rat, top, lef, rig, out)
    print("Bye!")
