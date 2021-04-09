url="http://naver.com"
my_str= url.replace("http://", "")
my_str=my_str[0:my_str.index(".")]
pw1=my_str[:3]
pw2=len(my_str)
pw3=my_str.count('e')
password=pw1+str(pw2)+str(pw3)+'!'
print("{0}의 비밀번호는 {1}입니다.".format(url,password))
