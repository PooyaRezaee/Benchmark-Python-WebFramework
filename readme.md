# Test speed web frameworks python


## Hello-World Test
- ASGI Server uvicorn
- python 3.10.5
- one worker

| Web Framework | request/secound in 100 request | request/secound in 5000 request |
| ------------- | ------------- | ------------- |
| FastApi  | 200 | 189 |
| Django  | 88 | 76 |
| Flask  | 162 | 166 |

Full Result in hello-world/first.txt


## How do test
Runned each web-framework by uvicorn(Ports: djnago=8000 fastapi=7000 flask=5000)
```bash
uvicorn --port port file:app
```

then use [loadtest](https://www.npmjs.com/package/loadtest/) version:5.2.0
```bash
loadtest -n count-requests url
```