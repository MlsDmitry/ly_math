# ly_math
Lyceum Yandex Math project
### Requirements

* python 3.x.x (tested on 3.7.9)

### Debug mode
In [config](src/config.py)
Change to ``` LOG_LEVEL = 10 ```

### Installation
```
git clone https://github.com/MlsDmitry/ly_math.git
cd ly_math
pip3 install -r requirements
```
### Startup application
```
python3 startup.py
```
### Project Structure
```
./src/
├── custom_widgets
│   ├── custom.py
│   ├── error_dialog.py
│   └── slide_widget.py
├── logger
│   └── logger.py
├── managers
│   ├── db_manager.py
│   ├── export_manager.py
│   └── file_manager.py
├── models
│   ├── expression.py
│   └── task.py
├── modules
│   └── expression
│       ├── expression_controller.py
│       ├── expression_model.py
│       └── expression_view.py
├── providers
│   ├── history_provider.py
│   └── preferences_provider.py
├── services
│   └── example_generator_service.py
├── config.py
└── main.py
```

<!-- | **custom_widgets** | reinhereted QtWidgets classes |
| sdf | sdf | -->
Module | Description 
--- | --- 
custom_widgets | reinhereted QtWidgets classes
logger | logging tools - ```log(*args, **kwargs)``` used everywhere
managers | work with sqlite db, export to docx, cross-platform paths
models | expression - signle math example, TaskModel knows everything to generate/save to db/export to docx
modules | modules help expand project easier
modules/expression | major module, ```QMainWindow``` is there
providers | work with database, save/delete snapshots, get default user path (ex: /Users/user1/Documents)
services | uncategorized stuff
services/example_generator_service | math problems generator, saves expressions to _field in TaskModel
### Run tests
```
python3 -m tests
```
### Recent update


![](/git_resources/main_window.png?raw=true)
![](/git_resources/save_dialog.png?raw=true)
