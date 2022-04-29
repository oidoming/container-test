FROM quay.io/centos/centos:stream8

RUN dnf update -y && \
    dnf install -y \ 
    python3-devel

COPY ./hello.py $HOME/

ENTRYPOINT ["python3", "./hello.py"]
