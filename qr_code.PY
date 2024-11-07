import qrcode

# 目标文本信息
url = "https://pass-ochre.vercel.app/" 

# 创建二维码
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.make(fit=True)

# 生成图像
img = qr.make_image(fill='black', back_color='white')

# 保存二维码图像
img.save("text_qrcode.png")
