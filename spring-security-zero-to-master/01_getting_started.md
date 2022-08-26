# Build Spring Boot Application

1. Getting Started.

Spring Initializer 를 사용하여 심플한 스프링 앱을 빌드한다.
의존성에 다음을 추가함.

- Spring Web

스프링 부트 스타터에 의해 필요한 모든 의존성이 구성됨.

1. REST API 를 구성. (Controller Hello World)
    - 보안이 없는 API 구성 완료.

2. 의존성에 Spring Security 를 추가.
    - 접근하려고 하면 로그인을 요청하게 됨.
    - user / 자동 생성 비밀번호로 로그인 가능. (Console 에 있음.)
3. application.properties 파일 수정
```YAML
spring.security.user.name=username
spring.security.user.password=password
```
아이디 비밀번호를 지정할 수 있게 된다. (자동생성 X)

## How it work?

1. 미인증 상태로 API 에 접근
2. Spring Security 가 로그인을 요구
3. 로그인 후에는 인증이 되어 서버가 쿠키를 기억함
4. 해당 쿠키를 이용해 접근을 하면, 다시 로그인을 요구 받지 않음. (인증이 저장)

## Spring Security Internal Flow 

0. User entered credentials
1. Authentication Filter
2. Authentication
3. Authentication Manager
4. Authentication Provider
    - Where decide if user is authenticated or not.
    5. User Details Service
    6. Password Encoder
7. Authentication Manager
8. Authentication Filter
9. Security Context 
    - Where the data whether the user is authenticated or not is stored.
10. User get authenticated
