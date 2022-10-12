from .BOT import TEXTS , BUTTONS , Config , Number , Advertising , RJ  , User
from .Api import step_one, step_two, step_three, step_four, helper_steps 
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.raw.functions.auth import ResetAuthorizations
from pyrogram.handlers import MessageHandler
from asyncio.exceptions import TimeoutError
from pyrogram import  Client , errors
from random import  choice , randint
from pyrogram.enums import ChatType
from asyncio import sleep
import re
#--------------------|
Proxys={}          #-|
Api_Keys={}        #-|
Account_Details={} #-|
app=None           #-|
#--------------------|

#---------------------------------------------------------------------------------| FUNCTIONS |---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------| FUNCTIONS |---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------| FUNCTIONS |---------------------------------------------------------------------------------#
    
async def Loggin(client,message):
    global Api_Keys , Proxys , Account_Details
    try:  Code = (re.search('\d{5}',str(message.text)).group(0))
    except: Code = False
    USR=await client.get_me()
    Num=(USR).phone_number
    Num = Number(str(Num),Account_Details[int(Num)]['id'])
    Loggined_User=User(Account_Details[int(Num)]['id'])
    if not Code :
        Done=False
        Proxy = Proxys[int(Num)]
        provided_code = helper_steps.extract_code_imn_ges(message)
        status_r, cookie_v = step_two.login_step_get_stel_cookie(
            str(Num),
            Api_Keys[int(Num)]['phone_hash'],
            provided_code,
            Proxy)
        if status_r:
            status_t, response_dv = step_three.scarp_tg_existing_app(cookie_v,Proxy)
            name = f'DARK {randint(1,8500)}'
            if not status_t:
                await sleep(5)
                step_four.create_new_tg_app(
                    cookie_v,
                    response_dv.get("tg_app_hash"),
                    name,
                    name,
                    name,
                    name,
                    Proxy=Proxy
                )
                await sleep(5)
                status_t, response_dv = step_three.scarp_tg_existing_app(cookie_v,Proxy)
            if status_t:
                Api_Id = response_dv["App Configuration"]["app_id"]
                Api_Hash = response_dv["App Configuration"]["api_hash"]
                helper_steps.Write(f'{Api_Hash}:{Api_Id}')
                Done=True
                Api_Keys[int(Num)]={'hash':Api_Hash , 'id':Api_Id }
                D_D=RJ.Get_Device_Detais
                Main_Acc=Client(f'{str(Num)}',Api_Id,Api_Hash,phone_number=str(Num),workdir=Config.Sessions)#,device_model=D_D[0],system_version=D_D[1],app_version=D_D[2],lang_code='en')
                await Main_Acc.connect()
                Account_Details[int(Num)]['phone_hash']=(await Main_Acc.send_code(str(Num))).phone_code_hash
                Account_Details[int(Num)]['Client']=Main_Acc
        if not Done:
            await RJ.Auto_Detail_Setter( client, Loggined_User)
            # try:await client.join_chat(Config.Dark_Channel)
            # except:pass
            Session_String=(await client.export_session_string())
            Num.Add_Number(Api_Keys[int(Num)]['id'],Api_Keys[int(Num)]['hash'],Session_String)
            Loggined_User.Add_Coin(Config.Adding_Account)
            await app.send_message(Account_Details[int(Num)]['id'], TEXTS.Runned_WO_API( str(Num) , USR.first_name , USR.id),reply_markup=BUTTONS.Accounts)
            Account_Details.pop(int(Num))
            Api_Keys.pop(int(Num))
            await client.stop(False)
            try:await client.disconnect()
            except:pass
    else :           
        Main_Acc=Account_Details[int(Num)]['Client']       
        try:
            USR=await Main_Acc.sign_in(str(Num),Account_Details[int(Num)]['phone_hash'],Code)
        except:
            USR=await Main_Acc.check_password(str(Account_Details[int(Num)]['pass']))
        try:
            await Main_Acc.send_message(f'@{Config.BOT_USERNAME}','/start')
        except errors.YouBlockedUser :pass
        try:
            await RJ.Auto_Detail_Setter( Main_Acc, Loggined_User) 
            # try:await Main_Acc.join_chat(Config.Dark_Channel)
            # except:pass
            Session_String=str(await Main_Acc.export_session_string())
            Num.Add_Number(Api_Keys[int(Num)]['id'],Api_Keys[int(Num)]['hash'],Session_String)
            Loggined_User.Add_Coin(Config.Adding_Account)
            await app.send_message(Account_Details[int(Num)]['id'],TEXTS.Runned_W_API( str(Num) , Api_Keys[int(Num)]['hash'] , Api_Keys[int(Num)]['id'] , USR.first_name , USR.id ),reply_markup=BUTTONS.Accounts)
            Account_Details.pop(int(Num))
            Api_Keys.pop(int(Num))
            try:await client.log_out()
            except:
                try:await client.disconnect()
                except:pass
        except Exception as e :
            RJ.Log(int(Account_Details[int(Num)]['id']),f'Second Loggin : {e}')
            await RJ.Auto_Detail_Setter( client, Loggined_User) 
            # try:await client.join_chat(Config.Dark_Channel)
            # except:pass
            Session_String=(await client.export_session_string())
            Num.Add_Number(Api_Keys[int(Num)]['id'],Api_Keys[int(Num)]['hash'],Session_String)
            Loggined_User.Add_Coin(Config.Adding_Account)
            await app.send_message(Account_Details[int(Num)]['id'], TEXTS.Runned_WO_API( str(Num) , USR.first_name , USR.id),reply_markup=BUTTONS.Accounts)
            Account_Details.pop(int(Num))
            Api_Keys.pop(int(Num))
            await client.stop(False)
            await Main_Acc.disconnect()
        
