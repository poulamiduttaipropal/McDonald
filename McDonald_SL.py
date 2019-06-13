from selenium import webdriver
from time import sleep
import json
import traceback
from selenium.webdriver.firefox.options import Options
import googlemaps
from datetime import datetime
import urllib.request


options = Options()
options.headless = True


profile = webdriver.FirefoxProfile()
profile.set_preference('permissions.default.stylesheet', 2) 
profile.set_preference('permissions.default.image', False)
profile.set_preference("javascript.enabled", True)
gmaps_key=googlemaps.Client(key = "")

#now = datetime.now()
#timestamp = datetime.timestamp(now)

n=1
while(n!=35):
	
	sleep(2)
	browser = webdriver.Firefox(options=options, executable_path = '/home/ubuntu/geckodriver')
	url='https://www.google.co.in/search?client=ubuntu&hs=mLl&q=mcdonald%27s+address+in+switzerland+list&npsic=0&rflfq=1&rlha=0&rllag=47121267,7948323,55672&tbm=lcl&ved=2ahUKEwjd6MCrqObiAhUI63MBHbROBpQQjGp6BAgKEC4&tbs=lrf:!2m1!1e3!3sIAE,lf:1,lf_ui:4&rldoc=1#rlfi=hd:;si:;mv:!1m2!1d47.650059399999996!2d9.7146488!2m2!1d45.9308347!2d5.942033599999999!3m12!1m3!1d834080.1028709799!2d7.8283412000000006!3d46.790447050000004!2m3!1f0!2f0!3f0!3m2!1i344!2i229!4f13.1;tbs:lrf:!2m1!1e3!3sIAE,lf:1,lf_ui:4'
	browser.get(url)
	num=0
	for x in range(1, 11):
		try:
			now = datetime.now()
			timestamp = datetime.timestamp(now)
			sleep(2)
			title=browser.find_elements_by_xpath('//*[@id="rl_ist0"]/div[1]/div[4]/div[" + str(x) + "]/div/div[2]/div/a[1]/div/div/div')
			address=browser.find_elements_by_xpath('//*[@id="rl_ist0"]/div[1]/div[4]/div[" + str(x) + "]/div/div[2]/div/a[1]/div/span/div[1]/span')
			phone_no=browser.find_elements_by_xpath('//*[@id="rl_ist0"]/div[1]/div[4]/div[" + str(x) + "]/div/div[2]/div/a[1]/div/span/div[2]/span')
			country="Switzerland"
			t=title[num].text
			a=address[num].text
			p=phone_no[text].text
			def download_image_four(url,path):
					#now = datetime.now()
					#timestamp = datetime.timestamp(now)
					fullname = path + str(timestamp) + ".png"
					urllib.request.urlretrieve(url,fullname)
			img="https://mcdonald.s3.eu-central-1.amazonaws.com/mcdonaldsl/"+ str(timestamp) + ".png"
				
			download_image_four("https://seeklogo.com/images/M/mcdonalds-green-logo-78D1E0747C-seeklogo.com.png","mcdonaldsl/")

			map_address=t + "," + a
			geocode_result=gmaps_key.geocode(map_address)
			lat=geocode_result[0]["geometry"]["location"]["lat"]
			lon=geocode_result[0]["geometry"]["location"]["lng"]
			dict={"address":a,"country":country,"phone_no.":phone_no,"property_image":[img],"title":t,"latitude":lat,"longitude":lon}
			print(dict)
			with open('/home/ubuntu/AH_One/McDonald_SL_data.json', 'a') as file:
				file.write(json.dumps(dict))
			num=num+1
			sleep(2)
			print(num)
		except:
			print (traceback.format_exc())
	