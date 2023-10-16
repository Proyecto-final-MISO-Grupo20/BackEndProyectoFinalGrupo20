FROM python:3.9

RUN groupadd -r user && useradd -r -g user user

EXPOSE 3000

WORKDIR /auth_microservice

ADD requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y libpq-dev
RUN pip uninstall -y pg8000
RUN pip install --no-cache-dir psycopg2

COPY . .

RUN chown -R user:user .
RUN ["chmod", "+x", "run_service.sh"]

CMD ["/bin/bash", "./run_service.sh"]

USER user