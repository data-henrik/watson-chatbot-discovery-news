# Discovery news as dialog action in IBM Watson Assistant
The code in this branch is an add-on for the updated version of the IBM Cloud solution tutorial [Build a database-driven Slackbot](https://cloud.ibm.com/docs/tutorials?topic=solution-tutorials-slack-chatbot-database-watson#build-a-database-driven-slackbot). Using the same 

# Setup
To get it working, set up the environment as described in the tutorial. Then provision [Watson Discovery](https://cloud.ibm.com/catalog/services/discovery).

Deploy the Cloud Function in [setupNews.sh](setupNews.sh) after setting the same secret as for the tutorial.

## Intent and entity

You need to define an intent or **getNews** with samples like "give me news about IBM" or "what is news for Apple".

Define an entity **newsTopic** with the following pattern. It is referenced later in the dialog node.
`["„“][A-Za-z0-9.:| @\']+["”“]`

## JSON for the dialog node

Use the following as JSON in a new dialog node under the **credential_node** to configure a slot and the call to a web action.

Configure a slot like this:

```
{
  "context": {
    "topic": "@newsTopic.literal"
  }
}
```


The response is set up like this:

```
{
  "context": {
    "skip_user_input": true
  },
  "output": {},
  "actions": [
    {

      "name": "/$private.cforg/slackdemo/getNews.json",
      "type": "web_action",
      "credentials": "$private.icfsecret",
      "parameters": {
        "topic": "<? $topic ?>"
      },
      "result_variable": "myNews"
    }
  ]
}```

Define a child node to return the result from the variable **myNews**.
