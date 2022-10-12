from .BOT import  TEXTS , BUTTONS , Config , Advertising , RJ

#---------------------------------------------------------------------- None Decorator 

@Advertising.on_message(RJ.prv & RJ.filters.command('start') , group=0)
@RJ.Join_Channel
@RJ.User_Details
async def Start_Bot(_,message,u):
    if RJ.is_Owner(message.from_user.id):
        await message.reply_text(TEXTS.Hello_Sear,reply_markup=BUTTONS.Management)
    else:               
        await message.reply_text(TEXTS.start,reply_markup=BUTTONS.Start)

@Advertising.on_message(RJ.prv & RJ.regex('^اتک ⚠️') , group=0)
@RJ.Join_Channel
@RJ.User_Details
async def Attack_Pannel(_,message,u):
    await message.reply_text(TEXTS.Attack_Pannel,reply_markup=BUTTONS.Attack)

@Advertising.on_message(RJ.prv & RJ.regex('^اتک🔰') , group=0)
@RJ.User_Details
async def Attack_Main_Pannel(_,message,u):
    await message.reply_text(TEXTS.Attack_Main_Pannel,reply_markup=BUTTONS.Main_Attack)
    
@Advertising.on_message(RJ.prv & RJ.regex('^برگشت➡️') , group=0)
@RJ.User_Details
async def Return_Attack(_,message,u):
    await message.reply_text(TEXTS.Attack_Pannel,reply_markup=BUTTONS.Attack)

@Advertising.on_message(RJ.prv & RJ.regex('^اکانت ها👤') , group=0)
@RJ.Join_Channel
@RJ.User_Details
async def Accounts(_,message,u):
    await message.reply_text(TEXTS.Account_Pannel,reply_markup=BUTTONS.Accounts)

@Advertising.on_message(RJ.prv & RJ.regex('^برگشت 🔙') , group=0)
@RJ.User_Details
async def Return_Accounts(_,message,u):
    await message.reply_text(TEXTS.Account_Pannel,reply_markup=BUTTONS.Accounts)
    
@Advertising.on_message(RJ.prv & RJ.regex('^بازگشت 🔙') , group=0)
@RJ.User_Details
async def Return_Main(_,message,u):
    await message.reply_text(TEXTS.Main_Pannel,reply_markup=BUTTONS.Start)
    
@Advertising.on_message(RJ.prv & RJ.regex('^سین و لایک 👁️') , group=0)
@RJ.User_Details
async def Seen_Like(_,message,u):
    await message.reply_text(TEXTS.Seen_Pannel,reply_markup=BUTTONS.Seen)
    
@Advertising.on_message(RJ.prv & RJ.regex('^پشتیبانی 👨‍💻') , group=0)
@RJ.User_Details
async def Support(_,message,u):
    await message.reply_text(TEXTS.Support,reply_markup=BUTTONS.Support(RJ.Owner_Username))
    
#----------------------------------------------------------------------

@Advertising.on_message(RJ.prv & RJ.regex('^حذف اکانت 🗑') , group=0)
@RJ.User_Details
async def Numbers_Deleting(_,message,u):
    await message.reply_text(TEXTS.Deleting_Numbers,reply_markup=BUTTONS.Account_Deleting)

@Advertising.on_message(RJ.prv & RJ.regex('^⚙️ تنظیمات اکانت') , group=0)
@RJ.User_Details
async def Acc_Setting(_,message,u):
    await message.reply_text(TEXTS.Account_Setting,reply_markup=BUTTONS.Account_Setting)
    
#----------------------------------------------------------------------
@Advertising.on_message(RJ.prv & RJ.regex('^بنر 📩') , group=0)
@RJ.User_Details
async def Banner_Pannel(_,message,u):
    await message.reply_text(TEXTS.Banner_Pannel,reply_markup=BUTTONS.banner)
    

#----------------------------------------------------------------------
@Advertising.on_message(RJ.prv & RJ.regex('^اشتراک 🔋') , group=0)
@RJ.User_Details
async def Membership(bot,message,User):
    if User.Coin > 0 or User.Active_Membership :
        m=User.Membership
        if User.Membership.strip() =='2004-2-24': m = 'None'
        await message.reply_text(TEXTS.Coin_Details(User.Coin,message.from_user.mention,m),reply_markup=BUTTONS.Start)
    else :await message.reply_text(TEXTS.Coin_Lack,reply_markup=BUTTONS.Support(RJ.Owner_Username))
