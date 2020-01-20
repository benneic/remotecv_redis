FROM minimalcompact/remotecv:latest

ENV HOME /app
ENV SHELL bash
ENV WORKON_HOME /app
WORKDIR /app

COPY requirements.txt /app/requirements_additional.txt
RUN pip install --trusted-host None --no-cache-dir -r /app/requirements_additional.txt

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["remotecv"]