# Этап сборки
FROM node:20-alpine AS build
WORKDIR /app

# Сначала копируем только файлы зависимостей (используем кеш, если они не менялись)
COPY frontend/package*.json ./
RUN npm install

# Копируем исходники и собираем проект
COPY frontend/ .
RUN npm run build

# Этап запуска
FROM nginx:stable-alpine

# Очищаем дефолтные файлы nginx (на всякий случай)
RUN rm -rf /usr/share/nginx/html/*

COPY yandex_*.html /usr/share/nginx/html/
COPY google*.html /usr/share/nginx/html/

COPY --from=build /app/dist /usr/share/nginx/html

# Копируем конфиг. Путь относительно корня проекта
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]