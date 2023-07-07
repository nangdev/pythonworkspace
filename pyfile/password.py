url = "http://google.com"
my_str = url.replace("http://","")
my_str =my_str[:my_str.find(".")]
#print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(f"{url}의 비밀번호는 {password} 입니다")