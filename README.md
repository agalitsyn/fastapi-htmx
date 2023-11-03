Attempt to implement web application without JS frameworks, like React.

- FastAPI for all HTTP stuff
- SQLAlchemy for defining storage models and building SQL queries.
- Pydantic for defining schemas and validate them, but there is no schemas except config when you use templates.
- Jinja2 for templating.
- TailwindCSS as CSS framework.
- Flowbite + Alpine.js for components library.
- HTMX for communication with backend.

Q: But FastAPI is for APIs, why not Django?
A: FastAPI is not required here, I used it just for fun, as minimal and modern web python engine (async, typings). None of "modern" features are required for building web app with templates and htmx. Use Django, Luke.
