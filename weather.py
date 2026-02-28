from http.server import BaseHTTPRequestHandler
import urllib.request
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 東京湾付近の緯度・経度を指定して気象データを要求
        url = "https://api.open-meteo.com/v1/forecast?latitude=35.6&longitude=139.8&current_weather=true"
        
        try:
            # 外部のAPIからデータを取得
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                weather = data.get('current_weather', {})
                wind_speed_kmh = weather.get('windspeed', 0)
                wind_dir = weather.get('winddirection', 0)
                
                # 風速をkm/hからm/sに変換して分かりやすくする
                wind_ms = round(wind_speed_kmh * 1000 / 3600, 1)
                
                result_text = f"風速: {wind_ms} m/s\n風向: {wind_dir}度"
        except Exception as e:
            result_text = "気象データの取得に失敗しました。"

        # 取得したデータを画面側にJSON形式で返す
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response_data = {
            "message": result_text
        }
        self.wfile.write(json.dumps(response_data).encode('utf-8'))
        return