# Handle client-side action for an IBM Watson Assistant chatbot
#
# The code requires my Watson Conversation Tool. For details see
# https://github.com/data-henrik/watson-conversation-tool
#
#
# Setup: Configure your credentials
# - for Watson Assistant see instructions for the tool
# - for Discovery change username / password below
#
#
# Written by Henrik Loeser

import json
from watson_developer_cloud import DiscoveryV1


def handleClientActions(context, actions, watsonResponse):
    print (">>> processing client actions...\n")

    # Initialize the Discovery API
    discovery = DiscoveryV1(
        version='2018-08-01',
        ## url is optional, and defaults to the URL below. Use the correct URL for your region.
        # url='https://gateway.watsonplatform.net/discovery/api',
        username='your-username',
        password='your-password')

    # We are going to access a system collection with English news
    # You could change the language to news-de or news-es...
    news_environment_id = 'system'
    collection_id = 'news-en'

    # We could query the different collections here
    # collections = discovery.list_collections(news_environment_id).get_result()
    # news_collections = [x for x in collections['collections']]
    # print(json.dumps(collections, indent=2))

    # Now query Discovery, sort the result and only return certain fields
    query_results = discovery.query(
        news_environment_id,
        collection_id,
        natural_language_query=context['topic'],
        deduplicate="true",
        sort="-score,-publication_date",
        return_fields='title,url,publication_date').get_result()

    # Write the result to our defined variable and return
    context.update({'myNews':query_results})
    return context