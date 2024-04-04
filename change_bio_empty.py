import telethon
import time
import datetime
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--string", required=True,
	help="String for txt")
ap.add_argument("-a", "--app", required=True,
        help="String for app_type")
ap.add_argument("-i", "--id", required=True,
        help="String for app_id")
ap.add_argument("-o", "--hash", required=True,
        help="String for app_hash")

args = vars(ap.parse_args())
string = args["string"]
app = args["app"]
app_id = args["id"]
app_hash = args["hash"]


with telethon.TelegramClient('me', app_id, app_hash) as client:
    async def do():
            if app == "plex" :
               nowstr = datetime.datetime.now().strftime('%H:%M') + ": \U0001F37F Plex | " + string + " \U0001F37F"
            else:
               nowstr = string
            try:
               await client(telethon.functions.account.UpdateProfileRequest(about=nowstr))
            except telethon.errors.rpcerrorlist.FloodWaitError as e:
               print('Flood waited for', e.seconds)
               time.sleep(e.seconds + 1)
               time.sleep(1)
               await client(telethon.functions.account.UpdateProfileRequest(about=nowstr))
    client.loop.run_until_complete(do())
