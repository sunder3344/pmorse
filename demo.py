'''
Created on 2018年3月16日

@author: b
'''
from pmorse import Pmorse

if __name__ == '__main__':
    pmorse = Pmorse.Pmorse()
    print(pmorse.encrypt("孙智东"))
    str = pmorse.decrypt('-..-./..-/...../-.../...../----./-..-./..-/-..../-..../--.../.-/-..-./..-/....-/./.----/-.-.')
#     print(str)
    print(pmorse.strDecode(str))
    