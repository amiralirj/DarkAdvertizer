from pyrogram.raw.functions.messages import GetAvailableReactions
from pyrogram.raw.functions.messages import GetMessagesViews
from pyrogram.raw.types import    (InputReportReasonChildAbuse,
                                  InputReportReasonCopyright ,
                                       InputReportReasonFake,
                            InputReportReasonGeoIrrelevant,
                           InputReportReasonIllegalDrugs,
                                InputReportReasonOther,
                    InputReportReasonPersonalDetails,
                      InputReportReasonPornography,
                           InputReportReasonSpam,
                     InputReportReasonViolence)
from pyrogram import Client , filters , errors
from pyrogram.types import InputPhoneContact
from Classes import UserClass , NumberClass
from os import remove , listdir , path 
from pyrogram.enums import ChatAction
from pyrogram.enums import ParseMode
from random import choice , randint
from Data.DataBase import DataBase
from datetime import datetime
from pyromod import listen
from time import sleep 
from Config import (API_ID,
           OWNER_USERNAME,
               API_HASH,
             BOT_TOKEN,
               OWNER,
             TEXTS,
          BUTTONS,
 Natural_Channels,
 BOT_USERNAME )
import Funcs as pr
import threading
import logging
import asyncio
import Config
#------------------------------------| This will make Sessions folder
from os import makedirs            #-|
makedirs('Sessions',exist_ok=True) #-|
del makedirs                       #-|
#------------------------------------|   

logging.disable()

#----------------------------------------------------------------------------------------------------------------|
#-------------------------------------------------| ADVERTIZER |-------------------------------------------------|        
#-------------------------------------------------| ADVERTIZER |-------------------------------------------------|        
#-------------------------------------------------| ADVERTIZER |-------------------------------------------------|
#----------------------------------------------------------------------------------------------------------------| Helper Class
class Rj:                                                                                                      #-|
    def __init__(self) -> None:                                                                                #-|
        self.data=DataBase                                                                                     #-|
        self.Owner = OWNER                                                                                     #-|
        self.Owner_Username = OWNER_USERNAME                                                                   #-|
        self.filters=filters                                                                                   #-|
        self.prv=self.filters.private                                                                          #-|
        self.regex=self.filters.regex                                                                          #-|
        self.choice = choice                                                                                   #-|
        self.remove=remove                                                                                     #-|
        self.Active_Procces={}                                                                                 #-|
        self.ms={}                                                                                             #-|
        self.report={'ChildAbuse':InputReportReasonChildAbuse,                                                 #-|
                     'Copyright':InputReportReasonCopyright,                                                   #-|
                     'Fake':InputReportReasonFake,                                                             #-|
                     'GeoIrrelevant':InputReportReasonGeoIrrelevant,                                           #-|
                     'IllegalDrugs':InputReportReasonIllegalDrugs,                                             #-|
                     'Other':InputReportReasonOther,                                                           #-|
                     'PersonalDetails':InputReportReasonPersonalDetails,                                       #-|
                     'Pornography':InputReportReasonPornography,                                               #-|
                     'Spam':InputReportReasonSpam,                                                             #-|
                     'Violence':InputReportReasonViolence}                                                     #-|
                                                                                                               #-|
#----------------------------------------------------------------------------------------------------------------| BOT DETAILS METHOD (registered numbers & users)
    @property                                                                                                  #-|
    def Details(self):                                                                                         #-|
        return [len(DataBase.All_Numbers),len(DataBase.All_Users)]                                             #-|
#----------------------------------------------------------------------------------------------------------------| BOT Owner recognize
    def is_Owner(self,user):                                                                                   #-|
        return int(user)==int(Config.OWNER)                                                                    #-|
