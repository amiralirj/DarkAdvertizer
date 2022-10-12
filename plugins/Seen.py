from .BOT import TEXTS , BUTTONS , Config , Number , Advertising , RJ  , User
from pyrogram.raw.functions.account import ReportPeer 
from pyrogram.raw.functions.messages import Report , GetMessagesViews
from asyncio.exceptions import TimeoutError
from pyrogram import  errors , Client
from asyncio import sleep


@Advertising.on_message(RJ.prv & RJ.regex('^سین 👁‍🗨') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Seen_post(bot,message,user:User):
    try:
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text)
        Link=str(((await bot.Ask(int(user),TEXTS.Ask_P_O_Link,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60,disable_web_page_preview =True))).text)
        if Link.split('/')[-2].isdigit():
            Channel=str(((await bot.Ask(int(user),TEXTS.Ask_Private_Link,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text).replace('https://','')
            Private=True
        else:
            Private=False
            Channel=Link.split('/')[-2]
        id=[int(Link.split('/')[-1])]
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Seen)
        return
    except:return
    
    Nums=RJ.Account(Nums,user)
    
    X=0
    gap_link=Channel
    
    for i in Nums:
        try:
            Chat=None
            app = await i.Start()
            try : 
                if Private :
                    Chat=await app.join_chat(gap_link)
                    Channel=int(Chat.id)
            except:pass
            await app.invoke(GetMessagesViews( peer= (await app.resolve_peer(Channel)) , id=id , increment = True))
            X+=1
        except Exception as e:RJ.Log(int(user),f'Seen : {e}')
        finally : 
            try:
                if Chat:await Chat.leave()
            except:pass
            try:await app.stop(False)
            except:pass
            
    user.Add_Coin(Config.seen * X)
    await message.reply_text(TEXTS.Procces_Compeleted(X),reply_markup=BUTTONS.Seen)
    
@Advertising.on_message(RJ.prv & RJ.regex('^لایک ♥️') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Send_Like(bot,message,user:User):
    try:
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text)
        Link=str(((await bot.Ask(int(user),TEXTS.Ask_P_O_Link,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60,disable_web_page_preview =True))).text)
        if Link.split('/')[-2].isdigit():
            Channel=str(((await bot.Ask(int(user),TEXTS.Ask_Private_Link,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text).replace('https://','')
            Private=True
        else:
            Private=False
            Channel=Link.split('/')[-2]
        id=int(Link.split('/')[-1])
        
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Seen)
        return
    except:return
    
    Nums=RJ.Account(Nums,user)
    
    X=0
    gap_link=Channel
    
    for i in Nums:
        try:
            Chat=None
            app = await i.Start()
            try : 
                if Private :
                    Chat=await app.join_chat(gap_link)
                    Channel=int(Chat.id)
            except:pass
            Butt=(await app.get_messages(Channel,id))
            await Butt.click(0)
            await sleep(1)
            X+=1
        except Exception as e:RJ.Log(int(user),f'Sending Reaction : {e}')
        finally : 
            try:
                if Chat:await Chat.leave()
            except:pass
            try:await app.stop(False)
            except:pass
            
    user.Add_Coin(Config.like * X)
    await message.reply_text(TEXTS.Procces_Compeleted(X),reply_markup=BUTTONS.Seen)
    
@Advertising.on_message(RJ.prv & RJ.regex('^انبلاک 🔓') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Unblock_User(bot,message,user:User):
    try:
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
        username=str(((await bot.Ask(int(user),TEXTS.Ask_Id,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text)
        if username.isdigit():user=int(user)
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Seen)
        return
    except:return

    Nums=RJ.Account(Nums,user)
    X=0
    for i in Nums:
        try:
            app = await i.Start()
            await app.unblock_user(username)
            await sleep(1)
            X+=1
        except Exception as e:RJ.Log(int(user),f'Unblock Users : {e}')
        finally : 
            try:await app.stop(False)
            except:pass
    user.Add_Coin(Config.block * X)
    await message.reply_text(TEXTS.Procces_Compeleted(X),reply_markup=BUTTONS.Seen)
            


    
@Advertising.on_message(RJ.prv & RJ.regex('^بلاک 🔒') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Block_User(bot,message,user:User):
    try:
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text)
        username=str(((await bot.Ask(int(user),TEXTS.Ask_Id,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text)
        if username.isdigit():user=int(user)
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Seen)
        return
    except:return

    Nums=RJ.Account(Nums,user)
    X=0
    for i in Nums:
        try:
            app = await i.Start()
            await app.block_user(username)
            await sleep(1)
            X+=1
        except Exception as e:RJ.Log(int(user),f'Block Users : {e}')
        finally : 
            try:await app.stop(False)
            except:pass
    user.Add_Coin(Config.block * X)
    await message.reply_text(TEXTS.Procces_Compeleted(X),reply_markup=BUTTONS.Seen)
            


    
@Advertising.on_message(RJ.prv & RJ.regex('^ری اکشن 🤩') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Send_Reaction(bot,message,user:User):
    try:
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
        Emoji=str(((await bot.Ask(int(user),TEXTS.Ask_Emoji,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text)
        Link=str(((await bot.Ask(int(user),TEXTS.Ask_P_O_Link,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60,disable_web_page_preview =True))).text)
        if Link.split('/')[-2].isdigit():
            Channel=str(((await bot.Ask(int(user),TEXTS.Ask_Private_Link,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text).replace('https://','')
        else:
            Channel=Link.split('/')[-2]
        id=int(Link.split('/')[-1])
        
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Seen)
        return
    except:return
    
    Nums=RJ.Account(Nums,user)
    
    X=0
    gap_link=Channel
    
    for i in Nums:
        try:
            Chat=None
            app = await i.Start()
            if  '/joinchat/' in Channel or  '+' in Channel :
                try : 
                    Chat=await app.join_chat(gap_link)
                    Channel=int(Chat.id)
                except:pass
            await app.send_reaction(Channel,id,Emoji)
            await sleep(1)
            X+=1
        except (errors.ReactionEmpty , errors.ReactionInvalid ):
            await message.reply_text(TEXTS.Invalied_Reaction,reply_markup=BUTTONS.Seen)
            try:await app.stop(False)
            except:pass
            return
        except Exception as e:RJ.Log(int(user),f'Sending Reaction : {e}')
        finally : 
            try:
                if Chat:await Chat.leave()
            except:pass
            try:await app.stop(False)
            except:pass
    user.Add_Coin(Config.reaction * X)
    await message.reply_text(TEXTS.Reaction_Compeleted(X,Emoji),reply_markup=BUTTONS.Seen)

@Advertising.on_message(RJ.prv & RJ.regex('^ریپورت کانال 🪓') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Repoet_User(bot,message,user:User):
    try:
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text)
        username=str(((await bot.Ask(int(user),TEXTS.Ask_Id,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text)
        Reason=str(((await bot.Ask(int(user),TEXTS.Ask_Reason,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text)
        
        if 't.me' in username:
            username=username.split('/')[-1]
            
        try:Reason=RJ.report[Reason]
        except:
            await message.reply_text(TEXTS.Wrong,reply_markup=BUTTONS.Seen)
            return
        Reason_message=TEXTS.report(RJ.Random_Name)
        if Reason==RJ.report['Other']:Reason_message=str(((await bot.Ask(int(user),TEXTS.ask_RMessage,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text)
        if username.isdigit():username=int(user)
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Seen)
        return
    except:return
    Nums=RJ.Account(Nums,user)
    X=0
    for i in Nums:
        try:
            app = await i.Start()
            victam=await app.resolve_peer(username)
            await app.invoke(ReportPeer(peer=victam,reason=Reason(),message=Reason_message))
            X+=1
        except Exception as e:RJ.Log(int(user),f'Report Users : {e}')
        finally : 
            try:await app.stop(False)
            except:pass
            
    user.Add_Coin(Config.report * X)
    await message.reply_text(TEXTS.Reported_by(X),reply_markup=BUTTONS.Seen)
            
@Advertising.on_message(RJ.prv & RJ.regex('^ریپورت پیام 🔪') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Report_Message(bot,message,user:User):
    try:
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text)
        Link=str(((await bot.Ask(int(user),TEXTS.Ask_P_O_Link,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text)
        Reason=str(((await bot.Ask(int(user),TEXTS.Ask_Reason,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text)
        try:Reason=RJ.report[Reason]
        except:
            await message.reply_text(TEXTS.Wrong,reply_markup=BUTTONS.Seen)
            return
        Reason_message=TEXTS.report(RJ.Random_Name)
        if Reason==RJ.report['Other']:Reason_message=str(((await bot.Ask(int(user),TEXTS.ask_RMessage,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text)
        if Link.split('/')[-2].isdigit():
            Channel=str(((await bot.Ask(int(user),TEXTS.Ask_Private_Link,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text).replace('https://','')
        else:
            Channel=Link.split('/')[-2]
        id=int(Link.split('/')[-1])
        
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Seen)
        return
    except:return
    Nums=RJ.Account(Nums,user)
    X=0
    gap_link=Channel
    for i in Nums:
        try:
            Chat=None
            app = await i.Start()
            if  '/joinchat/' in Channel or  '+' in Channel :
                try : 
                    Chat=await app.join_chat(gap_link)
                    Channel=int(Chat.id)
                except:pass
            channel_pear=await app.resolve_peer(Channel)
            await app.invoke(Report(peer=channel_pear,id=[id],reason=Reason(),message=Reason_message))
            X+=1
        except Exception as e:RJ.Log(int(user),f'Report MSG : {e}')
        finally : 
            try:
                if Chat:await Chat.leave()
            except:pass
            try:await app.stop(False)
            except:pass
    user.Add_Coin(Config.report * X)
    await message.reply_text(TEXTS.Reported_by(X),reply_markup=BUTTONS.Seen)


# @Advertising.on_message(RJ.prv & RJ.regex('^اکو ایردراپ 🔊💥') , group=0)
# @RJ.User_Details
# @RJ.Coin_Limit
# async def Echo_Bot(bot:Advertising,message,user:User):
#     try:
#         Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
#         Robot=str(((await bot.Ask(int(user),TEXTS.StartBot_User,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text)
#     except TimeoutError :
#         await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Seen)
#         return
#     except:return
    
#     Nums=RJ.Account(Nums,user)
#     cancel=False
#     Active_Nums=[]
#     for i in Nums:
#         try:
#             app=await i.Start()
#             Active_Nums.append(app)
#         except:pass
        
#     while cancel==False: 
#         try:
#             work =str(((await bot.Ask(int(user),TEXTS.Echo_Airdrop,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text)
#             txt =str(((await bot.Ask(int(user),TEXTS.Echo_Airdrop,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text)
#         except : break
#         if 'cancel' in work.lower() or TEXTS.Cancel_Proccess in  work:break
        
#         elif 'JOIN' in work.lower():
#             msg_ent=[i for i in work.entities if i.URL or ent.TEXT_LINK or ent.MENTION   ]
#             channels=[]
#             for i in msg_ent : 
#                 if i.URL or ent.TEXT_LINK : 
#                     channels+=RJ.RetLink(str(i.url))    
            
#             for i in message
                
    