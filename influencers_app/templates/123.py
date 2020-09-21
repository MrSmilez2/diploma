# from googleapiclient.discovery import build
#
# api_key = 'AIzaSyCWuZ5enVn4ga0G8s_F5LlTY9OkKCnd6tM'
#
# youtube = build('youtube', 'v3', developerKey=api_key)
# request = youtube.videos().list(
#     part="statistics",
#     id="C-sRWkjFmQ
# "
# )
#
# response = request.execute()
# print(response)
# print(response['items'][0]['statistics']['viewCount'])
# # for item in response['items']:
# #         print(item['statistics'].items())
# for item in response['items']:
#     for key, value in item['statistics'].items():
#         print(key, '->', value)
#
# def generate_hashtag(s):
#     if s == "":
#         return False
#     else:
#         x = s.split(" ")
#         print(x)
#         new_list = []
#         for el in x:
#             new_list.append(el.capitalize())
#         res ="#" + "".join(new_list)
#     return res
#
#
# print(generate_hashtag('Do We have A Hashtag'))


def increment_string(strng):
    # if strng.isalpha():
    #     return strng + '1'
    # elif strng == '':
    #     return strng + '1'
    # else:
    #     res = []
    #     for sym in strng:
    #         if sym.isdigit():
    #             res.append(sym)
    #     print(''.join(res))
    #     print(str(int(''.join(res)) + 1))
    #     if len(''.join(res)) != len(str(int(''.join(res)) + 1)):
    #         x = len(''.join(res)) - len(str(int(''.join(res)) + 1))
    #         return strng.replace(''.join(res), ('0' * x) + str(int(''.join(res)) + 1))
    #     else:
    #         return strng.replace(''.join(res), str(int(''.join(res)) + 1))
    prom = strng[::-1]
    res = []
    for cha in prom:
        if cha.isdigit():
            res.append(cha)
        else:
            break
    return ''.join(res)[::-1]


print(increment_string("nc28+$HK:~79246632y8;tlZ`4W$+6959089358514>343632263Fy_6350997,!96865@rUZ40000068231321"))