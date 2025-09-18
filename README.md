## An implementation of a JWT authentication server using FastAPI
### Prerequisites
#### Step1:
- Create Python Virtual Environment to avaoid python packages versions conflicts
```sh
python -m venv .venv
```
where <b>.venv</b> given user name for Python Virtual Environment
- Activate the virtual environment (.venv)
in Windows
```sh
.venv/Scripts/Activate.ps1
```

#### Step2:
You need to have Python and pip installed. Start by setting up a project directory and installing the necessary packages: 
```sh
pip install -r requirements.txt
```
Or 
```sh
pip install "fastapi[all]" python-jose[cryptography] passlib[bcrypt] pyjwt
```

Note: python-jose and passlib[bcrypt] are highly recommended for secure password hashing and JWT token handling. 

### Project structure
Create the following file structure for the server:
```text
FastAPI-Jwt-Server/
├── .venv
├── main.py
├── users.py
└── requirements.txt
