from S_AES import *

# 根据S-AES实现双重加密
def double_encrypt(plain_text, key1, key2):
    cipher_text1 = Encrypt(plain_text, key1)
    cipher_text2 = Decrypt(cipher_text1, key2)
    return cipher_text2

# 实现双重解密
def double_decrypt(cipher_text, key1, key2):
    plain_text1 = Encrypt(cipher_text, key2)
    plain_text2 = Decrypt(plain_text1, key1)
    return plain_text2

def double_test():
    print("测试双重加密解密")
    plain_text = '0110111101101011'
    key1 =  '0000000000000000'
    key2 =  '1010011100111011'
    print("明文：", plain_text)
    print("密钥1：", key1)
    print("密钥2：", key2)
    cipher_text = double_encrypt(plain_text, key1, key2)
    print("加密密文：", cipher_text)
    print("解密明文：", double_decrypt(cipher_text, key1, key2))
    if double_decrypt(cipher_text, key1, key2) == plain_text:
        print("双重加密解密成功")
    else:
        print("双重加密解密失败")

# double_test()

# 生成所有可能的密钥对
def generate_all_keys():
    for i in range(2 ** 32):
        key = bin(i)[2:].zfill(32)
        yield (key[:16], key[16:])

# 实现中间相遇攻击
def middle_meet_attack(known_plain_text_list, known_cipher_text_list):
    all_keys = generate_all_keys()
    found_key_list = []
    for key1, key2 in all_keys:
        flag = True
        for known_plain_text, known_cipher_text in zip(known_plain_text_list, known_cipher_text_list):
            middle_text1 = Encrypt(known_plain_text, key1)
            middle_text2 = Encrypt(known_cipher_text, key2)
            if middle_text1 != middle_text2:
                flag = False
                break
        if flag:
            print("找到密钥对：", key1, key2)
            found_key_list.append((key1, key2))
    return found_key_list


# 已知的明文和密文对组合
known_plain_text_list = ['0110111101101011', '1010011101001001', ]
known_cipher_text_list = ['0010100001100100', '1001011111010110', ]
# 密钥 0000000000000000 1010011100111011

# 测试中间相遇攻击
def test_attack():
    print("测试中间相遇攻击")
    found_key_list = middle_meet_attack(
        known_plain_text_list, known_cipher_text_list)
    if found_key_list:
        print("所有密钥对：", found_key_list)
    else:
        print("未找到密钥对")

test_attack()

# 实现三重加密
def triple_encrypt(plain_text, key1, key2):
    cipher_text1 = Encrypt(plain_text, key1)
    cipher_text2 = Decrypt(cipher_text1, key2)
    cipher_text3 = Encrypt(cipher_text2, key1)
    return cipher_text3

# 实现三重解密
def triple_decrypt(cipher_text, key1, key2):
    plain_text1 = Decrypt(cipher_text, key1)
    plain_text2 = Encrypt(plain_text1, key2)
    plain_text3 = Decrypt(plain_text2, key1)
    return plain_text3

def triple_test():
    plain_text = '0110111101101011'
    key1 =  '0000000000000000'
    key2 =  '1010011100111011'
    print("明文：", plain_text)
    print("密钥1：", key1)
    print("密钥2：", key2)
    cipher_text = triple_encrypt(plain_text, key1, key2)
    print("加密密文：", cipher_text)
    print("解密明文：", triple_decrypt(cipher_text, key1, key2))
    if triple_decrypt(cipher_text, key1, key2) == plain_text:
        print("三重加密解密成功")
    else:
        print("三重加密解密失败")

triple_test()                                                                   