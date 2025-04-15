# Create / open virtual environment
---
VS Code extention to make .md files more readable
[Markdown Preview Enhanced](https://marketplace.visualstudio.com/items/?itemName=shd101wyy.markdown-preview-enhanced)  

---

# Create env
```bash
python3 -m venv pm
```

# Run env

#### Mac/Linux
```bash
source pm/bin/activate
```

#### Windows CMD
```cmd
pymys\Scripts\activate
```

---

# Install dependencies
```bash
pip install -r req.txt
```
Note: Only need to install initally and when new dependencies are added

## Deactivate virtual environment
```bash
deactivate
```
Note: After deactivating you can reaccess your env at a later time

---

# File Struc
```bash
pymus/
├── pm/                # Virtual environment folder
├── src/               # Your project source code
│   ├── main.py        # Your Python files
│   └── other_files.py 
├── requirements.txt   # Dependency list
└── README.md          # Documentation
```

## Activate & Run 
###### Previous file strucure:
```bash
source pm/bin/activate  # Activate the virtual environment
```
```bash
python src/main.py      # Run your Python file
```
Note: If you created the virtual environment while your current directory was set to `src` (through cd), the `pm` folder will be located inside `src`.
###### In this case:

```bash
source pm/bin/activate  # Activate the virtual environment
```
```bash
python main.py      # Run your Python file
```
---

# Git 
There is a `.gitignore` file that stops your local envs from being pushed.
If you want to create a virtual env with different name add the env name `[env-name]/` to `.gitignore` file.

---