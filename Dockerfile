FROM mcr.microsoft.com/devcontainers/python:0-3.11

COPY requirements.txt /tmp/pip-tmp/
RUN pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 config set global.extra-index-url https://download.pytorch.org/whl/cu118
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
  && rm -rf /tmp/pip-tmp
RUN pip3 install dearpygui

WORKDIR /app
COPY app/ ./

EXPOSE 8000
# Start a lone service
#ENTRYPOINT [ "uvicorn", "--reload", "--host", "0.0.0.0", "fastapi_server:app" ]
# Use gui to select and launch service instead
CMD ["python", "model_selector_gui.py"]