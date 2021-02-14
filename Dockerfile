FROM python
RUN pip install Flask flask-restful psycopg2 pyyaml requests lxml -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
WORKDIR /app
ENV FLASK_ENV=development
COPY . /app
ENTRYPOINT ["flask","run", "--host=0.0.0.0", "--port=80"]