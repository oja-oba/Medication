FROM python:3.9
WORKDIR /app
COPY app.py requirements.txt ./
RUN pip install flask
CMD ["python", "app.py"]
EXPOSE 5001