from googleapiclient.discovery import build

api_key = 'AIzaSyCWuZ5enVn4ga0G8s_F5LlTY9OkKCnd6tM'

youtube = build('youtube', 'v3', developerKey=api_key)
request = youtube.videos().list(
    part="statistics",
    id="C-sRWkjFmQ
"
)

response = request.execute()
print(response)
print(response['items'][0]['statistics']['viewCount'])
# for item in response['items']:
#         print(item['statistics'].items())
for item in response['items']:
    for key, value in item['statistics'].items():
        print(key, '->', value)



