import pyotp
from time import sleep
import time


# 這是一個for 取得及時對應OTP金鑰的程序
# OTP 更新頻率為：每分0秒 / 每分30秒
# 首先 程序會output 一次 當下金鑰
# 接著程序會判斷秒數為 0 執行x, 秒數為30 則執行 y
# 參考連結：https://pyauth.github.io/pyotp/

# return OTP
def OTP(secretKey):
    totp = pyotp.TOTP(secretKey)               # 取得現在的金鑰
    timeNow = time.localtime(time.time())      # 返回時間元組
    print(f'{timeNow[3]}:{timeNow[4]}:{timeNow[5]} {totp.now()}')


if __name__ == '__main__':
    secretKey = "input your OTP".replace(" ", "")  # input your 32位元 金鑰
    OTP(secretKey)
    while True:
        timeNow = time.localtime(time.time())  # 返回時間元組
        if timeNow[5] == 0:                    # if second == 0
            OTP(secretKey)
            sleep(30)
            if timeNow[5] == 30:
                OTP(secretKey)
                sleep(30)
        elif timeNow[5] == 30:                 # elif second == 30
            OTP(secretKey)
            sleep(30)
            if timeNow[5] == 0:
                OTP(secretKey)
                sleep(30)
