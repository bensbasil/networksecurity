from pymongo import MongoClient
uri = "mongodb+srv://bensdbasil:123bens@cluster0.2cbaysm.mongodb.net/"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)