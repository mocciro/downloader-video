import os
from flask import Flask, render_template, request
import yt_dlp

# Konfigurasi folder templates agar terbaca dari dalam folder api
app = Flask(__name__, template_folder='../templates')

# Tambahkan ini agar Vercel mengenali aplikasi sebagai 'app'
application = app

@app.route('/', methods=['GET', 'POST'])
def home():
    video_info = None
    if request.method == 'POST':
        url = request.form.get('url_video')
      ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'check_formats': False,
            # Tambahkan baris di bawah ini:
            'format': 'best[ext=mp4]/best', 
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                video_info = ydl.extract_info(url, download=False)
        except Exception as e:
            print(f"Error: {e}")
            
    return render_template('index.html', video=video_info)

# Baris ini penting untuk local testing tapi tidak masalah jika ada di Vercel
if __name__ == '__main__':
    app.run(debug=True)
