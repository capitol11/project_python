import requests
from bs4 import BeautifulSoup
import urllib.request

keyword="dog"
#base_url="https://www.google.com/search?q={}"
base_url="https://www.google.com/search?q="
part_url="&rlz=1C1CHZN_enDE944DE944&sxsrf=AOaemvL3L194djdh4QIs2cBhIAWlG0rVAA:1632278579956&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj-2LrHx5HzAhXDdt4KHYGnBOYQ_AUoAXoECAEQAw&biw=1920&bih=937&dpr=1"
#res=requests.get(base_url.format(keyword)+part_url)
res=requests.get(base_url+keyword+part_url)
soup=BeautifulSoup(res.text,'html.parser')
img_lst=soup.find_all('img')

for i in img_lst:
    img_src=i.get('src')
    #img_name=img_src.replace("/","")
    print(img_src)
    #urllib.request.urlretrieve(img_url,"./img/"+img_name)