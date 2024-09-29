from pymongo import MongoClient
import boto3
from mongodb_handler import add_stock_into_watchlist, create_user_watchlists, remove_stock_from_watchlist
import json
#event["Records"][0]["s3"]["object"]["key"]


def lambda_handler(event, context):
    file_name = event["Records"][0]["s3"]["object"]["key"]

    s3_client = boto3.client('s3', region_name="ap-south-1")
    try:
        response = s3_client.get_object(Bucket="tradexcloudcqrseventlogs" ,Key=file_name)
        content = json.loads(response["Body"].read())
        if(content["Action"] == "CREATE"):
            create_user_watchlists({'_id' : int(content["UserID"]), 'Watchlist1' : [], 'Watchlist2' : []})

        elif(content["Action"] == "ADD"):
            add_stock_into_watchlist({'_id' : int(content["UserID"]), 'WatchlistID' : int(content["WatchlistID"]), "Stock": content["Stock"]})
        
        elif(content["Action"] == "REMOVE"):
            remove_stock_from_watchlist({'_id' : int(content["UserID"]), 'WatchlistID' : int(content["WatchlistID"]), "Stock": content["Stock"]})

    except Exception as e:
        print(e)


if __name__ == "__main__":
    #driver code
    lambda_handler(
        {
            "Records" : [
                {
                    "s3" : {
                        "object" : {
                            "key" : "remove_stock.json"
                        }
                    }
                }
            ]
        }
        ,
        {"Context": None} 
)
