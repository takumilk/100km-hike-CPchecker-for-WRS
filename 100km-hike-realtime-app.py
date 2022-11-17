# google.clab認証のためのコード
from google.colab import auth
auth.authenticate_user()
import gspread
from google.auth import default
creds, _ = default()
gc = gspread.authorize(creds)
from bs4 import BeautifulSoup
import requests

for j in range(5,12,1):
  res = requests.get(f'https://system.rs100.info/rs100kms/part/{j}')
  soup = BeautifulSoup(res.text,'html.parser')
  tags = soup.find_all('td')
  text_list = [x.string for x in tags]
  for i in range(3,18,2):
      print(text_list[i])

  ## スプレッドシートを開く
  url = "https://docs.google.com/spreadsheets/d/1TYbFrCuV9S0nqsweUqVyMx4xhvJCzILOSHyB0FemlCQ/edit?usp=sharing"
  ss = gc.open_by_url(url)

  # セルに入力
  st = ss.worksheet("menber")
  row = 4
  for i in range(3,18,2):
   st.update_cell( j-3, row , text_list[i]) 
   row += 1

#id191,213 のみ個別取り出し
num = 191
for j in range(1,3,1):
  res = requests.get(f'https://system.rs100.info/rs100kms/part/{num}')
  soup = BeautifulSoup(res.text,'html.parser')
  tags = soup.find_all('td')
  text_list = [x.string for x in tags]
  for i in range(3,18,2):
    print(text_list[i])
    
  row = 4
  for i in range(3,18,2):
   st.update_cell( j+8, row , text_list[i]) 
   row = row+1
  num +=22
