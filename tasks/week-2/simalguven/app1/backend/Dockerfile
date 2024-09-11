# Base image for backend
FROM node:14-alpine

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .
RUN npm install

# Copy the rest of the backend files
COPY . .

# Expose port 3000 and start the backend
EXPOSE 3000
CMD ["npm", "start"]
