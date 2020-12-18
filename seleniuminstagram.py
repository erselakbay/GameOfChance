from selenium import webdriver
import time
import sys
import random
import datetime

instagramUsername = sys.argv[1]
instagramPassword = sys.argv[2]
instagramUrl = sys.argv[3]
instagramComment = sys.argv[4]
instagramMinComment = sys.argv[5]

print ("\nBY ERSEL AKBAY\n")

print ("\ninstagramUsername %s" % (instagramUsername))
print ("instagramPassword %s" % (instagramPassword))
print ("instagramUrl %s" % (instagramUrl))
print ("instagramComment %s" % (instagramComment))
print ("instagramMinComment %s" % (instagramMinComment))

gondericounter = 1

browser = webdriver.Chrome()
browser.get(instagramUrl)
time.sleep(0.2)
girisyap = browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button")
girisyap.click()
time.sleep(1.5)
username = browser.find_element_by_name("username")
username.send_keys(instagramUsername)
time.sleep(0.01)
password = browser.find_element_by_name("password")
password.send_keys(instagramPassword)
girissyap = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div")
girissyap.click()
time.sleep(5)
simdidegil = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
simdidegil.click()
time.sleep(1)
while True:

    print('\n' , gondericounter , '. Gonderim Baslatiliyor...\n')
    commentArea = browser.find_element_by_class_name('Ypffh')
    commentArea.click()
    commentArea = browser.find_element_by_class_name('Ypffh')
    
    randomInstagramComment = str()
    commentList = instagramComment.split(' ')
    
    length = len(commentList)

    mincom = random.randint (int(instagramMinComment),length)

    while (mincom > 0):
        randomName = random.choice(commentList)
        randomInstagramComment += randomName + ' '
        commentList.remove(randomName)
        mincom -= 1

    #index kullanarak
    #while (mincom > 0):
    #    num = random.randint(0, length - 1) 
    #    randomInstagramComment += commentList[num] + ' '  
    #    del commentList[num]   
    #    mincom -= 1    

    commentArea.send_keys(randomInstagramComment)
    paylas = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[1]/article/div[3]/section[3]/div/form/button")
    paylas.click()
    print ('gonderilen yorum: ' , randomInstagramComment)
    wait = random.randint (480,1200) #480,1200 
    print (str(datetime.timedelta(seconds=wait)) , " sonra yeni yorum yapılacak\n" )
    time.sleep(wait)
    browser.get(instagramUrl)
    gondericounter += 1

