echo "BUILD START"
python3.10.7 -m pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
echo "BUILD END"