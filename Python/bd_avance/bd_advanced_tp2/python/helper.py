from rdflib import Graph, URIRef, BNode, Literal, Namespace
from rdflib.namespace import FOAF, RDF
from SPARQLWrapper import SPARQLWrapper, JSON

g = Graph()


def add_data(g):
    g.bind("foaf", FOAF)
    # create people nodes
    people_url = "http://example.org/people"
    bob = URIRef(people_url + "/Bob")
    alice = URIRef(people_url + "/Alice")
    nathan = URIRef(people_url + "/Nathan")
    josh = URIRef(people_url + "/Josh")

    # create movie nodes
    movie_url = "https://www.imdb.com/title"
    le_parrain = URIRef(movie_url + "/tt0068646")
    shawshank_redemption = URIRef(movie_url + "/tt0111161")
    dark_knight = URIRef(movie_url + "/tt0468569")
    twelve_angry_men = URIRef(movie_url + "/tt0050083")
    lord_of_the_ring = URIRef(movie_url + "/tt0167260")
    pulp_fiction = URIRef(movie_url + "/tt0110912")
    forrest_gump = URIRef(movie_url + "/tt0109830")

    # person
    g.add((bob, RDF.type, FOAF.Person))
    g.add((alice, RDF.type, FOAF.Person))
    g.add((nathan, RDF.type, FOAF.Person))
    g.add((josh, RDF.type, FOAF.Person))
    g.add((bob, RDF.type, FOAF.Person))

    # knows
    g.add((nathan, FOAF.knows, josh))
    g.add((alice, FOAF.knows, bob))
    g.add((nathan, FOAF.knows, alice))

    # movie
    Movie = URIRef("https://www.imdb.com")
    g.bind("movie", Movie)
    g.add((le_parrain, RDF.type, Movie))
    g.add((shawshank_redemption, RDF.type, Movie))
    g.add((dark_knight, RDF.type, Movie))
    g.add((twelve_angry_men, RDF.type, Movie))
    g.add((lord_of_the_ring, RDF.type, Movie))
    g.add((pulp_fiction, RDF.type, Movie))
    g.add((forrest_gump, RDF.type, Movie))

    g.add((nathan, FOAF.knows, pulp_fiction))
    g.add((alice, FOAF.knows, forrest_gump))
    g.add((josh, FOAF.knows, lord_of_the_ring))
    g.add((bob, FOAF.knows, twelve_angry_men))
    g.add((alice, FOAF.knows, dark_knight))
    g.add((nathan, FOAF.knows, shawshank_redemption))
    g.add((josh, FOAF.knows, le_parrain))

    for s, p, o in g.triples((nathan, FOAF.knows, None)):
        if 'https://www.imdb.com/title/' in o:
            print(f'Nathan has watched the following movie {o}')
        if 'http://example.org' in o:
            print(f'Nathan knows {o}')
            for s, p, o in g.triples((URIRef(o), FOAF.knows, None)):
                print(f'therefore, Nathan might enjoy the following movie: {o}')

def serialize(g):
    print(g.serialize(format="turtle").decode("utf-8"))
    g.serialize("../data/data.ttl", format="turtle")