#----------------------------------------------------------------------------------------------------------------| Decorator 
    def User_Details(self,Func):                                                                               #-| <Give User Class Instance to Func>
        async def Wrapper(Cli, message):                                                                       #-|
            User_id=int(message.from_user.id)                                                                  #-|
            if User_id in self.ms : self.ms[User_id]+=1                                                        #-|
            else:self.ms[User_id]=1                                                                            #-|
            await Func(Cli,message,UserClass.User(User_id))                                                    #-|
        return Wrapper                                                                                         #-|
                                                                                                               #-|
    def Coin_Limit(self,Func):                                                                                 #-| <Membership Decorator>
        async def Wrapper(Cli,message,User):                                                                   #-|
            if User.Coin > 0 or User.Active_Membership :                                                       #-|
                try:self.Active_Procces[int(User)]=True                                                        #-|
                except:pass                                                                                    #-|
                await Func(Cli,message,User)                                                                   #-|
                try:self.Active_Procces.pop(int(User))                                                         #-|
                except:pass                                                                                    #-|
            else:await message.reply_text(TEXTS.Buy_Coin,reply_markup=BUTTONS.Support(self.Owner_Username))    #-|
        return Wrapper                                                                                         #-|
#----------------------------------------------------------------------------------------------------------------| Errors & Logs Recording Method  
    def Log(self,Userid,message=None):                                                                         #-|
        with open('Logs.txt','a+',encoding='utf-8') as f :                                                     #-|
            f.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M")} - {Userid} → {message} \n \n ' )             #-|
#----------------------------------------------------------------------------------------------------------------|
#---------------------------------------------------------------------------------------------------------------------\
#--------------------------------------------------------------------------------------------------------------------------| Account Spliting 
    def Account(self,Nums:str,user,all=False) -> NumberClass.Number:                                                     #-|
        if all:Acc_List=user.All_numbers                                                                                 #-|
        else:Acc_List=user.All_Active_Numbers                                                                            #-|
        if Nums.isdigit() :                                                                                              #-|
            if len(str(abs(int(Nums)))) <= 4 :                                                                           #-|
                return NumberClass.Number(Acc_List[(int(Nums)-1)]['num'],int(user))                                      #-|
        if Nums.strip()==TEXTS.All_abrvtn :                                                                              #-|
            Nums=[NumberClass.Number(i['num'],int(user)) for i in Acc_List ]                                             #-|
        elif '+' not in Nums and '\n' not in Nums and ':' in Nums:                                                       #-|_____\
            Index=Nums.split(':')                                                                                        #-|2022  \
            Nums=[NumberClass.Number(i['num'],int(user)) for i in Acc_List[(int(Index[0])-1):(int(Index[1])-1)]]         #-|[ .]   |
        else:                                                                                                            #-|2022  /
            Text_list=Nums.split('\n')                                                                                   #-|_____/
            Nums=[NumberClass.Number(i,int(user)) for i in Text_list if (NumberClass.Number(i,int(user))).is_Owner ]     #-|
        if isinstance(Nums,str):                                                                                         #-|
            Nums=[NumberClass.Number(i['num'],int(user)) for i in Acc_List ]                                             #-|
        return Nums                                                                                                      #-|
#--------------------------------------------------------------------------------------------------------------------------|
#----------------------------------------------------------------------------------------------------------------------/
#----------------------------------------------------------------------------------------------------------------| profile / bio / name UPDATER
    async def Auto_Detail_Setter(self,app:Client,user:UserClass.User):                                         #-|
        try :                                                                                                  #-|
            if user.Auto_pic:                                                                                  #-|
                try:                                                                                           #-|
                    photo= await app.get_messages(Config.Banners_Channel,int(user.Auto_pic))                   #-|
                    photo=str( await photo.download())                                                         #-|
                    await app.set_profile_photo(photo=photo)                                                   #-|
                    user.Add_Coin(Config.update_profile)                                                       #-|
                    remove(photo)                                                                              #-|
                except Exception as e:self.Log(int(user),f' Auto Picture Method  : {e}')                       #-|
            if user.Auto_bio:                                                                                  #-|
                try:                                                                                           #-|
                    await app.update_profile(bio=user.Auto_bio)                                                #-|
                    user.Add_Coin(Config.update_profile)                                                       #-|
                except Exception as e:self.Log(int(user),f' Auto Bio Method  : {e}')                           #-|
            if user.AutoName:                                                                                  #-|
                try:                                                                                           #-|
                    await app.update_profile(first_name=user.AutoName)                                         #-|
                    user.Add_Coin(Config.update_profile)                                                       #-|
                except Exception as e:self.Log(int(user),f' Auto Name Method  : {e}')                          #-|
        except:pass                                                                                            #-|
