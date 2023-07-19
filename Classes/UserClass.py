from Data.DataBase import DataBase
from random import choice

class User:
    DataBase=DataBase
    def __init__(self,User_id:int) -> None:
        self.User_id = User_id
        self.__UserBase=self.__class__.DataBase.UserBase(User_id,self.__class__.DataBase.con)
        self.__UserBase.Add_User()
        self.Coin = self.__UserBase.User_Coin
        #User_Details=self.__UserBase.Show_User_All_Features()
        self.Auto_bio = self.__UserBase.Show_Auto_Bio #User_Details['Auto_bio']
        self.Auto_pic = self.__UserBase.Show_Auto_profile #User_Details['Auto_profile']
        self.__Banners = self.__UserBase.Show_Banners #User_Details['Banners']
        self.AutoName = self.__UserBase.Show_Auto_Name    #User_Details['Auto_name']
        self.A_Speed = float(self.__UserBase.Show_A_Speed)   #User_Details['Attack_speed']
        self.R_Speed = float(self.__UserBase.Show_R_Speed )  #User_Details['Round_speed']
        self.Auto_Api = int(self.__UserBase.Show_R_Speed)#User_Details['Auto_api']
        self.Membership = str(self.__UserBase.Show_Membership)
        self.Active_Membership=bool(self.__UserBase.Have_Membership)
        
    def Add_Coin(self,Amount,admin=False):
        if not admin and self.Active_Membership :return True
        self.__UserBase.addcoin(int(Amount))
        return True
    
    def Add_Sql_Membership(self,date):
        return self.__UserBase.Add_Sql_Membership((date))
    
    def Add_Membership(self,date):
        return self.__UserBase.Add_Membership(int(date))
    
    def Set_0(self):
        self.__UserBase.addcoin( (self.Coin *-1) )
        return True
    
    @property
    def Banners(self):
        if (self.__Banners):
            if self.__Banners!='0':return list(map(int,self.__Banners.split('-')))
            else:return False
        else:return False
    
    @property
    def Rand_Banner(self):
        try:
            return choice(self.Banners)
        except:return False
    def Change_A_Speed(self,Speed:int):
        Speed=abs(Speed)
        self.__UserBase.Set_Attack_Speed(Speed)
        return 'HaHa'
    
    def Change_R_Speed(self,Speed:int):
        Speed=abs(Speed)
        self.__UserBase.Set_Attack_Speed(Speed)
        return '!Im not depressed '
    
    def Change_Auto_Profile(self,Msg_ID:int):
        self.__UserBase.Set_Auto_profile(Msg_ID)
        return 'WWIII ?'
    
    def Change_Auto_BIO(self,Bio:str):
        self.__UserBase.Set_Auto_Bio(Bio)
        return '2022?'
    
    def Change_Auto_Name(self,Name:str):
        self.__UserBase.Set_Auto_Name(Name)
        return 'Vladimir Putin ?'
    
    def Add_Banner(self,Banner:int):
        self.__UserBase.Set_Banner(Banner)
        return 'A Legend ?'
    
    def Remove_Banner(Why_Self,Banner:int):
        Bnr_list=[int(i) for i in Why_Self.Banners]
        Bnr_list.remove(Banner)
        if len(Bnr_list) ==0:Why_Self.__UserBase.SQL_Add_Banner('0')
        else:Why_Self.__UserBase.SQL_Add_Banner(("-".join(map(str, Bnr_list))).strip('-'))
        return 'Or a War Criminal'
    
    #---------------------------------------------| Asarat bikarie |-------------------------------------------------------
        
    @property
    def All_numbers(self):#number,api_id,api_hash,session
        Numbers=[dict(zip(['num', 'api_id', 'api_hash', 'session','id'], i)) for i in self.__UserBase.User_Accounts]
        return  Numbers
    
    @property
    def All_Active_Numbers(self):
        Numbers=[dict(zip(['num', 'api_id', 'api_hash', 'session','id'], i)) for i in self.__UserBase.User_Active_Accounts]
        return  Numbers
    
    def Delete(self):
        self.__UserBase.Delete_All_Numbers()
        
    def __int__(self):
        return self.User_id
    
