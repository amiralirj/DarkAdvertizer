from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup , InlineQueryResultArticle, InputTextMessageContent
from pyrogram.types.bots_and_keyboards import force_reply 

Start=ReplyKeyboardMarkup([['اکانت ها👤','اتک ⚠️'],
                                ['سین و لایک 👁️']
                                ,['اشتراک 🔋']
                                ,['پشتیبانی 👨‍💻']],resize_keyboard =True)

Management=ReplyKeyboardMarkup([['دادن سکه 🪙','انقال اکانت 👻'],['نجوا 📩' , 'ادمین گیر 👀','اطلاعات 🔭'],['پنل اصلی ⚙️']],resize_keyboard =True)

Attack= ReplyKeyboardMarkup([['اتک🔰',
        'بنر 📩'],
        ['اسپم📛',
        'لیست گیر🚸'],
        ['تنظیمات حرفه ای⚙️','قوی ترین اتکر ⚔️🔥'],
        ['بازگشت 🔙']],resize_keyboard =True) 

Main_Attack=ReplyKeyboardMarkup([
        ["تخریبی💥💥💥"]
        ,['هوشمند🧠',
        'تبلیغاتی👀', 'ادر🫂'],
        ['برگشت➡️']
    ],resize_keyboard =True)

banner=ReplyKeyboardMarkup([[
        'بنر های فعلی 📧'] ,[          
        'ثبت بنر📝'
    ],['برگشت➡️']],resize_keyboard =True)

Cancel=ReplyKeyboardMarkup([['❌ انصراف ❌']],resize_keyboard =True)
Cancel_Attack=ReplyKeyboardMarkup([['🚫 لغو اتک 🚫']],resize_keyboard =True)
Cancel_Spam=ReplyKeyboardMarkup([['🚫 لغو اسپم 🚫']],resize_keyboard =True)

Accounts=ReplyKeyboardMarkup([['وضعیت اکانت ها 🗂️' ,
    'لیست اکانت ها 📜'],
    ['تغییر فعالیت 🔆'],
        ['ثبت اکانت 📥',
        'حذف اکانت 🗑'],
        ['⚙️ تنظیمات اکانت' , 
        '🤖 استارت ربات'],[
            'leave 🚨' 
            , 'join 🚨'
        ],['گرفتن کد 🗳' , 'پاکسازی ♻️'],
        ['راهنما ❓',
        'بازگشت 🔙']],resize_keyboard =True)

Account_Deleting=ReplyKeyboardMarkup([[
        'حذف همه اکانت ها 🗑'
        ,'حذف چند اکانت ❌'],
        ['حذف ریپورت شده ها 🔇'],
    ['برگشت 🔙']],resize_keyboard =True)

Account_Setting=ReplyKeyboardMarkup([[
    '♻️ تنظیم خودکار مشخصات ♻️'],['🔱 هویت سازی 🔱'],
    ['📨 انتقال اکانت 📨', '📝 نتظیم مشخصات 📝'] ,
    ['برگشت 🔙']],resize_keyboard =True)

Seen=ReplyKeyboardMarkup([['ری اکشن 🤩','لایک ♥️'],
                          ['بلاک 🔒','انبلاک 🔓'],
                          ['بازگشت 🔙']],resize_keyboard =True) 

#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------| INLINE |--------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
Attack_Inline=lambda username , btn: InlineKeyboardMarkup([[InlineKeyboardButton(f'{btn}', url=f'https://t.me/{username}')]])

Channel= InlineKeyboardMarkup([[InlineKeyboardButton('ᴅᴀʀᴋ ᴀᴛᴛᴀᴄᴋᴇʀ', url='https://t.me/DarkBotsChannel')]])

Support=lambda username: InlineKeyboardMarkup([[InlineKeyboardButton('📞 پشتیبانی', url=f'https://t.me/{username}')]])

Delete_Banner=lambda ID:InlineKeyboardMarkup([[InlineKeyboardButton('حذف بنر 🗑', callback_data=f'DeleteBNR {ID}')]])

Choosing_Auto_Details=InlineKeyboardMarkup([[InlineKeyboardButton('عکس خودکار 🌉', callback_data='Auto_Details Pic')],[InlineKeyboardButton('بیو خودکار ✒️', callback_data='Auto_Details Bio')],[InlineKeyboardButton('نام خودکار 🔖', callback_data='Auto_Details Name')]])

Attack_Setting=InlineKeyboardMarkup([[InlineKeyboardButton('توقف هر اتک ⏱', callback_data='Attack_Setting A')],
                                     [InlineKeyboardButton('توقف هر راند ⏱', callback_data='Attack_Setting R')]])

Force=force_reply.ForceReply()

def Speed_Inline( Model)  :
    x=[[InlineKeyboardButton(f'{(i-10)/10} sec', callback_data=f'Speed-{Model} {(i-10)/10}'),
        InlineKeyboardButton(f'{(i-5)/10} sec', callback_data=f'Speed-{Model} {(i-5)/10}'),
        InlineKeyboardButton(f'{(i)/10} sec', callback_data=f'Speed-{Model} {(i)/10}'),
        InlineKeyboardButton(f'{(i+5)/10} sec', callback_data=f'Speed-{Model} {(i+5)/10}'),
        InlineKeyboardButton(f'{(i+10)/10} sec', callback_data=f'Speed-{Model} {(i+10)/10}')] for i in range(10,300,20)]
    x.append([InlineKeyboardButton('وارد کردن دستی ⌛️', callback_data=f'Speed-{Model} Manual')])
    return InlineKeyboardMarkup(x)

def Activity(all,page=0):
    Inlines=[]
    page*=2
    li=[]
    for j,i in enumerate(all[page:]):
        if str(i) not in li :
            Inlines.append([InlineKeyboardButton(f'{i.Activity_Emoji}{i}', callback_data=f'Change_Activity {int(i)} {page}')])
            li.append(str(i))
        if j>=20:
            Inlines.append([InlineKeyboardButton(f'⬅️ صفحه بعد ⬅️', callback_data=f'Next {page}')])
            return InlineKeyboardMarkup(Inlines) 
    return InlineKeyboardMarkup(Inlines) 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
async def Inline_Answer(inline_query,Channel,Banner,btn):
    await inline_query.answer(
        results=[InlineQueryResultArticle(
                title="HaHa",
                input_message_content=InputTextMessageContent(
                    f"{Banner}"),
                description=f"! Dark Attacker !",
                reply_markup=Attack_Inline(Channel,btn))],
        cache_time=1
    )

