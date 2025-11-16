FROM redis:8.4-rc1-alpine

COPY ./conf/pokedex-redis.conf /usr/local/etc/redis/redis.conf

CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]


