# TestAutomation.Python
This is the base framework for a Page Object Model format using Selenium and Python. 
These instructions assume you are in a Unix environment, if you are on a Windows machine
additional steps are required that are not documented within this README.


## Table of Contents
1. [Getting Started](#getting-started)
	1. [Step 1 Installing Python3](#Step-1-Installing-Python3)
	2. [Step 2 Installing required Python3 modules](#Step-2-Installing-required-Python3-modules)
	3. [Step 3 Installing Selenium Chromedriver](#Step-3-Installing-Selenium-Chromedriver)
	4. [Step 4 Setting up the variables file](#Step-4-Setting-up-the-variables-file)
	5. [Step 5 Explanation of layout](#Step-5-Explanation-of-layout)
	6. [Step 6 Configuring the framework to your application](#Step-6-configuring-the-framework-to-your-application)
	7. [Step 7 How to run the tests](#Step-7-How-to-run-the-tests)
	8. [Step 8 How to run the tests with Junit xml output](#Step-8-How-to-run-the-tests-with-Junit-xml-output)
	9. [Step 9 How to run the tests with test coverage output](#Step-9-How-to-run-the-tests-with-test-coverage-output)
2. [Running code within a virtual environment](#running-the-code-in-a-virtual-environment)
	1. [Step 1 Installing required Python3 modules](#Step-1-Installing-required-Python3-modules)
	2. [Step 2 Create the Venv](#Step-2-Create-the-Venv)
	3. [Step 3 Activating and deactivating your venv](#Step-3-Activating-and-deactivating-your-venv)


## Getting started

These instructions will get you a copy of the project up and running on your 
local machine for development and testing purposes.

### Step 1 Installing Python3

Python3 is the language that is used for this repo. Instructions on getting it 
set up can be found here:

http://docs.python-guide.org/en/latest/starting/installation/

### Step 2 Installing required Python3 modules

Required Python3 modules are listed in the `python/requirements.txt` file. Via  
terminal, install all of these requirements using the `python/requirements.txt` file,
by using the following command:

```
pip3 install -r {{path_to_requirements.txt}}
```

Verify they appear in the list _additional pre-req modules may have been 
installed_:

```
pip3 list
```

*NOTE:* that if you get the following error:

```
Could not install packages due to an 
EnvironmentError: [Errno 13] Permission denied: '/usr/local/man'
Consider using the `--user` option or check the permissions.
```

You should run the install with a `--user` flag:

```
pip3 install --user -r {{path_to_requirements.txt}}
```

### Step 3 Installing Selenium Chromedriver

Install Homebrew: https://docs.brew.sh/Installation
Install selenium chromedriver with `brew cask install chromedriver`
Verify the installation with `chromedriver --version` if no errors are returned,
it was likely successful.

### Step 4 Setting Up the variables file

This file is not added to the repo, due to the file typically containing sensitive information. An
example of this file can be found in `python/ui/variables/example_variables_ui.py`. Simply create a copy 
of the file, rename it to be "variables_ui.py", and fill in the required fields.

```
python/ui/variables/example_variables_ui.py 
```

### Step 5 Explanation of Layout

The Page Object Model testing strategy is being used. Each page/feature has the 
following:

(a) method/module files
(b) test files
(c) variables files

Method/module files contains relevant code related to each of the features. The 
majority of action code lives here.

Test files contain the execution code for each test, and tests can be 
configured here.

Variable files contain any relevant variables needed to complete the tests. This
file is shared between multiple features.

Log files are automatically created, and keeps track a log of the automation.
These live in the log folder.

### Step 6 Configuring the framework to your application

By default the framework has a single method/module for testing a `landingpage` it is not configured.
To configure this perform the following steps. _This assumes you understand the Layout detailed in
step 5, and have an understanding on the code in the methods and tests_

Edit the `python/ui/variables.py` file to adjust the Example URL within the dictionary
to the URL of the application you would like to test.

Edit the `python/ui/methods/landingpages/landingpage.py` file and update the 
`LANDING_HEADER` variable to the appropriate selector of the header element in your application
that you would like to test and the `TXT_LANDING_HEADER` to what you expect the text of the landing
header to be. 

Proceed to Step 7 to run the tests and troubleshoot if your first test is working!

### Step 7 How to run the tests

Set your python path to the python folder.

While in the {{path_to..}}/python/ folder
```
PYTHONPATH=.
```

Run all tests in a folder using the following command:

```
pytest {{path_to..}}/python/eapi/tests/
```

Specify which tests to run by specifying the test file to run:

```
pytest {{path_to..}}/python/eapi/tests/test_heartbeats.py
```

NOTE, that you can run tests without the `pytest` command, but there are 
additional steps required. This is the easiest method of running tests.

### Step 8 How to run the tests with Junit XML output

Additionally, the pytest has built-in functionality which supports outputting 
to a JUnit XML format. This can help in integration with Bamboo logs. To do 
this, use the following command while running the tests:

```
pytest {{path_to..}}/python/eapi/tests/ --junitxml={{path_to_log_file.xml}}
```

### Step 9 How to run the tests with test coverage output

Also, there is a pytest library which allows for outputting of test coverage, 
"pytest-cov". This library is included in the requirements.txt file. This can 
help in integration with Bamboo logs. To do this, use the following command 
while running the tests:

```
pytest --cov={{path_to..}}/python/eapi/tests/ {{path_to..}}/python/eapi/tests/ 
    --junitxml=test_junit.xml
```

## Running code within a virtual environment

It is suggested that you run/install the Automation in a Virtual Environment 
_abbreviated as venv_. However, this is NOT a requirement, but highly recommended. These instructions 
will help you get up and rolling with one.

VENVs are useful, as they allow you to test your code free from other 
dependencies.

### Step 1 Installing required Python3 modules

A `virtualenv` library exists as a module for Python3. It should have been 
installed already, via the `requirements.txt` file installation listed above. 
However, if not, then the following command line can be run to install it
manually:

```
pip3 install virtualenv
```

### Step 2 Create the Venv

Navigate to the target folder where you want the venv to exist. Then, run the 
following terminal command, to create the venv in your current working 
directory:

```
python3 -m virtualenv {{name_of_your_venv}}
```

That's it. You now have a venv ready for use!

### Step 3 Activating and deactivating your venv

To start off with, locate your venv folder. Within the main venv parent 
folder, there will be a child folder called `bin`. Within the `bin` child 
folder, there is a file named `activate`. NOTE, that there are multiple
`activate` files. The one you want is the one without a file extension.

Once you know where the file is, run the following terminal command, to start
your venv:

```
source {{path_to_venv}}/bin/activate
```

This command will automatically start your venv, and put you into your venv.

To exit the venv, simply type this command while in the venv:

```
deactivate
```

You should now be removed from the venv, and back in your normal shell.

