'''学妹你好'''
import requests
input("修改login_url中的登陆地址")
login_url="http://URP_IP/loginAction.do"
Cookie="JSESSIONID="+requests.get(login_url).cookies["JSESSIONID"]
headers={
'Cookie':Cookie,
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
img_url="http://URP_IP/validateCodeAction.do"
with open("yzm.jpg","wb") as fob:
	fob.write(requests.get(img_url,headers=headers).content)
yzm=input("请查看当前目录下的验证码图片,输入验证码\n")
user=input("user?\n")
pwd=input("password?\n")
payload={'zjh1':'','tips':'','lx':'','evalue':'','eflag':'','fs':'','dzslh':'','zjh':user,'mm':pwd,'v_yzm':yzm}
print (requests.post(login_url,data=payload,headers=headers).text)
