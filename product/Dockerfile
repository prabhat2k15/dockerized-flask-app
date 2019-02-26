FROM python:3
COPY . /usr/src/app
RUN ls -l /usr/src/app
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
CMD ["python", "/usr/src/app/api.py"]
