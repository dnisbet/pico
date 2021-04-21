

#import RPi.GPIO as GPIO, imaplib, time
import os, sys
from O365 import Account

DEBUG = 1

USERNAME = "daniel.nisbet@jisc.ac.uk"     # just the part before the @ sign, add yours here (depending on your host)


secret = '7-A.-N6H4.RSUg4GxgoPF5JWgQk55H7QQe'
refresh = '0.AQUATTn5SBSKJ02CpvNfEjYSBS75vJ2u06xFp_W48x6hZZsFAAk.AgABAAAAAAD--DLA3VO7QrddgJg7WevrAQDs_wQA9P-xY4U96-SBIkOi45qd4werP3UDK0mFMhaU5MJGwXTOlwHH3EPmcIGkHFIVXPjz1rHpgc55kJ-DJrJ_vyHlDtrU0bMhbo4c_R25We_odaLd_Dp788gBz--8a72yVUMtrLOniv1dAgclHrGKtezgCTCNYvBntzi3mQC7nDr8UxDeQybzzuupL8Mo-7EhCxbNjdj-O7GNL8ot0vstuPX-gQTGwPvkexiDAjN1ApG9_ROCl-FMYXKSVodlalOZKuOuSzHi-tGoM_1EYoO2aS28rSuBpGAoS-7i9_4WKQxLssIlsKlPIlM6x5VoAn2NU_NGtWw3EFCkN5xNsHiEB2cL1GYtn3ABvSb1KroLMHs5rLv1e2tqnq1D4YjYWDbg3t_Ls3G2fV0BSWCbLjFTdJ3KaVoYIsfFfi5ejkuaWdkBPErdAdkksZM676eO7PQABRH5Xstsdtf7k7p9zFyGVBtzwhmvdpIbfyvuRs0HcwkEpAjYZxy7nAdV1mBYx8SEOO9SJlHeQzJcxtYFkYkYsR73nI-sJKA-wUMGvoPSOzho7je0YaC6okoeP6nuJ-Cs6hsBoR6ZJKDlATWsihmN7A0u93e8nQuhPpZ85JzZoSfDl84XMeAscJZQAcUGGpggv9gxR86eJp9ATLKCceY4pRaru05gkcG7Ok9nWQUrUuFXV5tj3j1aHwSrSHlPvCxUstURAyLh3uebf5bpiVhdgGMrMtxf6NozEOPmj1g6B06uiW68KqyQm5_-1o-pkFVYhGKeYFNstTLOFo3I-fSKN1YGp0oLsDDyydlOXgr0uAhjmoE-xgX4ICV2UYdNi3cqCLlB6Fi-N96-MAb9KVPWQwff7oJt6mKWkgJfm4oYkh_xRqADBAZMw7qRsgOQTaGr8i5xyKmfuX3VMLL0qDEhBKZ3OIi4_CB-7w5LmdG6MTumEp8nmQd1zvAtsF8-A7fWpXUHAkA_ijC6PphmEKnKD8iBxoiPxmyuDAmYcM4JWeUPfHHOolPP0uOyaulzpCpKZ9DUPt5sbghkGp-sJXLLGfzqO1iLhejmP2ZyI_uNFfUcFq3aOBB8s-s5OQ_SgTbikg-CW-Yt'
client_id= '9dbcf92e-d3ae-45ac-a7f5-b8f31ea1659b'

graph_query = 'https://graph.microsoft.com/v1.0/me/mailFolders/Inbox/messages?$filter=isRead eq false'



credentials = ('client_id', 'secret')
scopes = ['https://graph.microsoft.com/Mail.ReadWrite']

account = Account(credentials) #Login

mailbox = account.mailbox() #access mailbox

inbox = mailbox.inbox_folder() #access inbox folder

query = mailbox.new_query().on_attribute('isRead').equals(False) #get unread messages

