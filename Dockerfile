FROM ubuntu:22.04

RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list \
  && apt update \
  && DEBIAN_FRONTEND=noninteractive apt install -y libgl1-mesa-dev \
  && DEBIAN_FRONTEND=noninteractive apt install -y mesa-utils \
  && DEBIAN_FRONTEND=noninteractive apt install -y xorg-dev \
  && DEBIAN_FRONTEND=noninteractive apt install -y python3.10 \
  && DEBIAN_FRONTEND=noninteractive apt install -y python3-pip

COPY requirements.txt /tmp/pip-tmp/
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip config set global.extra-index-url https://download.pytorch.org/whl/cu118
RUN pip --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
  && rm -rf /tmp/pip-tmp

WORKDIR /app
COPY app/ ./

EXPOSE 8000
# Start a lone service
#ENTRYPOINT [ "uvicorn", "--reload", "--host", "0.0.0.0", "fastapi_server:app" ]
# Use gui to select and launch service instead
CMD ["python3", "model_selector_gui.py"]