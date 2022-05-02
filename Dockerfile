FROM quay.io/centos/centos:stream8

RUN dnf update -y && \
    dnf install -y \ 
    gcc \
    krb5-devel \
    python3-devel

ENV HOME /home/usr
RUN useradd -r -d $HOME usr
RUN usermod -aG wheel usr

RUN mkdir app

WORKDIR $HOME/app

RUN chown -R usr:wheel $HOME/app

COPY --chown=usr:wheel ./hello.py $HOME/app
COPY --chown=usr:wheel ./requirements.txt $HOME/app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "./hello.py"]

USER usr
