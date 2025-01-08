FROM python:3.12
COPY bot /bot
WORKDIR /bot
RUN python3 -m venv .venv \
    && source .venv/bin/activate \
    && .venv/bin/pip3 install -U g4f mmpy-bot requests g4f[image] httpx==0.27.2
CMD ["python3", "bot.py"]