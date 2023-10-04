#!/bin/sh
# Make migrations if required
echo "here"
echo $MAKE_MIGRATIONS
echo "here"
if [ $MAKE_MIGRATIONS = "True" ]; then
  echo "Making migrations..."
  python manage.py makemigrations
fi

if [ $MIGRATE = "True" ]; then
  echo "Migrating database..."
  python manage.py migrate
fi

if [ $COLLECT_STATIC = "True" ]; then
  echo "Collecting static files..."
  python manage.py collectstatic --no-input
fi


#Does a superuser need to be created?
echo "Checking for existent superuser"
if [ $SUPERUSER = "False" ]; then
  echo "Creating superuser..."
  python manage.py createsuperuser --noinput
fi

# start development server
python3 manage.py runserver 0.0.0.0:$PORT