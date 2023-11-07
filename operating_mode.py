from S_AES import *

# 实现密码分组链模式，输入明文字符串，16位2进制密钥，16位2进制初始向量，输出密文字符串
def CBC_encrypt(plain_text, key, IV):
    # 将明文分组
    plain_text_list = [plain_text[i:i + 16] for i in range(0, len(plain_text), 16)]
    # 用于存储密文
    cipher_text_list = []
    # 对每个分组进行加密
    for plain_text in plain_text_list:
        # 执行加密
        cipher_text = Encrypt(XOR(plain_text, IV), key)
        # 更新初始向量
        IV = cipher_text
        # 将密文添加到密文列表
        cipher_text_list.append(cipher_text)
    # 将密文列表转换为字符串
    cipher_text = ''.join(cipher_text_list)
    return cipher_text

# 实现密码分组链模式的解密
def CBC_decrypt(cipher_text, key, IV):
    # 将密文分组
    cipher_text_list = [cipher_text[i:i + 16] for i in range(0, len(cipher_text), 16)]
    # 用于存储明文
    plain_text_list = []
    # 对每个分组进行解密
    for cipher_text in cipher_text_list:
        # 执行解密
        plain_text = XOR(Decrypt(cipher_text, key), IV)
        # 更新初始向量
        IV = cipher_text
        # 将明文添加到明文列表
        plain_text_list.append(plain_text)
    # 将明文列表转换为字符串
    plain_text = ''.join(plain_text_list)
    return plain_text

# 测试密码分组链模式加密解密
def test_CBC():
    print("测试密码分组链模式加密解密")
    # # 定义明文
    # plain_text = '01101111011010111010011101001001'
    # # 定义密钥
    # key = '1010011100111011'
    plain_text = input("请输入明文：")
    key = input("请输入密钥：")
    # 定义初始向量
    IV = '1010101010101010'
    # 加密
    cipher_text = CBC_encrypt(plain_text, key, IV)
    print("加密密文：", cipher_text)
    # 解密
    print("解密明文：", CBC_decrypt(cipher_text, key, IV))
    # 比较
    if CBC_decrypt(cipher_text, key, IV) == plain_text:
        print("密码分组链模式加密解密成功")
    else:
        print("密码分组链模式加密解密失败")

test_CBC()
