from autotest.base.core.UI import UI

class WebApp(UI):
    def eee(self):
        pass

    def enter(self,url):
        self.driver.get(url)

