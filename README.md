# これは何？

一行でいうと  
**WhiteboardFoxによる板書の高画質保存を支援するツール**  
です

以下、OSはWindows10、ブラウザはChromeを仮定します

[WhiteboardFox][WhiteboardFox]という素晴らしいフリーのWebホワイトボードサービスがあります  
この板書を**参照性のために画像として保存したい**方も少なくないと思うのですが  
標準の保存機能では[この程度][before]の画質しか実現しません

一方、[Screenpresso][Screenpresso]という縦スクロール領域を連続してキャプチャできるアプリがあります  
ということは、たいてい縦長である板書を横幅いっぱいに表示してScreenpressoを利用すれば高画質保存ができそうです  
ところが、WhiteboardFoxは正確に縦スクロールするしくみを標準では備えていません  

そこで、当ツールはWhiteboardFoxにおける正確な縦スクロールを代行し  
Screenpressoによるキャプチャを支援します

# 導入に要する時間

PCはネットサーフィンくらいにしか使わないという方でも **30分** で導入できます

# 導入方法

1.  `Win`+`S`キーを押し検索ボックスに`sys`と入力、候補に出た`システム情報`を開き  
    `システムの種類`が`x64-ベース PC`であることを確認します
1.  [Miniconda][Miniconda]のページから`Miniconda3 Windows 64-bit`をダウンロードし起動、  
    指示に従ってインストールします
1.  `Win`+`S`キーを押し検索ボックスに`ana`と入力、候補に出た`Anaconda Prompt`を開き  
    次の例のとおりに入力します
    ```
    (base) C:\Users\satun>
    (base) C:\Users\satun> mkdir tools
    (base) C:\Users\satun> cd tools
    (base) C:\Users\satun\tools> mkdir whiteboardfox_capture
    (base) C:\Users\satun\tools> cd whiteboardfox_capture
    (base) C:\Users\satun\tools\whiteboardfox_capture>
    ```
    上記最終行を`(base)>`と略記することにすると  
    ```
    (base)> conda create -n whiteboardfox_capture selenium chromedriver-binary
    activate whiteboardfox_capture
    ```

1. 
1. 
1. 
1. 
1. 
1. 

# 利用方法

# 結び

Microsoft Whiteboard を使おう

[WhiteboardFox]:https://
[before]:https://
[Screenpresso]:https://
[Miniconda]:https://
[]:https://
[]:https://
[]:https://
[]:https://
