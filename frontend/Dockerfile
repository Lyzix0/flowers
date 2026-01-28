FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Этап 2: Раздача статики через Nginx
FROM nginx:stable-alpine
COPY --from=build /app/dist /usr/share/nginx/html
# Если у вас React/Vue, может понадобиться конфиг для роутинга
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]