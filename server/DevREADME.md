# Create / open virtual environment
---
VS Code extention to make .md files more readable
[Markdown Preview Enhanced](https://marketplace.visualstudio.com/items/?itemName=shd101wyy.markdown-preview-enhanced)  

---

# Create env
###### Recommended to be created within `server/` or dragged into folder
```bash
python3 -m venv venv
```

# Run env

#### Mac/Linux
```bash
source venv/bin/activate
```

#### Windows CMD
```cmd
pymys\Scripts\activate
```

---

# Install dependencies
```bash
pip install -r server/req.txt
```
Note: Only need to install initally and when new dependencies are added

## Deactivate virtual environment
```bash
deactivate
```
Note: After deactivating you can reaccess your env at a later time

---

# File Struc
## Current Structure
```bash
pymus/
├── client/            # Frontend side
│   ├── public/        # React.js public assets (e.g., static files)
│   └── src/           # React.js source code (e.g., components, hooks)
├── server/            # Backend side
│   ├── app/           # Python files
|   │   ├── server.py  # Entry point for backend logic
|   │   └── otherfiles.py  
│   ├── venv/          # Python Virtual environment folder
|   ├── req.txt        # Dependency list for backend
│   └── DevREADME.md   # Documentation for development direction
├── .env               # For sensitive data (e.g., API keys, database credentials)
├── .gitignore         # Specifies files to ignore (e.g., vir environments, .env)
└── README.md          # General project documentation
```

## Old Structure (before react frontend)
```bash
pymus/
├── pm/                # Virtual environment folder
├── src/               # Project source code
│   ├── DevREADME.md   # Documentation for development direction
│   ├── main.py        # Python files
│   └── otherfiles.py 
├── req.txt            # Dependency list
└── README.md          # Documentation
```


## Activate & Run 
```bash
source server/venv/bin/activate  # Activate the virtual environment
```
```bash
python server/app/main.py      # Run your Python file
```


# Git 
There is a `.gitignore` file that stops your local envs from being pushed.
If you want to create a virtual env with different name add the env name `[env-name]/` to `.gitignore` file.

---

# Last.fm pylast reference
[Source Code Test for pylast](https://github.com/pylast/pylast/tree/main/tests)