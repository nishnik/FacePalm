from splinter import Browser

# Your ID Password
user_email = "nishnik"
user_pass = "pass"
browser= Browser('firefox')
browser.visit('http://www.facebook.com')

browser.fill('email', user_email)
browser.fill('pass', user_pass)

button = browser.find_by_id('loginbutton')
button.click()

# Paste the url you need to download from
browser.visit('https://m.facebook.com/photo.php?fbid=780845462017409&id=100002758879147&set=oa.876940942416747&relevant_count=1&source=48&refid=18&_ft_=qid.6274517251577062760%3Amf_story_key.876940939083414%3Atl_objid.876940939083414')
# The number of consecutive pics you have to download
NUM_PICS = 56

i = 0
while i < NUM_PICS:
    i = i + 1
    browser.click_link_by_text('View full size')
    browser.screenshot("screenshot" + str(i) + ".png")
    browser.back()
    browser.click_link_by_text('Next')

browser.quit()
