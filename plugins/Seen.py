from .BOT import TEXTS , BUTTONS , Config , Number , Advertising , RJ  , User
from pyrogram.handlers import MessageHandler
from asyncio.exceptions import TimeoutError
from pyrogram import  errors
from asyncio import sleep

@Advertising.on_message(RJ.prv & RJ.regex('^لایک ♥️') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Send_Like(bot,message,user:User):
    try:
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text)
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
    for i in Nums:
        try:
            Chat=None
            app = await i.Start()
            try : 
                Chat=await app.join_chat(Channel)
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
    for i in Nums:
        try:
            Chat=None
            app = await i.Start()
            if  '/joinchat/' in Channel or  '+' in Channel :
                try : 
                    Chat=await app.join_chat(Channel)
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
            
    await message.reply_text(TEXTS.Reaction_Compeleted(X,Emoji),reply_markup=BUTTONS.Seen)