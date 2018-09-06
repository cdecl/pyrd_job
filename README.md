
# pyrd_job 
- Gitlab Web Hook (POST Method) 대응 API 프록시 서버
- Rundeck 서버와 같은 머신에서 운영

## Installation 
- python 3.6, pip
- flask, flask-aip, gunicorn

```bash
sudo yum install python36u python36u-pip

sudo ln -sf /usr/bin/python3.6 /usr/bin/python3 
sudo ln -sf /usr/bin/pip3.6 /usr/bin/pip3

sudo pip3 install flask, flask-aip, gunicorn

```

## Using 
```bash

# 실행 테스트 
python3 index.py

# gunicorn (wsgi)로 실행 
# -b 바인딩, 
# --reload Restart workers when code changes.
/usr/bin/gunicorn -b :8000 --reload index:app

```

## Systemd
- [pyrd_job.service](pyrd_job.service)

```bash

sudo cp -r [source dir]/* /var/pythonapp/pyrd_job/
sudo cp -r [source dir]/pyrd_job.service /etc/systemd/system/

sudo systemctl enable pyrd_job
sudo systemctl start pyrd_job

# Test Result : alive
curl localhost:8000 

```