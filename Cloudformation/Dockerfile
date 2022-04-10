FROM python:3

## Step 1:
WORKDIR /app

## Step 2:
COPY . src/ /app/

## Step 3:
COPY  src/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

## Step 4:
EXPOSE 80

## Step 5:
# Run app.py at container launch
CMD ["python", "server.py"]