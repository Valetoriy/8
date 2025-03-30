import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

class RequestEditTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        service = Service(executable_path="/usr/bin/chromedriver")

        cls.driver = webdriver.Chrome(service=service)
        cls.driver.implicitly_wait(5)

        cls.url = "http://localhost:8080/crs-1.0/admin_menu.jsp"

    def setUp(self):
        self.driver.get(self.url)

        requests = self.driver.find_element(By.CSS_SELECTOR, "form[action='reqs'] button")
        requests.click()

        edit = self.driver.find_element(By.CSS_SELECTOR, "form[action='editReq'] button")
        edit.click()

        # Ждём пока бот перейдёт на нужную страницу
        time.sleep(1)

    def test_empty_comment_empty_employee(self):
        """Пустой комментарий и сотрудник"""
        comment = self.driver.find_element(By.NAME, "comment")
        comment.clear()
        employee = self.driver.find_element(By.NAME, "res_employee")
        employee.clear()

        submit_button = self.driver.find_element(
            By.XPATH, 
            "//form[@class='aform']//button[contains(text(), 'Сохранить')]"
        )
        submit_button.click()

        self.assertEqual("Редактирование заявки", self.driver.title)
        time.sleep(2)

    def test_filled_comment_empty_employee(self):
        """Заполненный комментарий и пустой сотрудник"""
        comment = self.driver.find_element(By.NAME, "comment")
        comment.clear()
        comment.send_keys("Ремонт телевизора")
        employee = self.driver.find_element(By.NAME, "res_employee")
        employee.clear()

        submit_button = self.driver.find_element(
            By.XPATH, 
            "//form[@class='aform']//button[contains(text(), 'Сохранить')]"
        )
        submit_button.click()

        self.assertEqual("Редактирование заявки", self.driver.title)
        time.sleep(2)

    def test_empty_comment_filled_employee(self):
        """Пустой комментарий и заполненный сотрудник"""
        comment = self.driver.find_element(By.NAME, "comment")
        comment.clear()
        employee = self.driver.find_element(By.NAME, "res_employee")
        employee.clear()
        employee.send_keys("Андрей Андреев")

        submit_button = self.driver.find_element(
            By.XPATH, 
            "//form[@class='aform']//button[contains(text(), 'Сохранить')]"
        )
        submit_button.click()

        self.assertEqual("Редактирование заявки", self.driver.title)
        time.sleep(2)

    def test_filled_comment_filled_employee(self):
        """Заполненный комментарий и заполненный сотрудник"""
        comment = self.driver.find_element(By.NAME, "comment")
        comment.clear()
        comment.send_keys("Ремонт телевизора")
        employee = self.driver.find_element(By.NAME, "res_employee")
        employee.clear()
        employee.send_keys("Андрей Андреев")

        submit_button = self.driver.find_element(
            By.XPATH, 
            "//form[@class='aform']//button[contains(text(), 'Сохранить')]"
        )
        submit_button.click()

        self.assertEqual("Невыполненные заявки", self.driver.title)
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
