# Use the official Node.js image as the base image
FROM node:14 as build

# Build static frontend
WORKDIR /home/node/app
COPY . .
RUN npm install

CMD ["npm", "run", "serve"]