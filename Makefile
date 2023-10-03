ifneq (,$(wildcard ./.env))
    include .env
    export
endif


.PHONY: build-static
build-static:
	tailwindcss --minify -i src/static/css/tw.css -o src/static/css/main.css

.PHONY: run-static
run-static:
	tailwindcss --watch -i src/static/css/tw.css -o src/static/css/main.css

.PHONY: vendor-static
vendor-static:
	wget -O src/static/js/htmx.min.js https://unpkg.com/htmx.org@1.9.6/dist/htmx.min.js
	wget -O src/static/js/htmx.js https://unpkg.com/htmx.org@1.9.6/dist/htmx.js

.PHONY: run
run:
	uvicorn --app-dir src app.main:app --host=127.0.0.1 --port=8080 --reload --log-level=debug
