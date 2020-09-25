from flask import Blueprint
from flask.views import MethodView
from project.server import conn
from flask import Blueprint, request, make_response, jsonify

routes_blueprint = Blueprint('routes', __name__,)

class RoutesAPI(MethodView):
    """
    User Resource
    """
    def get(self):
        # get the auth token
        # routes = """ CREATE
        #             (a:Loc {name:"A"}),
        #             (b:Loc {name:"B"}),
        #             (c:Loc {name:"C"}),
        #             (d:Loc {name:"D"}),
        #             (e:Loc {name:"E"}),
        #             (a)-[:ROAD {cost:10}]->(b),
        #             (a)-[:ROAD {cost:20}]->(c),
        #             (b)-[:ROAD {cost:15}]->(d),
        #             (c)-[:ROAD {cost:30}]->(d),
        #             (b)-[:ROAD {cost:50}]->(e),
        #             (d)-[:ROAD {cost:30}]->(e)
        #        """
        #
        # shortestPath = conn.query(routes)
        cqlShorestPath = """MATCH (start:Loc{name:"A"}), (end:Loc{name:"D"})
                            CALL algo.shortestPath.stream(start, end, "cost")
                            YIELD nodeId, cost
                            MATCH (other:Loc) WHERE id(other) = nodeId
                            RETURN other.name AS name, cost"""

        shortestPath = conn.query(cqlShorestPath)
        total = 0
        for record in shortestPath:
            total += record['cost']
            print(record)
        print(total * (2.5 / 10))
        message = {'uptime': '',
                   'version': 1.2,
                   'status': 0
                   }
        response = jsonify(message)
        response.status_code = 200
        return response

        #Todo: get a entidi id from the client e list the alerts from enity
        return make_response(jsonify(responseObject)), 200

    def put(self):
        """This API will update into the database"""



routes_view = RoutesAPI.as_view('route_api')


routes_blueprint.add_url_rule(
    '/route',
    view_func=routes_view,
    methods=['GET']
)