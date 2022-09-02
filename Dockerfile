FROM python:3.9

WORKDIR /bot

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY main.py ./
ADD chessbot ./chessbot

ENTRYPOINT ["python"]
CMD ["main.py"]
