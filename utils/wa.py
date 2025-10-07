import json
import requests
from requests import Response
from django.conf import settings

albinaa_phone = settings.SENDER_ALBINAA_PHONE
token = settings.WABLAS_TOKEN

def send_message_individual(phone="085701570100", message=""):
    message = f'''*[NOTIFIKASI]*
{message}.

_Ini adalah pesan otomatis, jangan dibalas._'''
    url = f"https://jogja.wablas.com/api/send-message?phone={phone}&message={message}&token={token}"
    try:
        data = requests.get(url, timeout=5)
        return data
    except:
        return None
    
    
def send_message_individual_from_albinaa(phone="085701570100", message=""):
    message = f'''*[NOTIFIKASI]*
{message}.

_Ini adalah pesan otomatis, jangan dibalas._'''
    url = f"https://albinaa.sch.id/wp-content/wa/api.php?sender={albinaa_phone}&no=62{phone[1:] if phone.startswith('08') and phone != '0' else phone}&pesan={message}"
    try:
        data = requests.get(url, timeout=5)
        return data
    except:
        return send_message_individual(phone, message)


def send_message_group(group_phone="085701570100", message=""):
    url_wablas = "https://jogja.wablas.com/api/v2/send-message"
    payload = {
        "data": [
            {
                'phone': group_phone,
                'message': f'''*[NOTIFIKASI]*
{message}.

_Ini adalah pesan otomatis, jangan dibalas._''',
                'isGroup': 'true',
            },
        ]
    }

    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    try:
        data = requests.post(url_wablas, headers=headers, data=json.dumps(payload), verify=False, timeout=5)
        return data
    except:
        return None