#----------------------------------------------------------------------------------------------------------------| Random 
    @property
    def Random_Photo(self):
        return f'{Config.Photos_Path}/{(choice(listdir(Config.Photos_Path)))}'
    
    @property
    def Random_Bio(self):
        with open(f'{Config.Fake_Details_Path}/Bio.txt','r',encoding='utf-8') as f:
            return choice(f.readlines()).strip()
        
    @property
    def Random_Name(self):
        with open(f'{Config.Fake_Details_Path}/Name.txt','r',encoding='utf-8') as f:
            return choice(f.readlines()).strip()
        
    @property
    def Random_Username(self):
        with open(f'{Config.Fake_Details_Path}/Username.txt','r',encoding='utf-8') as f:
            username=choice(f.readlines()).strip()
            lst = list(username)
            if bool(randint(0,1)):
                lst.insert(randint(1, len(username)), str(randint(1365,1385)))
            else:
                lst.insert(randint(1, len(username)), str(randint(1990,2022)))
            return ("".join(lst))
    
    @property
    def Random_API(self):
        with open(f'APIs.txt','r') as f:
            api= choice(f.readlines()).split(':')
            return [api[0],int(api[1])]
        
    @property
    def All_Users(self):
        return self.data.All_Users
    
    @property
    def DataBase_Data(self):
        data=str(self.data.All_Data_Text)
        return data
    
    def Join_Channel(self,Func):
        async def Wrapper(client:Client, message):
            try:
                await client.get_chat_member(Config.Dark_Channel,int(message.from_user.id))
                await Func(client,message)
            except:await message.reply_text(TEXTS.Join_Channel(Config.Dark_Channel))
        return Wrapper
            
    @property 
    def Rand_Device(self):
        return choice(Config.D_MODEL).strip()
    
        
    def RandomString(self):
        characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
        Rand_String = ''
        for x in range(5):
            Rand_String +=choice(characters)
        return Rand_String

    @property
    def Get_Device_Detais(self):
        mod = choice([1, 2, 3])
        device_model = choice(Config.AndroidPhone) if mod == 1 else choice(
            Config.IosPhone) if mod == 2 else choice(self.RandomString())
        system_version = choice(Config.AndroidVersion) if mod == 1 else choice(
            Config.IosVersion) if mod == 2 else choice(Config.PcVersion)
        app_version = choice(Config.AppVersion)
        lang_code, system_lang_code = choice(Config.lan)
        return [str(device_model), str(system_version), str(app_version), str(lang_code), str(system_lang_code)]
    
    def RetLink(self,link):
        if '@' in link :return link
        elif (not '/joinchat/' in link and '+' not in link) and 't.me' in link :return (link.split("/")[-1]).split('@')[-1]
        elif 't.me' in link :return link.replace('https://','').replace('t.me/','')
        else:return False
        
    @property
    def Message(self):
        with open(f'{Config.Fake_Details_Path}/Messages.txt','r',encoding='utf-8') as f:
            return choice(f.readlines()).strip()

RJ=Rj()
#----------------------------------------------------|----------------------------------------------------
#||||||||||||||||-|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||-|||||||||||||||| 
#----------------------------------------------------|----------------------------------------------------
    
async def Seen(app):
    chnl=choice(Natural_Channels)
    async for i in app.get_chat_history(chnl,10):
        await app.invoke(GetMessagesViews( peer= (await app.resolve_peer(chnl)) , id=i.id , increment = True))
        sleep(randint(2,8))
        
