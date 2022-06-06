'''برای دریافت این فایل به صورت رایگان به پیوی 
@amiralirj_g 
مراجعه کنید ! 

ربات بدون این فایل هم به کار خود ادامه میدهد !'''

import logging


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
LOGGER = logging.getLogger(__name__)


def parse_to_meaning_ful_text(input_phone_number, in_dict):
    raise ConnectionRefusedError


def extract_code_imn_ges(ptb_message):
    raise ConnectionAbortedError

def get_phno_imn_ges(ptb_message):
    raise ConnectionAbortedError


def compareFiles(first, second):
    raise ConnectionAbortedError
def Write(Text):
    with open('APIs.txt','a+') as f :
        f.write(f'{Text}\n')
        
def Font(number):
    number=str(number)
    num={'0':'⁰','1':'¹','2':'²','3':'³','4':'⁴','5':'⁵','6':'⁶','7':'⁷','8':'⁸','9':'⁹'}
    for i in num:
        if i in number:
            number=number.replace(i,num[i])
    return number
