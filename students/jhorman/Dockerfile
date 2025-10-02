FROM node:20-alpine

RUN addgroup -S app && adduser -S app -G app

WORKDIR /app

COPY package*.json ./

RUN npm install --production

COPY jhorman.js .

RUN mkdir -p /var/log/app && chown -R app:app /var/log/app

USER app

EXPOSE 8080

CMD ["node", "jhorman.js"]
