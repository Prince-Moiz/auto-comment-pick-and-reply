import time
import random
from licensing.models import *
from licensing.methods import Key, Helpers

from playwright.sync_api import sync_playwright
import json
import pyperclip

username = "FlokiArmy2021x"
Name = "Floki Army 2021x"
RSAPubKey = "<RSAKeyValue><Modulus>1AUe++zwJxB3f1qL7/5LJbeyS37YZY7cZH3u4XcxyigTBLJsZcZBwi87Fjvwf9ZIi92N4lgg6/RuMV8vSvSzRe1GKLQzTCrvruf/sod6ykEtwVwUCoxQYYwibGdTvMl2eQO1CZB1TkGNVLZFz1ATLex5dcdeNu3DqJCA/KiNYNM/dppNtXbieb9YbMgtYv9srCrVGDewovI+/oUh+PiJ/+i7Imq2HtzxKDC/DniRExH/fT58I2fjbvqiZ51qZavox/yegKj8M1QANOmD4DA4Xp6wSjNgDvDDEtv1+hxdKhbLm+WZUQj45LRIQjnpf5+pVWV4bebQdSak0NtzzTNZtQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
auth = "WyI2OTIzMzY0OCIsImJ6MC90MExTYmhEdFl6WGhDV1V3azVwY2QvUysyc1RMTS91RHNmcU0iXQ=="

result = Key.activate(token=auth,
                      rsa_pub_key=RSAPubKey,
                      product_id=22996,
                      key="DVPTA-DEUZC-VEMGR-JNARQ",
                      machine_code=Helpers.GetMachineCode(v=2))

if result[0] is None or not Helpers.IsOnRightMachine(result[0], v=2):
    # an error occurred or the key is invalid or it cannot be activated
    # (eg. the limit of activated devices was achieved)
    print("The license does not work: {0}".format(result[1]))
    exit()
else:
    # everything went fine if we are here!
    print("The license is valid!")


