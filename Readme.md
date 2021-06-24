# Readme

### 실습 목적
1. Coroutine을 이용한 비동기 HTTP 요청 이해하기
2. Python GIL의 대안 찾기 

### 의존성 추가 관련
코루틴을 이용한 방식이 가시적인 성능 향상을 가져오지 않는다면, 두가지 원인을 의심해볼 수 있다.    
첫째는 aiohttp의 통신에 필요한 DNS resolve가 느리기 때문이다.    
둘째는 aiohttp는 기본적으로 res.text()에 대하여 chardet을 적용하기 때문이다.     

전자는 aiodns, 후자는 cchardet을 설치하면(코드는 그대로, 의존성만 추가하면) 속도가 빨라지게 된다.

`$ pip install aiodns cchardet`

### Reference
- [참고1](https://blog.humminglab.io/python-coroutine-programming-1/)
- [참고2](https://blog.weirdx.io/post/52588)
- [참고3](https://gist.github.com/mjhans/47d65ee9d95d9b4d3195531d9be2be17#asyncio)
