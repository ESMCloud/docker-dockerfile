# premier dockerfile


FROM fedora:latest

RUN dnf update -y
RUN dnf install wget tar git -y
#RUN wget

WORKDIR /home/work

COPY Chinook_Sqlite.sqlite /home/work
COPY row_factory_sql.py /home/work

CMD ["python3", "row_factory_sql.py"]

