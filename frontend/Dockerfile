# Build Vue Application
FROM node:latest AS build-stage
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Create NGINX Server to Host Image
#FROM nginx:latest AS production-stage
#RUN mkdir /app
#COPY --from=build-stage /app/dist /app
#COPY ./nginx/nginx.conf /etc/nginx/nginx.conf

#COPY ./nginx/nginx.conf /etc/nginx/conf.d/nginx.conf
FROM nginx:latest AS production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
