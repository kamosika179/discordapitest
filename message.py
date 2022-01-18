import requests

API_ENDPOINT = 'https://discord.com/api/v8'
def sendMessage(channel_id,data,header):
    r = requests.post(f'{API_ENDPOINT}/channels/{channel_id}/messages',data=data,headers=header)

def getMessage(channel_id,header):
    r = requests.get(f'{API_ENDPOINT}/channels/{channel_id}/messages',headers=header,params={"limit": 1})
    r_json = r.json()
    #print(r_json[0]["content"])
    return r_json[0]["content"]