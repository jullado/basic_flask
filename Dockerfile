FROM python:3.7.9
RUN apt update

# RUN mkdir /cxr
WORKDIR /cxr-api/

# Install python3 lib
ADD requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Add python code to pwd
ADD . .

CMD ["python", "run.py"]