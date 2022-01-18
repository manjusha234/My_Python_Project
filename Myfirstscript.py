from netmiko import ConnectHandler

dict123 ={
"device_type" : "cisco_ios",
"ip":"167.148.63.222",
"username": "admmanjub5@kbslp.com",
"password": "Sairam10203$"
}
ssh123 = ConnectHandler(**dict123)
b=["show switch","show ip int br", " show clock"]
for abc in b:
    out123 = ssh123.send_command(abc)
    print(out123)

