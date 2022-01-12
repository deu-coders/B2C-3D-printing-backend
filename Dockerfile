FROM python:3.8


# Download wait-for-it.sh
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /
RUN chmod +x /wait-for-it.sh


WORKDIR /app


# Install pip modules
COPY requirements.txt .
RUN pip install -r requirements.txt


# Add source codes
COPY . .
RUN chmod +x entrypoint.sh


# Set up environment variable
ENV PYTHONUNBUFFERED=0


# Set entry point
CMD ["bash", "-c", "./entrypoint.sh"]