import os
import yaml

desired_caps = {
                'platformName': 'Android',
                'platformVersion': '7.0',
                'deviceName': 'A5RNW18316011440',
                'appPackage': 'com.tencent.mm',
                'appActivity': '.ui.LauncherUI',
                'automationName': 'Uiautomator2',
                'unicodeKeyboard': [True,"hh"],
                'resetKeyboard': True,
                'noReset': True,
                'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
                }

curpath = os.path.dirname(os.path.realpath(__file__))
print(curpath)
yamlpath = os.path.join(curpath, "caps.yaml")
with open(yamlpath, "w", encoding="utf-8") as f:
    yaml.dump(desired_caps, f)
