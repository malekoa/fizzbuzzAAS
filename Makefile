local:
	flask run --host=0.0.0.0 --debug

css:
	npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch