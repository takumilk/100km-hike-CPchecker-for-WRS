# 100km-hike-CPchecker-for-WRS
<h2>100kmハイクのWRSメンバーのチェックポイント通過時間をリアルタイムで共有するapp</h2>
<h3>・仕組み<h3>
<img width="1025" alt="image" src="https://user-images.githubusercontent.com/78514031/202569135-d4ba95a4-1c92-4e1b-b0f9-99c8c09f6f3c.png">

<h3>・Glide app</h3>
  
<img height= "500" src="https://user-images.githubusercontent.com/78514031/202568710-42f42b14-8830-4b0d-9ed4-539b4ba304c4.png">

<h3>・今回の学び</h3>
<h4>→URL内に変数を入れて指定できる!</h4>
<p>Python3.6以降であれば、f''やf""のようにクォーテーションの前にfを付けて、文字列中には{変数名}や{式}などを書くだけ。
https://teratail.com/questions/311483
</p>

```
num = 4563
url = f'http://localhost:18080/kabusapi/board/{num}@1'
print(url)
```

```
http://localhost:18080/kabusapi/board/4563@1
```

<h3>・改善点</h3>
→colabratryでのスクレイピングなので、スプシ反映が手動である点。
  <br>
→glideのDBページがオンラインでないとDBが更新されない点。
