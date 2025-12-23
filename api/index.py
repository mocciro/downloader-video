from flask import Flask, render_template, request
import yt_dlp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    video_info = None
    if request.method == 'POST':
        url = request.form.get('url_video')
        # Settingan agar pencarian kilat
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'check_formats': False, 
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                video_info = ydl.extract_info(url, download=False)
        except Exception as e:
            print(f"Error: {e}")
            
    return render_template('index.html', video=video_info)

if __name__ == '__main__':
    app.run(debug=True)
