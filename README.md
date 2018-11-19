# Small chatbot with current news
A small chatbot showing how to incorporate IBM Watson Discovery News into a Watson Assistant bot

## Setup
Follow the instructions for the [Watson Conversation Tool](https://github.com/data-henrik/watson-conversation-tool) to configure the service credentials for IBM Watson Assistant. Then, in [processDiscoveryNews4chat.py](processDiscoveryNews4chat.py) replace the values for username and password with the correct ones for the Discovery service.

## Test
You can test the chatbot using the following command. Use your workspace_id:
`python wctool.py -dialog -id your-workspace-id -actionmodule processDiscoveryNews4chat -outputonly`

If you want to see the full JSON structures then leave out the option **outputonly**.

Here is a sample conversation:
> Please enter your input message:   
> news about "IBM Cloud"   
> \>\> processing client actions...   
>   
> Response:   
> [
  "This is what I found IBM reinforces enterprise multicloud growth // International Business Machines : IBM Introduces New Services to Automate Cloud Migration // Here's What You Missed Out by Overlooking IBM's Stock // IBM Extends Reach of Kubernetes Platform to Multiple Clouds // IBM reinforces multicloud growth with automation tools, ServiceNow expansion // Hundreds of Leading Global Enterprises Deploy IBM Cloud Private // SES Networks Enables Direct Connectivity to IBM Cloud via Global Satellite Network // International Business Machines : Hundreds of Leading Global Enterprises Deploy IBM Cloud Private // SES Networks Enables Direct Connectivity to IBM Cloud via Global Satellite Network // Industry Insight: IBM on Multicloud Search and AI Strategy"
]





