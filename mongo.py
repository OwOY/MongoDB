import pymongo

client = pymongo.MongoClient('mongodb+srv://OwOY:{password}@test-g7qjf.mongodb.net/test?retryWrites=true&w=majority')
db = client.test
collection = db.All

# --------------------------輸入單筆資料-----------------------------
# DB_dict = {
#     'title':'yaya',
#     'text':'yoyo',
#     'datetime':'2019-01-06'
# }

# result = collection.insert_one(DB_dict)
# --------------------------輸入多筆資料-----------------------------
# a = [1,2,3,4]
# b = [2,4,5,6]
# DB_dict = [
#     {'title': c,'text': d,'test':'test'} for c,d in zip(a,b)
# ]

# result = collection.insert_many(DB_dict)
# -------------------------------------------------------------------


# --------------------------尋找資料-----------------------------
# finddata = collection.find({'BRAND':'APPLE'})
# data = [data for data in finddata]
# for d in data:
#     print(d)
# ----------------------------尋找全部資料-------------------------
# finddata = collection.find({})
# data = [data for data in finddata]
# print(data)
# --------------------------尋找Column-----------------------------
# finddata = collection.find({}, {_id:0})    0為顯示   1為不顯示
# data = [data for data in finddata]
# for d in data:
#     print(d)
# -------------------------------------------------------------------



# ----------------------------刪除一筆資料-------------------------
# mvone = collection.delete_one({'title':'yaya'})
# ----------------------------刪除多筆資料-------------------------
# mvmany = collection.delete_many({'title':'haha'})
# ----------------------------刪除全部資料-------------------------
# mvall = collection.delete_many({})
# ----------------------------------------------------------------
