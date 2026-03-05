from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

def test_chatbot():
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    driver.get("http://127.0.0.1:5000")

    input_box = driver.find_element(By.ID, "message")
    input_box.send_keys("hello")

    driver.find_element(By.ID, "sendBtn").click()
    time.sleep(2)

    response = driver.find_element(By.ID, "response").text
    print("Bot response:", response)

    assert response != ""
    driver.quit()

if __name__ == "__main__":
    test_chatbot()
