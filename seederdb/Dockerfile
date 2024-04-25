FROM python:3.7

WORKDIR /app

# Install required packages
RUN pip install pymongo typing

COPY Musique_class.py /app/ 
#copier seeder dans seederdb sous app
COPY seederdb/seeder.py /app/seeder.py 

# Command to run the populate script
CMD ["python", "/app/seeder.py"]