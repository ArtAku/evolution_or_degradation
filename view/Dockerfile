FROM node:15.10.0-alpine3.13

WORKDIR /app

COPY *.json ./
RUN npm ci

COPY ./*.ts ./
RUN npm install -g typescript
RUN tsc -p tsconfig.json

ENTRYPOINT [ "node", "./main.js" ]
