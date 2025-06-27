import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def random_char():
    return random.choice(string.ascii_letters + string.digits)

def main():
    video_url = input("Enter TikTok video URL to test on: ").strip()
    
    driver = webdriver.Chrome()  # Or webdriver.Firefox()
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)
    
    driver.get(video_url)
    
    # Wait for the page to load
    time.sleep(5)
    
    print("Please log in manually if not already logged in, then press Enter here...")
    input()
    
    # Post a comment
    try:
        comment_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[data-e2e='comment-input']")))
        comment_text = "Teamwork" + random_char()
        comment_box.click()
        comment_box.clear()
        comment_box.send_keys(comment_text)
        comment_box.send_keys(Keys.RETURN)
        print(f"Comment posted: {comment_text}")
        time.sleep(3)
    except Exception as e:
        print(f"Failed to post comment: {e}")
    
    # Like all comments
    try:
        # Scroll down a bit to load comments (adjust scrolling as needed)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
        time.sleep(3)
        
        comments = driver.find_elements(By.CSS_SELECTOR, "div[data-e2e='comment-item']")
        print(f"Found {len(comments)} comments.")
        
        for comment in comments:
            try:
                like_button = comment.find_element(By.CSS_SELECTOR, "button[data-e2e='like-comment']")
                like_button.click()
                delay = random.choice([1, 2])
                time.sleep(delay)
            except Exception:
                continue
        
        print("Liked all comments found.")
    except Exception as e:
        print(f"Failed to like comments: {e}")
    
    driver.quit()

if __name__ == "__main__":
    main()


