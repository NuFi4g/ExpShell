#!/usr/bin/env python3
# coding=utf-8

# ******************************************************************
# @Time    :   2020/06/01 10:08:21
# @Author  :   NuFi4g
# @File    :   md5.py
# @Version :   1.0
# @Desc    :   已知密文，爆破被截断的明文
# ******************************************************************

from hashlib import sha256
from hashlib import md5

s_dic = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"


# ******************************************************************
# Created by NuFi4g
# Desc : 爆破进度条刷新
# ******************************************************************
def progress_bar(mesg):
    print(mesg, end="", flush=True)


# ******************************************************************
# Created by NuFi4g
# Desc : 输出格式化显示
# ******************************************************************
def print_f(mesg, type):
    if type == "title":
        print(mesg.center(66, "*"))
    elif type == "flag":
        flag_style = "\n\033[36m>>>FLAG: {}\033[0m\n"
        print(flag_style.format(mesg))
    else:
        base_style = "\033[31m>>>Hit: {}\033[0m"
        print(base_style.format(mesg))


# ******************************************************************
# Created by NuFi4g
# Desc : SHA_256
# ******************************************************************
def burp_sha256(salt_str, hash_str):
    ans = ""
    for a in s_dic:
        for b in s_dic:
            for c in s_dic:
                for d in s_dic:
                    ans = a + b + c + d
                    code = ans + salt_str
                    code_sha256 = sha256(code.encode('utf-8')).hexdigest()
                    if code_sha256 == hash_str:
                        print("\n" + code + " : " + code_sha256)
                        return ans
        progress_bar(a)
    return ans


# ******************************************************************
# Created by NuFi4g
# Desc : MD5(这里密文截取6位)
# ******************************************************************
def burp_md5(salt_str, hash_str):
    ans = ""
    for a in s_dic:
        for b in s_dic:
            for c in s_dic:
                for d in s_dic:
                    ans = a + b + c + d
                    code = ans + salt_str
                    code_md5 = md5(code.encode('utf-8')).hexdigest()
                    if code_md5[:6] == hash_str:
                        print("\n" + code + " : " + code_md5)
                        return ans
        progress_bar(a)
    return ans


# ******************************************************************
# Created by NuFi4g
# Desc : 执行流程
# ******************************************************************
def main_handle(decode_type, salt_str, hash_str):
    print_f(mesg=" Burp Code (%s) " % (decode_type), type="title")
    print("SALT: " + salt_str)
    print("HASH: " + hash_str + "\n")
    if decode_type == "sha256":
        ans = burp_sha256(salt_str, hash_str)
    elif decode_type == "md5":
        ans = burp_md5(salt_str, hash_str)
    else:
        print("Please set the decode type")
    print_f(mesg=ans, type="flag")


# ******************************************************************
# Created by NuFi4g
# Desc : 程序入口
# ******************************************************************
if __name__ == "__main__":
    decode_type = "sha256"
    salt_str = "cCJIEBWurlO8mdJd"
    hash_str = "0f3a9c1dd96bba733819e2ea0328bd5851ae33690b5912bc56284167f3a563e5"
    main_handle(decode_type, salt_str, hash_str)

    decode_type = "md5"
    salt_str = "TSw8BK8m"
    hash_str = "d3b6da"
    main_handle(decode_type, salt_str, hash_str)
