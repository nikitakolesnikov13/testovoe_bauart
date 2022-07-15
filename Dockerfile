FROM python:3.9

ARG CRYPTOGRAPHY_DONT_BUILD_RUST

RUN apt update \
    && apt install -y gcc musl-dev libffi-dev openssl make libaio-dev


COPY . .

RUN pip install uvicorn[standard]
RUN pip install --no-cache-dir poetry
RUN poetry install

WORKDIR /src

# ADD ansible_version.txt

CMD /.venv/bin/uvicorn main:app --host=0.0.0.0 --port=8000