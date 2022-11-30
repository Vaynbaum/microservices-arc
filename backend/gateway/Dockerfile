FROM python
WORKDIR /gateway
COPY . .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
CMD ["uvicorn", "gateway:app", "--host", "0.0.0.0", "--port", "3003"]
EXPOSE 3003