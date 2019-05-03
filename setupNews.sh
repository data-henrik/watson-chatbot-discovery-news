# create the getNews action
ibmcloud fn action create slackdemo/getNews getNews.py  --kind python-jessie:3 --web true --web-secure $theSecret

# bind the action to the discovery service
ibmcloud fn service bind discovery slackdemo/getNews 