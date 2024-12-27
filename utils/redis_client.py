import datetime

import redis

from config.config import project_config


class RedisClient:
    def __init__(self, redis_url: str, rate_limit: int = 2):
        self.rate_limit = rate_limit
        self.redis_client = redis.from_url(
            redis_url,
            decode_responses=True
        )

    def _get_redis(self) -> redis.Redis:
        return self.redis_client

    def set_ton_to_usdt(self, value):
        redis = self._get_redis()

        cache_key = f"ton_to_usdt"

        return redis.set(
            name=cache_key,
            value=value,
            ex=15
        )

    def get_ton_to_usdt(self):
        redis = self._get_redis()

        cache_key = f"ton_to_usdt"

        return redis.get(
            name=cache_key,
        )

    def check_throttle(self, user_id: str) -> tuple[bool, int]:
        """
        Проверяет троттлинг и возвращает статус и оставшееся время
        Returns:
            tuple: (is_throttled, time_left_seconds)
        """
        key = f"throttle:{user_id}"
        ttl = self.redis_client.ttl(key)

        if ttl > 0:
            return True, ttl
        return False, 0

    def set_throttle(self, user_id: str, throttle_time: int):
        """Устанавливает троттлинг для пользователя на заданное время"""
        self.redis_client.setex(
            f"throttle:{user_id}",
            throttle_time,
            1
        )

    def set_transaction(self,  transaction_id: int):
        redis = self._get_redis()

        cache_key = f"transaction:{transaction_id}"

        redis.set(
            cache_key,
            str(datetime.datetime.now()),
            ex=datetime.timedelta(seconds=60)
        )

    def get_transaction(self,  transaction_id: int):
        redis = self._get_redis()

        cache_key = f"transaction:{transaction_id}"

        return redis.get(
            cache_key,
        )


redis = RedisClient(
    redis_url=project_config.REDIS_URL
)
