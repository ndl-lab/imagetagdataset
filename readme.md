NDL-ImageLabelデータセット （ラベル付画像データセット）
==================

## データセットの概要

NDL-ImageLabelデータセットは以下のURLから公開しています。<br/>
現在(2021年6月)の最新バージョンは1.0です。<br/>

(URLを入れる)


1.概要
----

### 1.1 データセットの提供元

NDL-ImageLabelデータセットは、国立国会図書館デジタルコレクション（以下「デジコレ」といいます。）&lt;[*http://dl.ndl.go.jp/*](http://dl.ndl.go.jp/)&gt;が提供している、
著作権保護期間満了資料の画像データの中から自動的に切り出されたイラスト・写真・印影等に、
人手でラベルを付与して画像分類等のタスク向けのデータセットを作成したものです。


### 1.2 データセットの内訳

NDL-ImageLabelデータセット(ver1.0)の内訳は以下のとおりです。


  |ラベル名                   | 画像数
  |---------------------|----------
  |graphic_map          |581画像
  |graphic_graph        |371画像
  |graphic_illustcolor  |170画像
  |graphic_illust       |2,695画像
  |picture_landmark     |728画像
  |picture_outdoor      |748画像
  |picture_object       |401画像
  |picture_indoor       |232画像
  |stamp                |479画像

合計 6,405画像


  
### 1.3 データセットの権利
「PDM（パブリック・ドメイン・マーク）」&lt; https://creativecommons.org/publicdomain/mark/1.0/deed.ja &gt;

※本データセットは著作権保護期間満了資料のみを加工して作成しています。

NDL-ImageLabelデータセットは、自由な二次利用が可能です。ただし、二次利用に際しては、次の事項へのご配慮をお願いいたします。これらのお願いは法的な契約ではありませんが、できる限りご留意の上でご利用くださるよう、ご協力をお願いします。

- データを編集・加工等して利用する場合は、それを行ったことを記載してください。編集・加工等を、元となる作品・原資料の作者や当館が行なったかのような態様で公表しないようご留意ください。
- 当該データが自由に二次利用可能であることの表記を保持してください。
- 元となる作品や、その作者の名声を傷つける形での利用は行わないようご留意ください。また、元となる作品に関わる文化やコミュニティへの配慮を行ってください。
- 著作権以外の権利（著作者人格権、著作隣接権、肖像権、パブリシティ権、プライバシー権、商標権等）にも留意し、関連法令を遵守してください。
- 論文等に利用する場合には、先行研究や後続研究と比較を容易にするためNDL-ImageLabelデータセットとバージョンの明記にご協力ください。


2 データセットの説明
------------------

### 2.1 データセットの構成

NDL-ImageLabelデータセットは、ラベル付与対象となった画像がラベル名ごとに分かれて収録されています。
NDL-ImageLabelデータセットに含まれる画像は、1画像につき1つのラベルが対応付いています。

**各ラベルの簡単な説明**

- 図・イラスト等 
    - **graphic_map** :地図の描かれた図版に付与されます。
    古地図等を選択的に収集するモデルの学習用途を想定しています。
    - **graphic_graph**：円グラフ・棒グラフ・折れ線グラフ等の図版に付与されます。
    統計資料や論文等から図版の含まれるページをサジェストする用途等への利用を想定しています。
    - **graphic_illustcolor**：着色されたイラストに付与されます。
    カラー資料のみを抽出する用途等への利用を想定しています。
    - **graphic_illust** :上記3要素をいずれも持たないイラストに付与されます。写真とそれ以外を見分ける学習等への利用を想定しています。
- 写真等
    - **picture_landmark**：人工的な建造物等、撮影場所の特定に寄与するランドマークが映り込んだ写真に付与されます。
    既存のランドマークを推定するモデル等を利用して類似した建造物を探索したり、座標情報を付与することで更なる活用をしたりすることを想定しています。
    - **picture_outdoor**：屋外で撮影された写真のうち、場所の特定が困難な画像に付与されます。紛らわしい例として、例えば海上の船やテントなども含みます。
    写真の撮影時の屋内外を見分けるモデルや、ランドマークが含まれているかを判定するモデル等への利用を想定しています。
    - **picture_object**：屋内で撮影された骨董品や道具の写真に付与されます。例えば美術品に特化した検索を行うための学習等への利用を想定しています。
    - **picture_indoor**：屋内で撮影された写真に付与されます。例えば集会の様子や建物の内装等が含まれます。建物内部を選択的に検索するためのモデルの学習用途等を想定しています。
- その他
    - **stamp**：印影に付与されます。蔵書情報等の根拠となりうるページを特定するモデル等への利用を想定しています。

※公開用のデータセットには、バストアップ等特徴がはっきり視認できる人物写真は含まれていません。
<table style="table-layout:fixed;width:100%;"><tbody>
<tr>
<td align="center" style="word-wrap:break-word;">
<img alt="graphic_graphの画像例" src="./sampleimg/graphic_graph/1711226_72_0.jpg" title="graphic_graphの画像例"/>
<br/>graphic_graphの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="graphic_graphの画像例" src="./sampleimg/graphic_graph/1711992_95_1.jpg" title="graphic_graphの画像例"/>
<br/>graphic_graphの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="graphic_graphの画像例" src="./sampleimg/graphic_graph/1903147_256_1.jpg" title="graphic_graphの画像例"/>
<br/>graphic_graphの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="graphic_graphの画像例" src="./sampleimg/graphic_graph/1906438_25_0.jpg" title="graphic_graphの画像例"/>
<br/>graphic_graphの画像例</td>
</tr><tr>
<td align="center" style="word-wrap:break-word;">
<img alt="graphic_illustの画像例" src="./sampleimg/graphic_illust/1207765_104_0.jpg" title="graphic_illustの画像例"/>
<br/>graphic_illustの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="graphic_illustの画像例" src="./sampleimg/graphic_illust/1444548_122_1.jpg" title="graphic_illustの画像例"/>
<br/>graphic_illustの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="graphic_illustの画像例" src="./sampleimg/graphic_illust/1444548_43_0.jpg" title="graphic_illustの画像例"/>
<br/>graphic_illustの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="graphic_illustの画像例" src="./sampleimg/graphic_illust/904689_7_1.jpg" title="graphic_illustの画像例"/>
<br/>graphic_illustの画像例</td>
</tr><tr>
<td align="center" style="word-wrap:break-word;">
<img alt="graphic_illustcolorの画像例" src="./sampleimg/graphic_illustcolor/1208111_72_0.jpg" title="graphic_illustcolorの画像例"/>
<br/>graphic_illustcolorの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="graphic_illustcolorの画像例" src="./sampleimg/graphic_illustcolor/1234445_8_1.jpg" title="graphic_illustcolorの画像例"/>
<br/>graphic_illustcolorの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="graphic_illustcolorの画像例" src="./sampleimg/graphic_illustcolor/1286795_17_0.jpg" title="graphic_illustcolorの画像例"/>
<br/>graphic_illustcolorの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="graphic_illustcolorの画像例" src="./sampleimg/graphic_illustcolor/1286892_27_0.jpg" title="graphic_illustcolorの画像例"/>
<br/>graphic_illustcolorの画像例</td>
</tr><tr>
<td align="center" style="word-wrap:break-word;">
<img alt="graphic_mapの画像例" src="./sampleimg/graphic_map/1014897_9_1.jpg" title="graphic_mapの画像例"/>
<br/>graphic_mapの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="graphic_mapの画像例" src="./sampleimg/graphic_map/2571701_47_0.jpg" title="graphic_mapの画像例"/>
<br/>graphic_mapの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="graphic_mapの画像例" src="./sampleimg/graphic_map/2587246_153_0.jpg" title="graphic_mapの画像例"/>
<br/>graphic_mapの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="graphic_mapの画像例" src="./sampleimg/graphic_map/763717_49_0.jpg" title="graphic_mapの画像例"/>
<br/>graphic_mapの画像例</td>
</tr><tr>
<td align="center" style="word-wrap:break-word;">
<img alt="picture_indoorの画像例" src="./sampleimg/picture_indoor/1028124_14_0.jpg" title="picture_indoorの画像例"/>
<br/>picture_indoorの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="picture_indoorの画像例" src="./sampleimg/picture_indoor/1029816_6_0.jpg" title="picture_indoorの画像例"/>
<br/>picture_indoorの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="picture_indoorの画像例" src="./sampleimg/picture_indoor/1136786_160_0.jpg" title="picture_indoorの画像例"/>
<br/>picture_indoorの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="picture_indoorの画像例" src="./sampleimg/picture_indoor/1443967_42_0.jpg" title="picture_indoorの画像例"/>
<br/>picture_indoorの画像例</td>
</tr><tr>
<td align="center" style="word-wrap:break-word;">
<img alt="picture_landmarkの画像例" src="./sampleimg/picture_landmark/1051226_100_0.jpg" title="picture_landmarkの画像例"/>
<br/>picture_landmarkの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="picture_landmarkの画像例" src="./sampleimg/picture_landmark/1107204_184_0.jpg" title="picture_landmarkの画像例"/>
<br/>picture_landmarkの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="picture_landmarkの画像例" src="./sampleimg/picture_landmark/1234138_1844_0.jpg" title="picture_landmarkの画像例"/>
<br/>picture_landmarkの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="picture_landmarkの画像例" src="./sampleimg/picture_landmark/974390_1049_0.jpg" title="picture_landmarkの画像例"/>
<br/>picture_landmarkの画像例</td>
</tr><tr>
<td align="center" style="word-wrap:break-word;">
<img alt="picture_objectの画像例" src="./sampleimg/picture_object/1235003_24_0.jpg" title="picture_objectの画像例"/>
<br/>picture_objectの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="picture_objectの画像例" src="./sampleimg/picture_object/1170764_155_0.jpg" title="picture_objectの画像例"/>
<br/>picture_objectの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="picture_objectの画像例" src="./sampleimg/picture_object/1212286_60_0.jpg" title="picture_objectの画像例"/>
<br/>picture_objectの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="picture_objectの画像例" src="./sampleimg/picture_object/967549_31_0.jpg" title="picture_objectの画像例"/>
<br/>picture_objectの画像例</td>
</tr><tr>
<td align="center" style="word-wrap:break-word;">
<img alt="picture_outdoorの画像例" src="./sampleimg/picture_outdoor/1178514_94_0.jpg" title="picture_outdoorの画像例"/>
<br/>picture_outdoorの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="picture_outdoorの画像例" src="./sampleimg/picture_outdoor/1459078_26_1.jpg" title="picture_outdoorの画像例"/>
<br/>picture_outdoorの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="picture_outdoorの画像例" src="./sampleimg/picture_outdoor/932544_6_1.jpg" title="picture_outdoorの画像例"/>
<br/>picture_outdoorの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="picture_outdoorの画像例" src="./sampleimg/picture_outdoor/933749_28_2.jpg" title="picture_outdoorの画像例"/>
<br/>picture_outdoorの画像例</td>
</tr><tr>
<td align="center" style="word-wrap:break-word;">
<img alt="stampの画像例" src="./sampleimg/stamp/1908798_3_0.jpg" title="stampの画像例"/>
<br/>stampの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="stampの画像例" src="./sampleimg/stamp/1918781_4_0.jpg" title="stampの画像例"/>
<br/>stampの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="stampの画像例" src="./sampleimg/stamp/808179_7_0.jpg" title="stampの画像例"/>
<br/>stampの画像例</td>
<td align="center" style="word-wrap:break-word;">
<img alt="stampの画像例" src="./sampleimg/stamp/825268_2_0.jpg" title="stampの画像例"/>
<br/>stampの画像例</td>
</tr></tbody>
</table>

**ファイル命名規則**

命名規則は
(PID)_(コマ番号)_（同コマに含まれる0-indexの画像番号）
となっています。
例えば761290_190_0は、http://dl.ndl.go.jp/info:ndljp/pid/761290
のコマ番号190に含まれる最初の画像を意味します。

**metadata.csvの記載内容**

metadata.csvは、画像の出典となった資料のタイトルや当該資料のデジコレにおけるURL等の情報を含んでいます。
より詳細なメタデータが必要な場合には、次項の「PIDと資料名の対応表」を参考にしてください。

|ファイル名|ラベル名|ファイルのディレクトリパス|タイトル|資料のURL|当該画像のフルサイズのURL(IIIF Image API)
|--------|-------|----------------------|-------|--------|-------------------------------------
|1017141_454_0.jpg|graphic_graph|graphic_graph\1017141_454_0.jpg|経済学全集|https://dl.ndl.go.jp/info:ndljp/pid/1017141|"https://www.dl.ndl.go.jp/api/iiif/1017141/R0000454/pct:15.0,20.1,28.5,66.7/full/0/default.jpg"




**PIDと資料名の対応表**

デジコレの詳細な書誌データは以下から提供しています。

https://www.ndl.go.jp/jp/dlib/standards/opendataset/index.html

各メタデータは以下から、

https://dl.ndl.go.jp/files/dataset/dataset_202101_k_internet.zip


https://dl.ndl.go.jp/files/dataset/dataset_202101_t_internet.zip

それぞれダウンロード可能です。