from flask import Flask 
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        dict = {'status':200, 'message':'Success'}
        return dict
class GetMessageByID(Resource):
    def get(self, id):
        dict = {'status':200, 'id':id, 'message':'Success'}
        return dict
class GetMessage(Resource):
    def get(self, id):
        dict = {'status':200, 'msgid':id, 'message':'Success'}
        return dict

api.add_resource(HelloWorld, '/')
api.add_resource(GetMessageByID,'/<int:id>')
api.add_resource(GetMessage,'/message/<string:id>')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
