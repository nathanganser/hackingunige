import pprint

from rdflib import Graph, URIRef, BNode, Literal, Namespace
from rdflib.namespace import FOAF, RDF

g = Graph()
res = {}


def create_nodes():
    bob = URIRef("http://example.org/people/Bob")

    linda = BNode()  # Blank Node, a GUID is generated

    name = Literal('Bob')  # passing a string
    age = Literal(24)  # passing a python int
    height = Literal(76.5)  # passing a python float

    n = Namespace("http://example.org/people/")
    alice = n.Alice  # = rdflib.term.URIRef(u'http://example.org/people/Alice')

    res['bob'] = bob
    res['linda'] = linda
    res['name'] = name
    res['age'] = age
    res['height'] = height
    res['alice'] = alice

    for k, v in res.items():
        print(k, end=" --> ")
        pprint.pprint(v)


def add_nodes():
    g.bind("foaf", FOAF)  # creates the "foaf" prefix

    # adds a triple to the graph
    # s                               p        o
    # <http://example.org/people/Bob> rdf:type foaf:Person
    bob = URIRef("http://example.org/people/Bob")
    g.add((bob, RDF.type, FOAF.Person))


    n = Namespace("http://cui.unige.ch/people/")  # defines a new namespace
    ashley = n.Ashley  # creates a new node
    g.add((bob, FOAF.knows, ashley))
    # Adding triples:

    # <http://cui.unige.ch/people/Ashley> foaf:knows <http://example.org/people/Bob>
    g.add((ashley, FOAF.knows, res['bob']))

    # http://cui.unige.ch/people/Ashley> rdf:type foaf:Person
    g.add((ashley, RDF.type, FOAF.Person))

    # Sometimes only one value per resource makes sense (i.e. with max-cardinality = 1)
    # use set() instead of add()
    g.set((res['bob'], FOAF.age, Literal(20)))

    print(g.serialize(format="turtle").decode("utf-8"))


def remove_nodes():
    # removes all the triples that match with
    # s                                   p o
    # <http://cui.unige.ch/people/Ashley> * *
    g.remove((URIRef("http://cui.unige.ch/people/Ashley"), None, None))

    print(g.serialize(format="turtle").decode("utf-8"))


def main():
    create_nodes()
    add_nodes()
    # remove_nodes()
    g.serialize("../data/demo2.ttl", format="turtle")  # serializes the Graph


if __name__ == '__main__':
    main()
