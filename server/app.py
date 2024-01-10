from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

# - GET /messages: returns an array of all messages as
#   JSON, ordered by created_at in ascending order.
# - POST /messages: creates a new message with a body 
#   and username from params, and returns the newly 
#   created post as JSON.
# - PATCH /messages/<int:id>: updates the body of the 
#   message using params, and returns the updated 
#   message as JSON.
# - DELETE /messages/<int:id>: deletes the message from
#   the database.
@app.route('/messages', methods=['GET','POST'])
def messages():
    if request.method == 'GET':
        message_get = Message.query.order_by(Message.created_at).all()
        message_get_list = [msg.to_dict() for msg in message_get]
        return make_response(message_get_list,200)
    elif request.method == 'POST':
        data = request.get_json()
        message_post = Message(
            username=data["username"],
            body=data["body"]
        )
        db.session.add(message_post)
        db.session.commit()
        return make_response(message_post.to_dict(),201)

@app.route('/messages/<int:id>', methods=['PATCH','DELETE'])
def messages_by_id(id):
    if request.method == 'PATCH':
        message_patch = Message.query.filter_by(id=id).first()
        data = request.get_json()
        for attr in data:
            setattr(message_patch, attr, data[attr])
        db.session.add(message_patch)
        db.session.commit()
        message_patch_dict = message_patch.to_dict()
        return make_response(message_patch_dict, 200)
    elif request.method == 'DELETE':
        message_delete = Message.query.filter_by(id=id).first()
        db.session.delete(message_delete)
        db.session.commit()
        return make_response({'message':'post deleted'}, 200)

if __name__ == '__main__':
    app.run(port=5555)
