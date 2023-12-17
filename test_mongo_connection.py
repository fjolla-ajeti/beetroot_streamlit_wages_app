import pymongo

client = pymongo.MongoClient('****')

db = client['test_streamlit']

collection = db['wages']

data = {'name':'Fjolla',
        'city':'Prishtine',
        'profession':'instructor'}

result = collection.insert_one(data)

print(f'Inserted document id {result.inserted_id}')

# query_result = collection.find_one({'name':'Egzon'})
# print('Query result',query_result['city'])

# update_result = collection.update_one({'name':'Fjolla'},{'$set':{'city':'Prizren'}})
# print('Modified documents', update_result.modified_count)

# delete_result = collection.delete_one({'city':'Prizren'})
# print('Deleted items',delete_result.deleted_count)