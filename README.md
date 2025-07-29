# mlSandbox
Sandbox project to build ML models

# Setup
Execute the following steps to set up the repository, keys, and environment. The setup needs to be
executed only once to get started. For everyday development, see the `Development` Workflow section.

## Install System Dependencies
This repository relies on a variety of system tools to manage code, environments, and dependencies. Please
follow the instructions below appropriate for your OS. Reach out to one of the team-members if the instructions
for your OS are not yet available.

### Ubuntu & other Debian based OS
You can install necessary system dependencies using the following command in a terminal.
```shell
sudo apt install git ssh python3 python3-pip python3-venv
```

### Mac OS
To be verified.
```shell
brew install git ssh python3 python3-pip python3-venv
```

## Github
Follow these [instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) 
from GitHub on how to setup ssh based secure access to pull and push changes to the codebase.

## Clone this repository
Determine a directory where you would like to store the code repository on your system. Eg: `${HOME}/sandbox`.
Create this directory on your system and open a terminal in this directory. Execute the following command to clone
the repository.

```shell
git clone git@github.com:ajakhotia/mlSandbox.git
```

## Acquire OpenAI API key
Follow the steps below to acquire a key to access OpenAI resources.
1. Log into OpenAI's developer platform [here](https://platform.openai.com/docs/overview).
2. Go to Settings (Top right)
3. Click on API keys on the left panel
4. Click on `Create new secret key` on the top right
   1. Select `You` under `Owned by` field
   2. Give the key a name that includes your name or handle for future identification
   3. Select the appropriate project name under the `Project` field
   4. Select `All` under `Permissions` field
   5. Click the `Create secret key`
5. Copy the key right away. You won't be able to access it again if you leave the page.
6. In the project repository, create a file named `openai_api.key` under the `credentials` directory 
   and paste your key on the file
   * **NEVER SHARE** this key or commit this file to the repository.
   * If you do so accidentally, do the following immediately:
     1. Delete the key from [this](https://platform.openai.com/settings/organization/api-keys) page.
     2. Remove the key from the repository.
7. You should now be able to programmatically access Open AI.


## Build Virtual Environment
The dependencies of this repository are tracked using the `requirements.txt` file located at the root of the
repository. Python's virtual environments allow us to use conveniently install and manage the dependencies
using this file. You can build the virtual environment by executing the following in a terminal.

Change the directory to the root of the repository. 
```shell
cd /path/to/repository
```

Create a virtual environment called `.venv`.
```shell
python3 -m venv .venv
```

Activate the environment using the following.
```shell
source .venv/bin/activate
```

Install the project dependencies using the following.
```shell
pip install -r requirements.txt
```