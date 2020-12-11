# MongoDB
紀錄MongoDB的使用方式
## 時間戳記  自動刪除collection  

collection.insert({'time_decline':datetime.datetime.utcnow()})  
collection.create_index([("time_decline", pymongo.ASCENDING)], expireAfterSeconds=43200)   
