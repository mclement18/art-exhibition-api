# BUILDER
FROM python:3.9-alpine as builder

RUN python -m pip install --upgrade build

RUN mkdir /art_exhibition_api
COPY src/ art_exhibition_api/src/
COPY LICENSE MANIFEST.in pyproject.toml README.md setup.cfg /art_exhibition_api/

WORKDIR /art_exhibition_api
RUN python -m build

FROM python:3.9-alpine

COPY --from=builder /art_exhibition_api/dist/art_exhibition_api-*.whl .
RUN python -m pip install art_exhibition_api-*.whl && rm art_exhibition_api-*.whl
RUN python -m pip install gunicorn
ENV FLASK_ENV production
ENV FLASK_DEBUG 0
ENV FLASK_APP art_exhibition_api

EXPOSE 4000
CMD [ "gunicorn", "-w", "4", "-b", "0.0.0.0:4000", "art_exhibition_api:create_app()" ]
