import asyncio
import time
from typing import Any, Callable, TypeVar, Awaitable

T = TypeVar('T')

class RateLimiter:
    def __init__(self, max_calls: int = 2, period: int = 60):
        self.max_calls = max_calls
        self.period = period
        self.calls = []
        self.lock = asyncio.Lock()

    async def wait_if_needed(self):
        """Waits if query limit is reached"""
        async with self.lock:
            now = time.time()
            self.calls = [call for call in self.calls if call > now - self.period]

            if len(self.calls) >= self.max_calls:
                wait_time = self.period - (now - min(self.calls)) + 1
                print(f"The query limit has been reached, waiting {wait_time:.2f}s")
                await asyncio.sleep(wait_time)

            self.calls.append(time.time())

    async def apply(self, func: Callable[..., Awaitable[T]], *args, **kwargs) -> T:
        """Applies rate limiting to an asynchronous function"""
        await self.wait_if_needed()
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            if "rate_limit_exceeded" in str(e):
                print("Query limit encountered, waiting time 20 seconds...")
                await asyncio.sleep(20)
                return await self.apply(func, *args, **kwargs)
            raise e
