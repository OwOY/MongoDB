# MongoDB
<img  src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Mongodb.png/1200px-Mongodb.png"></img>
## 時間戳記  自動刪除collection  
```
collection.insert({'time_decline':datetime.datetime.utcnow()})  
collection.create_index([("time_decline", pymongo.ASCENDING)], expireAfterSeconds=43200)   
```
## 連接MongoDB   
```
client = pymongo.MongoClient(f'{IP}')  
collection = client[f'{db}'][f'{collection}']  
```
## Create
- 單筆
```
DB_dict = {
     'title':'yaya',
     'text':'yoyo',
     'datetime':'2019-01-06'
 }
 result = collection.insert_one(DB_dict)
```
- 多筆
```
a = [1,2,3,4]
b = [2,4,5,6]
DB_dict = [
   {'title': c,'text': d,'test':'test'} for c,d in zip(a,b)
]
result = collection.insert_many(DB_dict)
```
## Research
- 單筆
```
finddata = collection.find({'BRAND':'APPLE'})
data = [data for data in finddata]
for d in data:
    print(d)
```
- 多筆
```
finddata = collection.find({})
data = [data for data in finddata]
print(data)
```
- 篩選顯示條件
```
finddata = collection.find({}, {_id:0})    0為不顯示   1為顯示
data = [data for data in finddata]
for d in data:
    print(d)
```
## Delete
- 單筆刪除
```
mvone = collection.delete_one({'title':'yaya'})
```
- 批量刪除
```
mvmany = collection.delete_many({'title':'haha'})
```
- 全部刪除
```
mvall = collection.delete_many({})
```
## Update
- 修改單筆資料
```
collection.update_one(key, {'$set':{'text':'tetttst'}})
mvone = collection.update_one({'title':'yaya'}, {'$set':{'text':'tetttst'}})
```
- 修改address為S開頭資料
```
myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }

x = collection.update_many(myquery, newvalues)
```
- 修改資料並append到原資料
單筆
{'address':'S123', 'name':['test1']}
```
myquery = {'address':{"$regex": "^S"}}
newvalues = {'$push':{'name':'foo'}}
```
>> {'address':'S123', 'name':['test1', 'foo']}
多筆
{'address':'S123', 'name':['test1']}
```
myquery = {'address':{"$regex": "^S"}}
newvalues = {'$pushAll':{'name':['foo', 'bar']}}
```
>> {'address':'S123', 'name':['test1', 'foo', 'bar']}
## Aggregate 聚合用法
- $lookup  
  相似於 SQL 語法 join on  
  from：選擇 join 的 collection  
  localField：選擇該 collection 主鍵  
  foreignField：選擇被連結的 collection 外鍵  
  as：命名該物件為何  
- $match  
  條件式篩選  
- $project  
  篩選需求欄位
- $sort  
  依序欄位做升降冪
- $skip  
  跳過前幾筆資料
- $limit  
  選擇顯示幾筆資料
- $count  
  讓輸出只顯示筆數 ex : {'$count':'totalCount'}
  >> [{'totalCount':20}]

  ex：
  ```
  data_list = collection.aggregate([
     {
          '$lookup':{
               'from':colA,
               'localField':id,
               'foreignField:colA_id,
               'as':colA_info
          }
     },
     {
          '$match':{
               {'colA_info.match_num':20},
               {'create_at':{'$gte':time_start, '$lte':time_end}},
               {'name':{'$regex':'mat'}
          }
     },
     {
          '$project':{
               '_id':0, # 不顯示 _id 欄位
               'code':1, # 只顯示code 欄位
          }
     },
     {'$sort':{'createAt':-1}},
     {'$skip':((page-1)*10)},
     {'$limit':10},
  ])
  ```
