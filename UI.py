# from function import *
import tkinter as tk
from Ascii import *
from S_AES import *

window = tk.Tk()
window.title('S-AES')

# 尺寸设计
window.geometry('300x400')

# 选择模式部分
mode_frame = tk.Frame(window)
mode_frame.pack(side=tk.TOP)

# 创建一个变量来存储选择的模式，默认为'二进制'
mode_var = tk.StringVar()
mode_var.set('二进制')

# 创建两个Radiobutton来选择模式
binary_mode_button = tk.Radiobutton(mode_frame, text='二进制', variable=mode_var, value='二进制')
binary_mode_button.pack(side=tk.LEFT)
text_mode_button = tk.Radiobutton(mode_frame, text='字符', variable=mode_var, value='字符')
text_mode_button.pack(side=tk.LEFT)

# 输入部分
input_frame = tk.Frame(window)
input_frame.pack(side=tk.TOP)

# 明文(密文)输入
input_label = tk.Label(input_frame, text='明文(密文)')
input_label.grid(row=0, column=0)
input_entry = tk.Entry(input_frame)
input_entry.grid(row=0, column=1)

# 密钥输入
key_label = tk.Label(input_frame, text='密钥')
key_label.grid(row=1, column=0)
key_entry = tk.Entry(input_frame)
key_entry.grid(row=1, column=1)

# 输出部分
output_frame = tk.Frame(window)
output_frame.pack(side=tk.TOP)

# 输出标签
output_label = tk.Label(output_frame, text='输出')
output_label.pack(side=tk.LEFT)

# 输出显示
output_entry = tk.Entry(output_frame)
output_entry.pack(side=tk.LEFT)

# 加密解密按钮
button_frame = tk.Frame(window)
button_frame.pack(side=tk.TOP)

# 如果使用加密值使用encrypt函数，如果使用解密则使用decrypt函数
def encrypt_or_decrypt():
    mode = mode_var.get()  # 获取选择的模式

    if encrypt_or_decrypt_var.get() == '加密':
        output_entry.delete(0, tk.END)
        if mode == '二进制':
            output_entry.insert(0, Encrypt(input_entry.get(), key_entry.get()))
        else:
            cipher_text = ascii_encrypt(input_entry.get(), key_entry.get())
            output_entry.insert(0, cipher_text)
    else:
        output_entry.delete(0, tk.END)
        if mode == '二进制':
            output_entry.insert(0, Decrypt(input_entry.get(), key_entry.get()))
        else:
            decrypted_text = ascii_decrypt(input_entry.get(), key_entry.get())
            output_entry.insert(0, decrypted_text)

# 加密按钮和解密按钮，点击确认之后再显示结果
encrypt_or_decrypt_var = tk.StringVar()
encrypt_or_decrypt_var.set('加密')
encrypt_button = tk.Radiobutton(button_frame, text='加密', variable=encrypt_or_decrypt_var, value='加密', command=encrypt_or_decrypt)
encrypt_button.pack(side=tk.LEFT)
decrypt_button = tk.Radiobutton(button_frame, text='解密', variable=encrypt_or_decrypt_var, value='解密', command=encrypt_or_decrypt)
decrypt_button.pack(side=tk.LEFT)

# 清空按钮
clear_button = tk.Button(button_frame, text='清空', command=lambda: [input_entry.delete(0, tk.END), key_entry.delete(0, tk.END), output_entry.delete(0, tk.END)])
clear_button.pack(side=tk.LEFT)

# 退出按钮
exit_button = tk.Button(button_frame, text='退出', command=window.quit)
exit_button.pack(side=tk.LEFT)

# 运行界面
window.mainloop()

