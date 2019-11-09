# これは何？

一行でいうと  
**WhiteboardFoxによる縦長の板書を良画質保存するツール**  
です

以下、OSはWindows10、ブラウザはChromeを仮定します

[WhiteboardFox][WhiteboardFox]という素晴らしいフリーのWebホワイトボードサービスがあります  
この板書を**参照性のために画像として保存したい**方も少なくないと思うのですが  
標準の保存機能では[この程度][before]の画質しか実現しません

当ツールはWhiteboardFoxによる縦長の板書を[良画質][after]で保存します

# 導入に要する時間

PCはネットサーフィンくらいにしか使わないという方でも **30分** で導入できます

# 導入方法

0.  MinicondaまたはAnacondaのインストールがお済みの方は  
    [Make Project and Environment](#make-project-and-environment)から始めてください

    ## Conda Installation

2.  `Windows`+`S`キーを押し検索ボックスに`sys`と入力、候補に出た`システム情報`を開き  
    `システムの種類`が`x64-ベース PC`であることを確認します

3.  [Miniconda][Miniconda]のページから`Miniconda3 Windows 64-bit`をダウンロードし起動、  
    指示に従ってインストールします

    ## Make Project and Environment

4.  `Windows`+`S`キーを押し検索ボックスに`ana`と入力、候補に出た`Anaconda Prompt`を開き  
    次の例のとおりに入力します
    ```
    (base) C:\Users\satun>
    (base) C:\Users\satun> mkdir tools
    (base) C:\Users\satun> cd tools
    (base) C:\Users\satun\tools> mkdir wbfsave
    (base) C:\Users\satun\tools> cd wbfsave
    (base) C:\Users\satun\tools\wbfsave>
    ```
    以降、上記最終行を`(base)>`と略記します
    ```
    (base)> conda create -n wbfsave selenium chromedriver-binary opencv 
    (base)> activate wbfsave
    (wbfsave)> pip install img2pdf
    ```

5.  このページの`Clone or download`から`Download ZIP`を選択しダウンロードしたZIPを右クリック、  
    `すべて展開`し`works-wbfsave-master`以下を先に作成した`tools\wbfsave`以下にコピーします

    ![Download ZIP](images/download_zip.PNG)

    ## The First Configuration G

6.  素材（スクリーンショット）集めに関する初期設定を行います  
    `Anaconda Prompt`に戻り、次の例のとおり入力します
    ```
    (wbfsave)> python gather.py 360 1 666666-4444-4444 0
    ```
    ただし、`360`としたのは1回のスクロール量、`1`としたのはスクロールごとの休止時間（秒）、  
    `666666-4444-4444`としたのは適当なホワイトボードのURL末尾のID、  
    `0`としたのは一時保存ファイル名の連番の開始位置です
    ```
    Hello!
    ```
    との表示とともにChromeウィンドウが立ち上がります  
    ウィンドウを最大化し、板書が表示されたら適度なスケールに調整し、スタート位置に移動します

7.  `Anaconda Prompt`に戻り、`y`と入力します
    ```
    Are you ready?
    : y
    Ctrl+C at the end of your picture.
    ```

8.  板書の末尾までスクロールしたら`Ctrl+C`を入力します
    ```
    Ctrl+C pressed.
    some screenshots saved.
    Now terminating driver...
    Bye!
    ```

9.  スクロール量と休止時間を変更したい場合は再び
    [同手順](#the-first-configuration-g)
    を行います
    
10. スクロール量と休止時間がこれで良ければ次の例のように入力します
    ```
    (wbfsave)> python configure.py gather 360 1
    ```

11. 次のように表示されれば初期設定の前半は完了です！
    ```
    Config has been modified:
    {"scr": 360, "slp": 1}
    See you!
    ```

    ## The First Configuration C

12. 集めた素材のトリミングと結合に関する初期設定を行います  
    `Anaconda Prompt`に次の例のとおり入力します
    ```
    (wbfsave)> python concat.py 2.000 100 150 2650 out.pdf
    ```
    ただし、`2.000`としたのはスクロール量に対する縦のトリミング量の比率、  
    `100` `150` `2650`としたのはそれぞれ上、左、右のトリミング座標、    
    `out.pdf`としたのは結合の成果ファイル名で、拡張子は他に`png` `jpg`が可能です

13. 次の表示があり`storage`ディレクトリ以下に結合ファイルが生成されるので、確認してください
    ```
    Successfully 17 images are clipped and concatenated to:
    storage\out.pdf
    ```

14. 納得するまで[同手順](#the-first-configuration-c)を繰り返して各数値を調整します

15. 納得したら次の例のように入力します
    ```
    python configure.py concat 2.000 100 150 2650
    ```

16. 次のように表示されれば初期設定の後半も完了です！
    ```
    Config has been modified:
    {"rat": 2.0, "top": 100, "lef": 150, "rig": 2650}
    See you!
    ```

# 利用方法

1. `Anaconda Prompt`を開き、プロジェクトルートに移動、つまり
    ```
    (base) C:\Users\satun>
    (base) C:\Users\satun> cd tools\wbfsave
    (base) C:\Users\satun\tools\wbfsave>
    ```

1. `wbfsave`環境を有効に、つまり
    ```
    (base)> activate wbfsave
    (wbfsave)> 
    ```

1.  次の例のとおり入力します
    ```
    (wbfsave)> python main.py 666666-4444-4444 out.pdf 
    ```
    ただし、`666666-4444-4444`としたのは保存したいホワイトボードのURL末尾のID、  
    `out.pdf`としたのは成果ファイル名で、拡張子は他に`png` `jpg`が可能です

1.  ```
    Hello!
    ```
    との表示とともにChromeウィンドウが立ち上がります  
    ウィンドウを最大化し、板書が表示されたら適度なスケールに調整し、スタート位置に移動します

1.  `Anaconda Prompt`に戻り、`y`と入力します
    ```
    Are you ready?
    : y
    Ctrl+C at the end of your picture.
    ```

1.  板書の末尾までスクロールしたら`Ctrl+C`を入力します
    ```
    Ctrl+C pressed.
    some screenshots saved.
    Now terminating driver...
    ```

1.  次の表示があり`storage`ディレクトリ以下に成果ファイルが生成されます
    ```
    Successfully 17 images are clipped and concatenated to:
    storage\out.pdf
    ```

1.  また使ってね！
    ```
    See you!
    ```
   
# 課題

**余白の自動判定**ができれば次のようなことも可能でしょう
1. Slackで `/wbf 666666-4444-4444` のようなコマンドを一発たたく
   * AWS Lambdaなどに置いたスクリプトが走る
2. 直後に板書の画像が投稿される

# 結び

標準で高画質保存ができる [Microsoft Whiteboard][Microsoft Whiteboard] を使いましょう

[WhiteboardFox]:https://whiteboardfox.com/
[before]:images/before.png
[Miniconda]:https://docs.conda.io/en/latest/miniconda.html
[Microsoft Whiteboard]:https://products.office.com/ja-jp/microsoft-whiteboard/digital-whiteboard-app
