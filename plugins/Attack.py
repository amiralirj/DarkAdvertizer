from .BOT import TEXTS , BUTTONS , Config , Number , Advertising , RJ  , User
from asyncio.exceptions  import  TimeoutError
from pyrogram.enums import ChatMemberStatus , ChatMembersFilter , UserStatus
from pyrogram import errors
from asyncio import sleep 
from time import time
from os import remove
import datetime
import sys , re


User_Links={}
User_Attacking={}
User_Spamming={}

    
#---------------------------------------------------------------------------------| BANNER |---------------------------------------------------------------------------------#
@Advertising.on_message(RJ.prv & RJ.regex('^ثبت بنر📝') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Add_Benner(bot,message,user:User):
    try:
        Banner=await bot.Ask(int(user),TEXTS.Add_Benner,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120)
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Attack)
        return
    Banner_Message=await Banner.copy(Config.Banners_Channel)
    user.Add_Banner(int(Banner_Message.id))
    await message.reply_text(TEXTS.Banner_Added, reply_markup=BUTTONS.Attack)
    
@Advertising.on_message(RJ.prv & RJ.regex('^بنر های فعلی 📧') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def watch_Banners(bot,message,user:User):
    try:
        if User.Banners:
            for i in user.Banners:
                await bot.copy_message(int(user),Config.Banners_Channel,int(i),reply_markup=BUTTONS.Delete_Banner(i))
    except:await message.reply_text(TEXTS.No_Banner_Setted,reply_markup=BUTTONS.Attack)

@Advertising.on_message(RJ.prv & RJ.regex('^قوی ترین اتکر ⚔️🔥') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Best_Attackers(bot,message,user:User):
    Users=[[len(User(int(i)).All_numbers),int(i)] for i in RJ.All_Users]
    Text=''
    Emojies={0:'⭐🔥⚡',1:'🔥⚡',2:'🔥'}
    for j , i in enumerate(['WWW.GITHUB.COM','/','AMIRALIRJ']):
        try:
            X=max(Users)
            if X[1] in [71068207,5070374948]:continue
            Mention=(await bot.get_users(X[1])).mention
            Text+=f'{Emojies[j]} {Mention} → {X[0]} \n'
            Users.remove(X)
        except Exception as e:RJ.Log(int(user),f'Best Attackers : {e}')
        
    await message.reply_text(TEXTS.Bests(Text),reply_markup=BUTTONS.Attack)

@Advertising.on_message(RJ.prv & RJ.regex('^⭐ رتبه من ⭐') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Attacker_Rank(bot,message,user:User):
    Users=sorted([len(User(int(i)).All_numbers) for i in RJ.All_Users])
    Users.reverse()
    rank=Users.index(len(user.All_numbers))+1
    await message.reply_text(TEXTS.My_Rank(rank),reply_markup=BUTTONS.Attack)
    
#---------------------------------------------------------------------------------| Attack |---------------------------------------------------------------------------------# 
#---------------------------------------------------------------------------------| Attack |---------------------------------------------------------------------------------# 
#---------------------------------------------------------------------------------| Attack |---------------------------------------------------------------------------------# 
def Link(link:str):
    if not '/joinchat/' in link and '+' not in link :
        return (link.split("/")[-1]).split('@')[-1]
    else:
        return link.replace('https://','').replace('t.me/','')

async def Attack(app,i,link,user,msg,message):
    if not User_Attacking[int(user)] :raise UnicodeError
    try:
        if link:
            try:
                bot_results = await app.get_inline_bot_results(Config.BOT_USERNAME, f"{int(user)}")
                await app.send_inline_bot_result(i, bot_results.query_id, bot_results.results[0].id)
            except:
                try:await msg.forward(i)
                except:await app.copy_message(i,Config.Banners_Channel,user.Rand_Banner)
        else:
            await app.copy_message(i,Config.Banners_Channel,user.Rand_Banner)
        user.Add_Coin(Config.Attack)
        await sleep(user.A_Speed)
    except (errors.bad_request_400.UsernameInvalid,errors.bad_request_400.UsernameNotOccupied , errors.bad_request_400.UsernameNotModified)  :
        await message.reply_text(TEXTS.Username_NV(i))
    except errors.ChatWriteForbidden :
        await message.reply_text(TEXTS.Username_Ch(i))
    except errors.YouBlockedUser:
        try:
            await app.unblock_user(user)
            if link:
                try:
                    bot_results = await app.get_inline_bot_results(Config.BOT_USERNAME, f"{int(user)}")
                    await app.send_inline_bot_result(i, bot_results.query_id, bot_results.results[0].id)
                except:
                    try:await msg.forward(i)
                    except:await app.copy_message(i,Config.Banners_Channel,user.Rand_Banner)
            else:
                await app.copy_message(i,Config.Banners_Channel,user.Rand_Banner)
            user.Add_Coin(Config.Attack)
            await sleep(user.A_Speed)
        except:pass

#---------------------------------------------------------------------------------| Attack HANDLERS |---------------------------------------------------------------------------------# 
#---------------------------------------------------------------------------------| Attack HANDLERS |---------------------------------------------------------------------------------#
@Advertising.on_message(RJ.prv & RJ.regex('^بدون فلاد 💥') , group=-1)
@RJ.User_Details
@RJ.Coin_Limit
async def None_Flood_Attack(bot,message,user:User):
    global User_Attacking , User_Links
    if not user.Banners:
        await message.reply_text(TEXTS.No_Banner_Setted,reply_markup=BUTTONS.Attack)
        return
    try:
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120,Msg=message))).text)
        Usernames=str(((await bot.Ask(int(user),TEXTS.Ask_Usernames,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120,Msg=message))).text)
        Links=str(((await bot.Ask(int(user),TEXTS.Link_Attack,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120,Msg=message))).text)
        try:User_Round=int(((await bot.Ask(int(user),TEXTS.Ask_Round,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120,Msg=message))).text)
        except:User_Round=10**10
        if Links!=TEXTS.No:
            link=Link(Links)
            btn=str(((await bot.ask(int(user),TEXTS.Link_btn_Attack,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
            if len(btn)> 15 :
                btn=TEXTS.Join_Btn
            User_Links[int(user)]=[link,btn]
            
        else :
            link=False
        if TEXTS.Cancel_btn in [Nums,Usernames] :
            await message.reply_text(TEXTS.Cancel,reply_markup=BUTTONS.Attack)
            return
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Attack)
        return
    except:return
    #-----------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------
    Nums=RJ.Account(Nums,user)
    #-----------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------
    msg=None
    Flooded={}
    Det={}
    Text=''
    X=0
    User_List=Usernames.split('\n')
    User_Dict={i:0 for i in User_List}
    User_Attacking[int(user)]=True
    for num in Nums:
        if not User_Attacking[int(user)] :return
        try:
            #-----------------------------------------------------------------------------------------------------------
            app = await num.Start()
            try:
                bot_results = await app.get_inline_bot_results(Config.BOT_USERNAME, f"{int(user)}")
                msg=await app.send_inline_bot_result(f'@{Config.BOT_USERNAME}', bot_results.query_id, bot_results.results[0].id)
            except:pass
            for j,i in enumerate(User_List):
                if User_Dict[i] > User_Round:continue
                if not User_Attacking[int(user)] :return
                try:
                    if link:
                        try:
                            bot_results = await app.get_inline_bot_results(Config.BOT_USERNAME, f"{int(user)}")
                            await app.send_inline_bot_result(i, bot_results.query_id, bot_results.results[0].id)
                        except:
                            try:await msg.forward(i)
                            except:await app.copy_message(i,Config.Banners_Channel,user.Rand_Banner)
                    else:
                        await app.copy_message(i,Config.Banners_Channel,user.Rand_Banner)
                    X+=1
                    User_Dict[i]+=1
                    user.Add_Coin(Config.Attack)
                    await sleep(user.A_Speed)
                    Det[str(num)]=j
                except ConnectionError : pass
                except (errors.UsernameInvalid,errors.UsernameNotOccupied)  :
                    await message.reply_text(TEXTS.Username_NV(i))
                except errors.ChatWriteForbidden :
                    await message.reply_text(TEXTS.Username_Ch(i))
                except errors.YouBlockedUser:
                    try:
                        await app.unblock_user(user)
                        if link:
                            try:
                                bot_results = await app.get_inline_bot_results(Config.BOT_USERNAME, f"{int(user)}")
                                await app.send_inline_bot_result(i, bot_results.query_id, bot_results.results[0].id)
                            except:
                                try:await msg.forward(i)
                                except:await app.copy_message(i,Config.Banners_Channel,user.Rand_Banner)
                        else:
                            await app.copy_message(i,Config.Banners_Channel,user.Rand_Banner)
                        X+=1
                        User_Dict[i]+=1
                        user.Add_Coin(Config.Attack)
                        await sleep(user.A_Speed)
                        Det[str(num)]=j
                    except:pass
                except errors.FloodWait as e:
                    try:
                        await app.stop(False)
                        Flooded[str(num)]=[time(),e.x,j]
                    except:pass
                except Exception as e:RJ.Log(int(user),f'Flooded Attack 1 : {e}')
            #-----------------------------------------------------------------------------------------------------------
            for i in Flooded:
                try:
                    if time()-Flooded[i][0] < e.x:
                        Flooded.pop(i)
                        for i in User_List[Flooded[i][2]:]:
                            if User_Dict[i] > User_Round:continue
                            app=await Number(i,int(user)).Start()
                            try:
                                if link:
                                    try:
                                        bot_results = await app.get_inline_bot_results(Config.BOT_USERNAME, f"{int(user)}")
                                        await app.send_inline_bot_result(i, bot_results.query_id, bot_results.results[0].id)
                                    except:
                                        try:await msg.forward(i)
                                        except:await app.copy_message(i,Config.Banners_Channel,user.Rand_Banner)
                                else:
                                    await app.copy_message(i,Config.Banners_Channel,user.Rand_Banner)
                                X+=1
                                User_Dict[i]+=1
                                await sleep(user.A_Speed)
                                user.Add_Coin(Config.Attack)
                            except (errors.UsernameInvalid,errors.UsernameNotOccupied,errors.ChatWriteForbidde,errors.YouBlockedUser):pass
                            except:break
                except Exception as e:RJ.Log(int(user),f'Flooded Attack 2 : {e}')
                        
            #-----------------------------------------------------------------------------------------------------------
            try:await app.stop(False)
            except:pass
            await sleep(user.R_Speed)
        except (errors.UserDeactivatedBan , errors.UserDeactivated):
            num.Delete()
            await message.reply_text(TEXTS.Number_Is_Deleted(num) , reply_markup=BUTTONS.Cancel_Attack)
        except (errors.AuthKeyInvalid , errors.AuthKeyUnregistered) as e:
            num.Delete()
            await message.reply_text(TEXTS.Number_Is_Terminated(num) , reply_markup=BUTTONS.Cancel_Attack)
            RJ.Log(int(user),f'AuthKeyUnregistered : {e}')
        except errors.PeerFlood:
            await message.reply_text(TEXTS.Reported(num) , reply_markup=BUTTONS.Cancel_Attack)
            try:Nums.remove(num)
            except:pass
        except Exception as e:RJ.Log(int(user),f'Flooded Attack 3 : {e}')
        
    for i in User_Dict:
        Attack_Text+=f'⚜️{i} → {User_Dict[i]} \n'
        if len(Attack_Text.split('\n')) > 40 :
            await message.reply_text(TEXTS.Username_Details(Attack_Text),reply_markup=BUTTONS.Attack)
            Attack_Text=''
    if len(Attack_Text.split('\n')) > 0 :
        await message.reply_text(TEXTS.Username_Details(Attack_Text),reply_markup=BUTTONS.Attack)
    
    for i in Det:
        Text+=f'🔰{i} → {Det[i]} \n '
        if len(Text.split('\n')) > 40 :
            await message.reply_text(TEXTS.Attack_Details(Text,X),reply_markup=BUTTONS.Attack)
            Text=''
            
    if len(Text.split('\n')) > 0 :
        await message.reply_text(TEXTS.Attack_Details(Text,X),reply_markup=BUTTONS.Attack)





def chunks(L, n):
    """ Yield successive n-sized chunks from L.
    """
    for i in range(0, len(L), n):
        yield L[i:i+n]
        
@Advertising.on_message(RJ.prv & RJ.filters.command('devattack') , group=-1)
@RJ.User_Details
@RJ.Coin_Limit
async def dev_attack(bot,message,user:User):
    try:
        sys.setrecursionlimit(7000)
        global User_Attacking , User_Links
        if not user.Banners:
            await message.reply_text(TEXTS.No_Banner_Setted,reply_markup=BUTTONS.Attack)
            return
        Nums=str(message.command[2])
        Usernames=str(message.reply_to_message.text)
        User_Round=int(message.command[1])
        link=False
        
        #-----------------------------------------------------------------------------------------------------------
        Nums=RJ.Account(Nums,user)
        #-----------------------------------------------------------------------------------------------------------
        msg=None
        Det={}
        username_text=''
        username_failed_text=''
        X=0
        Round=0
        User_List=[x for x in re.findall(r'\B@(?=\w{5,32}\b)[a-zA-Z0-9]+(?:_[a-zA-Z0-9]+)*', Usernames)]
        User_Attacking[int(user)]=True
        await message.reply_text(TEXTS.Proccess_Started,reply_markup=BUTTONS.Cancel_Attack)
        Started_Attack_Time=time()
        #-----------------------------------------------------------------------------------------------------------
        number_dev = round(len(User_List) / len(Nums) )
        print(number_dev)
        uli=[i for i in chunks(User_List,number_dev) ]
        print(uli)
        attack_li = list(zip(uli, Nums))
        print(attack_li)
        for user_ultimate_list , num in attack_li:
            if not User_Attacking[int(user)] :break
            try:
                #-----------------------------------------------------------------------------------------------------------
                app = await num.Start()
                try:
                    if link:
                        bot_results = await app.get_inline_bot_results(Config.BOT_USERNAME, f"{int(user)}")
                        msg=await app.send_inline_bot_result(f'@{Config.BOT_USERNAME}', bot_results.query_id, bot_results.results[0].id)
                except:pass
                User_Dict={ii:0 for ii in user_ultimate_list}
                for j,i in enumerate(user_ultimate_list):
                    if i=='' : continue
                    if not User_Attacking[int(user)] :break
                    if User_Dict[i] >= User_Round:continue
                    try:
                        await Attack(app,i,link,user,msg,message)
                        User_Dict[i]+=1
                        Det[str(num)]=j
                        X+=1
                    except ConnectionError :
                        await message.reply_text(TEXTS.Connecting_e(num))
                        break
                    except UnicodeError : 
                        return
                    except errors.FloodWait as e:
                        if e.value < 200 :
                            await message.reply_text(TEXTS.Flood_Attack(num,e.value))
                            await sleep(e.value)
                        else:
                            await message.reply_text(TEXTS.High_Flood_Attack(num))
                            break
                    
                await sleep(user.R_Speed)
                Round+=1
            except (errors.UserDeactivatedBan , errors.UserDeactivated):
                num.Delete()
                await message.reply_text(TEXTS.Number_Is_Deleted(num) , reply_markup=BUTTONS.Cancel_Attack)
            except (errors.AuthKeyInvalid , errors.AuthKeyUnregistered) as e:
                num.Delete()
                await message.reply_text(TEXTS.Number_Is_Terminated(num) , reply_markup=BUTTONS.Cancel_Attack)
                RJ.Log(int(user),f'AuthKeyUnregistered : {e}')
            except errors.PeerFlood:
                await message.reply_text(TEXTS.Reported(num) , reply_markup=BUTTONS.Cancel_Attack)
                try:Nums.remove(num)
                except:pass
            except Exception as e:RJ.Log(int(user),f'dev Attack  : {e}')
            finally:
                for target  in User_Dict:
                    if User_Dict[target] == 0 :
                        username_failed_text += f'{target}  \n'
                    else:username_text+=f'{target} - {User_Dict[target]}  \n'
                
                if username_failed_text !='':
                    await message.reply_text(TEXTS.Failed_attack(username_failed_text,num) , reply_markup=BUTTONS.Cancel_Attack)
                
                await message.reply_text(TEXTS.dev_attack_fin(username_text,num,X), reply_markup=BUTTONS.Cancel_Attack)
                        
                X=0
                username_failed_text=''
                username_text=''
                        
                try:await app.stop(False)
                except:pass
        await message.reply_text('finished',reply_markup=BUTTONS.Attack)
    except Exception as e:RJ.Log(int(user),f'dev Attack 2 : {e}')
    
@Advertising.on_message(RJ.prv & RJ.filters.command('attack') , group=-1)
@RJ.User_Details
@RJ.Coin_Limit
async def Fast_Attack(bot,message,user:User):
    global User_Attacking , User_Links
    sys.setrecursionlimit(7000)
    global User_Attacking
    if not user.Banners:
        await message.reply_text(TEXTS.No_Banner_Setted,reply_markup=BUTTONS.Attack)
        return
    try:
        Nums=str(message.command[2])
        Usernames=str(message.reply_to_message.text)
        User_Round=int(message.command[1])
        link=False
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Attack)
        return
    except:return
    #-----------------------------------------------------------------------------------------------------------
    Nums=RJ.Account(Nums,user)
    #-----------------------------------------------------------------------------------------------------------
    msg=None
    Det={}
    Text=''
    Attack_Text=''
    X=0
    Round=0
    User_List=[x for x in re.findall(r'\B@(?=\w{5,32}\b)[a-zA-Z0-9]+(?:_[a-zA-Z0-9]+)*', Usernames)]
    User_Dict={i:0 for i in User_List}
    User_Attacking[int(user)]=True
    await message.reply_text(TEXTS.Proccess_Started,reply_markup=BUTTONS.Cancel_Attack)
    Started_Attack_Time=time()
    for num in Nums:
        if not User_Attacking[int(user)] :break
        try:
            #-----------------------------------------------------------------------------------------------------------
            app = await num.Start()
            try:
                if link:
                    bot_results = await app.get_inline_bot_results(Config.BOT_USERNAME, f"{int(user)}")
                    msg=await app.send_inline_bot_result(f'@{Config.BOT_USERNAME}', bot_results.query_id, bot_results.results[0].id)
            except:pass
            for j,i in enumerate(User_List):
                if i=='' : continue
                if not User_Attacking[int(user)] :break
                if User_Dict[i] >= User_Round:continue
                try:
                    await Attack(app,i,link,user,msg,message)
                    User_Dict[i]+=1
                    Det[str(num)]=j
                    X+=1
                except ConnectionError :
                    await message.reply_text(TEXTS.Connecting_e(num))
                    break
                except UnicodeError : 
                    return
                except errors.FloodWait as e:
                    if e.value < 200 :
                        await message.reply_text(TEXTS.Flood_Attack(num,e.value))
                        await sleep(e.value)
                    else:
                        await message.reply_text(TEXTS.High_Flood_Attack(num))
                        break
            await sleep(user.R_Speed)
            Round+=1
        except (errors.UserDeactivatedBan , errors.UserDeactivated):
            num.Delete()
            await message.reply_text(TEXTS.Number_Is_Deleted(num) , reply_markup=BUTTONS.Cancel_Attack)
        except (errors.AuthKeyInvalid , errors.AuthKeyUnregistered) as e:
            num.Delete()
            await message.reply_text(TEXTS.Number_Is_Terminated(num) , reply_markup=BUTTONS.Cancel_Attack)
            RJ.Log(int(user),f'AuthKeyUnregistered : {e}')
        except errors.PeerFlood:
            await message.reply_text(TEXTS.Reported(num) , reply_markup=BUTTONS.Cancel_Attack)
            try:Nums.remove(num)
            except:pass
        except Exception as e:
            RJ.Log(int(user),f'Fast Attack 3 : {e}')
        finally:
            try:await app.stop(False)
            except:pass
            
    for i in User_Dict:
        Attack_Text+=f'⚜️{i} → {User_Dict[i]} \n'
        if len(Attack_Text.split('\n')) > 40 :
            await message.reply_text(TEXTS.Username_Details(Attack_Text),reply_markup=BUTTONS.Attack)
            Attack_Text=''
    if len(Attack_Text.split('\n')) > 0 :
        await message.reply_text(TEXTS.Username_Details(Attack_Text),reply_markup=BUTTONS.Attack)
    
    for i in Det:
        Text+=f'🔰{i} → {int(Det[i])+1} \n '
        if len(Text.split('\n')) > 40 :
            await message.reply_text(TEXTS.Attack_Details(Text,X, datetime.timedelta(seconds=float(f"{time()-Started_Attack_Time:.1f}"))),reply_markup=BUTTONS.Attack)
            Text=''
            
    if len(Text.split('\n')) > 0 :
        await message.reply_text(TEXTS.Attack_Details(Text,X, datetime.timedelta(seconds=float(f"{time()-Started_Attack_Time:.1f}"))),reply_markup=BUTTONS.Attack)

            # try:
            #     if 'connection' in str(e) : 
            #         await app.restart(False)
            #         pass
            # except:continue
    
@Advertising.on_message(RJ.prv & RJ.regex('^تبلیغاتی👀') , group=-1)
@RJ.User_Details
@RJ.Coin_Limit
async def Ads_Attack(bot,message,user:User):
    sys.setrecursionlimit(7000)
    global User_Attacking , User_Links
    if not user.Banners:
        await message.reply_text(TEXTS.No_Banner_Setted,reply_markup=BUTTONS.Attack)
        return
    try:
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
        Usernames=str(((await bot.Ask(int(user),TEXTS.Ask_Usernames,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
        Links=str(((await bot.Ask(int(user),TEXTS.Link_Attack,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
        if Links!=TEXTS.No:
            link=Link(Links)
            btn=str(((await bot.Ask(int(user),TEXTS.Link_btn_Attack,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
            if len(btn)> 15 :
                btn=TEXTS.Join_Btn
            User_Links[int(user)]=[link,btn]
        else :
            link=False
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Attack)
        return
    except:return
    #-----------------------------------------------------------------------------------------------------------
    Nums=RJ.Account(Nums,user)
    #-----------------------------------------------------------------------------------------------------------
    msg=None
    Det={}
    Text=''
    Y=0
    Round=0
    User_list={i:0 for i in [x for x in re.findall(r'.*\B@(?=\w{5,32}\b)[a-zA-Z0-9]+(?:_[a-zA-Z0-9]+)*.', Usernames)]}
    User_Attacking[int(user)]=True
    await message.reply_text(TEXTS.Proccess_Started,reply_markup=BUTTONS.Cancel_Attack)
    Started_Attack_Time=time()
    for num in Nums:
        if all(User_list.values()):
            break
        if not User_Attacking[int(user)] :break
        try:
            #-----------------------------------------------------------------------------------------------------------
            app = await num.Start()
            try:
                if link:
                    bot_results = await app.get_inline_bot_results(Config.BOT_USERNAME, f"{int(user)}")
                    msg=await app.send_inline_bot_result(f'@{Config.BOT_USERNAME}', bot_results.query_id, bot_results.results[0].id)
            except:pass
            for j,i in enumerate(User_list):
                if User_list[i] >= 1:continue
                if not User_Attacking[int(user)] :break
                try:
                    await Attack(app,i,link,user,msg,message)
                    User_list[i]+=1
                    Det[str(num)]=j
                    Y+=1
                except ConnectionError :
                    await message.reply_text(TEXTS.Connecting_e(num))
                    break
                except UnicodeError : 
                    return
                except errors.FloodWait as e:
                    if e.value < 200 :
                        await message.reply_text(TEXTS.Flood_Attack(num,e.value))
                        await sleep(e.value)
                    else:
                        await message.reply_text(TEXTS.High_Flood_Attack(num))
                        break
            await sleep(user.R_Speed)
            Round+=1
        except (errors.UserDeactivatedBan , errors.UserDeactivated):
            num.Delete()
            await message.reply_text(TEXTS.Number_Is_Deleted(num) , reply_markup=BUTTONS.Cancel_Attack)
        except (errors.AuthKeyInvalid , errors.AuthKeyUnregistered) as e:
            num.Delete()
            await message.reply_text(TEXTS.Number_Is_Terminated(num) , reply_markup=BUTTONS.Cancel_Attack)
            RJ.Log(int(user),f'AuthKeyUnregistered : {e}')
        except errors.PeerFlood:
            await message.reply_text(TEXTS.Reported(num) , reply_markup=BUTTONS.Cancel_Attack)
            try:Nums.remove(num)
            except:pass
        except Exception as e:
            await message.reply_text(TEXTS.Problem_with(str(num),f'{e}'))
            RJ.Log(int(user),f'Ads Attack  : {e}')
        finally:
            try:await app.stop(False)
            except:pass
        
    for i in Det:
        Text+=f'🔰{i} → {int(Det[i])+1} \n '
        if len(Text.split('\n')) > 40 :
            await message.reply_text(TEXTS.Attack_Details(Text,Y, datetime.timedelta(seconds=float(f"{time()-Started_Attack_Time:.1f}"))),reply_markup=BUTTONS.Attack)
            Text=''
            
    if len(Text.split('\n')) > 0 :
            await message.reply_text(TEXTS.Attack_Details(Text,Y, datetime.timedelta(seconds=float(f"{time()-Started_Attack_Time:.1f}"))),reply_markup=BUTTONS.Attack)



@Advertising.on_message(RJ.prv & RJ.regex('^فرواردی▶️') , group=-1)
@RJ.User_Details
@RJ.Coin_Limit
async def Forward_Attack(bot,message,user:User):
    sys.setrecursionlimit(7000)
    global User_Attacking , User_Links
    if not user.Banners:
        await message.reply_text(TEXTS.No_Banner_Setted,reply_markup=BUTTONS.Attack)
        return
    try:
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
        Usernames=str(((await bot.Ask(int(user),TEXTS.Ask_Usernames,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
        try:User_Round=int(((await bot.Ask(int(user),TEXTS.Ask_Round,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
        except:User_Round=10**10
        link=False
        banner=(await bot.Ask(int(user),TEXTS.askforward_banner,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))
        banner_id = int((await banner.forward(Config.Banners_Channel)).id)
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Attack)
        return
    except:return
    #-----------------------------------------------------------------------------------------------------------
    Nums=RJ.Account(Nums,user)
    #-----------------------------------------------------------------------------------------------------------
    msg=None
    Det={}
    Text=''
    Attack_Text=''
    X=0
    Round=0
    User_List=[x for x in re.findall(r'\B@(?=\w{5,32}\b)[a-zA-Z0-9]+(?:_[a-zA-Z0-9]+)*', Usernames)]
    User_Dict={i:0 for i in User_List}
    User_Attacking[int(user)]=True
    await message.reply_text(TEXTS.Proccess_Started,reply_markup=BUTTONS.Cancel_Attack)
    Started_Attack_Time=time()
    for num in Nums:
        if not User_Attacking[int(user)] :break
        try:
            #-----------------------------------------------------------------------------------------------------------
            app = await num.Start()
            for j,i in enumerate(User_List):
                if i=='' : continue
                if not User_Attacking[int(user)] :break
                if isinstance(User_Round,str) : User_Round =999
                if isinstance(User_Dict[i],str) : User_Dict[i] =999
                if User_Dict[i] >= User_Round:continue
                #------------------------------------
                try:
                    if not User_Attacking[int(user)] :raise UnicodeError
                    try:
                        await app.forward_messages(i,Config.Banners_Channel,banner_id)
                        user.Add_Coin(Config.Attack)
                        await sleep(user.A_Speed)
                    except (errors.bad_request_400.ChatForwardsRestricted,errors.bad_request_400.UsernameInvalid,errors.bad_request_400.UsernameNotOccupied , errors.bad_request_400.UsernameNotModified)  :
                        await message.reply_text(TEXTS.Username_NV(i))
                    except errors.ChatWriteForbidden :
                        await message.reply_text(TEXTS.Username_Ch(i))
                    except errors.YouBlockedUser:
                        try:
                            await app.unblock_user(user)
                            await app.forward_messages(i,Config.Banners_Channel,banner_id)
                            user.Add_Coin(Config.Attack)
                            await sleep(user.A_Speed)
                        except:pass
                #------------------------------------
                    User_Dict[i]+=1
                    Det[str(num)]=j
                    X+=1
                except ConnectionError :
                    await message.reply_text(TEXTS.Connecting_e(num))
                    break
                except UnicodeError : 
                    return
                except errors.FloodWait as e:
                    if e.value < 200 :
                        await message.reply_text(TEXTS.Flood_Attack(num,e.value))
                        await sleep(e.value)
                    else:
                        await message.reply_text(TEXTS.High_Flood_Attack(num))
                        break
            await sleep(user.R_Speed)
            Round+=1
        except (errors.UserDeactivatedBan , errors.UserDeactivated):
            num.Delete()
            await message.reply_text(TEXTS.Number_Is_Deleted(num) , reply_markup=BUTTONS.Cancel_Attack)
        except (errors.AuthKeyInvalid , errors.AuthKeyUnregistered) as e:
            num.Delete()
            await message.reply_text(TEXTS.Number_Is_Terminated(num) , reply_markup=BUTTONS.Cancel_Attack)
            RJ.Log(int(user),f'AuthKeyUnregistered : {e}')
        except errors.PeerFlood:
            await message.reply_text(TEXTS.Reported(num) , reply_markup=BUTTONS.Cancel_Attack)
            try:Nums.remove(num)
            except:pass
        except Exception as e:
            await message.reply_text(TEXTS.Problem_with(str(num),f'{e}'))
            RJ.Log(int(user),f'Forward Attack 3 : {e}')
        finally:
            try:await app.stop(False)
            except:pass
            
    for i in User_Dict:
        Attack_Text+=f'⚜️{i} → {User_Dict[i]} \n'
        if len(Attack_Text.split('\n')) > 40 :
            await message.reply_text(TEXTS.Username_Details(Attack_Text),reply_markup=BUTTONS.Attack)
            Attack_Text=''
    if len(Attack_Text.split('\n')) > 0 :
        await message.reply_text(TEXTS.Username_Details(Attack_Text),reply_markup=BUTTONS.Attack)
    
    for i in Det:
        Text+=f'🔰{i} → {int(Det[i])+1} \n '
        if len(Text.split('\n')) > 40 :
            await message.reply_text(TEXTS.Attack_Details(Text,X, datetime.timedelta(seconds=float(f"{time()-Started_Attack_Time:.1f}"))),reply_markup=BUTTONS.Attack)
            Text=''
            
    if len(Text.split('\n')) > 0 :
        await message.reply_text(TEXTS.Attack_Details(Text,X, datetime.timedelta(seconds=float(f"{time()-Started_Attack_Time:.1f}"))),reply_markup=BUTTONS.Attack)


@Advertising.on_message(RJ.prv & RJ.regex('^هوشمند🧠') , group=-1)
@RJ.User_Details
@RJ.Coin_Limit
async def Inteligence_Attack(bot,message,user:User):
    sys.setrecursionlimit(7000)
    global User_Attacking , User_Links
    if not user.Banners:
        await message.reply_text(TEXTS.No_Banner_Setted,reply_markup=BUTTONS.Attack)
        return
    try:
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
        Usernames=str(((await bot.Ask(int(user),TEXTS.Ask_Usernames,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
        Links=str(((await bot.Ask(int(user),TEXTS.Link_Attack,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
        try:User_Round=int(((await bot.Ask(int(user),TEXTS.Ask_Round,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
        except:User_Round=10**10
        if Links!=TEXTS.No:
            link=Link(Links)
            btn=str(((await bot.Ask(int(user),TEXTS.Link_btn_Attack,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
            if len(btn)> 15 :
                btn=TEXTS.Join_Btn
            User_Links[int(user)]=[link,btn]
        else :
            link=False
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Attack)
        return
    except:return
    #-----------------------------------------------------------------------------------------------------------
    Nums=RJ.Account(Nums,user)
    #-----------------------------------------------------------------------------------------------------------
    msg=None
    Det={}
    Text=''
    Attack_Text=''
    X=0
    Round=0
    User_List=[x for x in re.findall(r'\B@(?=\w{5,32}\b)[a-zA-Z0-9]+(?:_[a-zA-Z0-9]+)*', Usernames)]
    User_Dict={i:0 for i in User_List}
    User_Attacking[int(user)]=True
    await message.reply_text(TEXTS.Proccess_Started,reply_markup=BUTTONS.Cancel_Attack)
    Started_Attack_Time=time()
    for num in Nums:
        if not User_Attacking[int(user)] :break
        try:
            #-----------------------------------------------------------------------------------------------------------
            app = await num.Start()
            try:
                if link:
                    bot_results = await app.get_inline_bot_results(Config.BOT_USERNAME, f"{int(user)}")
                    msg=await app.send_inline_bot_result(f'@{Config.BOT_USERNAME}', bot_results.query_id, bot_results.results[0].id)
            except:pass
            for j,i in enumerate(User_List):
                if i=='' : continue
                if not User_Attacking[int(user)] :break
                if isinstance(User_Round,str) : User_Round =999
                if isinstance(User_Dict[i],str) : User_Dict[i] =999
                if User_Dict[i] >= User_Round:continue
                try:
                    await Attack(app,i,link,user,msg,message)
                    User_Dict[i]+=1
                    Det[str(num)]=j
                    X+=1
                except ConnectionError :
                    await message.reply_text(TEXTS.Connecting_e(num))
                    break
                except UnicodeError : 
                    return
                except errors.FloodWait as e:
                    if e.value < 200 :
                        await message.reply_text(TEXTS.Flood_Attack(num,e.value))
                        await sleep(e.value)
                    else:
                        await message.reply_text(TEXTS.High_Flood_Attack(num))
                        break
            await sleep(user.R_Speed)
            Round+=1
        except (errors.UserDeactivatedBan , errors.UserDeactivated):
            num.Delete()
            await message.reply_text(TEXTS.Number_Is_Deleted(num) , reply_markup=BUTTONS.Cancel_Attack)
        except (errors.AuthKeyInvalid , errors.AuthKeyUnregistered) as e:
            num.Delete()
            await message.reply_text(TEXTS.Number_Is_Terminated(num) , reply_markup=BUTTONS.Cancel_Attack)
            RJ.Log(int(user),f'AuthKeyUnregistered : {e}')
        except errors.PeerFlood:
            await message.reply_text(TEXTS.Reported(num) , reply_markup=BUTTONS.Cancel_Attack)
            try:Nums.remove(num)
            except:pass
        except Exception as e:
            await message.reply_text(TEXTS.Problem_with(str(num),f'{e}'))
            RJ.Log(int(user),f'AI Attack 3 : {e}')
        finally:
            try:await app.stop(False)
            except:pass
            
    for i in User_Dict:
        Attack_Text+=f'⚜️{i} → {User_Dict[i]} \n'
        if len(Attack_Text.split('\n')) > 40 :
            await message.reply_text(TEXTS.Username_Details(Attack_Text),reply_markup=BUTTONS.Attack)
            Attack_Text=''
    if len(Attack_Text.split('\n')) > 0 :
        await message.reply_text(TEXTS.Username_Details(Attack_Text),reply_markup=BUTTONS.Attack)
    
    for i in Det:
        Text+=f'🔰{i} → {int(Det[i])+1} \n '
        if len(Text.split('\n')) > 40 :
            await message.reply_text(TEXTS.Attack_Details(Text,X, datetime.timedelta(seconds=float(f"{time()-Started_Attack_Time:.1f}"))),reply_markup=BUTTONS.Attack)
            Text=''
            
    if len(Text.split('\n')) > 0 :
        await message.reply_text(TEXTS.Attack_Details(Text,X, datetime.timedelta(seconds=float(f"{time()-Started_Attack_Time:.1f}"))),reply_markup=BUTTONS.Attack)

@Advertising.on_message(RJ.prv & RJ.regex('^ادر🫂') , group=-1)
@RJ.User_Details
@RJ.Coin_Limit
async def Add_Users(bot,message,user:User):
    global User_Attacking , User_Links
    try:
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
        link=str(((await bot.Ask(int(user),TEXTS.Ask_Adding_Link,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text).replace('https://','')
        if link.isdigit():link=int(link)
        elif not '/joinchat/' in link and not '+' in link :link=f'@{link.split("/")[-1]}'
        Usernames=str(((await bot.Ask(int(user),TEXTS.Ask_Usernames,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=120))).text)
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Attack)
        return
    except:return
    #-----------------------------------------------------------------------------------------------------------
    Nums=RJ.Account(Nums,user)
    #-----------------------------------------------------------------------------------------------------------
    User_Attacking[int(user)]=True
    User_List=[x for x in re.findall(r'\B@(?=\w{5,32}\b)[a-zA-Z0-9]+(?:_[a-zA-Z0-9]+)*', Usernames)]
    User_Dict={i:0 for i in User_List}
    Attack_Text=''
    X=0
    await message.reply_text(TEXTS.Proccess_Started,reply_markup=BUTTONS.Cancel_Attack)
    Started_Attack_Time=time()
    for num in Nums:
        if all(User_Dict.values()) and 0 not in User_Dict.values() : break
        if not User_Attacking[int(user)] :break
        try:
            app = await num.Start()
            try:
                Chat = await app.join_chat(link)
            except errors.UserAlreadyParticipant : 
                Chat = await app.get_chat(link)
            for i in (User_List):
                if User_Dict[i] >= 1:continue
                if i=='' : continue
                if not User_Attacking[int(user)] :break
                try:
                    await app.add_chat_members(Chat.id,i.strip(),0)
                    user.Add_Coin(Config.Add)
                    User_Dict[i]+=1
                    X+=1
                except errors.PeerFlood:pass
                except errors.UserAlreadyParticipant :pass
                except ConnectionError as e: 
                    RJ.Log(int(user),f'connection  : {e}')
                    await app.stop(False)
                    await app.start()
                except ( errors.bad_request_400.UserIdInvalid,errors.bad_request_400.UsernameInvalid,errors.bad_request_400.UsernameNotOccupied,errors.bad_request_400.PeerIdInvalid , errors.bad_request_400.UsernameNotModified , errors.bad_request_400.UsernameInvalid,errors.bad_request_400.UsernameNotOccupied)  :
                    await message.reply_text(TEXTS.Username_NV(i))
                except errors.ChatWriteForbidden :
                    await message.reply_text(TEXTS.AddRestricted(i))
                except (errors.forbidden_403.UserPrivacyRestricted , errors.bad_request_400.UserNotMutualContact ):
                    await message.reply_text(TEXTS.AddRestricted(i))
                await sleep(user.A_Speed)
            
        except (errors.UserDeactivatedBan , errors.UserDeactivated):
            num.Delete()
            await message.reply_text(TEXTS.Number_Is_Deleted(num) , reply_markup=BUTTONS.Cancel_Attack)
        except (errors.AuthKeyInvalid , errors.AuthKeyUnregistered) as e:
            num.Delete()
            await message.reply_text(TEXTS.Number_Is_Terminated(num) , reply_markup=BUTTONS.Cancel_Attack)
            RJ.Log(int(user),f'AuthKeyUnregistered : {e}')
        # except errors.PeerFlood:
        #     await message.reply_text(TEXTS.Reported(num) , reply_markup=BUTTONS.Cancel_Attack)
        #     try:Nums.remove(num)
        #     except:pass
        except Exception as e:RJ.Log(int(user),f'Adder  : {e}')
        finally:
            try:await Chat.leave()
            except:pass
            try:await app.stop(False)
            except:pass
        await sleep(user.R_Speed)
        
    for i in User_Dict:
        if User_Dict[i]==0:
            Attack_Text+=f'{i} \n'
        if len(Attack_Text.split('\n')) > 40 :
            await message.reply_text(TEXTS.Username_Added_Details(Attack_Text,X,datetime.timedelta(seconds=float(f"{time()-Started_Attack_Time:.1f}"))),reply_markup=BUTTONS.Attack)
            Attack_Text=''
            
    if len(Attack_Text.split('\n')) > 0 :
        await message.reply_text(TEXTS.Username_Added_Details(Attack_Text,X,datetime.timedelta(seconds=float(f"{time()-Started_Attack_Time:.1f}"))),reply_markup=BUTTONS.Attack)

@Advertising.on_message(RJ.prv & RJ.filters.command('split') , group=-1)
@RJ.User_Details
@RJ.Coin_Limit
async def Split_duc(bot,message,user:User):
    try:
        amount = int(str(message.command[1]))
        end = int(str(message.command[2]))
        if amount > 300 : 
            await message.reply_text(TEXTS.Wrong,reply_markup=BUTTONS.Attack)
            return
        x=await message.reply_to_message.download(file_name = f'List_{int(user)}.txt')
        y=''
        count=0
        with open(x , 'r') as f:
            all=f.read().split('\n')
            
            for i in all:
                y+=f'{i} \n'
                
                if len(y.split('\n')) >= amount : 
                    await message.reply_text(y)
                    count+=1
                    y=''
                    await sleep(3)
                    
                if count >= end : return
                
        if y != '' : 
            await message.reply_text(y)
            
    except Exception as e:print(e)
    
    remove(x)
    
@Advertising.on_message(RJ.prv & RJ.regex('^لیست گیر🚸') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Username_Catcher(bot,message,user:User):
    try:
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=90))).text)
        Gap_Link=str(((await bot.Ask(int(user),TEXTS.Ask_Link,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=30))).text)
        User_Limit=int(((await bot.Ask(int(user),TEXTS.User_Limit,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=30))).text)
        Kind=str(((await bot.Ask(int(user),TEXTS.Catcher_Kind,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=30))).text)
        type=str(((await bot.Ask(int(user),TEXTS.Catcher_type,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=30))).text)
        Left_After=str(((await bot.Ask(int(user),TEXTS.Left_after_task,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=30))).text)
        if Left_After == TEXTS.yes : Left_After=True
        else:Left_After=False 
        if 'ONLINE' in type.upper():only_onlines = True
        else:only_onlines = False
        if 'RECENTLY' in type.upper():only_recentlies = True
        else:only_recentlies = False
        if 'PHOTO' in type.upper():only_photo = True
        else:only_photo = False
        if 'ADMINS' in type.upper():only_admins = True
        else:only_admins = False
        if 'MEMBERS' in type.upper():only_members = True
        else:only_members = False
        if 'PREMIUM' in type.upper():only_pre = True
        else:only_pre = False
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Attack)
        return
    except:return
    Nums=RJ.Account(Nums,user)
    
    if Gap_Link.isdigit():Gap_Link=int(Gap_Link)
    elif not '/joinchat/' in Gap_Link and not  '+' in Gap_Link:Gap_Link=f'@{Gap_Link.split("/")[-1]}'
    else :Gap_Link=Gap_Link.replace('https://','')
    Users={}
    await message.reply_text(TEXTS.Proccess_Started,reply_markup=BUTTONS.Cancel_Attack)
    for i in Nums:
        if len(Users) > User_Limit:break
        try:
            app = await i.Start()
            try:
                Chat = await app.join_chat(Gap_Link)
            except errors.UserAlreadyParticipant : 
                Chat = await app.get_chat(Gap_Link)
            except Exception as e : await message.reply_text(TEXTS.Problem_with(str(i),f'{e}'))
            try:
                Admins=[]
                async for ttt in Chat.get_members(filter=ChatMembersFilter.ADMINISTRATORS):
                    Admins.append(int(ttt.user.id))
            except:pass
                
            if TEXTS.Members in Kind:
                async for tt in app.get_chat_members(int(Chat.id)):
                    if len(Users) > User_Limit:break
                    try:
                        if not tt.user:continue
                        
                        if only_members :
                            if int(tt.user.id) in Admins:continue
                        elif only_admins:
                            if not int(tt.user.id) in Admins :continue
                        if only_pre:
                            if not tt.user.is_premium  : continue
                        if only_photo : 
                            if not tt.user.photo  : continue
                        if only_onlines : 
                            if not tt.user.status == UserStatus.ONLINE:continue
                        elif only_recentlies : 
                            if not tt.user.status == UserStatus.RECENTLY:continue
                        
                        
                        if tt.user.is_bot: continue
                        if tt.user.username:Users[tt.user.username]='https://WWW.GITHUB.COM/AMIRALIRJ'
                    except Exception as e:
                        RJ.Log(int(user),f'List Catcher 2.1 : {e}')
            else:
                if User_Limit > 1000 : 
                    await message.reply_text(TEXTS.Limit_Catchers)
                    return
                all_user_list=[ii async for ii in app.get_chat_history(int(Chat.id),limit=User_Limit*10)]
                if len(all_user_list) < 10 : 
                    try:await app.stop(False)
                    except:pass
                    await message.reply_text(TEXTS.History_Closed,reply_markup=BUTTONS.Attack)
                    return
                for iii in all_user_list:
                    try:
                        if len(Users) > User_Limit:break
                        if not iii.from_user:continue
                        if iii.from_user.is_bot  : continue
                        
                        if only_members :
                            if int(iii.from_user.id) in Admins:continue
                        elif only_admins:
                            if not int(iii.from_user.id) in Admins :continue
                        if only_pre:
                            if not iii.from_user.is_premium  : continue
                        if only_photo : 
                            if not iii.from_user.photo  : continue
                        if only_onlines : 
                            if not iii.from_user.status == UserStatus.ONLINE:continue
                        elif only_recentlies : 
                            if not iii.from_user.status == UserStatus.RECENTLY:continue
                            
                        if iii.from_user.username:Users[iii.from_user.username]='https://WWW.GITHUB.COM/AMIRALIRJ'
                    except Exception as e:
                        RJ.Log(int(user),f'List Catcher 2.2 : {e}')
        except (errors.InviteHashExpired , errors.LinkNotModified , errors.InviteHashEmpty , errors.InviteHashInvalid , errors.InviteRevokedMissing ):
            if Left_After :    
                try:await Chat.leave()
                except:pass
            try:await app.stop(False)
            except:pass
            await message.reply_text(TEXTS.Link_Invalied,reply_markup=BUTTONS.Attack)
            return
        except Exception as e:
            if 'INVITE_REQUEST_SENT' in str(e): 
                await message.reply_text(TEXTS.Requested_Chat,reply_markup=BUTTONS.Attack)
                try:await app.stop(False)
                except:pass
                return
            else:
                RJ.Log(int(user),f'List Catcher : {e}')
                await message.reply_text(TEXTS.Problem_with(str(i),f'{e}'))
        finally:
            if Left_After :    
                try:await Chat.leave()
                except:pass
            try:await app.stop(False)
            except:pass
    
    try:
        with open(f'XXID{int(user)}.txt','a+') as f : 
            for i in Users :
                f.write(f'@{i} \n')
        await message.reply_document(document = f'XXID{int(user)}.txt' , file_name  = '@darkbotschannel.txt',reply_markup=BUTTONS.Attack)
        
        remove(f'XXID{int(user)}.txt')
    except Exception as e:
        RJ.Log(int(user),f'List Catcher END : {e}')
              
    # X=''
    # for i in Users:
    #     if len(X.split('\n')) > 50 :
    #         await message.reply_text(TEXTS.Username_Catched(X),reply_markup=BUTTONS.Attack)
    #         X=''
    #     X+=f'@{i} \n'
    #     user.Add_Coin(Config.Chatcher)

    # if len(X.split('\n')) > 0 :
    #     await message.reply_text(TEXTS.Username_Catched(X),reply_markup=BUTTONS.Attack)
        

@Advertising.on_message(RJ.prv & RJ.regex('^اسپم📛') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Spam(bot,message,user:User):
    try:
        try:
            Spam_Banners_num=abs(int(((await bot.Ask(int(user),TEXTS.AskSpam_Banners_num,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=30))).text))
            if Spam_Banners_num > 10 or Spam_Banners_num==0:raise ValueError
        except ValueError:
            await message.reply_text(TEXTS.Wrong,reply_markup=BUTTONS.Attack)
            return
        Banners=[]
        for i in range(Spam_Banners_num):
            Bnr=(((await bot.Ask(int(user),TEXTS.Ask_SpamBanner,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=45))))
            Bnr_id=int((await Bnr.copy(Config.Banners_Channel)).id)
            Banners.append(int(Bnr_id))
        Nums=str(((await bot.Ask(int(user),TEXTS.Ask_Nums,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=30))).text)
        Chat_Link=str(((await bot.Ask(int(user),TEXTS.Ask_Link,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=30))).text).replace('https://','')
        Spam_Count=int(((await bot.Ask(int(user),TEXTS.Spam_Count,Msg=message,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=30))).text)
    except TimeoutError :
        await message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Attack)
        return
    
    
    if Chat_Link.isdigit():Chat=int(Chat_Link)
    elif not 'joinchat/' in Chat_Link and not '+' in Chat_Link:Chat=f'@{Chat_Link.split("/")[-1].replace("@","")}'
    else:Chat = Chat_Link
    Nums=RJ.Account(Nums,user)
    User_Spamming[int(user)]=True
    X=0
    await message.reply_text(TEXTS.Proccess_Started,reply_markup=BUTTONS.Cancel_Spam)
    Active_Nums=[]
    for i in Nums:
        if not User_Spamming[int(user)] :break
        try:
            app=await i.Start()
            Active_Nums.append(app)
        except:pass
    gap_link=Chat
    for app in Active_Nums : 
        if not User_Spamming[int(user)] :break
        try :
            try:
                Chat = await app.join_chat(gap_link)
            except errors.UserAlreadyParticipant : 
                Chat = await app.get_chat(gap_link)
            Chat_id= Chat.id
        except (errors.InviteHashExpired , errors.LinkNotModified , errors.InviteHashEmpty , errors.InviteHashInvalid , errors.InviteRevokedMissing ) : await message.reply_text(TEXTS.Acc_banned(str(app.phone_number)),reply_markup=BUTTONS.Accounts)
        except Exception as e:
            RJ.Log(int(user),f'Spam Joining : {e}')
            continue
    restricted=[]
    try:
        for i in range(Spam_Count):
            for app in Active_Nums : 
                try:
                    if app.phone_number in restricted: continue
                    if not User_Spamming[int(user)] : break
                    await app.copy_message(Chat.id,Config.Banners_Channel,RJ.choice(Banners))
                    X+=1
                    if bool(user.A_Speed) :await sleep(user.A_Speed)
                except:
                    try:
                        RJ.Log(int(user),f'Spam Sending : {e}')
                        restricted.append(app.phone_number)
                    except:pass
        
    except Exception as e:RJ.Log(int(user),f'Spam : {e}')
    
    for app in Active_Nums :
        try:
            await app.leave_chat(Chat_id)
        except:pass
        finally:
            try:await app.stop(False)
            except:pass
        
    user.Add_Coin(Config.Spam * (X))
    await message.reply_text(TEXTS.Spam_Complited(X),reply_markup=BUTTONS.Attack)
        
        
@Advertising.on_message(RJ.prv & RJ.regex('^تنظیمات حرفه ای⚙️') , group=0)
@RJ.User_Details
@RJ.Coin_Limit
async def Attack_Setting(bot,message,user:User):
    await message.reply_text(TEXTS.Attack_Setting,reply_markup=BUTTONS.Attack_Setting)
    
@Advertising.on_message(RJ.prv & RJ.regex('^🚫 لغو اتک 🚫') , group=0)
@RJ.User_Details
async def Cancel_Attack(bot,message,user:User):
    User_Attacking[int(user)]=False
    await message.reply_text(TEXTS.Cancel,reply_markup=BUTTONS.Attack)
    
@Advertising.on_message(RJ.prv & RJ.regex('^🚫 لغو اسپم 🚫') , group=0)
@RJ.User_Details
async def Cancel_Spam(bot,message,user:User):
    User_Spamming[int(user)]=False
    await message.reply_text(TEXTS.Cancel,reply_markup=BUTTONS.Attack)

#------------------------------------------------------------------| INLINE |-----------------------------------------------------------------#

@Advertising.on_inline_query()
async def Inline_Query_Callback(bot:Advertising,query):
    user=User(int(query.query))
    Banner=(await bot.get_messages(Config.Banners_Channel,user.Rand_Banner))
    if Banner.text:
        await BUTTONS.Inline_Answer(query,User_Links[int(user)][0],Banner.text,User_Links[int(user)][1])
        