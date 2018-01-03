FROM nginx:1.13.3

RUN rm /etc/nginx/nginx.conf
COPY configuracionnginx.conf /etc/nginx/

RUN rm /etc/nginx/conf.d/default.conf
COPY proyecto.conf /etc/nginx/conf.d/
