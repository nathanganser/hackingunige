import pprint

from rdflib import Graph

g = Graph()


def read_local():
    g.parse("../data/demo.ttl", format="turtle")

    print("Triples: {}".format(len(g)))  # prints 2

    for stmt in g:
        pprint.pprint(stmt)

    # prints :
    # (rdflib.term.URIRef('http://bigasterisk.com/foaf.rdf#drewp'),
    #  rdflib.term.URIRef('http://example.com/says'),
    # rdflib.term.Literal('Hello world'))
    # (rdflib.term.URIRef('http://bigasterisk.com/foaf.rdf#drewp'),
    # rdflib.term.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type'),
    # rdflib.term.URIRef('http://xmlns.com/foaf/0.1/Person'))


def read_remote():
    g.parse("http://bigasterisk.com/foaf.rdf")  # default format = xml
    print("Triples: {}".format(len(g)))  # prints 62


def serialize():
    print(g.serialize(format="turtle").decode("utf-8"))  # prints the Graph to the console
    # g.serialize("data/foaf.ttl", format="turtle")  # serializes the Graph


def main():
    read_local()
    # read_remote()
    serialize()


if __name__ == '__main__':
    main()
