import os

os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
os.system("python get-pip.py")
os.system("pip install virtualenv")
os.system("virtualenv env")
os.system("source env/bin/activate")
os.system("env/bin/pip install -r requirements.txt")
os.system("echo "" | env/bin/streamlit run app.py")
