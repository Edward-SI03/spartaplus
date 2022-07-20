from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient('15.165.158.21', 27017, username="test", password="test")
db = client.dbsparta_plus_week3


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/matjip', methods=["GET"])
def get_matjip():
    # 맛집 목록을 반환하는 API
    matjip_list = list(db.matjips.find({}, {'_id': False}))
    # matjip_list 라는 키 값에 맛집 목록을 담아 클라이언트에게 반환합니다.
    return jsonify({'result': 'success', 'matjip_list': matjip_list})

@app.route('/likeaddress', methods=["POST"])
def likeaddress():
    title_receive = request.form['title_give']
    print(title_receive)
    db.matjips.update_one({'title': title_receive}, {'$set': {'like': "true"}})
    return jsonify({'result': 'success', 'msg': '이 장소 좋아요'})

@app.route('/dislikeaddress', methods=["POST"])
def dislikeaddress():
    title_receive = request.form['title_give']
    print(title_receive)
    db.matjips.update_one({'title': title_receive}, {'$set': {'like': "no"}})
    return jsonify({'result': 'success', 'msg': '좋아요 취소'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)