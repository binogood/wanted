# Wecode X Wanted 과제 제출

## 구현방법 및 실행방법

Python Web Framework인 Flask와 DB Sqlite3를 사용하여 구현하였습니다.

MVC패턴을 사용하여 구현을 하였습니다.

MVC패턴에 따라 View(VIEW) > Service(CONTROLLER) > Model(MODEL) > Service(CONTROLLER) > View(VIEW) 순으로 실행이 됩니다.

실행은 python run.py로 실행시키면 서버가 실행이 됩니다.

DB파일은 wanted.db파일입니다.

### User

User는 유저 생성과 유저 로그인 2가지 기능을 구현하였습니다.

#### 유저생성

유저를 생성합니다.

127.0.0.1:5000/user/create로 통신이 가능합니다

키값은 username과 password를 받습니다.

서버 실행후 아래 명령어 입력시 유저 생성이 됩니다.

```
http POST 127.0.0.1:5000/user/create username='song' password='12345678'

HTTP/1.0 200 OK
Access-Control-Allow-Origin: *
Content-Length: 53
Content-Type: application/json
Date: Mon, 25 Oct 2021 16:14:16 GMT
Server: Werkzeug/1.0.1 Python/3.8.5

{
    "message": "USER_CREATED",
    "result": "POST"
}

```

Password는 암호화를 진행하여 DB저장시 암호화된 패스워드가 저장이됩니다.

```
sqlite> select * from users;
1|song|$2b$12$7qj11qpfYEP4fLi3fgzQ.O6kMDoOcG7OimJ45056QlDk/ZAv3X3NS|2021-10-26 01:14:16
```

#### 유저 로그인

생성한 유저로 로그인을 합니다.

http POST 127.0.0.1:5000/user/login로 통신이 가능합니다.

키값은 username과 password를 받습니다.

서버 실행후 아래 명령어 입력시 유저 로그인이 됩니다.

```
http POST 127.0.0.1:5000/user/login username='song' password='12345678'

HTTP/1.0 201 CREATED
Access-Control-Allow-Origin: *
Content-Length: 139
Content-Type: application/json
Date: Mon, 25 Oct 2021 16:17:14 GMT
Server: Werkzeug/1.0.1 Python/3.8.5

{
    "accessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.NnoFLDtoSND5ZMcM40yeECltEKziq-XuW65sMK15KWQ",
    "userId": 1
}
```

로그인을 하면 토큰을 받게 됩니다.

### Post

Post는 CRUD를 구현하였습니다.

C는 로그인이 된 상태에서만 가능합니다.

R은 Detail과 List 2가지로 구현하였습니다. R은 인증이 필요없습니다.

UD는 해당글을 작성한 ID만 가능하도록 구현하였습니다.

#### Create

Create는 로그인이 된 상태에서만 가능합니다.

위에서 로그인하여 얻은 토큰을 사용해야합니다.

키값은 title과 contents 두가지를 받고 있습니다.

```
http POST 127.0.0.1:5000/post/create "Authorization:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.NnoFLDtoSND5ZMcM40yeECltEKziq-XuW65sMK15KWQ" title="test title1" contents="test contents1"

HTTP/1.0 200 OK
Access-Control-Allow-Origin: *
Content-Length: 52
Content-Type: application/json
Date: Mon, 25 Oct 2021 16:29:51 GMT
Server: Werkzeug/1.0.1 Python/3.8.5

{
    "message": "CREATE_POST",
    "resutl": "POST"
}


sqlite> select * from posts;
7|1|test title1|test contents1|2021-10-26 01:29:51|2021-10-26 01:29:51

```

게시글이 생기는 것을 확인이 가능합니다.

#### Read

Read는 Datail view와 list view 2가지를 확인이 가능합니다.

Datail view는 해당 글의 id가 필요합니다.

```
http GET 127.0.0.1:5000/post/7 (해당 글의 ID)
HTTP/1.0 200 OK
Access-Control-Allow-Origin: *
Content-Length: 102
Content-Type: application/json
Date: Mon, 25 Oct 2021 16:34:49 GMT
Server: Werkzeug/1.0.1 Python/3.8.5

{
    "data": [
        "test title1",
        "test contents1",
        "song",
        "2021-10-26 01:29:51"
    ]
}
```

글 제목, 글 내용, 작성자, 작성 시간을 알 수 있습니다.

list view는 기본 limit 10과 offset 0을 설정해 놓아서

최대 10개까지만 출력이 됩니다.

```
http GET 127.0.0.1:5000/post/list

HTTP/1.0 200 OK
Access-Control-Allow-Origin: *
Content-Length: 809
Content-Type: application/json
Date: Mon, 25 Oct 2021 16:40:08 GMT
Server: Werkzeug/1.0.1 Python/3.8.5

{
    "data": [
        [
            "test title1",
            "song",
            "2021-10-26 01:29:51"
        ],
        [
            "test title2",
            "song",
            "2021-10-26 01:32:23"
        ],
        [
            "test title3",
            "song",
            "2021-10-26 01:32:29"
        ],
        [
            "test title4",
            "song",
            "2021-10-26 01:32:34"
        ],
        [
            "test title5",
            "song",
            "2021-10-26 01:32:38"
        ],
        [
            "test title6",
            "song",
            "2021-10-26 01:32:43"
        ],
        [
            "test title7",
            "song",
            "2021-10-26 01:32:47"
        ],
        [
            "test title8",
            "song",
            "2021-10-26 01:32:52"
        ],
        [
            "test title9",
            "song",
            "2021-10-26 01:39:51"
        ],
        [
            "test title10",
            "song",
            "2021-10-26 01:39:56"
        ]
    ]
}

http://127.0.0.1:5000/post/list?limit=12&offset=5
{
    "data": [
        [
            "test title6",
            "song",
            "2021-10-26 01:32:43"
        ],
        [
            "test title7",
            "song",
            "2021-10-26 01:32:47"
        ],
        [
            "test title8",
            "song",
            "2021-10-26 01:32:52"
        ],
        [
            "test title9",
            "song",
            "2021-10-26 01:39:51"
        ],
        [
            "test title10",
            "song",
            "2021-10-26 01:39:56"
        ],
        [
            "test title11",
            "song",
            "2021-10-26 01:40:00"
        ],
        [
            "test title12",
            "song",
            "2021-10-26 01:40:05"
        ]
    ]
}
```