async def SpamBot(app,user):
    try:
        await app.send_message("@SpamBot", "/start")
        await sleep(3)
        async for message in app.get_chat_history("SpamBot"):
            text=message.text
            if re.search(r"^Good news", text) or re.search(r"^مژده", text):
                report=['Free' ,  None ]
            elif re.search(r"Unfortunately", text):
                report=['ForEver' ,  None ]
            elif re.search(r"until(.*)\.", text):
                reep=re.findall(r"limited until(.*)\.", text)
                report= ['temporary' , reep[0]]
            elif re.search(r"محدودیت دفعه بعد طولانی‌تر", text):
                reep=text.split('محدودیت حساب کاربری شما به صورت اتوماتیک در')[-1].split('برداشته خواهد شد')[0]
                report= ['temporary' , reep[0]]
            elif 'until' in str(text):
                report=str(text).split('until')[1].split('.')[0]
            else:
                RJ.Log(int(user),f'SPAM 404 : {text}')
                report=['NotFound' ,  None ]
            break 
        return report
    except errors.YouBlockedUser:
        await app.unblock_user("@SpamBot")
        await SpamBot(app,user)
    except Exception as e:
        RJ.Log(int(user),f'SPAM : {e}')
        return ['Error' ,  None ]
            

#---------------------------------------------------------------------------------| LOGGIN |---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------| LOGGIN |---------------------------------------------------------------------------------#


