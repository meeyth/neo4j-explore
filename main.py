from neo4j import GraphDatabase, RoutingControl, Driver

# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
URI = "your uri"
AUTH = ("neo4j", "your password")

def add_friend(driver: Driver, name: str, friend_name: str):
    driver.execute_query(
        "MERGE (a:Person {name: $name}) "
        "MERGE (friend:Person {name: $friend_name}) "
        "MERGE (a)-[:KNOWS]->(friend)",
        name=name, friend_name=friend_name, database_="neo4j",
    )


def print_friends(driver: Driver, name: str):
    records, _, _ = driver.execute_query(
       "MATCH p=()-[:PURCHASED]->() RETURN p LIMIT 3",
        name=name, database_="neo4j", routing_=RoutingControl.READ,
    )
    for record in records:
        print(record["p"])


with GraphDatabase.driver(URI, auth=AUTH) as driver:
    # add_friend(driver, "Arthur", "Guinevere")
    # add_friend(driver, "Arthur", "Lancelot")
    # add_friend(driver, "Arthur", "Merlin")
    print_friends(driver, "Arthur")