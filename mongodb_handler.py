from pymongo import MongoClient

def create_user_watchlists(data):

    try:
        client = MongoClient("mongodb+srv://tradexcloud:tradexcloudadmin@tradexcloud.stdy9.mongodb.net/?retryWrites=true&w=majority&appName=TradeXCloud")
        db = client["UsersInfo"]
        print("database connected successfully")

        collection = db["UsersWatchlists"]
        result = collection.insert_one(data)
        print("data inserted successfully {0}", result)
    except Exception as e:
         print(f"Error occured while creating user watchlist {e}")


def add_stock_into_watchlist(data):
    #function to insert stock into user's watchlist
    try:
        client = MongoClient("mongodb+srv://tradexcloud:tradexcloudadmin@tradexcloud.stdy9.mongodb.net/?retryWrites=true&w=majority&appName=TradeXCloud")
        db = client["UsersInfo"]
        collection = db["UsersWatchlists"]
        print("database connected successfully")

        document = collection.find_one({'_id' : data['_id']})
       
        if data['WatchlistID'] == 1:
            if data["Stock"] in document['Watchlist1']:
                pass
            else:
                document['Watchlist1'].append(data['Stock'])

        elif data['WatchlistID'] == 2:
            if data["Stock"] in document['Watchlist2']:
                pass
            else:
                document['Watchlist2'].append(data['Stock'])
        else:
            print("Invalid WatchList ID")


        # print(document)
        collection.replace_one({'_id': data["_id"]}, document)



    except Exception as e:
        print(f"Error occured adding stock into watchlist {e}")


def remove_stock_from_watchlist(data):
    #function to remove stock from watchlist
    try:
        client = MongoClient("mongodb+srv://tradexcloud:tradexcloudadmin@tradexcloud.stdy9.mongodb.net/?retryWrites=true&w=majority&appName=TradeXCloud")
        db = client["UsersInfo"]
        collection = db["UsersWatchlists"]
        print("database connected successfully")

        document = collection.find_one({'_id' : data['_id']})
       
        if data['WatchlistID'] == 1:
            if data["Stock"] not in document['Watchlist1']:
                pass
            else:
                document['Watchlist1'].remove(data['Stock'])

        elif data['WatchlistID'] == 2:
            if data["Stock"] not in document['Watchlist2']:
                pass
            else:
                document['Watchlist2'].remove(data['Stock'])
        else:
            print("Invalid WatchList ID")

        collection.replace_one({'_id': data["_id"]}, document)

    except Exception as e:
        print("Error occured while removing stock from watclist {e}")

