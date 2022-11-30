FROM python
WORKDIR /game
COPY . .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
CMD ["uvicorn", "game:app", "--host", "0.0.0.0", "--port", "3000"]
EXPOSE 3000