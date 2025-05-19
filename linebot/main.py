from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage

from dotenv import load_dotenv
import os

from utils.news_scraper import get_news_summary
from utils.indicator_analyzer import analyze_market
from utils.image_generator import generate_graph_image

load_dotenv()

app = Flask(__name__)

line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_msg = event.message.text

    if "วิเคราะห์" in user_msg:
        summary = get_news_summary()
        analysis = analyze_market()
        image_url = generate_graph_image()

        reply_text = f"""🤖 สรุปข่าว:
{summary}

📊 วิเคราะห์จากจักรวาล:
{analysis}
"""
        line_bot_api.reply_message(event.reply_token, [
            TextSendMessage(text=reply_text),
            ImageSendMessage(original_content_url=image_url, preview_image_url=image_url)
        ])
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="พิมพ์ว่า 'วิเคราะห์' เพื่อให้ฉันวิเคราะห์ให้! 🚀")
        )

if __name__ == "__main__":
    app.run()