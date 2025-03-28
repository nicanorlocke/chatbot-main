# Build node.js app
FROM node:14
WORKDIR /home/node/app
COPY . .
RUN npm install
EXPOSE 5000

CMD ["npx", "nodemon", "index.ts"]