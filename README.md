# 処理終了通知関数  
______
## 概要  
pythonコードからLINEで通知

## 作成理由  
プログラムの終了を通知させるため

## demo  
最初にLINEトークンを取得する必要あり  
下記サイトを参照  
[Pythonの実行終了をLINEで通知する](https://qiita.com/aoyahashizume/items/13848b013daa18f6461b)  
```python3 notify.py``` で実行

## 使用方法  
```python3:関数読み込み
import notify
```  
```python3：関数呼び出し
notify.lineNotify("通知する内容")
```  

## 本家様
[LINE](https://notify-bot.line.me/doc/ja/)

