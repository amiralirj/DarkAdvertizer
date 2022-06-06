from .BOT import TEXTS , BUTTONS , Config , Number , Advertising , RJ  , User

@Advertising.on_callback_query(RJ.regex('^DeleteBNR') , group=0)
@RJ.User_Details
async def Remove_Banner(bot:Advertising,query,user:User):
    Id=str(query.data).split(' ')[-1]
    user.Remove_Banner(int(Id))
    await query.edit_message_text(TEXTS.Banner_Removed,reply_markup=BUTTONS.Attack)
    
@Advertising.on_callback_query(RJ.regex('^Change_Activity') , group=0)
@RJ.User_Details
async def Change_Activity(bot:Advertising,query,user:User):
    C,Num,Page=(query.data).split(' ')
    Num=Number(int(Num),int(user))
    if Num.active:act=False
    else:act=True
    Num.Change_Activity(act)
    Nums=[Number(i['num'],int(user)) for i in user.All_numbers ]
    await query.edit_message_text(TEXTS.Change_Activity,reply_markup=BUTTONS.Activity(Nums,int(Page)))
    
@Advertising.on_callback_query(RJ.regex('^Next') , group=0)
@RJ.User_Details
async def Next_Page(bot:Advertising,query,user:User):
    Page=int((query.data).split(' ')[-1])
    Nums=[Number(i['num'],int(user)) for i in user.All_numbers ]
    await query.edit_message_text(TEXTS.Change_Activity,reply_markup=BUTTONS.Activity(Nums,Page))
    
@Advertising.on_callback_query(RJ.regex('^Auto_Details') , group=0)
@RJ.User_Details
async def Auto_Detailing_Accs(bot:Advertising,query,user:User):
    Kind=(query.data).split(' ')[-1]
    if Kind=='Pic':Text=TEXTS.Pro_Text
    elif Kind=='Bio':Text=TEXTS.Bio_Text
    else:Text=TEXTS.Name_Text
    try:
        Message=(((await bot.ask(int(user),TEXTS.Get_Details(Text),filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=60))))
        if Message.text :
            if TEXTS.Cancel_btn in Message.text :
                await query.message.reply_text(TEXTS.Cancel,reply_markup=BUTTONS.Accounts)
                return
    except TimeoutError :
        await query.message.reply_text(TEXTS.Time_Out,reply_markup=BUTTONS.Accounts)
        return
    except:return
    
    if Kind=='Pic':
        if Message.photo:
            pic=await Message.copy(Config.Banners_Channel)
            user.Change_Auto_Profile(pic.id)
            TXT='WWW.GITHUB.COM/AMIRALIRJ'
        else:
            user.Change_Auto_Profile(0)
            TXT='None'
        
    elif Kind=='Bio':
        TXT=Message.text
        if Message.text==TEXTS.Cancel_Proccess:
            TXT='None'
        user.Change_Auto_BIO(str(TXT))
            
    else:
        TXT=Message.text
        if Message.text==TEXTS.Cancel_Proccess:
            TXT='None'
        user.Change_Auto_Name(str(TXT))
        
    if TXT=='None':await query.message.reply_text(TEXTS.Auto_Details_Deleted(Text),reply_markup=BUTTONS.Accounts)
    else:await query.message.reply_text(TEXTS.Auto_Details_Setted(Text),reply_markup=BUTTONS.Accounts)

@Advertising.on_callback_query(RJ.regex('^Attack_Setting') , group=0)
@RJ.User_Details
async def Attack_Setting_Pannel(bot:Advertising,query,user:User):
    Data=str(query.data).split(' ')[-1]
    if Data=='R': await query.edit_message_text(TEXTS.R_Speed_Setting(user.R_Speed),reply_markup=BUTTONS.Speed_Inline(Data))
    else: await query.edit_message_text(TEXTS.A_Speed_Setting(user.A_Speed),reply_markup=BUTTONS.Speed_Inline(Data))
    
@Advertising.on_callback_query(RJ.regex('^Speed-') , group=0)
@RJ.User_Details
async def Attack_Setting_Set(bot:Advertising,query,user:User):
    Data=str(query.data).split(' ')
    Kind=Data[0].split('-')[-1]
    try:speed=float((Data[-1]))
    except:speed=float((await bot.ask(int(user),TEXTS.Ask_Speed,filters=RJ.filters.user(int(user)),reply_markup=BUTTONS.Cancel,timeout=20)).text)
    if Kind=='R':user.Change_R_Speed(abs(speed))
    else:user.Change_A_Speed(abs(speed))
    await query.edit_message_text(TEXTS.Speed_Setted(speed),reply_markup=BUTTONS.Attack)
    
    