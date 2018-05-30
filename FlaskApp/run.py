from App import app
from flask import request,jsonify,render_template


@app.errorhandler(404)
@app.errorhandler(405)
def _handle_api_error(ex):
    if request.path.startswith('/api/'):
        return jsonify({'msg':'invalid url'})
    else:
        return render_template('404.html')


app.run(debug=True)

