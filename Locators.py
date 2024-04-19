
class WebLocators:

    def __init__(self):
        # self.userNameLocator = "//*[@class='oxd-input oxd-input--active']  [@name = 'username']"
        self.userNameLocator = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
        # self.passwordLocator = "//*[@class='oxd-input oxd-input--active']  [@name = 'Password']"
        self.passwordLocator = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
        self.loginButtonLocator = "//*[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']"
        self.profileIconLocator = "//*[@class='oxd-userdropdown-name']"
        self.logoutLocator = "//a[@class='oxd-userdropdown-link'][@href = '/web/index.php/auth/logout' ]"
