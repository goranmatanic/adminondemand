FROM node:alpine as build
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
CMD ["npm", "run", "prod"]