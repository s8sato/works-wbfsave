import cv2
import os
import sys
import glob
import img2pdf
import json


def clip(image_name_pattern, top, bot, lef, rig):
    """:return [image]"""
    images = glob.glob(image_name_pattern)
    return [cv2.imread(image)[top:bot, lef:rig] for image in images]


def save(filename, image, tmp_img_for_pdf):
    ext = filename[-4:]
    if ext in ['.png', '.jpg']:
        cv2.imwrite(filename, image)
    elif ext == '.pdf':
        cv2.imwrite(tmp_img_for_pdf, image)
        with open(filename, 'wb') as f:
            f.write(img2pdf.convert(tmp_img_for_pdf))
            os.remove(tmp_img_for_pdf)
    else:
        print("boo!")


if __name__ == '__main__':
    print("Hello!")
    with open('config.json') as f:
        c = json.load(f)
    # python concat.py ratio top left right output
    rat = float(sys.argv[1])  # スクロール量に対する、クリップ領域の縦幅の比率
    top = int(sys.argv[2])
    bot = int(top + c['scr'] * rat)
    lef = int(sys.argv[3])
    rig = int(sys.argv[4])
    out = sys.argv[5]  # 出力ファイル名

    image_name_pattern = os.path.join(c['temporary_shots_dir'], c['temporary_shot_prefix'] + '*.png')
    images = clip(image_name_pattern, top, bot, lef, rig)

    out_file = os.path.join(c['out_dir'], out)
    save(out_file,
         cv2.vconcat(images),
         c['temporary_img_for_pdf'])
    print("Successfully {} images are clipped and concatenated to: ".format(len(images)))
    print(out_file)
    print("Bye!")
