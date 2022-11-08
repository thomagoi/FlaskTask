from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, abort, reqparse
from flask_marshmallow import Marshmallow

app = Flask(__name__)
api = Api(app) #init that restful api
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name= {self.name}, views= {self.views}, likes= {self.likes})"

class VideoSchema(ma.Schema): #creates a schema for the VideoModel
    class Meta: #options object for schema 
        fields = ("id", "name", "views", "likes") #fields to include in serialized result
        #exclude = () #fields to exclude
        model = VideoModel

video_schema = VideoSchema() #used for single video
videos_schema = VideoSchema(many=True) #used for multiple videos


# video_put_args = reqparse.RequestParser() # parses the input into json format
# video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
# video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
# video_put_args.add_argument("likes", type=int, required=True)

videos = {}

def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="Could not find video")

def abort_if_video_exists(video_id):
    if video_id in videos:
        abort(409, message="Video already exists")


class VideoList(Resource):
    def get(self):
        # result = VideoModel.query.get(id=video_id)
        # return result
        videos = VideoModel.query.all()
        return videos_schema.dump(videos)

    def post(self):
        new_video = VideoModel(
            name = request.json['name'],
            views = request.json['views'],
            likes = request.json['likes']
        )

        db.session.add(new_video)
        db.session.commit()
        return video_schema.dump(new_video)

api.add_resource(VideoList, "/videos")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
