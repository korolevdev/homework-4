# coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Model(object):
    def __init__(self, driver):
        self.driver = driver

    def getElementByPath(self, path):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(path)
        )

    def getDropdownByPath(self, path):
        element = self.getElementByPath(path)
        return element.find_element_by_class_name('nav-pills_dropdown__active__title')

    def getUserByPath(self, path):
        element = self.getElementByPath(path)
        return element.find_element_by_class_name('username')

    def getAreaByPath(self, path):
        element = self.getElementByPath(path)
        return element.find_element_by_class_name('input-text')

    def getPeriodSwitcher(self):
        return self.getElementByPath((By.XPATH, "//li/a[text()='Весь семестр']"))

    def getUser(self):
        return self.getUserByPath((By.XPATH, "//div[@class='dropdown-user']"))

    def getSheduleTable(self):
        return self.getElementByPath((By.XPATH, "//table[@class='schedule-timetable']"))

    def getSettings(self):
        return self.getElementByPath((By.XPATH, "//div[@class='settings']"))

    def getMessages(self):
        return self.getElementByPath((By.XPATH, "//table[@class='table table-talk']"))

    def getLastMessage(self, text):
        return self.getElementByPath((By.XPATH, "//p[text()='%s']" % text))

    def getAddButton(self):
        return self.getElementByPath((By.XPATH, "//a[text()='Написать заметку']"))

    def getDelete(self):
        try:
            element = self.getElementByPath((By.XPATH, "//a[@id='usernote-button-delete']"))
        except TimeoutException:
            return None
        return element

    def getMessageButton(self):
        return self.getElementByPath((By.XPATH, "//a[@class='button button-primary new-direct-message']"))

    def getSaveButton(self):
        return self.getElementByPath((By.XPATH, "//button[text()='Сохранить']"))

    def getSendButton(self):
        return self.getElementByPath((By.XPATH, "//button[@type='submit']"))

    def getSaveSettingsButton(self):
        return self.getElementByPath((By.XPATH, "//button[@name='submit_profile_edit']"))

    def getSaveAdditionalButton(self):
        return self.getElementByPath((By.XPATH, "//button[@type='submit']"))

    def getNoteInput(self):
        return self.getAreaByPath((By.XPATH, "//div[@id='usernote-form']"))

    def getNote(self):
        return self.getElementByPath((By.XPATH, "//p[@id='usernote-note-text']"))

    def getAboutInput(self):
        return self.getElementByPath((By.XPATH, "//textarea[@id='profile_about']"))

    def getMessageInput(self):
        return self.getElementByPath((By.XPATH, "//textarea[@id='message_text']"))

    def getPhoneNumberInput(self):
        return self.getElementByPath((By.XPATH, "//input[@id='phone_number']"))

    def getOKInput(self):
        return self.getElementByPath((By.XPATH, "//input[@id='id_odnoklassniki']"))

    def getCabinet(self):
        return self.getElementByPath((By.XPATH, "//div[@class='profile']"))

    def getUserDropdown(self):
        return self.getElementByPath((By.XPATH, "//div[@class='dropdown-user-trigger']"))

    def getScheduleElement(self):
        return self.getElementByPath((By.XPATH, "//tr[@class='schedule-timetable__item']"))

    def getDisciplineDropdown(self):
        return self.getDropdownByPath((By.XPATH, "//div[@class='schedule-filters__item schedule-filters__item_discipline']"))

    def getGroupDropdown(self):
        return self.getDropdownByPath((By.XPATH, "//div[@class='schedule-filters__item schedule-filters__item_group']"))

class AjaxLoader(object):
    def waitToDisappear(self, driver):
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//div[@class='icon-ajax-loader']"))
        )
