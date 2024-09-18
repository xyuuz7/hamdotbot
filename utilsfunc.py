from time import time
from dotenv import load_dotenv
import os
import emoji

load_dotenv()

def genrand_stickerpack_name(msg):
        cur_time = int(time());
        return [
                f'Sticker {msg.from_user.first_name} {msg.from_user.last_name}',
                f'a{msg.from_user.id}_on_{cur_time}_by_{os.getenv("BOT_USERNAME")}',
        ]

def get_file_id(msg):
        if msg.reply_to_message.photo != None:
                return msg.reply_to_message.photo.file_id
        if msg.reply_to_message.animation != None:
                return msg.reply_to_message.animation.file_id
        if msg.reply_to_message.sticker != None:
                return msg.reply_to_message.sticker.file_id
        
def sanitize_emoji(msg):
    

    try:
        cur = msg.command[1]
        
        if len(msg.command[1]) > 1:
            return {
                "err": 1,
                "msg": "A custom emoji must be just 1 chars length",
                "ret": None
            }
        
        if emoji.is_emoji(msg.command[1]) == False:
            return {
                "err": 1,
                "msg": "You need emoji, not a chars",
                "ret": None
            }
    except IndexError:
        cur = "🗿"
        
    return {
        "err": 0,
        "msg": None,
        "ret": cur
    }
            

                        