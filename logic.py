import redis

rd = redis.StrictRedis(host='redis', port=6379)
KEY = 'visit'


def pick_bucket(num: int, bucket_num: int = 2) -> int:
    assert bucket_num > 0
    return num % bucket_num


def auto_incr() -> int:
    rd.incrby(KEY, 2)
    return int(rd.get(KEY))
