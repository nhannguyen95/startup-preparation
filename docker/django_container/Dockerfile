FROM python:3

WORKDIR /root/django_app

# Copy all files in the current dir to `WORKDIR`
# Notice: COPY (and ADD) can't copy the directory
# but instead the files in the directory.
# So if you want to copy the foo directory, do this:
# COPY foo foo (to `WORKDIR`/foo)
# don't do this:
# COPY foo . (this will copy foo/* into .)
COPY . .

RUN pip install -r ./requirements/local.txt

EXPOSE 8080

# Use ENTRYPOINT when you want the container to run as an executable
ENTRYPOINT ["./manage.py"]
CMD ["runserver", "0.0.0.0:8080"]
