import requests

# Posting
def YOUR_MESSAGE():

    dict_input = {"mission_time" : input("Input a time in seconds: "),
                  "comms" : input("Input a message: "),
                  "speaker" : input("Your name is: ")
                }
    response_post= requests.post(url="http://127.0.0.1:9000/insertrow", params=dict_input)

    return response_post

def SORRY_I_REGRET():

    dict_input = {"speaker" : input("Whose messages do you want to delete?: ")
                }
    response_delete= requests.post(url="http://127.0.0.1:9000/deleterow", params=dict_input)

    return response_delete