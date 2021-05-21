FROM python:3.6-slim
COPY setup.py ./setup.py
RUN pip install -e .

COPY data /data
COPY src /src
COPY models /models
COPY app.py /app.py

WORKDIR .

ENV PATH_MODEL="models/model_dump.pkl"

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]