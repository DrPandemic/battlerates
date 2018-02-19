FROM node:9-alpine

WORKDIR /app
COPY package* ./
RUN npm install
COPY app.js/ ./
COPY src/ ./src/

CMD ["npm", "start"]