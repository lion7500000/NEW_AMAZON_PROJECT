import os

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from app.logger import MyListener, logger
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver


bs_user = 'lion74'
bs_pw =  'y2HxEGBDfLA2mp9A3nks'

# def get_browser():
#     if 'browser' not in os.environ:
#         raise ValueError ('Browser was not provided !')
#     if os.environ['browser'] == 'chrome':
#         return webdriver.Chrome()
#     elif os.environ['browser'] == 'ff' or "firefox":
#         return webdriver.Firefox()
#     elif os.environ['browser'] == 'safari':
#         return webdriver.Safari()



def browser_init(context,name):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome()#executable_path=" "
    # context.driver = get_browser()
    #context.driver = webdriver.Safari()
    #context.driver = webdriver.Firefox()

    #### EventFiringWebDriver ####
    # context.driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())

    ### Browser Stack ###
    # desired_cap = {
    #    'browser': 'Chrome',
    #    'browser_version': '93.0',
    #    'os': 'OS X',
    #    'os_version': 'Catalina',
    #     'name': name,
    #     'browserstack.networkLogs' : True
    # }
    #
    # url = f'http://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'
    # # url = f'http://{bs_user}:{bs_pw}@api.browserstack.com / automate / sessions / < session - id >.json'
    #
    # context.driver = webdriver.Remote( url, desired_capabilities=desired_cap )



    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 20)
    context.app = Application(context.driver)

    #### HEADLESS ####
    #options = webdriver.ChromeOptions()
    #options.add_argument( 'headless' )
    #context.driver = webdriver.Chrome( chrome_options=options )



def before_scenario(context, scenario):
    logger.info(f'\nStarted scenario: , {scenario.name}')
    print('\nStarted scenario: ', scenario.name)
    browser_init(context,scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'\nStarted step: , {step}')

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.info(f'\nStep failed: , {step}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()