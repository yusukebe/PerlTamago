これは何？
----------------

Perl初心者向けのごくごくシンプルなサンプルスクリプトを
置いていこうと思います。
「Perlたまご」といいます。
サンプル集たくさんあると思いますが、なんとなく自分で書いてみたかったという
個人的な事情により作って行きます。

CGIの実行方法
----------------

Plackを入れてれば、apache等無しで、plackupコマンドでテスト環境を立ち上げられます。

  plackup -MPlack::App::CGIBin -e 'Plack::App::CGIBin->new(root => "./cgi-bin")->to_app' -R ./cgi-bin

作者
----------------

Yusuke Wada ( yusuke at kamawada.com )


