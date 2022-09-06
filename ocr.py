from aip import AipOcr

def get_file_content(filePath):
      with open(filePath, "rb") as fp:
         return fp.read()



""" 你的 APPID AK SK """
APP_ID = '22988699'
API_KEY = 'BSHTSRb6nW22qv3BIiI349Gt'
SECRET_KEY = 'u8vgOVqsPXK9cToNpSyQNBU0dcNtnRYK'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

image = get_file_content('C:\\Users\\Administrator\\Documents\\BaiduNetdiskWorkspace\\20220830\\1661867160055.png')

options = {}
# options["language_type"] = "CHN_ENG"
# options["detect_direction"] = "true"
# options["detect_language"] = "true"
# options["probability"] = "true"
res_image = client.basicGeneral(image, options)
print(res_image)

for text in res_image["words_result"]:
	print(text["words"])