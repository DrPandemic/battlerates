FROM nginx:alpine

WORKDIR /app
COPY ./web/dst/ ./dst/
COPY ./edge/nginx.conf /etc/nginx/nginx.conf
COPY ./edge/mime_types /etc/nginx/mime_types

CMD ["nginx", "-g", "daemon off;"]
