# Use an official Python runtime as the parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the local package files to the container's workspace
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Install spacy model
RUN python -m spacy download es_core_news_sm

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run nlp_test.py when the container launches
CMD ["python", "ner_api.py"]
