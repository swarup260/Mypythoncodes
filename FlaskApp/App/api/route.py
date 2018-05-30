from flask import Blueprint,jsonify


mod = Blueprint('api',__name__)

@mod.route('/')
def test():
    return jsonify("'msg':'Flask App Working'")


# @mod.errorhandler(404)
# def page_not_found(e):
#     return jsonify('invalid request')

# @mod.route('/find/<name>')
# def find(name):
#     user = mongo.db.users
#     result = user.find_one({'name': name})
#     if result:
#         output = [{"name": result['name']}]
#         return jsonify({'result': output})
#     else:
#         return jsonify({'result': 'NOt found'})


# @mod.route('/select')
# def select():
#     user = mongo.db.users
#     result = []
#     for a in user.find():
#         result.append({"name": a['name']})
#     return jsonify({'result': result})


# @mod.route('/add/<name>/<password>')
# def add(name, password):
#     user = mongo.db.users
#     user.insert({'name': name, 'password': password})
#     return "<h1>User ADD</h1>"
