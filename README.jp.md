# Pico Macro Key
登録しておいた文字列をワンボタンで呼び出すマクロキーボードです。  
以下の特徴があります。  
- PCなどにUSB接続して利用します。
- 複数の文字列を登録して呼び出せます。（上限はRaspberryPicoの容量上限です）
- キーボードのタイピングとして入力されます。（文字列がそのまま送信されるわけではありません）
- USキーボードとJPキーボードの入力に対応しています。
- 起動時のPinの入力を設定できます。途中でロックもできます。

# 実装
## 用意するもの
- Raspberry Pi Pico
- シフトキー用ボタンスイッチ
- ボタンスイッチx3
- 3Vで動作するブザー（なくても可）
- LCD 128x32 I2C接続のもの

※ シフトキーと通常ボタンは形か色を変えるとわかりやすいです。

## Raspberry Pi Picoのセットアップ
1. Circuit Pythonをインストールしてください。  
https://circuitpython.org/board/raspberry_pi_pico/
2. [src](src) 以下のファイルをRaspberry Pi Picoのフォルダにコピーする  
<img src="./circuitpython_dir.png" width="320" />
3. 以上です

## 電子回路を配線する
<img src="./pico-macro-key_bb.png" width="400" />
