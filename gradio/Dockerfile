FROM svizor/zoomcamp-model:3.11.5-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["gradio_interface.py", "model.bin", "dv.bin", "./"]

EXPOSE 7860

CMD ["python", "gradio_interface.py"]
