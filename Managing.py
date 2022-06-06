from .BOT import TEXTS , BUTTONS , Config , Number , Advertising , RJ , User
from pyrogram.enums import  ChatMembersFilter
from pyrogram import errors

@Advertising.on_message(RJ.filters.user(RJ.Owner) & RJ.regex('دادن سکه 🪙') , group=0)
async def Add_Coin(bot,message):
    user=Config.OWNER
    try:
        Id=str((await bot.Ask(int(user),TEXTS.Ask_Id,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120)).text)
        Coin=int((await bot.Ask(int(user),TEXTS.Ask_Coin_Amount,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120)).text)
    except TimeoutError :pass
    
    if Id.isdigit():Id=int(Id)
    try:
        user= (await bot.get_users(Id)).id
        User(user).Add_Coin(Coin)
        await bot.send_message( user , TEXTS.Coin_Tranfered(Coin))
        await message.reply_text(TEXTS.Coin_Submitted , reply_markup=BUTTONS.Management)
    except:await message.reply_text(TEXTS.Not_Started , reply_markup=BUTTONS.Management)
    
@Advertising.on_message(RJ.filters.user(RJ.Owner) & RJ.regex('انقال اکانت 👻') , group=0)
async def Transfere_Deleted_Account_Numbers(bot,message):pass

@Advertising.on_message(RJ.filters.user(RJ.Owner) & RJ.regex('نجوا 📩') , group=0)
async def Send_All(bot,message):
    try:
        text=((await bot.Ask(int(RJ.Owner),TEXTS.Ask_Text,Msg=message,filters=RJ.filters.user(int(RJ.Owner)),reply_markup=BUTTONS.Cancel,timeout=120)))
    except TimeoutError :pass
    X=0
    for i in RJ.All_Users:
        try:
            await text.copy(int(i))
            X+=1
        except:pass
        
    await message.reply_text(TEXTS.Procces_Compeleted(X) , reply_markup=BUTTONS.Management)
        
@Advertising.on_message(RJ.filters.user(RJ.Owner) & RJ.regex('ادمین گیر 👀') , group=0)
async def Admin_Catchers(bot,message):
    user=User(RJ.Owner)
    try:
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=90))).text)
        Gap_Link=str(((await bot.Ask(int(user),TEXTS.Ask_Link,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=30))).text)
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Management)
        return
    except:return
    
    Nums=RJ.Account(Nums,user)
    
    if Gap_Link.isdigit():Gap_Link=int(Gap_Link)
    elif not '/joinchat/' in Gap_Link and not  '+' in Gap_Link:Gap_Link=f'@{Gap_Link.split("/")[-1]}'
    else :Gap_Link=Gap_Link.replace('https://','')
    Users={}
    for i in Nums:
        try:
            app = await i.Start()
            try:
                Chat = await app.join_chat(Gap_Link)
            except errors.UserAlreadyParticipant : 
                Chat = await app.get_chat(Gap_Link)
            async for i in Chat.get_members(filter=ChatMembersFilter.ADMINISTRATORS):
                if i.user.is_bot : continue
                if i.user.username:Users[(str(i.user.username))]='2022 :) '
            try:await app.stop(False)
            except:pass
        except Exception as e:RJ.Log(int(user),f'Admin Catcher : {e}')
    X=''
    for i in Users:
        if len(X.split('\n')) >= 50 : 
            await message.reply_text(TEXTS.Username_Catched(X),reply_markup=BUTTONS.Management)
            X=''
        X+=f'@{i} \n'

    if len(X.split('\n')) > 0 :
            await message.reply_text(TEXTS.Username_Catched(X),reply_markup=BUTTONS.Management)
        

@Advertising.on_message(RJ.filters.user(RJ.Owner) & RJ.regex('اطلاعات 🔭') , group=0)
async def Stats(bot,message):
    bot_state=RJ.Details
    Users=(RJ.All_Users)
    X=sum([Users[i] for i in (Users)])
    await message.reply_text(TEXTS.Stats(bot_state,X),reply_markup=BUTTONS.Management)
    Data=RJ.DataBase_Data
    with open('Premenet_File.txt','a+') as f:
        f.write(str(Data))
    await message.reply_document(r'Premenet_File.txt' , file_name  = 'WWW.GITHUB.COM/AMIRALIRJ.txt')
    RJ.remove('Premenet_File.txt')


@Advertising.on_message(RJ.filters.user(RJ.Owner) & RJ.filters.command('who') , group=0)
async def User_Stats_M(bot,message):
    user= (await bot.get_users(int(message.command[1])))
    await message.reply_text(TEXTS.User_Details(user.username, user.first_name , user.mention , user.id ),reply_markup=BUTTONS.Management)
    
@Advertising.on_message(RJ.filters.user(RJ.Owner) & RJ.regex('پنل اصلی ⚙️') , group=0)
async def Move_To_Pannel(bot,message):
    await message.reply_text(TEXTS.start,reply_markup=BUTTONS.start)
    