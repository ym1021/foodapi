import requests
import xml.etree.ElementTree as ET

url = 'http://apis.data.go.kr/1390802/AgriFood/FdFoodCkryImage/getKoreanFoodFdFoodCkryImageList'
params ={'serviceKey' : 'FSiJ0gZ5rLtvA6IM8LeEFCA2CCiR/KlhEBHq0+RtS0YSG6wStGx5dfvyAfiVc0WzRWtdSwZmEtwpULyA0kDvig==', 'service_Type' : 'xml', 'Page_No' : '1', 'Page_Size' : '20', 'food_Name' : '밥', 'ckry_Name' : '조리' }

response = requests.get(url, params=params)
# print(response.content)

list = ['fd_Nm']
file1 = response.content.decode('utf-8')
tree = ET.fromstring(file1)
tree = tree.findall('body/items/item')
for item in tree:
    for i in item:
        if i.tag in list:
            print(i.tag, i.text)