#### Delete

Delete는 작성자만 삭제가 가능합니다.

```
17|1|test title11|test contents11|2021-10-26 01:40:00|2021-10-26 01:40:00
18|1|test title12|test contents12|2021-10-26 01:40:05|2021-10-26 01:40:05
```

17번은 작성자로 지워보고
18번은 작성자가 아닌 계정으로 지워보도록 하겠습니다.

```
http DELETE 127.0.0.1:5000/post/delete/17 "Authorization:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.NnoFLDtoSND5ZMcM40yeECltEKziq-XuW65sMK15KWQ"
HTTP/1.0 200 OK
Access-Control-Allow-Origin: *
Content-Length: 54
Content-Type: application/json
Date: Mon, 25 Oct 2021 16:55:53 GMT
Server: Werkzeug/1.0.1 Python/3.8.5

{
    "message": "DELETE_POST",
    "result": "DELETE"
}

지워지는 것을 확인이 가능합니다.

http DELETE 127.0.0.1:5000/post/delete/18 "Authorization:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyfQ.9C-zQWUWpTby0dnHctaEAP5uNHoVB-0qWOs4I7QElP0"
HTTP/1.0 500 INTERNAL SERVER ERROR
Connection: close
Content-Type: text/html; charset=utf-8
Date: Mon, 25 Oct 2021 16:57:42 GMT
Server: Werkzeug/1.0.1 Python/3.8.5
X-XSS-Protection: 0

raise ApiException(400, NOT_THE_AUTHOR)
responses.ApiException: (400, '글쓴이가 아닙니다')

글이 지워지지 않는것을 확인이 가능합니다.

```

#### Update

Update도 Delete와 같이 작성자만 수정이 가능합니다.

```
아래 글을 수정해보도록 하겠습니다.
18|1|test title12|test contents12|2021-10-26 01:40:05|2021-10-26 01:40:05

http PATCH 127.0.0.1:5000/post/update/18 "Authorization:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.NnoFLDtoSND5ZMcM40yeECltEKziq-XuW65sMK15KWQ" title='change title' contents='합 격하고싶어요'
HTTP/1.0 200 OK
Access-Control-Allow-Origin: *
Content-Length: 53
Content-Type: application/json
Date: Mon, 25 Oct 2021 17:01:07 GMT
Server: Werkzeug/1.0.1 Python/3.8.5

{
    "message": "UPDATE_POST",
    "result": "PATCH"
}

sqlite> select * from posts;
18|1|change title|합격하고싶어요|2021-10-26 01:40:05|2021-10-26 02:06:05

수정이 되는 것을 확인이 가능합니다.
```

따로따로도 수정이 가능합니다.

```
http PATCH 127.0.0.1:5000/post/update/18 "Authorization:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.NnoFLDtoSND5ZMcM40yeECltEKziq-XuW65sMK15KWQ"  contents='합격하고싶어요 꼬오옥'
HTTP/1.0 200 OK
Access-Control-Allow-Origin: *
Content-Length: 53
Content-Type: application/json
Date: Mon, 25 Oct 2021 17:07:45 GMT
Server: Werkzeug/1.0.1 Python/3.8.5

{
    "message": "UPDATE_POST",
    "result": "PATCH"
}

sqlite> select * from posts;
18|1|change title|합격하고싶어요 꼬오옥|2021-10-26 01:40:05|2021-10-26 02:07:45


 http PATCH 127.0.0.1:5000/post/update/18 "Authorization:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.NnoFLDtoSND5ZMcM40yeECltEKziq-XuW65sMK15KWQ"  title='합격시켜주세요요오오'
HTTP/1.0 200 OK
Access-Control-Allow-Origin: *
Content-Length: 53
Content-Type: application/json
Date: Mon, 25 Oct 2021 17:08:40 GMT
Server: Werkzeug/1.0.1 Python/3.8.5

{
    "message": "UPDATE_POST",
    "result": "PATCH"
}

18|1|합격시켜주세요요오오|합격하고싶어요 꼬오옥|2021-10-26 01:40:05|2021-10-26 02:08:40


```

작성자가 아니면 수정이 안됩니다.

```
http PATCH 127.0.0.1:5000/post/update/18 "Authorization:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyfQ.9C-zQWUWpTby0dnHctaEAP5uNHoVB-0qWOs4I7QElP0" title='수정돼라'
HTTP/1.0 500 INTERNAL SERVER ERROR
Connection: close
Content-Type: text/html; charset=utf-8
Date: Mon, 25 Oct 2021 17:10:04 GMT
Server: Werkzeug/1.0.1 Python/3.8.5
X-XSS-Protection: 0

raise ApiException(400, NOT_THE_AUTHOR)
responses.ApiException: (400, '글쓴이가 아닙니다')
```

이상입니다.
