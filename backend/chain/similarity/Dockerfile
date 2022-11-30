FROM python
WORKDIR /similarity
COPY . .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
CMD ["uvicorn", "similarity:app", "--host", "0.0.0.0", "--port", "3002"]
EXPOSE 3002