async def reAction(app):
    try:
        chnl=choice(Natural_Channels)
        li=(await app.get_chat(chnl))
        reactions=[i.emoji for i in li.available_reactions.reactions ]
        print(reactions) 
        async for i in app.get_chat_history(chnl,10):
                await app.invoke(GetMessagesViews( peer= (await app.resolve_peer(chnl)) , id=[i.id] , increment = True))
                await app.send_reaction(chnl , i.id, choice(reactions))
                sleep(randint(2,8))
    except Exception as e:
        RJ.Log(int(1111),f'Natural Account reaction : {e}')

async def Save(app):
    chnl=choice(Natural_Channels)
    async for i in app.get_chat_history(chnl,10):
        if not bool(randint(0,3)):
            try:
                await i.forward('me')
                sleep(randint(2,8))
            except Exception as e:
                RJ.Log(int(1111),f'Natural Account Forward : {e}')
            
async def Join(app):
    chnl=choice(Natural_Channels)
    await app.join_chat(chnl)
    
async def Robot_Intract(app):
    try:
        await app.send_chat_action(f'@{BOT_USERNAME}', ChatAction.TYPING)
        sleep(0.5)
        mes=await app.send_message(f'@{BOT_USERNAME}','/start')
        sleep(0.7)
        await mes.click(0)
    except:await app.unblock_user(f'@{BOT_USERNAME}')
        
async def Intract_With_Others(app,nums): # in khafange
    friend=choice(nums)
    try:
        friend_app=(await friend.Start())
        main_id=(await app.get_me())
        friend_details=await friend_app.get_me()
        try:
            await friend_app.import_contacts([InputPhoneContact(str(main_id.phone_number), f"{RJ.Random_Name} {randint(1,3)}")])
        finally:
            await friend_app.stop()
        user=await app.import_contacts([InputPhoneContact(str(friend), f"{RJ.Random_Name} {randint(1,3)}")])
        
    
    except Exception as e:
        RJ.Log(int(11111),f'Intract whith others {e}')
        friend=choice(nums)
        friend_app=(await friend.Start())
        friend_details=await friend_app.get_me()
        main_id=await app.get_me()
        try:
            await friend_app.import_contacts([InputPhoneContact(str(main_id.phone_number), f"{RJ.Random_Name} {randint(1,3)}")])
        finally:
            await friend_app.stop()
        user=await app.import_contacts([InputPhoneContact(str(friend), f"{RJ.Random_Name} {randint(1,3)}")])
    try:
        await app.send_chat_action( int(friend_details.id) , ChatAction.TYPING)
        sleep(randint(5,25))
        for b in range(randint(1,4)):
            await app.send_message(int(friend_details.id) , RJ.Message )
            sleep(randint(5,25))
        await app.send_message(int(friend_details.id),f'bYe I LOve daRk {RJ.Random_Bio}')
    except Exception as e:
        RJ.Log(int(11111),f'Intract whith others sending message  {e}')
        
async def Intract_Back(app):
    async for i in app.get_dialogs():
        try:
            text = 'bYe I LOve daRk'
            message = i.top_message
            result = (message.text or message.caption)
            if text in result and not message.outgoing  :
                try:
                    if not bool(randint(0,1)):
                        await app.read_chat_history(int(i.chat.id))
                        sleep(randint(1,10))
                        for b in range(randint(1,4)):
                            await app.send_chat_action( int(i.chat.id) , ChatAction.TYPING)
                            sleep(randint(10,30))
                            await app.send_message(int(i.chat.id) , RJ.Message )
                            sleep(randint(10,30))
                        await app.send_message(f'bYe I LOve daRk {RJ.Random_Bio}' , RJ.Message )
                except Exception as e:
                    RJ.Log(int(11111),f'Intract BACK Inner for    {e}')
        except Exception as e:
            RJ.Log(int(11111),f'Intract BACK   {e}')
        
