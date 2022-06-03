from Data.DataBase import DataBase
from pyrogram import Client

class Number:
    DataBase=DataBase
    def __init__(self,Number:str,User_id:int) -> None:
        self.Number=int(str(Number).replace(' ', '').replace('(','').replace(')','').replace('-','').replace('_',''))
        self.__NumberBase=self.__class__.DataBase.NumberBase(User_id,self.Number,self.__class__.DataBase.con)
        self.User_id=User_id
        self.Is_Regestered = self.__NumberBase.Number_Check()
        if self.Is_Regestered : 
            detail=self.__NumberBase.Number_Details()
            self.api_id=detail[2]
            self.api_hash=detail[1]
            self.session=detail[3]
            self.active=bool(int(detail[5]))
            self.Owner=detail[4]
            self.Details={'num' : f'+{self.Number}' , 'api_id' : detail[2] , 'api_hash' : detail[1] , 'session' : detail[3] ,'id' : detail[4] }
    
    def Add_Number(self,Api_id,Api_hash,Session):
        self.__NumberBase.regester_account(Api_hash,Api_id,Session)
        
    def Change_Activity(self,active:bool):
        self.__NumberBase.Activity(active)
        
    def Transfer(self,New_owner:int):
        if self.is_Owner:
            self.__NumberBase.Transfer(New_owner)
        
    @property
    def is_Owner(self):
        return self.__NumberBase.Account_Verify()
    
    @property
    def Activity_Emoji(self):
        if self.active:return '🟢'
        else:return '🔴'
    
    def Delete(self):
        if self.is_Owner:
            self.__NumberBase.Delete_Number()
    
    def __str__(self) -> str:
        return f'+{int(self.Number)}'
    
    def __int__(self):
        return int(self.Number)
        
    def __dict__(self):
        return self.Details
        
    async def Start(self):
        app=Client(name=f'S{self.Number}S',session_string  =self.session,api_id=self.api_id , api_hash=self.api_hash , sleep_threshold=5 , in_memory=True)
        await app.start()
        return app