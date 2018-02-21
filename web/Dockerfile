FROM node:9-alpine

WORKDIR /app
COPY ./package* ./
RUN npm install

CMD ["npm", "run", "serve"]
