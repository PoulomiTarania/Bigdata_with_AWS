from sodapy import Socrata
import requests
from requests.auth import HTTPBasicAuth
import json
import argparse
import sys
import os

parser = argparse.ArgumentParser(description='NYC Fire Incidents')
parser.add_argument('--page_size', type=int, help='how many rows to get per page', required=True)
parser.add_argument('--num_pages', type=int, help='how many pages to get in total')
args = parser.parse_args(sys.argv[1:])
print(args)


DATASET_ID=os.environ["DATASET_ID"]
APP_TOKEN=os.environ["APP_TOKEN"]
ES_HOST=os.environ["ES_HOST"]
ES_USERNAME=os.environ["ES_USERNAME"]
ES_PASSWORD=os.environ["ES_PASSWORD"]
INDEX_NAME=os.environ["INDEX_NAME"]

if __name__ == '__main__': 
    try:
        resp = requests.put(f"{ES_HOST}/{INDEX_NAME}", auth=HTTPBasicAuth(ES_USERNAME, ES_PASSWORD),
            json={
                "settings": {
                    "number_of_shards": 1,
                    "number_of_replicas": 1
                },
                "mappings": {
                    "properties": {
                        "starfire_incident_id": {"type": "keyword"},
                        "incident_datetime": {"type": "date"},
                        "alarm_box_location": {"type": "keyword"},
                        "incident_borough": {"type": "keyword"},
                        "alarm_source_description_tx": {"type": "keyword"},
                        "incident_classification": {"type": "keyword"},
                        "incident_classification_group": {"type": "keyword"},
                        "dispatch_response_seconds_qy": {"type": "float"},
                        "incident_response_seconds_qy": {"type": "float"},
                        "incident_travel_tm_seconds_qy": {"type": "float"},
                        "engines_assigned_quantity": {"type": "float"},
                        
                    }
                },
            }
        )
        resp.raise_for_status()
        print(resp.json())
        
    except Exception as e:
        print("Index already exists! Skipping")    
    
    client = Socrata("data.cityofnewyork.us", APP_TOKEN, timeout=100000)
    total_records= client.get(DATASET_ID, select='COUNT(*)')
    total_records = ' '.join([key['COUNT'] for key in total_records])
    page_size=args.page_size
    
    if args.num_pages == None:
        total_num_pages = int(total_records)/page_size + 1
        num_pages = int(total_num_pages)
        print("Total Records in Dataset:",total_records)
    else:
        num_pages=args.num_pages
   

    
    for page_num in range(1,num_pages):
        rows = client.get(DATASET_ID, where="starfire_incident_id is NOT NULL or incident_datetime is NOT NULL", limit=page_size, offset=(page_num-1)*page_size)
        es_rows=[]
        
        for row in rows:
            try:
                es_row = {}
                es_row["starfire_incident_id"] = row["starfire_incident_id"]
                es_row["incident_datetime"] = row["incident_datetime"]
                es_row["alarm_box_location"] = row["alarm_box_location"]
                es_row["incident_borough"] = row["incident_borough"]
                es_row["alarm_source_description_tx"] = row["alarm_source_description_tx"]
                es_row["incident_classification"] = row["incident_classification"]
                es_row["incident_classification_group"] = row["incident_classification_group"]
                es_row["dispatch_response_seconds_qy"] = float(row["dispatch_response_seconds_qy"])
                es_row["incident_response_seconds_qy"] = float(row["incident_response_seconds_qy"]) 
                es_row["incident_travel_tm_seconds_qy"] = float(row["incident_travel_tm_seconds_qy"]) 
                es_row["engines_assigned_quantity"] = float(row["engines_assigned_quantity"]) 
            except Exception as e:
                continue
            es_rows.append(es_row)
        
    
        bulk_upload_data = ""
        for line in es_rows: 
            action = '{"index": {"_index": "' + INDEX_NAME + '", "_type": "_doc", "_id": "' + line["starfire_incident_id"] + '"}}'
            data = json.dumps(line)
            bulk_upload_data += f"{action}\n"
            bulk_upload_data += f"{data}\n"
            
        
        try:
            resp = requests.post(f"{ES_HOST}/_bulk",data=bulk_upload_data,auth=HTTPBasicAuth(ES_USERNAME, ES_PASSWORD), headers = {"Content-Type": "application/x-ndjson"})
            resp.raise_for_status()
            print ('Done')
        except Exception as e:
            print(f"Failed to insert in ES: {e}")
        page_num = page_num + 1

# print("Total Records in Dataset:",total_records)
# print("Total Pages:",num_pages)
