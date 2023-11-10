FROM python:3.10

WORKDIR /
RUN pip install pipenv

RUN git clone https://github.com/natynaro/awas.git

WORKDIR /awas/fASTAPI

RUN pip install -r requirements.txt


EXPOSE 80

CMD ["uvicorn", " main:app", "--host", "0.0.0.0", "--port", "80"]