# Kiteen (Pallo) Project

A framework to Automation Web based on Python, Pytest, and Allure Report for the following browsers: Chrome, Firefox, Edge (Chromium) and Internet Explorer on Incognito mode and/or Headless mode

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. In this case this framework work in Windows environment. This framework has not been tested on GNU/Linux environments (we are working on this).

For this version is not possible to run Edge (chromium) on headless or incognito mode (This feature will come on Selenium 4). Some features don't work on Internet Explorer (*for example Mouse Over*) if you need this or another feature please send us your requirement.

### Prerequisites

> #### Python 
> - Go to [Python](https://www.python.org/downloads/)
> - Download the latest version or >= to 3.8.0
> - Install Python and set the environments variables.
> - Verify your Python installation with *python --version* fron any console/terminal
> ```
> PS C:\Users\you_user> python --version
> Python 3.8.0
> ```

> #### Allure 
>
> - You need install allure in you environment
> - Go to [allure release](https://github.com/allure-framework/allure2/releases/)
> - Download the zip version: **2.13.3**
> - Unzip into you directory preferred
> ```
> C:\allure
> ```
> - Add allure *bin* folder into Environment Variables *PATH*. For any help go to [how to set a environment variable on Windows 10](https://superuser.com/questions/949560/how-do-i-set-system-environment-variables-in-windows-10)
> - From Powershell or any console/terminal you must verify allure with *allure -- version* 
> ```
> PS C:\Users\you_user> allure --version
> 2.13.3
> ```

> #### WebDriver 
>
> - You need a WebDriver to run your test for your browser/s, so you must know what is the current version from your browser (for example: Google Chrome Version 81.0.4044.129 (Official Build) (64-bit))
> - Go to download a Webdriver that could be support your browser (*for example: If you are using Chrome version 81, please download ChromeDriver 81.0.4044.69*)
> - For more information go to site of your browser WebDriver:
>   - [FirefoxDriver (GeckoDriver)](https://github.com/mozilla/geckodriver/releases)
>   - [ChromeDriver](https://chromedriver.chromium.org/downloads)
>   - [EdgeDriver(chromium)](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/#downloads)
>   - [InternetExplorerDriver(3.9)](https://selenium-release.storage.googleapis.com/index.html)
> - Unzip into *drivers* folder. *For example*:
>```
> PS C:\Users\you_user\you_workspace\kiteen_project\drivers> ls
> Name
> ----
> chromedriver.exe
> geckodriver.exe
> IEDriverServer.exe
> msedgedriver.exe
>```

### Installing

> #### Python Libs
> - You need install project module/libs from *requirements.txt* file
> ```
> PS C:\Users\you_user\you_workspace\kiteen_project> pip install -r requirements.txt
> ```
> - After finish install process you can verify the modules installed with *pip freeze* and you must see the following modules installed:
> ```
> PS C:\Users\you_user\you_workspace\kiteen_project> pip freeze
> ...
> allure-pytest==2.8.13
> allure-python-commons==2.8.13
> pytest==5.4.1
> selenium==3.141.0
> ...
>```

### Settings
> To run the first tests we need to understand the file **config.json**. This file has the following attributes:
> - **browser** : *str* (a string name of your browser. Must be: "firefox", "chrome", "edge", "ie").
> - **driverPath** : *str* (a string with the path where you have your weddriver. We recommender: "./drivers/your_webdriver.exe").
> - **urlApp** : *str* (a string with your url App to test. For example: "https://www.your-url-app.com".
> - **defaultWait** : *int* (an integer with the time in seconds to wait for a load of all elements before doing any action. If an element doesn't is present or visible in this time your test case will fail).
> - **incognito** : *bool* (a boolean value to run your test cases in mode Incognito/Private. true for executing in this mode, false to execute without this mode).
> - **headless** : *json* (a dict that contains attributes *enabled* and *window_size*)
> - - **enabled** : *bool* (a boolean value to run your test cases without visualizing the window browser (headless). true for executing in this mode, false to execute without this mode). If you configure true and the browser doesn't support it (like edge chromium or internet explorer) all test cases will execute without these settings).
> - - **window_size** : *json* (a dict that contains window size as X and Y axis. This parameter is only for headless mode).
> - - - **X** : *int* (an integer for X axis value. For example: 800)
> - - - **Y** : *int* (an integer for Y axis value. For example: 600)


> An example of the *config.json* file:

>
>```
>{
>    "browser": "chrome",
>    "driverPath": "./drivers/chromedriver.exe",
>    "urlApp": "http://demo.automationtesting.in/Index.html",
>    "defaultWait": 15,
>    "incognito": false,
>    "headless": {
>         "enabled": false,
>         "window_size":{
>             "X":1920,
>             "Y":1080
>         }
>     }
>}
>```

## Running the tests

Explain how to run the automated tests for this system


### And coding style tests


## Deployment



## Built With



## Contributing



## Versioning

We use [SemVer](http://semver.org/) for versioning. 

## Authors

* **David Gonzalez** - *Initial work* - [github](https://github.com/dsgon/) - [twitter](https://twitter.com/__dsgon)



## License



## Acknowledgments


