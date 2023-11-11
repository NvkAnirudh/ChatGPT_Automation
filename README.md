# ChatGPT_Automation

This project aims to monitor a designated folder for recently added video transcript files and automate the execution of a Python script. This script leverages the content within the transcript files to generate prompts for [GPT-3.5-Turbo](https://openai.com/blog/gpt-3-5-turbo-fine-tuning-and-api-updates) by [OpenAI](https://openai.com/) to obtain summaries. <br>

## Overview

The `auto_run.py` script employs the **watchdog** library to monitor file system events within a specified folder. Upon the addition of a new transcript file, it automatically initiates the execution of the `chatgpt_automation.py` script, passing the name of the newly added file as an argument. In the latter script, an API call is made to GPT-3.5-Turbo, utilizing the content of the transcript file as a prompt, and the model's response is obtained as the summary.

## Installation

OpenAI and watchdog are the important libraries required for the scripts to run successfully. 

```
pip install --upgrade openai watchdog
```
## Setting up OpenAI's API Key

Check [this](https://platform.openai.com/docs/quickstart?context=python) to add an environment variable and make your API key accessible to all projects.

## Usage

1) Open the `auto_run.py` file and update the **FOLDER_TO_MONITOR** variable with the absolute path of the folder you want to monitor.

2) Run the script:

   ```
   python auto_run.py
   ```
   This script will now monitor the specified folder, and whenever a new file is added, it will trigger the execution of `chatgpt_automation.py` with the file's name as an argument.

## Customization

1) You can customize the behavior of the script by modifying the **MyHandler** class in the `auto_run.py` file.

2) Adjust the logic in `chatgpt_automation.py` to process the newly added file according to your requirements.

## Pricing

Understanding pricing is really important before you run this project. So please KEEP THIS IN MIND! <br>

You can check out OpenAI's pricing structure [here](https://openai.com/pricing)

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.