def comment_on_tweets(page):
    # global usertext

    # Get all tweets in the timeline
    tweets = page.query_selector_all('div[data-testid="cellInnerDiv"]')
    print(len(tweets))

    for tweet in tweets:
        # profile = tweet.wait_for_selector("[data-testid='Tweet-User-Avatar']")
        # profile.click()
        # time.sleep(5)
        # back = page.query_selector("[data-testid='app-bar-back']")
        # back.click()
        # time.sleep(3)
        # tweet.scroll_into_view_if_needed()

        # if username:
        #     bounding_box = username.bounding_box()
        #     if bounding_box:
        #         # Get the y-coordinate of the bottom of the element plus some extra space (e.g., 100 pixels)
        #         scroll_to_position = bounding_box['y'] + bounding_box['height'] + 100
        #
        #         # Scroll the page to the calculated position
        #         page.evaluate(f"window.scrollTo(0, {scroll_to_position})")

        # Check if the tweet is liked or not
        like_button = None
        usertext = ""
        dealing_person = ""

        username = tweet.query_selector('.css-1qaijid')

        try:
            usertext = username.inner_text()
            dealing_person = username.inner_text()

            like_button = tweet.query_selector('div[data-testid="like"]')


        except:
            pass

            # if like_button and usertext != usertext:
        if usertext != "Black King  Army " and dealing_person != Name and like_button:

            try:
                max_attempts = 50
                attempt_count = 0

                while attempt_count < max_attempts:
                    try:
                        if like_button.is_visible() and like_button.is_enabled():
                            like_button.click()
                            print('Liked')
                            print(usertext)
                            break
                    except Exception:
                        pass
                    attempt_count += 1
                    print(attempt_count)

                if attempt_count == max_attempts:
                    print("Iteration limit reached............................")
                    page.reload()
                    page.goto(f'https://twitter.com/{username}/with_replies')
                    # page.goto('https://twitter.com')

                    time.sleep(2)
                    try:
                        print('finding')
                        close = page.query_selector('div[data-testid="tweetTextarea_0RichTextInputContainer"]')
                        finnder = page.query_selector('div[data-testid="app-bar-close"]')

                        print('finded')
                        if close and close.is_enabled():
                            finnder.click()
                            print('finded and closed')
                        else:
                            print('cant find continue')
                            continue
                    except:
                        print('Pass executed')
                        pass

                    break
            except Exception as e:
                print(e)

            # time.sleep(0.5)
            # If tweet is not liked, click the like button

            # Add a slight delay to ensure the like action is completed
            # time.sleep(1)

        else:
            print('already liked')
            print(usertext)
            page.evaluate('window.scrollBy(0, 50);')

            # If tweet is already liked, skip to the next tweet
            continue

            # Refresh the like button element or handle the error gracefully
        # Find all reply buttons within each tweet
        reply_button = tweet.wait_for_selector('div[data-testid="reply"]')
        try:
            if reply_button.is_disabled():
                print('button is not enabled')
                break
        except:
            print('button is enable')
            # time.sleep(20)  test
            continue
        # reply_button= tweet.text_content("")

        if reply_button:
            print('commenting')
            reply_button.click()
            time.sleep(1)

            # Find the comment box and submit your comment
            # comment_box = page.wait_for_selector('div[data-testid="tweetTextarea_0"]')

            comment_box = page.wait_for_selector('div[data-testid="tweetTextarea_0RichTextInputContainer"]')
            # comment_box= page.locator('//html//body//div[1]//div//div//div[1]//div[2]//div//div//div//div//div//div[2]//div[2]//div//div//div//div[3]//div[2]//div[2]//div//div//div//div[1]//div[2]//div//div//div//div//div//div//div//div//div//div//div//label//div[1]//div//div//div//div//div//div[2]//div//div//div//div//span//br')
            # comment_box= page.locator('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            # comment_box = page.locator('tweetTextarea_0')
            print('find')
            if comment_box.is_visible():
                comment_box.click()
                print('text is visible')
                texts = [
                    "I see 🚀 coming LFG",
                    "U only need one 1000x👀🚀",
                    "Let's go!! 🔥🔥 That's great! Can we talk about your amazing project? 🤔 DM me! 📩🚀",
                    "Talk to me, I have an interesting proposal for you let's collaborate 🔥🔥",
                    "Hello sir , I have a business proposal for you. Let's dm me 🔥🤝",
                    "We definitely need to discuss something huge for your project. 📨",
                    "ONLY UP from here. Moon is programmed 🌕🌕",
                    "Hey!! They seem like a good project to me, can we talk? send me dm! 🚀📩",
                    "Hey dear!! I'm really interested in your Project.🤞let's collaborate🤗! Send me DM!💫🌟",
                    "I have something special for this future top project 🚀Dm Me📥"
                ]

                random_text = random.choice(texts)

                # comment_box.fill(text)
                print('before pasted')

                pyperclip.copy(random_text)
                # comment_box.click()
                page.keyboard.down('Control')
                page.keyboard.press('KeyV')
                page.keyboard.up('Control')
                print('pasted')
                post_button = page.query_selector('div[data-testid="tweetButton"]')

                # time.sleep(0.3)
                # Locate and click the post button
                # try:
                #     start_index = 0
                #     max_iterations = 10
                #     while start_index < max_iterations:
                #         try:
                #             post_button = page.wait_for_selector('div[data-testid="tweetButton"]')
                #             if post_button.is_enabled():
                #                 print('before click')
                #                 post_button.click()
                #                 print('after clicking')
                #                 break
                #         except Exception:
                #             pass
                #         start_index += 1
                #         if start_index == max_iterations:
                #             print('error ecured refreshing')
                #             page.reload()
                # except Exception as e:
                #     print(e)
                try:
                    print('entreing')
                    max_attempts = 10
                    attempt_count = 0

                    while attempt_count < max_attempts:
                        print('trying')
                        try:
                            if post_button.is_visible() and post_button.is_enabled():
                                post_button.click()
                                print('twetted')
                                print(usertext)
                                break
                        except Exception:
                            pass
                        print('trying')
                        attempt_count += 1

                    if attempt_count == max_attempts:
                        print("Iteration limit reached............................")
                        page.reload()
                        page.goto(f'https://twitter.com/{username}/with_replies')
                        # page.goto('https://twitter.com')


                        time.sleep(5)
                        break
                except Exception as e:
                    print(e)

                # time.sleep(0.8)  # Wait before proceeding to the next tweet


if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context()
        context.set_default_timeout(600000)  # Set to 60 seconds (adjust as needed)

        # Load cookies from the JSON file
        with open('cookies.json', 'r') as file:
            cookies = json.load(file)
            context.add_cookies(cookies)

        page = context.new_page()
        # page.goto('https://twitter.com')

        page.goto(f'https://twitter.com/{username}/with_replies')
        # followers = page.locator(
            # '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/nav/div/div[2]/div/div[2]/a/div/div/span')
        # followers.click()
        # page.evaluate("""
        #                 setInterval(() => {
        #                     location.reload();
        #                 }, 20000); // 300,000 milliseconds = 5 minutes
        #             """)
        # time.sleep(3)
        # comment_on_tweets(page)

        while True:
            comment_on_tweets(page)

            # Delay for 10 minutes (600 seconds)
        # Keeping the browser open for a while to observe the changes
        # time.sleep(10)
