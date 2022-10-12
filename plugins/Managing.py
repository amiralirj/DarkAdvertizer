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
        User(user).Add_Coin(Coin,True)
        await bot.send_message( user , TEXTS.Coin_Tranfered(Coin))
        await message.reply_text(TEXTS.Coin_Submitted , reply_markup=BUTTONS.Management)
    except:await message.reply_text(TEXTS.Not_Started , reply_markup=BUTTONS.Management)

@Advertising.on_message(RJ.filters.user(RJ.Owner) & RJ.regex('اشتراک روزانه 📅') , group=0)
async def Add_Membership(bot,message):
    user=Config.OWNER
    try:
        Id=str((await bot.Ask(int(user),TEXTS.Ask_Id,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120)).text)
        Date=int((await bot.Ask(int(user),TEXTS.Ask_Date,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120)).text)
    except TimeoutError :pass
    
    if Id.isdigit():Id=int(Id)
    try:
        user= (await bot.get_users(Id)).id
        Ex_date=User(user).Add_Membership(Date)
        await bot.send_message( user , TEXTS.Membership_Added(Ex_date))
        await message.reply_text(TEXTS.Membership_Submitted , reply_markup=BUTTONS.Management)
    except Exception as e :
        print(e)
        await message.reply_text(TEXTS.Not_Started , reply_markup=BUTTONS.Management)


@Advertising.on_message(RJ.filters.user(RJ.Owner) & RJ.regex('انقال اکانت 👻') , group=0)
async def Transfer_Deleted_Account_Numbers(bot,message):
    user=int((await bot.Ask(int(RJ.Owner),TEXTS.AskDeleted_Account,Msg=message,filters=RJ.filters.user(int(RJ.Owner)),reply_markup=BUTTONS.Cancel,timeout=120)).text)
    new_user=str((await bot.Ask(int(RJ.Owner),TEXTS.Ask_Reciver,Msg=message,filters=RJ.filters.user(int(RJ.Owner)),reply_markup=BUTTONS.Cancel,timeout=120)).text)
    user=User(user)
    try:
        new_user= (await bot.get_users(new_user)).id
    except:
        await message.reply_text(TEXTS.Not_Started , reply_markup=BUTTONS.Management)
        return
    new_user=User(int(new_user))
    new_user.Add_Coin(user.Coin,True)
    user.Set_0()
    x=''
    for i in user.All_numbers :
        Number(str(i['num']),int(user)).Transfer(int(new_user))
        x+=f'` +{i["num"]} ` \n '
        
        if len(x.split('\n')) > 50 :
            x=''
            await message.reply_text(TEXTS.Account_Tranferred(x,int(user),int(new_user)))
            await bot.send_message(int(new_user),TEXTS.Account_Tranferred(x,int(user),int(new_user)))
            
    if len(x.split('\n')) >=1  :
        await message.reply_text(TEXTS.Account_Tranferred(x,int(user),int(new_user)),reply_markup=BUTTONS.Management)
        await bot.send_message(int(new_user),TEXTS.Account_Tranferred(x,int(user),int(new_user)),reply_markup=BUTTONS.Management)
                
                
            
            

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
        
@Advertising.on_message(RJ.filters.user(RJ.Owner) & RJ.regex('فرایند ها 🔆') , group=0)
async def Active_Users(bot,message):
    Users=RJ.Active_Procces
    text=''
    for i in Users:
        text+=f'` {i} ` \n '
    
    text2=TEXTS.message_C
    ms=RJ.ms
    for i in ms :
        text2+=f'{i} >>> {ms[i]} '
        
    await message.reply_text(text2,reply_markup=BUTTONS.Management)
    await message.reply_text(TEXTS.Active_Procceses_Len(len(Users)),reply_markup=BUTTONS.Management)
    await message.reply_text(TEXTS.Active_Procceses(text),reply_markup=BUTTONS.Management)
    
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

@Advertising.on_message(RJ.filters.user(RJ.Owner) & RJ.filters.command('zero') , group=0)
async def Set_Coins_Zero(bot,message):
    user= (int(message.command[1]))
    User(user).Set_0()
    await message.reply_text(TEXTS.Procces_Compeleted_WO_NO , reply_markup=BUTTONS.Management)
    
    
@Advertising.on_message(RJ.filters.user(RJ.Owner) & RJ.regex('پنل اصلی ⚙️') , group=0)
async def Move_To_Pannel(bot,message):
    await message.reply_text(TEXTS.start,reply_markup=BUTTONS.Start)
    