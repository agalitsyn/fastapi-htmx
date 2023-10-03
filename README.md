Attempt to implement web application without JS frameworks, like React.

- FastAPI for all HTTP stuff
    - But FastAPI is for APIs, why not Django? And you are correct, FastAPI is not required here, I used it just as minimal and modern tool (async, typings), and none of "modern" features are required. Use Django.
- SQLAlchemy for defining storage models and building SQL queries.
- Pydantic for defining schemas and validate them, but there is no schemas except config when you use templates.
- Jinja2 for templating.
- TailwindCSS as CSS framework.
- Flowbite + Alpine.js for components library.
- HTMX for communication with backend.
