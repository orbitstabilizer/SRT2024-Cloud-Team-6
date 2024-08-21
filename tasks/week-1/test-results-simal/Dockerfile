# Use Node.js base image
FROM node:14

# Set the working directory inside the container
WORKDIR /app

# Copy the package.json and install dependencies
COPY package.json /app


RUN npm install

COPY . /app

EXPOSE 8080
# Start the app
CMD ["npm", "start"]

