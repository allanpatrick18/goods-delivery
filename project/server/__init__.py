# project/server/__init__.py

import os
from flask_migrate import Migrate
from project.server.connection import Neo4jConnection
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from time import time


app = Flask(__name__)

app_settings = os.getenv(
    'APP_SETTINGS',
    'project.server.config.DevelopmentConfig'
)
app.config.from_object(app_settings)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
conn = Neo4jConnection(app.config['DB_URI'], app.config['DB_USER'],
                       app.config['DB_PASSWORD'])

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

# shortestPath = conn.query(routes)
# cqlShorestPath = """MATCH (start:Loc{name:"A"}), (end:Loc{name:"D"})
#                     CALL algo.shortestPath.stream(start, end, "cost")
#                     YIELD nodeId, cost
#                     MATCH (other:Loc) WHERE id(other) = nodeId
#                     RETURN other.name AS name, cost"""
#
#
# shortestPath = conn.query(cqlShorestPath)
# total = 0
# for record in shortestPath:
#     total += record['cost']
#     print(record)
# print(total*(2.5/10))
start_time = int(time())

from project.server.health_check.health_check import health_check_blueprint
app.register_blueprint(health_check_blueprint)