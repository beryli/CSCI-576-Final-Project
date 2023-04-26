# csci-576-final-project
## You need to set up the virtual environment(if you haven't):
```
python -m venv venv
```

## activate the virtual environment:
  * **Linux and MacOS venv activation**
  ```
  source venv/bin/activate
  ```
  * **Windows venv activation**
  ```
  .\venv\Scripts\activate
  ```

## install packages
* **To install**:
```
pip install -r requirements.txt
```
## freeze environment
* If you install any new packages, you need to freeze the new environment into requirement.txt
* **To freeze**:
```
pip freeze -l > requirements.txt 
```

## download model
* Before using place365 pretrained model, download from there:
  http://places2.csail.mit.edu/models_places365/resnet152_places365.caffemodel



