# Use IBM Watson Discovery News with Watson Assistant
# Henrik Loeser / hloeser@de.ibm.com
# (c) 2019 IBM Corporation


import json, sys
from watson_developer_cloud import DiscoveryV1


def main(args):
    
    # initialize, credentials are taken from the IBM Cloud Functions binding
    discovery = DiscoveryV1(
        version='2018-08-01',
        url=args["__bx_creds"]["discovery"]["url"],
        username=args["__bx_creds"]["discovery"]["username"],
        password=args["__bx_creds"]["discovery"]["password"])

    # some setup to query news and decide on which language
    news_environment_id = 'system'
    collection_id = 'news-en'
    if 'entities' in args:
        messageEntities = args["entities"]

        for entity in messageEntities:
            if entity['entity']=="country" and entity['value']=="Germany":
                collection_id='news-de'
            elif entity['entity']=="country" and entity['value']=="Spain":
                collection_id='news-es'

    # Query the news collection
    query_results = discovery.query(
        news_environment_id,
        collection_id,
        natural_language_query=args["topic"],
        deduplicate="true",
        sort="-score,-publication_date",
        return_fields='title,url,publication_date')

    # Extract only the title, publication date and url
    res=[]
    for i in query_results["results"]:
        res.append({"pubdate": i['publication_date'],"title" : i['title'],"url": i['url']})

    return {"myNews" : res}

if __name__ == "__main__":
    main(json.loads(sys.argv[1]))