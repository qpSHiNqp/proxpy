# proxpy
Clone project from the original [proxpy](https://code.google.com/p/proxpy/ "Link to the original project page").

元祖[proxpy](https://code.google.com/p/proxpy/ "Link to the original project page")のクローンプロジェクトです.


The quoted README from the original project page is placed at the bottom of this file.
In this README file, additional information to original one is written.

元プロジェクトのREADMEがこのファイルの最下部に添付してあります.
このREADMEでは元のREADMEに加えるべき補足的内容を記載しています.

## About - 概要
ProxPy is a really simple HTTP/HTTPS proxy program written in Python.
It is so simple that you can easily customize it or add some plugins into it.
You can run it in your commandline like below:

```
$ cd proxpy/
$ ./proxpy.py
```

ProxPyはPythonで書かれた極めてシンプルなHTTP/HTTPSプロキシです.
シンプルなので, 改変しやすくプラグインも作成しやすいです.
上記のコマンドで, コマンドラインから実行可能です.

## Changes from original - 元プロジェクトからの主な変更点

### Handling on CONNECT method - CONNECTメソッドの処理
In the original handler of CONNECT method, proxpy terminates SSL session and makes a SSL Handshake.
This implementation is wrong, so SSL handling process is changed.
Now proxpy makes a tunnel for SSL payload when CONNECT request is issued. Once a tunnel established, proxpy  terminats only TCP sessions and relays encrypted SSL payloads between two TCP sockets without any changes.
Due to this fix, users now can successfully get secure resources (whose url begins with https~).

元のCONNECTメソッドハンドラでは, proxpy内部でSSLハンドシェイクを行い, 暗号化通信路を終端していた.
これはHTTPプロキシの実装として正しくないので, SSLをトンネルするように変更した.
つまり, proxpy内部ではTCPセッションのみ終端し, その上のペイロードには変更を加えずにサーバ・クライアント間でリレーさせる.
これによりセキュアなリソース(httpsで始まるurlリソース)の取得も正常に行えるようになった.

### License statements - ライセンス記述
There were statements about HyperDbg, which have nothing to do with this project. Deleted it.

HyperDbgに関する記述があったが, 関係ないので修正した.
(ライセンスには詳しくないので, 正しいのかわからない.)

### CORS cheat plugin - ずるしてCORSするためのプラグイン
When a web service which utilizes resources on another site is being tested on local laptop, CORS permission setting is required on the site's server.
However if the testers/developers don't have administrator role on that server, they will have trouble testing their service.
To avoid such trouble, I developed a plugin which relays XMLHttpRequest from the tested service to Origin server, along with removing Origin header in HTTP request.
Just run proxpy with the option `-x plugin/cors.py` to enable this feature, and config HTTP proxy on your browsers.

ローカルPC上で外部サイトのリソースを利用するWebサービスの動作テストを行う場合, 外部サイトのサーバにCORSを許可する設定が必要である.
しかし, 外部サイトのサーバ管理権限を持たない場合はこの設定ができない.
こういったテストの際の不都合を回避するため, テスト対象サービスからのXMLHttpRequestなどにおけるOriginヘッダを消してリクエストを中継するローカルプロキシが欲しかったので作った.
proxpyに _plugin/cors.py_ をプラグインとして読込み, ブラウザにHTTPプロキシとしてproxpyを利用する設定を加えると良い.

```
$ ./proxpy.py -x plugin/cors.py
```

## TODO
To be listed


> ## About
> ProxPy is a highly customizable HTTP/HTTPS proxy, written in Python. It is very handy for web penetration testers and for developers interested in testing their web applications.
> 
> ProxPy works as a "man-in-the-middle" between the browser and the target application. It has been developed with the purpose to be easily customizable. At this aim, users can write plug-in with minimal effort. Plug-ins are written in Python, and can modify HTTP/HTTPS requests and response on-the-fly.
> 
> Please note that ProxPy is currently under heavy development, so the plug-ins interface may change in the near future.
> 
> ## A sample plug-in
> Consider this simple ProxyPy plug-in:
> 
> ```
> def proxy_mangle_request(req):
>     req.setHeader("User-Agent", "ProxPy Agent")
>     return req
> 
> def proxy_mangle_response(res):
>     v = res.getHeader("Content-Type")
>     if len(v) > 0 and "text/html" in v[0]:
>         res.body = res.body.replace("Google", "elgooG")
>     return res
> ```
> 
> If present, the proxy_mangle_request and proxy_mangle_response methods are invoked on each HTTP request and response, respectively. In this example, the plug-in performs the following operations:
> 
> - For each HTTP request, the value of the User-Agent HTTP header is set to "ProxPy Agent"
> - For each HTTP response, any occurrence of the "Google" substring is replaced with "elgooG"
> 
> Obviously real-world plug-ins are typically more complex than this.
> 
> ## Usage
> To test the plug-in described in the previous section, run ProxPy with a command-line similar to the following one:
> 
> ```
> $ ./proxpy.py -x plugins/changeagent.py 
> [*] <b73986c0> Server 0.0.0.0 listening on port 8080
> ```
> 
> Then, the browser should be configured to connect through ProxPy on TCP port 8080. All available command-line options are shown invoking ProxPy with the "-h" switch.

