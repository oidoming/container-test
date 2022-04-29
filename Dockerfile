FROM quay.io/centos/centos:stream8

RUN dnf update -y && \
    dnf install -y \ 
    python3-devel

ENV HOME /home/usr
RUN useradd -r -d $HOME usr
RUN usermod -aG wheel usr

WORKDIR $HOME

RUN chown -R usr:wheel $HOME

COPY --chown=usr:wheel ./hello.py $HOME/

RUN chgrp -R 0 $HOME && \
    chmod -R g=u $HOME

USER 1001

ENTRYPOINT ["python3", "./hello.py"]
