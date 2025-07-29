from flask import Flask, request, abort, render_template
from flask_sqlalchemy import SQLAlchemy
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import PostbackEvent #功能
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, URITemplateAction
from linebot.models import QuickReply, QuickReplyButton, MessageAction #快速選單需求
import openai
import string
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
line_channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
line_channel_secret = os.getenv("LINE_CHANNEL_SECRET")


app = Flask(__name__)

line_bot_api = LineBotApi(line_channel_access_token)
handler = WebhookHandler(line_channel_secret)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data( as_text = True ) 
    try :
        handler.handle( body, signature ) 
    except InvalidSignatureError :
        abort( 400 )
    return "OK"

@handler.add( MessageEvent, message = TextMessage )
def handle_message( event ):
    
    lineid    = event.source.user_id
    userinput = event.message.text
    if ( userinput == "鏈結串列( Linked List )") :
        chapter1( event )
    elif ( userinput == "堆疊與佇列( Stack and Queue )" ) :
        chapter2( event )
    elif ( userinput == "樹狀結構與二元樹( Tree and Binary Tree )" ) :
        chapter3( event )
    elif ( userinput == "堆積( Heap )" ) :
        chapter4( event )
    elif ( userinput == "圖形結構與最短路徑" ) :
        chapter5( event )
    elif ( userinput == "排序、搜尋、雜湊" ) :
        chapter6( event )
    elif ( userinput[:9] == "To GPT : " ) :
        GPT_Start( event, userinput )


@handler.add( PostbackEvent )
def GPT_Start( event, userinput ) :
    input_message = userinput[9:] + "，請用250字以內回覆給我"

    messages = []
    messages.append({"role":"user","content":input_message})   # 添加 user 回應
        
    try : 
        response = openai.ChatCompletion.create(
            model="gpt-4",
            max_tokens=512,
            temperature=0.5,
            messages=messages,
        )
    except Exception as exc :
        print(exc)

    gpt_response = response.choices[0].message.content.replace('\n','')
    line_bot_api.reply_message( event.reply_token, TextSendMessage(text=f'{gpt_response}') )

def chapter1( event ) :
    message = TextSendMessage(
        text="請選擇想詢問的問題",
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(label="Linked List介紹", text="To GPT : 簡單介紹Linked List")
                ),
                QuickReplyButton(
                    action=MessageAction(label="Linked List與陣列的差別", text="To GPT : 簡單介紹Linked List與陣列的差別")
                ),
                QuickReplyButton(
                    action=MessageAction(label="Linked List種類", text="To GPT : Linked List有哪些種類")
                ),
                QuickReplyButton(
                    action=MessageAction(label="單向Linked List範例", text="To GPT : 給我一個C語言單向Linked List的範例")
                ),
                QuickReplyButton(
                    action=MessageAction(label="雙向Linked List範例", text="To GPT : 給我一個C語言雙向Linked List的範例")
                ),
                QuickReplyButton(
                    action=MessageAction(label="環狀Linked List範例", text="To GPT : 給我一個C語言環狀Linked List的範例")
                ),
            ]
        )
    )
    
    line_bot_api.reply_message( event.reply_token, message )

def chapter2( event ) :
    message = TextSendMessage(
        text="請選擇想詢問的問題",
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(label="堆疊(Stack)介紹", text="To GPT : 簡單介紹堆疊(Stack)")
                ),
                QuickReplyButton(
                    action=MessageAction(label="堆疊(Stack)範例", text="To GPT : 給我一個C語言堆疊(Stack)的範例")
                ),
                QuickReplyButton(
                    action=MessageAction(label="佇列(Queue)介紹", text="To GPT : 簡單介紹佇列(Queue)")
                ),
                QuickReplyButton(
                    action=MessageAction(label="佇列(Queue)範例", text="To GPT : 給我一個C語言佇列(Queue)的範例")
                ),
            ]
        )
    )
    
    line_bot_api.reply_message( event.reply_token, message )

