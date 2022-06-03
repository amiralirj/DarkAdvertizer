from Classes import UserClass , NumberClass
from os import remove , listdir , path 
from pyrogram import Client , filters
from pyrogram.enums import ParseMode
from random import choice , randint
from Data.DataBase import DataBase
from datetime import datetime
from pyromod import listen
from Config import (API_ID,
           OWNER_USERNAME,
               API_HASH,
             BOT_TOKEN,
               OWNER,
             TEXTS,
          BUTTONS)
import Proxy as pr
import threading
import Config

#------------------------------------| This will make Sessions folder
from os import makedirs            #-|
makedirs('Sessions',exist_ok=True) #-|
del makedirs                       #-|
#------------------------------------|
#----------------------------------------------------------------------------------------------------------------| Inheriting from Client(pyrogram)
class Advertising(Client):                                                                                     #-|
    def __init__(self):                                                                                        #-|
        #---------------------------------------------------| Threading Functions in SCADULE                   #-|
        Thread=threading.Thread(target=pr.proxy_getter)   #-|                                                  #-|
        Thread.start()                                    #-|                                                  #-|
        Thread=threading.Thread(target=self.Delete_Files) #-|                                                  #-|
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
            workers=80,
            in_memory=True)                                                                                        #-|
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
    def Delete_Files(self):                                                                                    #-|
        dir=Config.Sessions                                                                                    #-|
        for f in listdir(Config.Sessions):                                                                     #-|
            remove(path.join(dir, f))                                                                          #-|
            threading.Timer(84600,self.Delete_Files).start()                                                   #-|
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
            await Func(Cli,message,UserClass.User(User_id))                                                    #-|
        return Wrapper                                                                                         #-|
                                                                                                               #-|
    def Coin_Limit(self,Func):                                                                                 #-| <Membership Decorator>
        async def Wrapper(Cli,message,User):                                                                   #-|
            if User.Coin > 0 :                                                                                 #-|
                await Func(Cli,message,User)                                                                   #-|
            else:await message.reply_text(TEXTS.Buy_Coin,reply_markup=BUTTONS.Support(self.Owner_Username))    #-|
        return Wrapper                                                                                         #-|
#----------------------------------------------------------------------------------------------------------------| Errors & Logs Recording Method  
    def Log(self,Userid,message=None):                                                                         #-|
        with open('Logs.txt','a+',encoding='utf-8') as f :                                                     #-|
            f.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M")} - {Userid} → {message} \n \n ' )             #-|
#----------------------------------------------------------------------------------------------------------------|
#---------------------------------------------------------------------------------------------------------------------\
#--------------------------------------------------------------------------------------------------------------------------| Account Spliting 
    def Account(self,Nums:str,user) -> NumberClass.Number:                                                               #-|
        if Nums.strip()==TEXTS.All_abrvtn :                                                                              #-|
            Nums=[NumberClass.Number(i['num'],int(user)) for i in user.All_Active_Numbers ]                              #-|
        elif '+' not in Nums and '\n' not in Nums and ':' in Nums:                                                       #-|
            Index=Nums.split(':')                                                                                        #-|
            Nums=[NumberClass.Number(i['num'],int(user)) for i in user.All_Active_Numbers[int(Index[0]):int(Index[1])]]  #-|
        else:                                                                                                            #-|
            Text_list=Nums.split('\n')                                                                                   #-|
            Nums=[NumberClass.Number(i,int(user)) for i in Text_list if (NumberClass.Number(i,int(user))).is_Owner ]     #-|
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
            