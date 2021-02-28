FROM node:15.10.0-alpine3.13

WORKDIR /app

COPY *.json ./
RUN npm ci

COPY ./*.js .

ENTRYPOINT [ "node", "./main.js" ]