def chapter3( event ) :
    message = TextSendMessage(
        text="請選擇想詢問的問題",
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(label="樹狀結構介紹", text="To GPT : 簡單介紹資料結構的樹狀結構")
                ),
                QuickReplyButton(
                    action=MessageAction(label="樹狀結構範例", text="To GPT : 給我一個C語言樹狀結構的範例")
                ),
                QuickReplyButton(
                    action=MessageAction(label="二元樹介紹", text="To GPT : 簡單介紹資料結構的二元樹")
                ),
                QuickReplyButton(
                    action=MessageAction(label="二元樹範例", text="To GPT : 給我一個C語言二元樹的範例")
                ),
                QuickReplyButton(
                    action=MessageAction(label="前序法介紹", text="To GPT : 簡單介紹資料結構中的前序法(Preorder Traversal)")
                ),
                QuickReplyButton(
                    action=MessageAction(label="中序法介紹", text="To GPT : 簡單介紹資料結構中的中序法(Inorder Traversal)")
                ),
                QuickReplyButton(
                    action=MessageAction(label="後序法介紹", text="To GPT : 簡單介紹資料結構中的後序法(Postorder Traversal)")
                ),

                
            ]
        )
    )
    
    line_bot_api.reply_message( event.reply_token, message )

def chapter4( event ) :
    message = TextSendMessage(
        text="請選擇想詢問的問題",
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(label="累堆(Heap)介紹", text="To GPT : 簡單介紹資料結構中的累堆(Heap)")
                ),
                QuickReplyButton(
                    action=MessageAction(label="最大累堆(Max Heap)介紹", text="To GPT : 簡單介紹資料結構中的最大累堆(Max Heap)")
                ),
                QuickReplyButton(
                    action=MessageAction(label="最小累堆(Min Heap)介紹", text="To GPT : 簡單介紹資料結構中的最小累堆(Min Heap)")
                ),
                QuickReplyButton(
                    action=MessageAction(label="最大累堆(Max Heap)範例", text="To GPT : 給我一個C語言最大累堆(Max Heap)的範例")
                ),
                QuickReplyButton(
                    action=MessageAction(label="最小累堆(Min Heap)範例", text="To GPT : 給我一個C語言累堆(Min Heap)的範例")
                ),
            ]
        )
    )
    
    line_bot_api.reply_message( event.reply_token, message )

def chapter5( event ) :
    message = TextSendMessage(
        text="請選擇想詢問的問題",
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(label="圖形結構介紹", text="To GPT : 簡單介紹資料結構中的圖形結構")
                ),
                QuickReplyButton(
                    action=MessageAction(label="最短路徑介紹", text="To GPT : 簡單介紹資料結構中的最短路徑")
                ),
                QuickReplyButton(
                    action=MessageAction(label="深度優先搜尋介紹", text="To GPT : 簡單介紹資料結構中的深度優先搜尋(Depth-first Search)")
                ),
                QuickReplyButton(
                    action=MessageAction(label="廣度優先搜尋介紹", text="To GPT : 簡單介紹資料結構中的深度優先搜尋(Breath-first Search)")
                ),
                QuickReplyButton(
                    action=MessageAction(label="最小成本生成樹介紹", text="To GPT : 簡單介紹資料結構中的最小成本生成樹(Minimum Spanning Tree)")
                ),
                QuickReplyButton(
                    action=MessageAction(label="Sollin's演算法介紹", text="To GPT : 簡單介紹資料結構中的Sollin's Algorithm")
                ),
                QuickReplyButton(
                    action=MessageAction(label="Prim's演算法介紹", text="To GPT : 簡單介紹資料結構中的Prim's Algorithm")
                ),
                QuickReplyButton(
                    action=MessageAction(label="Kruskal's演算法介紹", text="To GPT : 簡單介紹資料結構中的Kruskal's Algorithm")
                ),
            ]
        )
    )
    
    line_bot_api.reply_message( event.reply_token, message )

def chapter6( event ) :
    message = TextSendMessage(
        text="請選擇想詢問的問題",
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(label="排序法介紹", text="To GPT : 簡單介紹資料結構的排序法")
                ),
                QuickReplyButton(
                    action=MessageAction(label="排序法種類", text="To GPT : 資料結構中有哪些類型的排序法")
                ),
                QuickReplyButton(
                    action=MessageAction(label="搜尋法介紹", text="To GPT : 簡單介紹資料結構的搜尋法")
                ),
                QuickReplyButton(
                    action=MessageAction(label="搜尋法種類", text="To GPT : 資料結構中有哪些類型的搜尋法")
                ),
                QuickReplyButton(
                    action=MessageAction(label="雜湊介紹", text="To GPT : 簡單介紹雜湊")
                ),
                QuickReplyButton(
                    action=MessageAction(label="雜湊的應用", text="To GPT : 資料結構中的雜湊有哪些應用")
                ),
            ]
        )
    )
    
    line_bot_api.reply_message( event.reply_token, message )

if __name__ == '__main__':
    app.run()

