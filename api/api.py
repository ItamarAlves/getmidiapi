import os
from flask  import Flask, request, jsonify
from youtube import Download

app = Flask(__name__)
        
@app.route('/')
def home():
    return jsonify({"Home":"Bem Vindo!"})

@app.route('/download', methods=["POST"])
def downloadVideo():
    print(request.headers)
    print(request.get_json())
    data = request.get_json()
    
    download = Download(data.get('url'))
    print(download)
    download.downloadVideo()

    return jsonify({"Mensagem":"Vídeo Baixado com Sucesso!"})    

if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='192.168.0.103', port=port, debug=True)
    

