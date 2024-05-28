import redis

r = redis.Redis(
  host='optimum-ringtail-52670.upstash.io',
  port=6379,
  password='Ac2-AAIncDFkMjZhOTk2YmZhNDg0YjQ0OTg4OTc3NmQ3ZjkwNjk3ZHAxNTI2NzA',
  ssl=True
)

r.set('foo', 'bar')
print(r.get('foo'))