FROM python:3.8

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY ./NameClassifier/ /code/NameClassifier

COPY ./Notebooks/ /code/Notebooks

COPY ./saved_model/ /code/saved_model


# EXPOSE 8000

CMD ["uvicorn", "NameClassifier.api_router:app", "--host", "0.0.0.0", "--port", "8000"]
