FROM node:20-alpine
WORKDIR /projects
RUN npm install -g @angular/cli@17.3.1
RUN npm install --save-dev @angular/cli @angular-devkit/build-angular
RUN npm install
EXPOSE 4200
CMD ["ng", "serve", "--host", "0.0.0.0"]