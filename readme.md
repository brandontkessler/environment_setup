# Development Workspace Setup

## Setup

Run the `setup.py` file to start the process.

* The 'Workspace' can be created in any folder but is created in root by default.
* Updates to bashrc and bash_profile are optional
* Only one 'Workspace' should exist at a time, eliminate others before starting new.
  
## Eliminate

Clears out the existing 'Workspace'.


## Checklist

1. Workspace folder structure should be created
   1. Git repos cloned into code
   2. Empty bcreds files (one in code, one in work/code)
   3. Configs folder with vscode workspace config
   4. Notes folder cloned from git
   5. Work folder with empty structure
   6. Backups folder should be created if not already exists at ~/backups
2. Bash files created (if confirmed):
   1. .bash_profile
   2. .bashrc
   3. .bash_prompt
   4. .bash_aliases
3. Folder for .aws and dummy creds file (if one doesn't already exist)
4. Folder for .ssh and dummy config file
   1. Keys rsa public/private pairing (if confirmed)