FROM python:3.9

RUN groupadd -r user && useradd -r -g user user

EXPOSE 3000

WORKDIR /entrevistas_microservice

ADD requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

RUN chown -R user:user .
RUN ["chmod", "+x", "run_service.sh"]

CMD ["/bin/bash", "./run_service.sh"]

USER user