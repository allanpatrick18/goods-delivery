from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# from project.server.connection import Neo4jConnection


# uri = "bolt://localhost:7687"
# driver = GraphDatabase.driver(uri, auth=("test", "123mudar"))

# conn = Neo4jConnection(uri,"test", "123mudar" )

def create_friend_of(tx, name, friend):

    tx.run("""CREATE 
             (a:Loc {name:"A"}),
             (b:Loc {name:"B"}),
             (c:Loc {name:"C"}),
             (d:Loc {name:"D"}),
             (e:Loc {name:"E"}),
             (f:Loc {name:"F"}),
             (a)-[:ROAD {cost:50}]->(b),
             (a)-[:ROAD {cost:50}]->(c),
             (a)-[:ROAD {cost:100}]->(d),
             (b)-[:ROAD {cost:40}]->(d),
             (c)-[:ROAD {cost:40}]->(d),
             (c)-[:ROAD {cost:80}]->(e),
             (d)-[:ROAD {cost:30}]->(e),
             (d)-[:ROAD {cost:80}]->(f),
             (e)-[:ROAD {cost:40}]->(f)""")


# with driver.session() as session:
#     session.write_transaction(create_friend_of, "Alice", "Bob")
# cqlShorestPath = """MATCH (start:Loc{name:"A"}), (end:Loc{name:"F"})
#                     CALL algo.shortestPath.stream(start, end, "cost")
#                     YIELD nodeId, cost
#                     MATCH (other:Loc) WHERE id(other) = nodeId
#                     RETURN other.name AS name, cost"""
# # with driver.session() as session:
#     # session.write_transaction(create_friend_of, "Alice", "Carl")
#     # Find the shortest path between two nodes..in this case two people
# shortestPath = conn.query(cqlShorestPath)
    # shortestPath = session.run(cqlShorestPath)
    #
    # print("Shortest path between nodes - Ansa and Elias:")

# for record in shortestPath:
#     print(record)

        # nodes = record["R"].nodes
        #
        # for node in nodes:
        #     print(node)

# driver.close()

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
