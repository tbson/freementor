FROM nginx:1.12.1
RUN mkdir /resource
RUN mkdir /resource/ssl
RUN mkdir /resource/public
ADD ./cors /etc/nginx
WORKDIR /resource
