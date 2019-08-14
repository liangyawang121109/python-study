from urllib3.contrib import pyopenssl as reqs
import idna
from datetime import datetime
import sys

def sslmon():
    x509 = reqs.OpenSSL.crypto.load_certificate(reqs.OpenSSL.crypto.FILETYPE_PEM, reqs.ssl.get_server_certificate(('www.qixiangjinrong.com',443)))

    x509.get_notAfter()

    notafter = datetime.strptime(x509.get_notAfter().decode()[0:-1],'%Y%m%d%H%M%S')
    notabefore = datetime.strptime(x509.get_notBefore().decode()[0:-1], '%Y%m%d%H%M%S')
    print('有效期至：%s'%notafter)
    print('颁发日期：%s'%notabefore)
    print('当前北京时间：%s'%datetime.now())
    remain = notafter - datetime.now()

    print(remain.days)

sslmon()
"""
print(reqs.get_subj_alt_name(x509))
fenge()
print(x509.get_issuer())
fenge()
print(x509.get_notBefore())
fenge()
print(x509.get_pubkey())
fenge()
print(x509.get_serial_number())
fenge()
print(x509.get_signature_algorithm())
fenge()
print(x509.get_subject())
fenge()
print(x509.get_version())
fenge()
art = x509.gmtime_adj_notBefore()
print(art)
fenge()
print(x509.has_expired())
fenge()
#print(x509.set_issuer())
#print(x509.set_notAfter())
#print(x509.set_notBefore())

"""