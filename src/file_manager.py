import os

def open_file(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    elif platform.system() == 'Linux':
        subprocess.Popen(["xdg-open", path])
    
def app_path():
    return os.path.dirname(os.path.abspath(__file__))

def documents_path():
    home = os.path.expanduser("~")
    print(home)
    documents_path = home.join('Documents')
    
    return documents_path