
from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from project.server import start_time, time
health_check_blueprint = Blueprint('health_check', __name__,)


class HealthCheckAPI(MethodView):
    """
    User Resource
    """
    def get(self):
        # get the auth token
        uptime = int(time()) - start_time
        message = {'uptime': uptime,
                   'version': 1.2,
                   'status': 0
                   }
        response = jsonify(message)
        response.status_code = 200
        return response

        #Todo: get a entidi id from the client e list the alerts from enity
        return make_response(jsonify(responseObject)), 200



health_view = HealthCheckAPI.as_view('health_check_api')



health_check_blueprint.add_url_rule(
    '/status',
    view_func=health_view,
    methods=['GET']
)