FROM continuumio/anaconda3:4.4.0
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install --no-cache-dir -r requirements.txt
CMD python app.py
