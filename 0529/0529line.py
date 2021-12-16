from linebot import LineBotApi
from linebot.models import TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage, VideoSendMessage


bot = LineBotApi("SO3U/GpBN0KYGAdsrT/NEGh9lQ8q7SCb1rj/ajDhWsYNyC2uHEPvRWzFaXUgeDVoj0k6tCFjFERXUUfcJozzIG88dGLmpBK8WR6PE+xSLneu+wuebE3mgQRt4WZ1LRAgr3RrGv+n3jlNPIYgeT2euQdB04t89/1O/w1cDnyilFU=")
userID = 'U828989e3a59614b66e4262c62f480c6f'

message = TextSendMessage(text="asjienfskjefn")
bot.push_message(userID, message)

for i in range(1, 15):
    sticker = StickerSendMessage(package_id='1', sticker_id=str(i))
    bot.push_message(userID, sticker)

image = ImageSendMessage(original_content_url="https://cdn.eso.org/images/thumb300y/eso1907a.jpg", preview_image_url="https://cdn.eso.org/images/thumb300y/eso1907a.jpg")
bot.push_message(userID, image)

location = LocationSendMessage(title="wjkenkjnwe", address="skjervnjksenv", latitude=23.312, longitude=120.64)
bot.push_message(userID, location)

video = VideoSendMessage(original_content_url="https://i.imgur.com/krCpXjG.mp4", preview_image_url="https://cdn.eso.org/images/thumb300y/eso1907a.jpg")
bot.push_message(userID, video)

allMessage = [video, location, image, sticker, message]
bot.push_message(userID, allMessage)