async def Natural_Activities(database):
    Nums=[NumberClass.Number(i[0],int(i[4])) for i in database.Natural_Accounts ]
    for i in Nums:
        if not bool(randint(0,3)):continue
        try:
            app= await i.Start()
            await app.send_chat_action('me', ChatAction.CANCEL)
            #      هرچی گل مچاله تر رایحه بیشتر      *-*
            work=choice([Seen,reAction,Save,Robot_Intract,Join])
            await reAction(app)
            await work(app)
            RJ.Log(int(11111),f'has done  : {work.__name__}')
            sleep(randint(30,60))
            await Intract_With_Others(app,Nums)
            sleep(randint(30,60))
            await Intract_Back(app)
            RJ.Log(int(11111),f'has doneeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
        except (errors.AuthKeyInvalid , errors.AuthKeyUnregistered , errors.SessionRevoked , errors.SessionExpired , errors.UserDeactivatedBan , errors.UserDeactivated ):
            i.Delete()
            #bot.send_message( i.Owner , TEXTS.Num_Natural_Deleted)
        except Exception as e:
            try:await app.stop()
            except:pass
            RJ.Log(int(11111),f'Natural Account : {e}')
        finally:
            try:await app.stop()
            except:pass
            
    sleep(randint(40000,130000))
    await Natural_Activities(database)


#----------------------------------------
async def Delete_Files():                                                          
    dir=Config.Sessions                                                                   
    for f in listdir(Config.Sessions):                                                
        remove(path.join(dir, f))                                                         
    await sleep(87000)
    await Delete_Files()
#----------------------------------------
def StartNatural(Db):
    async def start(Database):
        await Natural_Activities(Database)
    asyncio.run(start(Db))
    
def StartDeleting():
    async def start():
        await Delete_Files()
    asyncio.run(start())
    
def StartProxy():
    async def start():
        await pr.proxy_getter()
    asyncio.run(start())
#----------------------------------------

#----------------------------------------------------------------------------------------------------------------| Inheriting from Client(pyrogram)
class Advertising(Client):                                                                                     #-|
    def __init__(self):                                                                                        #-|
        #---------------------------------------------------| Threading Functions in SCADULE                   #-|
        Thread=threading.Thread(target=StartProxy)   #-|                                                  #-|
        Thread.start()                                    #-|                                                  #-|
        Thread=threading.Thread(target=StartDeleting) #-|                                                  #-|
        Thread.start()                                    #-|                                                  #-|  
        Thread=threading.Thread(target=StartNatural,args=[DataBase]) #-|                                       #-|
        Thread.start()                                    #-|                                                  #-|
        #---------------------------------------------------|                                                  #-|
        super().__init__(                                                                                      #-|
            ":memory:",                                                                                        #-|
            plugins=dict(root=r'plugins'),                                                                     #-|
            api_id=API_ID,                                                                                     #-|
            api_hash=API_HASH,                                                                                 #-|
            bot_token=BOT_TOKEN,                                                                               #-|
            sleep_threshold=60,                                                                                #-|
            parse_mode=ParseMode.MARKDOWN,                                                                     #-|
            workers=80,                                                                                        #-|
            in_memory=True)                                                                                    #-|
#----------------------------------------------------------------------------------------------------------------| Add Cancel text recognize to ask(pyromood) Method
    async def Ask(self, chat_id, text, filters=None, timeout=None,Msg=None, *args, **kwargs):                  #-|
        x=await self.ask( chat_id, text, filters, timeout , *args, **kwargs)                                   #-|
        if x.text==TEXTS.Cancel_btn:                                                                           #-|
            await Msg.reply_text(TEXTS.Cancel,reply_markup=BUTTONS.Start)                                      #-|
            raise ConnectionRefusedError                                                                       #-|
        else :                                                                                                 #-|
            return x                                                                                           #-|
#----------------------------------------------------------------------------------------------------------------| Proxies from "api.proxyscrape.com" ➝ Proxy.py
    @property                                                                                                  #-|
    def Get_Proxy(self):                                                                                       #-|
        return pr.get_proxy()                                                                                  #-|
#----------------------------------------------------------------------------------------------------------------|