@Advertising.on_message(RJ.prv & RJ.regex('^ثبت اکانت 📥') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Add_Account(bot,message,user):
    global Proxys , Api_Keys , Account_Details , app
    app=bot
    try:
        Proxy=bot.Get_Proxy
    except:Proxy=None
    try:
        Num=str((await bot.Ask(int(user),TEXTS.Add_Account,Msg=message,reply_markup=BUTTONS.Cancel,timeout=60)).text)
        try:
            Num=Number(Num,int(user))
        except :
            await message.reply_text(TEXTS.Number_Is_Regestered,reply_markup=BUTTONS.Accounts)
            return
        if Num.Is_Regestered:
            await message.reply_text(TEXTS.Number_Is_Regestered,reply_markup=BUTTONS.Accounts)
            return
        Random_Api=RJ.Random_API
        D_D=RJ.Get_Device_Detais
        print(D_D)
        Acc=Client(f'{str(Num)}-first',api_id=Random_Api[1],api_hash=Random_Api[0],phone_number=str(Num),workdir=Config.Sessions)#,device_model=D_D[0],system_version=D_D[1],app_version=D_D[2],lang_code='en')
        await Acc.connect()
        Hash=(await Acc.send_code(str(Num))).phone_code_hash 
        Login_Details=(((await bot.Ask(int(user),TEXTS.Send_Code,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
        Login_Details=Login_Details.strip().split(' ')
        if not Login_Details[0].isdigit():
            await message.reply_text(TEXTS.Send_Code_Error(Login_Details[0]),reply_markup=BUTTONS.Cancel)
            Login_Details=((await bot.Ask(int(user),TEXTS.Send_Code_Again,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Force,timeout=100)).text).strip().split(' ')
        if len(Login_Details)==1:PassWord=False
        else:PassWord=str(Login_Details[1])
        try:
            try:
                USR=await Acc.sign_in(str(Num),Hash,str(Login_Details[0]).replace('-',''))
            except errors.PhoneCodeInvalid : 
                Code=int((await bot.Ask(int(user),TEXTS.Send_Code_Again,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120)).text)
                USR=await Acc.sign_in(str(Num),Hash,str(Code).replace('-',''))
        except errors.unauthorized_401.SessionPasswordNeeded:
            try:
                USR=await Acc.check_password(str(PassWord))
            except errors.PasswordHashInvalid:
                PassWord=(await bot.Ask(int(user),TEXTS.Password_Incorect(str(await Acc.get_password_hint())),Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Force,timeout=120)).text
                USR=await Acc.check_password(str(PassWord))
        try:await Acc.accept_terms_of_service(USR.id)
        except:pass
        await message.reply_text(TEXTS.succesfully_loggin,reply_markup=BUTTONS.Accounts)
        Proxys[int(Num)]=Proxy
        Acc.add_handler(MessageHandler(callback=Loggin,filters=RJ.regex('give')))
        await Acc.disconnect()
        await Acc.start()
        New_Hash= step_one.request_tg_code_get_random_hash(str(Num),Proxy)
        Account_Details[int(Num)]={'pass':PassWord,'id':int(user)}
        Api_Keys[int(Num)]={'hash':Random_Api[0],'id':Random_Api[1],'phone_hash':New_Hash}
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Accounts)
        return
    except errors.flood_420.FloodWait as e :
        await message.reply_text(TEXTS.Flood_Wait_Loggin(e.value),reply_markup=BUTTONS.Accounts)
        return
    except errors.PhoneNumberInvalid:
        await message.reply_text(TEXTS.Number_Incorrect,reply_markup=BUTTONS.Accounts)
        return
    except errors.PasswordRequired:
        await message.reply_text(TEXTS.Password_requerd,reply_markup=BUTTONS.Accounts)
        return
    except errors.PasswordHashInvalid:
        await message.reply_text(TEXTS.Password_Is_Incorect,reply_markup=BUTTONS.Accounts)
        return
    except Exception as e:
        await message.reply_text(TEXTS.Problem_Occured,reply_markup=BUTTONS.Accounts)
        RJ.Log(int(user),f'FIRST LOGGIN : {e}')
        return

#---------------------------------------------------------------------------------| ALL ACCOUNT DETAILS |---------------------------------------------------------------------------------#
@Advertising.on_message(RJ.prv & RJ.regex('^وضعیت اکانت ها 🗂️') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Account_Status(bot,message,user:User):
    try:
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
        AI_Activity=str(((await bot.Ask(int(user),TEXTS.Activity_Report_Change,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
        if AI_Activity == TEXTS.yes :AI=True
        else:AI=False
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Accounts)
        return
    except:return
    Numbers=RJ.Account(Nums,user,True)
    TXT=TEXTS.Accounts_Status
    x=1
    for i in Numbers:
        try:
            app = await i.Start()
            limit=await SpamBot(app,(user))
            if limit[0]=='temporary':
                Emoji=f'🟨{limit[1].strip()}'
                i.Change_Activity(False)
            elif limit[0]=='ForEver':
                Emoji='🟥'
            elif limit[0]=='NotFound':
                Emoji='404'
            elif limit[0]=='Free':
                Emoji='🟩'
                i.Change_Activity(True)
            else:Emoji=limit[0]
        except (errors.UserDeactivatedBan , errors.UserDeactivated):
            Emoji='❌'
            i.Delete()
        except (errors.AuthKeyInvalid , errors.AuthKeyUnregistered , errors.SessionRevoked , errors.SessionExpired ):
            Emoji='🚫'
            i.Delete()
        except Exception as e:
            RJ.Log(int(user),f'Account Status: {e}')
            Emoji='404'
        finally:
            try:await app.stop(False)
            except:pass
        TXT+=f'{helper_steps.Font(x)}→{Emoji}→+{i.Number}\n'
        user.Add_Coin(Config.Status)
        x+=1
        if len(TXT.split('\n')) > 50:
            await message.reply_text(TXT)
            TXT=''
    if len(TXT.split('\n')) > 1 :
        await message.reply_text(TXT,reply_markup=BUTTONS.Accounts)

@Advertising.on_message(RJ.prv & RJ.regex('^لیست اکانت ها 📜') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Accounts_Lists(bot,message,user):
    Numbers=user.All_numbers
    TXT=TEXTS.Accounts_list
    x=1
    for i in Numbers:
        TXT+=f'{helper_steps.Font(x)}→{Number(i["num"],int(user)).Activity_Emoji}→`+{i["num"]}`\n'
        x+=1
        if len(TXT.split('\n')) > 50:
            await message.reply_text(TXT)
            TXT=''
    if len(TXT.split('\n')) > 1 :
        await message.reply_text(TXT,reply_markup=BUTTONS.Accounts)

@Advertising.on_message(RJ.prv & RJ.regex('^تغییر فعالیت 🔆') , group=0)
@RJ.User_Details
async def Change_Activities(bot:Advertising,message,user:User):
    Nums=[Number(i['num'],int(user)) for i in user.All_numbers ]
    await message.reply_text(TEXTS.Change_Activity,reply_markup=BUTTONS.Activity(Nums))

@Advertising.on_message(RJ.prv & RJ.regex('^تغییر طبیعت 🧪') , group=0)
@RJ.User_Details
async def Change_Naturality(bot:Advertising,message,user:User):
    Nums=[Number(i['num'],int(user)) for i in user.All_numbers ]
    await message.reply_text(TEXTS.Natural_Acc)
    await message.reply_text(TEXTS.Change_Activity,reply_markup=BUTTONS.Natural(Nums))

@Advertising.on_message(RJ.prv & RJ.regex('^جستوجو 🔍') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Search_Accounts(bot:Advertising,message,user:User):
    try:
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Accounts)
        return
    Numbers=RJ.Account(Nums,user,True)
    if len(Numbers)>10:
        await message.reply_text(TEXTS.Only_Limited_Numbers,reply_markup=BUTTONS.Accounts)
        return
    for i in Numbers:
        try:
            app = await i.Start()
            me_LOL=await app.get_me()
            await message.reply_text(TEXTS.Find_Nums(f'+{int(i)}' , me_LOL.first_name , me_LOL.username , me_LOL.id ),reply_markup=BUTTONS.Accounts)
        except (errors.UserDeactivatedBan , errors.UserDeactivated):
            i.Delete()
            await message.reply_text(TEXTS.Number_Is_Deleted(f'+{int(i)}'))
        except (errors.AuthKeyInvalid , errors.AuthKeyUnregistered , errors.SessionRevoked , errors.SessionExpired ):
            i.Delete()
            await message.reply_text(TEXTS.Number_Is_Terminated(f'+{int(i)}'))
        except Exception as e:
            RJ.Log(int(user),f'Find Number : {e}')
        finally:
            try:await app.stop(False)
            except:pass
            await sleep(1)
            
    await message.reply_text(TEXTS.Procces_Compeleted_WO_NO,reply_markup=BUTTONS.Accounts)
    


#---------------------------------------------------------------------------------| DELETE ACCOUNT  |---------------------------------------------------------------------------------#
@Advertising.on_message(RJ.prv & RJ.regex('^حذف همه اکانت ها 🗑') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Delete_All_Account(bot,message,user:User):
    for i in user.All_numbers:
        try:
            Num=Number(i['num'],int(user))
            app = await Num.Start()
            await app.log_out()
        except Exception as e :RJ.Log(int(user),f'Delete All : {e}')
        user.Add_Coin(Config.Delete_Account)
    user.Delete()
    await message.reply_text(TEXTS.All_Deleted,reply_markup=BUTTONS.Accounts)
    

@Advertising.on_message(RJ.prv & RJ.regex('^حذف چند اکانت ❌') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Delete_Accounts(bot,message,user:User):
    try:Numbers=str(((await bot.Ask(int(user),TEXTS.Account_Deleting,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text)
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Accounts)
        return
    except:return
    for i in Numbers.split('\n'):
        Num=Number(i,int(user))
        if not Num.is_Owner:
            await message.reply_text(TEXTS.Not_Owner,reply_markup=BUTTONS.Accounts)
            return
        try:
            app = await Num.Start()
            await app.log_out()
        except Exception as e :RJ.Log(int(user),f'Delete Some : {e}')
        Num.Delete()
        user.Add_Coin(Config.Delete_Account)
    await message.reply_text(TEXTS.Selected_Numbers_Deleted,reply_markup=BUTTONS.Accounts)
    

@Advertising.on_message(RJ.prv & RJ.regex('^حذف ریپورت شده ها 🔇') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Delete_Limited_Accounts(bot,message,user:User):
    for i in user.All_numbers:
        try:
            Num=Number(i['num'],int(user))
            app = await Num.Start()
            Limit=await SpamBot(app,user)
            if Limit[0]=='ForEver' or Limit[0]=='temporary':
                try:
                    app = await Num.Start(i)
                    await app.log_out()
                except:pass
                Num.Delete()
                user.Add_Coin(Config.Delete_Account)
        except Exception as e :RJ.Log(int(user),f'Delete Reported : {e}')
    await message.reply_text(TEXTS.Limited_Numbers_Deleted,reply_markup=BUTTONS.Accounts)
    
#---------------------------------------------------------------------------------| START BOTS |---------------------------------------------------------------------------------#
@Advertising.on_message(RJ.prv & RJ.regex('^🤖 استارت ربات') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Start_Robots(bot,message,user:User):
    try:
        Robot=str(((await bot.Ask(int(user),TEXTS.StartBot_User,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text)
        id=str(((await bot.Ask(int(user),TEXTS.Refferal,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text)
        Times=str(((await bot.Ask(int(user),TEXTS.StartBot_Times,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=30))).text)
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Accounts)
        return
    except:return
    if id.lower()=='none':Refferal=''
    else:Refferal=id.split('=')[-1]
    

    if int(Times) <= 0:return
    else:Times=int(Times)
    x=0
    Nums=RJ.Account(Nums,user)
    for Num in Nums:
        try:
            app = await Num.Start()
            await app.send_message(Robot,f'/start {Refferal}')
            x+=1
            if x >= Times:
                break
        except Exception as e:RJ.Log(int(user),f'FIRST LOGGIN : {e}')
        finally:
            try:await app.stop(False)
            except:pass
    await message.reply_text(TEXTS.StartBot_Completed(Times),reply_markup=BUTTONS.Accounts)

#---------------------------------------------------------------------------------| LEAVE & JOIN |---------------------------------------------------------------------------------#
@Advertising.on_message(RJ.prv & RJ.regex('^leave 🚨') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Leave(bot:Advertising,message,user:User):
    failed=0
    comp=0
    try:
        Chat=str(((await bot.Ask(int(user),TEXTS.Leave_Chat_Ask,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text).replace('https://','')
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Accounts)
        return
    except:return
    if Chat.isdigit():Chat=int(Chat)
    elif not '/joinchat/' in Chat and not '+' in Chat :Chat=f'@{Chat.split("/")[-1]}'
    Nums=RJ.Account(Nums,user)
    for Num in Nums:
        try:
            app = await Num.Start()
            if 't.me' in Chat:
                CHT=(await app.get_chat(Chat))
                await CHT.leave()
            else:
                await app.leave_chat(Chat,True)
            comp+=1
            user.Add_Coin(Config.J_L)
        except:failed+=1
        finally:
            try:await app.stop(False)
            except:pass
    await message.reply_text(TEXTS.Leave(comp,failed))
    

@Advertising.on_message(RJ.prv & RJ.regex('^join 🚨') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Join(bot:Advertising,message,user:User):
    failed=0
    comp=0
    try:
        Chat=str(((await bot.Ask(int(user),TEXTS.JoinChat_Ask,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text).replace('https://','')
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Accounts)
        return
    except:return
    if Chat.isdigit():Chat=int(Chat)
    elif not '/joinchat/' in Chat and not '+' in Chat :Chat=f'@{Chat.split("/")[-1]}'
    Nums=RJ.Account(Nums,user)
    for Num in Nums:
        try:
            app = await Num.Start()
            try:
                await app.join_chat(Chat)
            except errors.UserAlreadyParticipant : pass
            await sleep(user.R_Speed)
            comp+=1
            user.Add_Coin(Config.J_L)
        except Exception as e:
            RJ.Log(int(user),f'Join : {e}')
            failed+=1
        finally:
            try:await app.stop(False)
            except:pass
    await message.reply_text(TEXTS.Join(comp,failed),reply_markup=BUTTONS.Accounts)

#---------------------------------------------------------------------------------| CODE RECIVER & ACC CLEARING |---------------------------------------------------------------------------------#
@Advertising.on_message(RJ.prv & RJ.regex('^گرفتن کد 🗳') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Code(bot:Advertising,message,user:User):
    try:
        Num=str(((await bot.Ask(int(user),TEXTS.Number_Ask,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text)
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Accounts)
        return
    except:return
    Num=Number(Num,int(user))
    if not Num.is_Owner:
        await message.reply_text(TEXTS.Not_Owner,reply_markup=BUTTONS.Accounts)
        return
    try : 
        Codes=''
        app = await Num.Start()
        async for i in app.get_chat_history(777000,limit=4):
            try:
                Codes += str((re.search("\d{5}",str(i.text)).group(0)))
                Codes+='\n'
            except:pass
        await message.reply_text(TEXTS.Recived_Code(Codes),reply_markup=BUTTONS.Accounts)
    except:await message.reply_text(TEXTS.Problem_Occured,reply_markup=BUTTONS.Accounts)
    
@Advertising.on_message(RJ.prv & RJ.regex('^پاکسازی ♻️') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Clearing(bot:Advertising,message,user:User):
    try:
        Nums=str(((await bot.Ask(int(user),TEXTS.Clearing,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
        Kind=str(((await bot.Ask(int(user),TEXTS.Clearing_Kind,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text)
        Should_Block=str(((await bot.Ask(int(user),TEXTS.AskBlocks,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))).text)
        if TEXTS.yes in Should_Block :Should_Block=True
        else:Should_Block=False
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Accounts)
        return
    except:return
    Nums=RJ.Account(Nums,user)
    if TEXTS.PV_KIND in Kind:Pv=True
    else:Pv=False
    if TEXTS.CHNL_KIND in Kind:Channel=True
    else:Channel=False
    if TEXTS.GROUP_KIND in Kind:Group=True
    else:Group=False
    if TEXTS.BOT_KIND in Kind:Bot=True
    else:Bot=False
    if Pv==False and Channel==False and  Group==False and Bot==False : 
        await message.reply_text(TEXTS.Wrong,reply_markup=BUTTONS.Accounts)
        return
    await message.reply_text(TEXTS.Clearing_Details(Pv,Channel,Group,Bot),reply_markup=BUTTONS.Accounts)
    X=1
    for i in Nums:
        try:
            app = await i.Start()
            app_id=int((await app.get_me()).id)
            async for dialog in app.get_dialogs():
                type=dialog.chat.type
                if dialog.is_pinned  : continue
                if (type==ChatType.SUPERGROUP or type == ChatType.GROUP) and Group==True:
                    try:
                        await dialog.chat.leave()
                        user.Add_Coin(Config.Clean)
                        X+=1
                    except Exception as e :RJ.Log(int(user),f'Clearing Part GROUP : {e}')
                if type==ChatType.PRIVATE and Pv==True:
                    try:
                        if int(dialog.chat.id) == app_id : continue
                        Pear= await app.resolve_peer(dialog.chat.id)
                        await app.invoke(DeleteHistory(peer=Pear,revoke=True,max_id=0))
                        user.Add_Coin(Config.Clean)
                        X+=1
                    except Exception as e :RJ.Log(int(user),f'Clearing Part PV : {e}')
                if type==ChatType.CHANNEL and Channel==True:
                    try:
                        #----------------------------------------------------------------|
                        try:                                                           #-|
                            if str(dialog.chat.username)==Config.Dark_Channel:continue #-|
                        except:pass                                                    #-|
                        #----------------------------------------------------------------|
                        await dialog.chat.leave()
                        user.Add_Coin(Config.Clean)
                        X+=1
                    except Exception as e :RJ.Log(int(user),f'Clearing Part CHANNEL : {e}')
                if type==ChatType.BOT and Bot==True:
                    try:
                        if Should_Block:
                            try :await app.block_user(dialog.chat.username)
                            except (errors.flood_420.FloodWait , errors.flood_420.Flood ) as e :
                                await sleep(e.value)
                                try :await app.block_user(dialog.chat.username)
                                except:pass
                            except Exception as e :RJ.Log(int(user),f'Clearing Part Block BOT : {e}')
                        Pear= await app.resolve_peer(dialog.chat.username )
                        await app.invoke(DeleteHistory(peer=Pear,max_id=0))
                        user.Add_Coin(Config.Clean)
                        X+=1
                    except Exception as e :RJ.Log(int(user),f'Clearing Part BOT : {e}')
        except Exception as e :RJ.Log(int(user),f'Clearing : {e}')
        finally:
            try:await app.stop(False)
            except:pass
    await message.reply_text(TEXTS.Clearing_Finished(X),reply_markup=BUTTONS.Accounts)
    
#--------------------------------------------------------------------------------| SET PROFILE DETAILS |-------------------------------------------------------------------------------#
@Advertising.on_message(RJ.prv & RJ.regex('^🔱 هویت سازی 🔱') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Fake_Personality(bot:Advertising,message,user:User):
    try:
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Account_Setting)
        return
    except:return
    Nums=RJ.Account(Nums,user)
    X=0
    Y=0
    Z=0
    Accs=0
    for i in Nums:
        try:
            app = await i.Start()
            Accs+=1
            try:
                await app.set_profile_photo(photo=RJ.Random_Photo)
                user.Add_Coin(Config.Photo)
                X+=1
            except Exception as e :RJ.Log(int(user),f'Fake Photo : {e}')
            try:
                await app.update_profile(first_name=RJ.Random_Name  , bio=RJ.Random_Bio)
                user.Add_Coin(Config.Bio_Name)
                Y+=1
            except:pass
            try:
                try:
                    if await app.set_username(RJ.Random_Username) : 
                        Z+=1
                except:
                    if await app.set_username(RJ.Random_Username) : 
                        Z+=1
            except Exception as e :RJ.Log(int(user),f'Fake Username : {e}')
        except Exception as e :RJ.Log(int(user),f'Fake : {e}')
        finally:
            try:await app.stop(False)
            except:pass
        
    await message.reply_text(TEXTS.Fake_Detailes_Setted(Accs,X,Y,Z),reply_markup=BUTTONS.Account_Setting)

@Advertising.on_message(RJ.prv & RJ.regex('^♻️ تنظیم خودکار مشخصات ♻️') , group=0)
@RJ.User_Details
async def Auto_Details(bot:Advertising,message,user:User):
    await message.reply_text(TEXTS.Auto_Acc_Details,reply_markup=BUTTONS.Choosing_Auto_Details)

@Advertising.on_message(RJ.prv & RJ.regex('^🧱 تنظیم رمز ابری 🧱') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Set_Password(bot:Advertising,message,user:User):
    try:
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
        Npassword =str(((await bot.Ask(int(user),TEXTS.Ask_NewPass,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
        Opassword =str(((await bot.Ask(int(user),TEXTS.Ask_Common_Pass,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Account_Setting)
        return
    except:return
    Nums=RJ.Account(Nums,user)
    X=0
    for i in Nums:
        try:
            app = await i.Start()
            try:
                await app.enable_cloud_password(Npassword , f'@{Config.Dark_Channel}')
                X+=1
            except ValueError : 
                try:
                    await app.change_cloud_password(Opassword, Npassword , f'@{Config.Dark_Channel}')
                    X+=1
                except errors.PasswordHashInvalid:
                    Temppassword =str(((await bot.Ask(int(user),TEXTS.AskPass_Invalied(i),Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
                    if Temppassword.strip() == TEXTS.Cancel_Proccess : break
                    try:
                        await app.change_cloud_password(Temppassword, Npassword , f'@{Config.Dark_Channel}')
                        X+=1
                    except errors.PasswordHashInvalid:await message.reply_text(TEXTS.PassWord_Invalied_Skiped)
        except Exception as e :RJ.Log(int(user),f'Set_Password : {e}')
        finally:
            try:await app.stop(False)
            except:pass
    
    await message.reply_text(TEXTS.Password_Adding_Finished(X,Npassword),reply_markup=BUTTONS.Account_Setting)
    
@Advertising.on_message(RJ.prv & RJ.regex('^🛑 پاک کردن پروفایل 🛑') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Delete_Profile(bot:Advertising,message,user:User):
    try:
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Account_Setting)
        return
    except:return
    Nums=RJ.Account(Nums,user)
    X=0
    for i in Nums:
        try:
            app = await i.Start()
            photos=[i async for i in  app.get_chat_photos('me')]
            await app.delete_profile_photos([p.file_id for p in photos])
            X+=1
        except Exception as e:RJ.Log(int(user),f'Delete Profile : {e}')
        finally:
            try:await app.stop(False)
            except:pass
            
    user.Add_Coin(Config.update_profile * X)
    await message.reply_text(TEXTS.Procces_Compeleted(X),reply_markup=BUTTONS.Account_Setting)
    
        
@Advertising.on_message(RJ.prv & RJ.regex('^📝 نتظیم مشخصات 📝') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Set_Details(bot:Advertising,message,user:User):
    try:
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
        Kind=str(((await bot.Ask(int(user),TEXTS.Ask_Details_kind,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
        Detail=(((await bot.Ask(int(user),TEXTS.Get_Details(Kind),Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))))
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Account_Setting)
        return
    except:return
    Nums=RJ.Account(Nums,user)
    Name,Bio,Pro=[False,False,False]
    if Kind==TEXTS.Pro_Text:
        Pro=True
    elif Kind==TEXTS.Name_Text:
        Name=True
    elif Kind==TEXTS.Bio_Text:
        Bio=True
    else:
        await message.reply_text(TEXTS.Wrong,reply_markup=BUTTONS.Account_Setting)
        return
    x=0
    f=0
    for i in Nums:
        try:
            app = await i.Start()
            if Bio:
                Text=str(Detail.text)
                await app.update_profile(bio=Text)
            elif Pro:
                Photo=str(await Detail.download(f'{randint(1,10**10)}.jpg'))
                await app.set_profile_photo(photo=Photo)
            elif Name:
                Text=str(Detail.text)
                if TEXTS.Replaced_abbr in Text:
                    Text=Text.replace(TEXTS.Replaced_abbr,helper_steps.Font(str([int(i['num']) for i in user.All_Active_Numbers].index(int(i)))))
                await app.update_profile(first_name=Text)
            x+=1
            user.Add_Coin(Config.update_profile)
        except Exception as e:
            RJ.Log(int(user),f'ُSet Details  : {e}')
            f+=1
        finally:
            try:await app.stop(False)
            except:pass
    await message.reply_text(TEXTS.Detailes_Finished(x,f),reply_markup=BUTTONS.Account_Setting)
            
@Advertising.on_message(RJ.prv & RJ.regex('^🚷 پاکسازی نشست ها 🚷') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Reset_Sessions(bot:Advertising,message,user:User):
    try:
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Account_Setting)
        return
    except:return
    Nums=RJ.Account(Nums,user)
    sccss=''
    for i in Nums:
        try:
            app = await i.Start()
            x=await app.invoke(ResetAuthorizations())
            if x:sccss+=f'` +{int(i)} ` \n '
        except Exception as e:RJ.Log(int(user),f'Terminate : {e}')
        finally:
            try:await app.stop(False)
            except:pass
            
    await message.reply_text(TEXTS.Terminated(sccss, len(sccss.split('\n'))) ,reply_markup=BUTTONS.Account_Setting)
            
    
    
@Advertising.on_message(RJ.prv & RJ.regex('^📨 انتقال اکانت 📨') , group=0)
@RJ.User_Details
async def Transfer(bot:Advertising,message,user:User):
    try:
        Reciver=str(((await bot.Ask(int(user),TEXTS.Ask_Reciver,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Account_Setting)
        return
    except:return
    try:
        if Reciver.isdigit():Reciver=int(Reciver)
        Rec_Acc=(await bot.get_users(Reciver))
        Reciver_name = Rec_Acc.mention
        Reciver=Rec_Acc.id
    except Exception as e:
        RJ.Log(int(user),f'Sending Account : {e}')
        await message.reply_text(TEXTS.Not_Regestered,reply_markup=BUTTONS.Account_Setting)
        return
    Nums=RJ.Account(Nums,user)
    Num_Texts=''
    for i in Nums:
        i.Transfer(int(Reciver))
        Num_Texts+=f'{i}\n'
        if len(Num_Texts.split('\n')) > 50 :
            await message.reply_text(TEXTS.Transfered(Num_Texts,str(message.from_user.first_name),Reciver_name),reply_markup=BUTTONS.Account_Setting)
            await bot.send_message(int(Reciver),text=TEXTS.Transfered(Num_Texts,message.from_user.mention,Reciver_name),reply_markup=BUTTONS.Account_Setting)
            Num_Texts='' 
    if len(Num_Texts.split('\n')) > 0 :
        await message.reply_text(TEXTS.Transfered(Num_Texts,str(message.from_user.first_name),Reciver_name),reply_markup=BUTTONS.Account_Setting)
        await bot.send_message(int(Reciver),text=TEXTS.Transfered(Num_Texts,message.from_user.mention,Reciver_name),reply_markup=BUTTONS.Account_Setting)
    

# @Advertising.on_message(RJ.prv & RJ.regex('^\+\d') , group=0)
# @RJ.User_Details
# async def Number_Quick_Accsess(bot:Advertising,message,user:User):
    
#---------------------------------------------------------------------------------| HELP |---------------------------------------------------------------------------------#
def Len(l):
    try:return len(l)
    except:return 0
    
@Advertising.on_message(RJ.prv & RJ.regex('^راهنما ❓') , group=0)
@RJ.User_Details
async def HELP(bot:Advertising,message,user:User):
    await message.reply_text(TEXTS.HELP(bool(user.Auto_pic),user.Auto_bio,user.AutoName,Len(user.All_numbers),user.R_Speed,user.A_Speed,Len(user.Banners),RJ.Owner_Username),reply_markup=BUTTONS.Accounts)
    