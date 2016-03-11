#Run Flask Application

from app import app
from redisTokenSeeder import RedisTokenSeed
redisSeed = RedisTokenSeed()
redisSeed.putTokens()

if __name__ == '__main__': 
    app.run(debug=True, port = 8000)