FROM python:3

ADD book.py /

CMD [ "python", "./book.py" ]
