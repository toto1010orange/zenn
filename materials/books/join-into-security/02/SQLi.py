from http.server import HTTPServer, BaseHTTPRequestHandler
import sqlite3
import urllib.parse

# 1. データベースの初期化とサンプルデータの作成
def init_db():
    conn = sqlite3.connect(':memory:')  # メモリ上に一時的なDBを作成
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    ''')
    cursor.execute("INSERT INTO users (username, password) VALUES ('alice', 'secret123')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('bob', 'password567')")
    conn.commit()
    return conn

conn = init_db()

# 2. Webサーバーの処理定義
class RequestHandler(BaseHTTPRequestHandler):
    # GETリクエスト：ログインフォームを表示
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        html = '''
            <h2>ログインフォーム</h2>
            <form method="POST">
                ユーザー名: <input type="text" name="username"><br><br>
                パスワード: <input type="password" name="password"><br><br>
                <input type="submit" value="ログイン">
            </form>
        '''
        self.wfile.write(html.encode('utf-8'))

    # POSTリクエスト：フォーム送信後の認証処理
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = urllib.parse.parse_qs(post_data)
        
        input_username = params.get('username', [''])[0]
        input_password = params.get('password', [''])[0]

        # 脆弱なSQLクエリ（SQLインジェクション学習用）
        cursor = conn.cursor()
        query = f"SELECT username FROM users WHERE username = '{input_username}' AND password = '{input_password}'"
        
        try:
            cursor.execute(query)
            result = cursor.fetchone()
        except Exception as e:
            result = None

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        if result:
            response_text = f"<h1>HELLO {result[0]}</h1>"
        else:
            response_text = "<h1>ログイン失敗</h1><a href='/'>戻る</a>"
            
        self.wfile.write(response_text.encode('utf-8'))

# 3. サーバーの起動
if __name__ == '__main__':
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("サーバーを起動しました: http://localhost:8000")
    print("停止するには Ctrl+C を押してください")
    httpd.serve_forever()
