from http.client import HTTPSConnection 
from sys import stderr 
from json import dumps 
from time import sleep 


with open("channel_id","r") as channel_in:
    channel_id = channel_in.readline()

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 
 
def send_message(conn, channel_id, message_data, token): 
    # try: 
        header_data = { 
            "content-type": "application/json", 
            "user-agent": "discordapp.com", 
            "authorization": None, 
            "host": "discordapp.com",
            "referer": "https://discord.com/channels/829801507800743986/829810532960960563" 
        }
        header_data["authorization"] = token

        conn.request("POST", f"/api/v6/channels/{channel_id}/messages", message_data, header_data) 
        resp = conn.getresponse() 
         
        if 199 < resp.status < 300: 
            print("Message sent...") 
            pass
 
        else: 
            stderr.write(f"Received HTTP {resp.status}: {resp.reason}\n") 
            pass 
 
    # except: 
        # stderr.write("Failed to send_message\n") 

def main(message,token_file): 
    message_data = { 
        "content": message, 
        "tts": "false", 
    }
    fin = open(token_file,"r")
    token = fin.readline().strip()

    send_message(get_connection(), channel_id, dumps(message_data), token) 
 
if __name__ == '__main__': 
    while True:     # Infinite loop 
        main("hihi")      # Send the message
        sleep(3600) # Wait an hour to repeat