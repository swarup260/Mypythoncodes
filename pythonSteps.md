# Step To Create virtual Environment in Python

## 1. To Create a virtual Environment

```shell
     pip install virtualenv
     virtualenv $project_name
```

## 2. To Run Environment

```shell
    source $project_name/bin/activate
```

## 3. To check its Working

```shell
    which python , which pip
```

## 4. To Deactive

```shell
    deactive
```

## 5. python package manager

```shell
    pip freeze --local >reqirements.txt
    to install package from reqirements.txt
    pip install -r reqirements.txt
```

### python flask

```python
    class flask.Flask(import_name, static_path=None, static_url_path=None, static_folder='static', template_folder='templates', instance_path=None, instance_relative_config=False, root_path=None)
```