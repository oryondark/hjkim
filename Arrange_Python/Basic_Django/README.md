# Django Installation Guide

### Step 1. install & run docker container
```shell
docker pull ubuntu:latest
docker run -it --name your docker ubuntu:latest /bin/bash
apt-get update
apt-get install python3.8 python3.8-dev
curl -o get-pip.py https://bootstrap.pypa.io/get-pip.py
pip install Django Django-chartjs
```

### Step 2. Example using Template
```shell
django-admin startproject myhome
cd myhome
python manage.py startapp polls
vi polls/views.py
```

### Step 2. Make Template to use chartjs
[ref](https://pypi.org/project/django-chartjs/)
```python
line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()
```
but, may be you should setup template environment.
```shell
vi myhome/setting.py
...
TEMPLATES = [
  {
    ...
    'DIRS':[os.path.join('myhome_path', 'view_path')]
  }
]
```
