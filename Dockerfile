FROM python:3.12
COPY app /app
WORKDIR /app
RUN pip3 install -U g4f mmpy-bot requests g4f[image] httpx==0.27.2
CMD ["python3", "bot.py"]