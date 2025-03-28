# Use the official Node.js image as the base image
FROM node:14 as build

# Build static frontend
WORKDIR /home/node/app
COPY ./chatbot-frontend .
RUN npm install
RUN npm run build

# Build node.js app
FROM node:14 as production
WORKDIR /home/node/app
COPY --from=build /home/node/app/dist ./dist
COPY ./chatbot-backend .
RUN npm install
RUN npm run build
EXPOSE 3000

CMD ["npm", "start"]