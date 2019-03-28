def pick_bucket(num: int, bucket_num: int = 2) -> int:
    assert bucket_num > 0
    return num % bucket_num
