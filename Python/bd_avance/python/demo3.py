from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, FOAF

g = Graph()
bob = URIRef("http://example.org/people/Bob")


def search_bob():
    if (bob, RDF.type, FOAF.Person) in g:
        print("This graph knows that Bob is a person!")

    if (bob, None, None) in g:
        print("This graph contains triples about Bob!")


def search_people():
    for s, p, o in g.triples((None, RDF.type, FOAF.Person)):
        print("{} is a person".format(s))


def get_value():
    g.add((bob, FOAF.name, Literal("Bob")))
    name = g.value(bob, FOAF.name)  # get any name of bob
    print("Bob's name is: {} ".format(name))

    # get the one person that knows bob and raise an exception if more are found
    bob_friend = g.value(predicate=FOAF.knows, object=bob, any=False)
    print(bob_friend)


def main():
    g.parse("../data/demo2.ttl", format="turtle")
    search_bob()
    # search_people()
    # get_value()


if __name__ == '__main__':
    main()
