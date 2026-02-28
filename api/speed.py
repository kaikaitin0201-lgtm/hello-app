from http.server import BaseHTTPRequestHandler
from urllib import parse
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # URLから送られてきたデータ（ノット）を取得
        url_parts = parse.urlsplit(self.path)
        query_string = dict(parse.parse_qsl(url_parts.query))
        
        try:
            knots = float(query_string.get("knots", 0))
            # 1ノット = 1.852 km/h で計算
            kmh = knots * 1.852
            result_text = f"{knots}ノットは、時速 {kmh:.2f} km です。"
        except ValueError:
            result_text = "正しい数値を入力してください。"

        # フロントエンド（画面）へJSON形式で結果を返す設定
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response_data = {
            "message": result_text
        }
        self.wfile.write(json.dumps(response_data).encode('utf-8'))
        return