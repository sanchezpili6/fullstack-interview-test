back:
	pip3 install -r ./backend/requirements.txt
	python3 ./backend/app.py

front:
	cd ./frontend; npm install axios; npm install; npm run serve
