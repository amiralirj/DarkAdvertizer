import sqlite3 as db
from tabulate import tabulate

import os
#SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) 
del os

class Data:
    def __init__(self) -> None:    
        self.con = db.connect(f"AttackBase.db" , detect_types=db.PARSE_DECLTYPES, check_same_thread = False)
        self.c=self.con.cursor()#banner INT 
        #,  INT,  INT, New INT ,  TEXT ,autopro INT,autobio TEXT
        self.c.execute('CREATE TABLE IF NOT EXISTS Users (User_id INT PRIMARY KEY, Coins INT , Latary INT )')
        self.c.execute('CREATE TABLE IF NOT EXISTS Attack (User_id INT PRIMARY KEY , Banners TEXT , Round_speed INT , Attack_speed INT , Auto_name TEXT , Auto_profile INT , Auto_bio TEXT , Auto_api INT)')
        self.c.execute('CREATE TABLE IF NOT EXISTS Accounts (number INT PRIMARY KEY , api_hash TEXT , api_id INT , session TEXT ,user_id INT, active INT )')
        self.c.execute('CREATE TABLE IF NOT EXISTS Deleted (number INT PRIMARY KEY )')
        self.c.execute('CREATE TABLE IF NOT EXISTS API_Keys (API TEXT PRIMARY KEY , App_ID INT , User_id INT )')
        self.con.commit()
        print('DataBase Has Successfully Loaded') 
    
    @property
    def All_Users(self):
        self.c.execute('SELECT User_id,Coins FROM Users')
        return {i[0]:int(i[1]) for i in (self.c.fetchall())}
    
    @property
    def All_Numbers(self):
        self.c.execute('SELECT number,api_id,api_hash,session,user_id FROM accounts')
        rows=self.c.fetchall()
        return rows
    
    @property 
    def All_Data_Text(self) -> str:
        Text='DARK ADVERTIZER -  DARK ADVERTIZER - DARK ADVERTIZER \n WWW.GITHUB.COM/AMIRALIRJ \n DARK ADVERTIZER -  DARK ADVERTIZER - DARK ADVERTIZER \n \n '
        Tabels={'Users':['User_id','Coins','Latary'],'Attack':['User_id','Banners','Round_speed','Attack_speed','Auto_name','Auto_profile','Auto_bio','Auto_api'],'Accounts':['number','api_hash','api_id','session','user_id','active']}
        for i in Tabels :
            Data=self.c.execute(f'SELECT * FROM {i}').fetchall()
            tab=tabulate(Data , Tabels[i],  tablefmt="pretty")
            Text+=f"{tab} \n \n "
            Text+='DARK ADVERTIZER -  DARK ADVERTIZER - DARK ADVERTIZER DARK ADVERTIZER -  DARK ADVERTIZER - DARK ADVERTIZER \n  WWW.GITHUB.COM/AMIRALIRJ - WWW.GITHUB.COM/AMIRALIRJ\n DARK ADVERTIZER -  DARK ADVERTIZER - DARK ADVERTIZER DARK ADVERTIZER -  DARK ADVERTIZER - DARK ADVERTIZER \n \n  '
        return Text
    
    class UserBase:
        def __init__(self,User_id:int,con) -> None:
            self.User_id=int(User_id)
            self.con=con
            self.c=self.con.cursor()
            self.dev='@Amiralirj_g'
            self.git='www.github.com\amiralirj'
        
        def Add_User(self):
            self.c.execute('INSERT OR IGNORE INTO Users (User_id,Coins,Latary) VALUES (:User_id,:Coins,:Latary)',{'User_id':self.User_id,'Coins':0,'Latary':0})
            self.c.execute('INSERT OR IGNORE INTO Attack (User_id,Banners,Round_speed,Attack_speed,Auto_name,Auto_profile,Auto_bio,Auto_api) VALUES (:User_id,:Banners,:Round_speed,:Attack_speed,:Auto_name,:Auto_profile,:Auto_bio,:Auto_api)',
                           {'User_id':self.User_id,'Banners':0,'Round_speed':1,'Attack_speed':1,'Auto_name':'None','Auto_profile':0,'Auto_bio':'None','Auto_api':1})
            self.con.commit()
            
        def addcoin(self,Amount:int):
            self.c.execute(f'UPDATE Users set Coins=Coins+{int(Amount)} WHERE User_id=:user',{'user':int(self.User_id)})
            self.con.commit()
            
        def Reduce_Coin(self,Amount:int):
            self.c.execute(f'UPDATE Users SET Coins=Coins-{int(Amount)} WHERE User_id=:user',{'user':int(self.User_id)})
            self.con.commit()
        
        @property
        def User_Coin(self):
            self.c.execute('SELECT Coins FROM Users WHERE User_id=:user_id',{'user_id':int(self.User_id)})
            return (self.c.fetchall())[0][0]
        
        #----------------------------------------------------------------------------------------------------
        def Set_Auto_API(self,Api:int):
            self.c.execute(f'UPDATE Attack SET Auto_api={int(Api)} WHERE User_id=:user',{'user':int(self.User_id)})
            self.con.commit()
            
        @property
        def Show_Auto_API(self):
            self.c.execute('SELECT Auto_api FROM Attack WHERE User_id=:user_id',{'user_id':int(self.User_id)})
            return (self.c.fetchall())[0][0]
        
        @property
        def Show_Banners(self):
            self.c.execute('SELECT Banners FROM Attack WHERE User_id=:user_id',{'user_id':int(self.User_id)})
            banners=(self.c.fetchall())[0][0]
            try:
                if int(banners)==0:return False
                else:return str(banners)
            except:return str(banners)
            
        def SQL_Add_Banner(self,Banner:str):
            self.c.execute(f'UPDATE Attack SET Banners=:bnr WHERE User_id=:user',{'user':int(self.User_id),'bnr':Banner})
            self.con.commit()
            
        def Set_Banner(self,Banner_id:int):
            USR_BNR=self.Show_Banners
            if  USR_BNR!=False:
                banner_str=str(USR_BNR) + '-' + str(Banner_id)
                self.SQL_Add_Banner(banner_str)
                return True
            else:
                self.SQL_Add_Banner(str(Banner_id))
                return True
            
        def Set_Round_Speed(self,speed:int):
            self.c.execute(f'UPDATE Attack SET Round_speed={float(speed)} WHERE User_id=:user',{'user':int(self.User_id)})
            self.con.commit()
        
        @property
        def Show_R_Speed(self):
            self.c.execute('SELECT Round_speed FROM Attack WHERE User_id=:user_id',{'user_id':int(self.User_id)})
            return (self.c.fetchall())[0][0]
        
        def Set_Attack_Speed(self,speed:int):
            self.c.execute(f'UPDATE Attack SET Attack_speed={float(speed)} WHERE User_id=:user',{'user':int(self.User_id)})
            self.con.commit()
        
        @property
        def Show_A_Speed(self):
            self.c.execute('SELECT Attack_speed FROM Attack WHERE User_id=:user_id',{'user_id':int(self.User_id)})
            return (self.c.fetchall())[0][0]
    
        def Set_Auto_Name(self,Name:str):
            self.c.execute(f'UPDATE Attack SET Auto_name=:nm WHERE User_id=:user',{'user':int(self.User_id),'nm':str(Name)})
            self.con.commit()
        
        @property
        def Show_Auto_Name(self):
            self.c.execute('SELECT Auto_name FROM Attack WHERE User_id=:user_id',{'user_id':int(self.User_id)})
            NM=(self.c.fetchall())[0][0]
            if NM=='None':
                return False
            else:
                return str(NM)
            
        def Set_Auto_Bio(self,bio:str):
            self.c.execute(f'UPDATE Attack SET Auto_bio=:bio WHERE User_id=:user',{'user':int(self.User_id),'bio':str(bio)})
            self.con.commit()
        
        @property
        def Show_Auto_Bio(self):
            self.c.execute('SELECT Auto_bio FROM Attack WHERE User_id=:user_id',{'user_id':int(self.User_id)})
            BIO=(self.c.fetchall())[0][0]
            if BIO=='None':
                return False
            else:
                return str(BIO)
            
        def Set_Auto_profile(self,speed:int):
            self.c.execute(f'UPDATE Attack SET Auto_profile={int(speed)} WHERE User_id=:user',{'user':int(self.User_id)})
            self.con.commit()
        
        @property
        def Show_Auto_profile(self):
            self.c.execute('SELECT Auto_profile FROM Attack WHERE User_id=:user_id',{'user_id':int(self.User_id)})
            PR=(self.c.fetchall())[0][0]
            if int(PR)==0:return False
            else : return int(PR)
            
        def Show_User_All_Features(self):
            self.c.execute('SELECT Banners,Round_speed,Attack_speed,Auto_name,Auto_profile,Auto_bio,Auto_api FROM Attack WHERE User_id=:user_id',{'user_id':int(self.User_id)})
            FT=(self.c.fetchall())[0]
            return {'Banners':FT[0],'Round_speed':FT[1],'Attack_speed':FT[2],'Auto_name':FT[3],'Auto_profile':FT[4],'Auto_bio':FT[5],'Auto_api':FT[6]}
        
        @property
        def User_Accounts(self):
            '''number,api_id,api_hash,session'''
            self.c.execute('SELECT number,api_id,api_hash,session,user_id FROM accounts WHERE user_id=:user_id ',{'user_id':int(self.User_id)})
            rows=self.c.fetchall()
            return rows
        
        @property
        def User_Active_Accounts(self):
            '''number,api_id,api_hash,session'''
            self.c.execute('SELECT number,api_id,api_hash,session,user_id FROM accounts WHERE user_id=:User_id AND active=1 ',{'User_id':int(self.User_id)})
            rows=self.c.fetchall()
            return rows
        
        def Delete_All_Numbers(self):
            self.c.execute('DELETE FROM accounts WHERE  user_id=:user_id',{'user_id':int(self.User_id)})
            self.con.commit()
            
        def Add_Api(self,API:str,App_ID:int):
            try:
                self.c.execute('INSERT  INTO API_Keys (API,App_ID,User_id) VALUES (:API,:App_ID,:User_id)',{'User_id':self.User_id,'App_ID':App_ID,'API':API})
                self.con.commit()
            except:return False
            
        @property
        def User_Api(self):
            self.c.execute('SELECT API,App_ID,User_id FROM accounts WHERE User_id=:user_id ',{'user_id':int(self.User_id)})
            rows=self.c.fetchall()
            return rows
    #--------------------------------------------------------------------------------------------------------------------
    class NumberBase:
        
        def __init__(self,User_id:int,Number:int,con) -> None:
            self.Number=int(Number)
            self.User_id=int(User_id)
            self.con=con
            self.c=self.con.cursor()
            self.dev='@Amiralirj_g'
            self.git='www.github.com\amiralirj'
            
        def Active_Check(self):
            self.c.execute('SELECT active FROM accounts WHERE number=:number',{'number':self.Number})
            if self.c.fetchall()[0][0]==1:
                return True
            else:
                return False
            
        def Number_Check(self):
            self.c.execute('SELECT number FROM accounts WHERE number=:number',{'number':self.Number})
            q=self.c.fetchall()
            if q==[]:
                return False
            else:
                return True
        
        def Number_Details(self):
            try:
                self.c.execute('SELECT * FROM accounts WHERE number=:number AND  user_id=:user_id ',{'number':self.Number,'user_id':int(self.User_id)})
                q=self.c.fetchall()
                return q[0]
            except:False

        def regester_account(self,api_hash,api_id,setion_str):
            self.c.execute('insert into accounts (number,api_hash,api_id,session,user_id,active) values (:number,:api_hash,:api_id,:session,:user_id,:active)',{'active':1,'number':int(self.Number),'api_hash':str(api_hash),'api_id':int(api_id),'session':str(setion_str),'user_id':int(self.User_id)})
            self.con.commit()
        

        def Delete_Number(self):
            x=self.c.execute('SELECT number FROM accounts WHERE user_id=:user_id  ',{'user_id':int(self.User_id)}).fetchall()[0]
            self.c.execute('DELETE FROM accounts WHERE number=:num AND user_id=:user_id',{'user_id':int(self.User_id),'num':int(self.Number)})
            self.con.commit()


        def Account_Verify(self):
            self.c.execute('SELECT number FROM accounts WHERE user_id=:user_id AND  number=:number' ,{'user_id':int(self.User_id),'number':int(self.Number)})
            row=self.c.fetchall()
            try:
                row[0][0]
                return True
            except:
                return False
            
        def Activity(self,Activity:bool):
            self.c.execute(f'UPDATE accounts SET active=:act WHERE number=:number' ,{'act':int(Activity),'number':int(self.Number)})
            self.con.commit()
        

        def Transfer(self,Reciver):
            num=self.c.execute('SELECT number,api_hash,api_id,session FROM accounts WHERE user_id=:user_id AND number=:num  ',{'user_id':int(self.User_id),'num':self.Number}).fetchall()[0]
            self.c.execute('DELETE FROM accounts WHERE number=:num AND user_id=:user_id',{'user_id':int(self.User_id),'num':int(self.Number)})
            try:self.Delete_Number()
            except:pass
            self.c.execute('INSERT into accounts (number,api_hash,api_id,session,user_id,active) values (:num,:api_hash,:api_id,:session,:user_id,:active)',{'active':1,'num':str(num[0]),'api_hash':str(num[1]),'api_id':int(num[2]),'session':str(num[3]),'user_id':int(Reciver)})
            self.con.commit()
            return self.Number


#----------------|لنز اعتمادو باید وارونه بزاره ادم |
DataBase=Data()#-|لنز اعتمادو باید وارونه بزاره ادم |
#----------------|لنز اعتمادو باید وارونه بزاره ادم |