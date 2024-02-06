# docker run -p 8000:8000 -it app
FROM python:3.11.6-bookworm

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY DM-CA.crt .
RUN cp DM-CA.crt /usr/local/share/ca-certificates/ && update-ca-certificates
ENV ACCEPT_EULA=Y
RUN apt-get update -y && apt-get update \
  && apt-get install -y --no-install-recommends curl gcc g++ gnupg unixodbc-dev
RUN curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg
RUN curl https://packages.microsoft.com/keys/microsoft.asc | tee /etc/apt/trusted.gpg.d/microsoft.asc \
    && curl https://packages.microsoft.com/config/debian/12/prod.list | tee /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update -y && apt-get update
RUN ACCEPT_EULA=Y apt-get -y install msodbcsql17




RUN pip install --upgrade pip "poetry==1.6.1"
RUN poetry config virtualenvs.create false --local

COPY poetry.lock pyproject.toml ./

RUN poetry install

COPY . .

EXPOSE 8000

CMD python manage.py migrate \
    && python manage.py collectstatic --noinput \
    && python manage.py runserver 0.0.0.0:8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "&&", "python", "manage.py", "migrate"]

