FROM node:lts AS development

WORKDIR /code

COPY package.json ./

RUN npm install

COPY . /code

EXPOSE 3000

CMD ["npm", "run", "dev"]