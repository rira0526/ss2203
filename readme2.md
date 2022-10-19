# スキルゼミ課題 SS2203-02
## 課題名：CT画像の体幹抽出
氏名：枡本りら

## 開発環境

Windows 10 Home　21H1
gcc ver 9.4.0
## 実行方法
```bash
$ python ss2203-02.py 
```

## コメント
- モルフォロジ変換までしか完成しなかった。まずmhdファイルを読み込み、画像処理に必要な情報を得た。rawファイルを読み込み、閾値処理とモルフォロジ変換を行った。閾値処理では、閾値を100とした。

## 参考資料
- (https://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.ndimage.morphology.binary_erosion.html)
- [【画像処理】Numpyでモルフォロジー演算](https://qiita.com/aa_debdeb/items/9404d481d7b01cb7b41b)