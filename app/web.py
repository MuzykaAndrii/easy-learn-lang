from app import app
from app.models import User, Bundle

@app.route('/index')
def index():
    return 'It works!'

@app.route('/api/<int:user_id>/<int:bundle_id>')
def get_bundle(user_id, bundle_id):
    user = User.query.first_or_404(user_id)
    bundle = Bundle.query.filter(Bundle.id == bundle_id, Bundle.creator_id == user_id).first_or_404()

    return bundle.words