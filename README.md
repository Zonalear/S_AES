# 作业2：S-AES算法实现

**1 作业任务：**

根据"信息安全导论"课程第8-9次课讲述的AES算法，在课外认真阅读教科书附录D的内容，学习了解S-AES算法，并使用你们自己最擅长的程序语言(C++/QT或Java+Swing、Python+QT等)来编程实现加、解密程序。

二人一组，共同完成。

**2 算法标准设定：**

参考教科书《密码编码学于网络安全—原理与实践(第8版)》，附录D：简化AES。请同学们认真阅读。

**3 编程和测试要求**

**3.1 第1关：基本测试**

根据S-AES算法编写和调试程序，提供GUI解密支持用户交互。输入可以是16bit的数据和16bit的密钥，输出是16bit的密文。

**3.2 第2关：交叉测试**

考虑到是"**算法标准"**，所有人在编写程序的时候需要使用相同算法流程和转换单元(替换盒、列混淆矩阵等)，以保证算法和程序在异构的系统或平台上都可以正常运行。

设有A和B两组位同学(选择相同的密钥K)；则A、B组同学编写的程序对明文P进行加密得到相同的密文C；或者B组同学接收到A组程序加密的密文C，使用B组程序进行解密可得到与A相同的P。

**3.3 第3关：扩展功能**

考虑到向实用性扩展，加密算法的数据输入可以是ASII编码字符串(分组为2 Bytes)，对应地输出也可以是ACII字符串(很可能是乱码)。

**3.4 第4关：多重加密**

3.4.1 双重加密

将S-AES算法通过双重加密进行扩展，分组长度仍然是16 bits，但密钥长度为32 bits。

3.4.2 中间相遇攻击

假设你找到了使用相同密钥的明、密文对(一个或多个)，请尝试使用中间相遇攻击的方法找到正确的密钥Key(K1+K2)。

3.4.3 三重加密

将S-AES算法通过三重加密进行扩展，下面两种模式选择一种完成：

(1)按照32 bits密钥Key(K1+K2)的模式进行三重加密解密，

(2)使用48bits(K1+K2+K3)的模式进行三重加解密。

**3.5 第5关：工作模式**

基于S-AES算法，使用密码分组链(CBC)模式对较长的明文消息进行加密。注意初始向量(16 bits) 的生成，并需要加解密双方共享。

在CBC模式下进行加密，并尝试对密文分组进行替换或修改，然后进行解密，请对比篡改密文前后的解密结果。

## 测试结果

### 第一关：基本测试

**代码编写**

主要代码主体如下（详情见main_function.py）：

```python
# 实现加密
def Encrypt(plain_text, key):
    # 密钥扩展
    expanded_key = KeyExpansion(key)
    # 密钥加
    cipher_text = AddRoundKey(plain_text, expanded_key[0])
    # 轮函数
    cipher_text = SubNib(cipher_text)
    cipher_text = ShiftRows(cipher_text)
    cipher_text = MixColumns(cipher_text)
    # 密钥加
    cipher_text = AddRoundKey(cipher_text, expanded_key[1])
    # 轮函数
    cipher_text = SubNib(cipher_text)
    cipher_text = ShiftRows(cipher_text)
    # 密钥加
    cipher_text = AddRoundKey(cipher_text, expanded_key[2])
    return cipher_text

# 实现解密
def Decrypt(cipher_text, key):
    # 密钥扩展
    expanded_key = KeyExpansion(key)
    # 密钥加
    plain_text = AddRoundKey(cipher_text, expanded_key[2])
    # 轮函数
    plain_text = ShiftRows(plain_text)
    plain_text = InvSubNib(plain_text)
    # 密钥加
    plain_text = AddRoundKey(plain_text, expanded_key[1])
    plain_text = InvMixColumns(plain_text)
    # 轮函数
    plain_text = ShiftRows(plain_text)
    plain_text = InvSubNib(plain_text)
    # 密钥加
    plain_text = AddRoundKey(plain_text, expanded_key[0])
    return plain_text
```

**UI界面**

通过筛选，我们选择使用简单轻便的tkinter作为UI显示交互的框架。具体交互界面如下图所示（代码实现见UI.py）

![image1](https://github.com/Zonalear/S_AES/assets/100207608/b9edc24f-d5dd-4f8e-8066-4ef8750565c5)


我们用 明文= 0110111101101011 ；密钥= 1010011100111011 进行加密

![image2](https://github.com/Zonalear/S_AES/assets/100207608/77b438cc-bdee-422c-8901-16d2e96c5a3e)


得到密文= 0000011100111000，反之进行解密同样可得到明文。

![image3](https://github.com/Zonalear/S_AES/assets/100207608/878cc8e1-8c68-461b-96ee-fdbc5a9e7933)

### 第二关：交叉测试

已与其他队进行同密钥和明文测试（与第一关相同），两边具有相同加密后的密文。

![image4](https://github.com/Zonalear/S_AES/assets/100207608/b73ff969-aac6-4bb2-b7a5-6e7b632db937)

![image5](https://github.com/Zonalear/S_AES/assets/100207608/ff58eb34-3175-4322-92b9-845a1ad09663)

### 第三关：多重加密

当前要求以ASII编码字符串(分组为2 Bytes)，对应地输出也可以是ACII字符串(很可能是乱码)。

我们以明文= 12345678， 密文= 1010011100111011，进行加密（加密代码见extend_function.py），UI界面如下

![image6](https://github.com/Zonalear/S_AES/assets/100207608/84890b3e-0c3b-4b56-ac74-2dd9dda9b111)


### 第四关：多重加密

实现代码见 multi_encrypt.py文件

#### 4.1 双重加密 

**代码实现**

```python
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
```

**测试效果**

```txt
测试双重加密解密
明文： 0110111101101011
密钥1： 0000000000000000
密钥2： 1010011100111011

加密密文： 0010100001100100
解密明文： 0110111101101011
双重加密解密成功
```

#### 4.2 中间相遇攻击

已知的明密文对如下

```
known_plain_text_list = ['0110111101101011', '1010011101001001', ]
known_cipher_text_list = ['0010100001100100', '1001011111010110', ]
```

中间相遇攻击代码测试如下

```python
def test_attack():
    print("测试中间相遇攻击")
    found_key_list = middle_meet_attack(
        known_plain_text_list, known_cipher_text_list)
    if found_key_list:
        print("所有密钥对：", found_key_list)
    else:
        print("未找到密钥对")


# 运行结果如下：
"""
测试中间相遇攻击
找到密钥对： 0000000000000000 1010011100111011
"""
```



#### 4.3 三重加密

我们选择模式(1)按照32 bits密钥Key(K1+K2)的模式进行三重加密解密，

实现代码主体如下

```python
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
```

进行加解密测试如下

```
明文： 0110111101101011
密钥1： 0000000000000000
密钥2： 1010011100111011

加密密文： 0000111110110100
解密明文： 0110111101101011
三重加密解密成功
```



### 第五关：工作模式

主体代码见 operating_mode.py文件

```python
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
```

运行结果如下

```
测试密码分组链模式加密解密
请输入明文：01101111011010111010011101001001
请输入密钥：1010011100111011
加密密文： 01011100011000010111000011101010
解密明文： 01101111011010111010011101001001
密码分组链模式加密解密成功
```

