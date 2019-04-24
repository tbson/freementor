server {
    listen 80;
    server_name my.domain;
    root /resource/public/__app_name__;
    index index.html;
    location ~ /.well-known {
        allow all;
    }
    location / {
        return 301 https://$server_name$request_uri;
    }
}

server {
    listen 443 ssl http2 default_server;
    server_name my.domain;
    root /resource/public/__app_name__;
    index index.html;
    charset utf-8;

    ssl on;
    ssl_certificate /resource/ssl/live/my.domain/fullchain.pem;
    ssl_certificate_key /resource/ssl/live/my.domain/privkey.pem;

    location /api/v1/ {
        include cors;
        proxy_pass http://__app_name___api:8001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /dadmin/ {
        proxy_pass http://__app_name___api:8001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /schemas/ {
        proxy_pass http://__app_name___api:8001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /public {
        try_files $uri $uri/ /index.html;
        rewrite ^/public(/.*)$ $1 break;
        add_header Access-Control-Allow-Origin *;
    }

    location /public/media {
        try_files $uri $uri/ /index.html;
        rewrite ^/public(/.*)$ $1 break;
        add_header Access-Control-Allow-Origin *;

        expires 7d;
        access_log off;
        add_header Cache-Control "public";
    }

    location / {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        if ($http_user_agent ~ (facebookexternalhit|Twitterbot|Googlebot|Slack|LinkedInBot|Pinterest)) {
            proxy_pass http://__app_name___api:8001;
            break;
        }
        root /resource/public/__app_name__/clients/front;
        try_files $uri $uri/ /index.html =404;
        add_header Access-Control-Allow-Origin *;

        # expires 7d;
        # add_header Cache-Control "public";
    }

    location /admin {
        root /resource/public/__app_name__/clients;
        try_files $uri $uri/ /admin/index.html =404;
        add_header Access-Control-Allow-Origin *;
    }

    location /user {
        root /resource/public/__app_name__/clients;
        try_files $uri $uri/ /user/index.html =404;
        add_header Access-Control-Allow-Origin *;
    }
}
