from SPARQLWrapper import SPARQLWrapper, JSON
from flask import Flask, render_template
from helper import add_data, serialize
from rdflib import Graph, URIRef, BNode, Literal, Namespace
from rdflib.namespace import FOAF, RDF

app = Flask(__name__)
g = Graph()
add_data(g)


@app.route('/')
def index():
    sparql = SPARQLWrapper("https://dbpedia.org/sparql/")

    sparql.setQuery("""
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX dbo: <http://dbpedia.org/ontology/>
            SELECT ?movie ?gross
            WHERE { ?movie a dbo:Film .
                    ?movie dbo:budget  ?gross . 
            FILTER ( ?gross >= "6.963E8"^^<http://dbpedia.org/datatype/Currency> )
            }
            LIMIT 100
        """)
    sparql.setReturnFormat(JSON)
    triples = sparql.query().convert()
    print(triples["results"]["bindings"])
    return render_template('index.html', triples=triples["results"]["bindings"])


@app.route('/movie/<uri>')
def get_movie(uri):
    data = {}
    sparql = SPARQLWrapper("https://dbpedia.org/sparql/")

    # abstract
    sparql.setQuery("""
                PREFIX dbo: <http://dbpedia.org/ontology/>
                SELECT ?c
                WHERE { <http://dbpedia.org/resource/""" + str(uri) + """> dbo:abstract ?c }
                LIMIT 100
            """)
    sparql.setReturnFormat(JSON)
    triples = sparql.query().convert()
    data['abstract'] = triples["results"]["bindings"][0]['c']['value']

    # title
    data['title'] = uri
    print('got the title')

    # director
    sparql.setQuery("""
                    PREFIX dbp: <http://dbpedia.org/property/>
                    SELECT ?c
                    WHERE { <http://dbpedia.org/resource/""" + str(uri) + """> dbp:director ?c }
                    LIMIT 100
                """)
    sparql.setReturnFormat(JSON)
    triples = sparql.query().convert()
    data['director'] = triples["results"]["bindings"][0]['c']['value'].replace("http://dbpedia.org/resource/", "")
    print('got the director ' + data['director'])

    sparql.setQuery("""
                        PREFIX dbr: <http://dbpedia.org/resource/>
                        PREFIX dbo: <http://dbpedia.org/ontology/>
                        SELECT ?movie
                        WHERE { ?movie dbo:director dbr:""" + data['director'].replace(" ", "_") + """ }
                        LIMIT 100
                    """)
    sparql.setReturnFormat(JSON)
    triples = sparql.query().convert()
    # print(triples["results"]["bindings"])
    data['same_director'] = []
    for movie in triples["results"]["bindings"]:
        data['same_director'].append(movie['movie']['value'].replace("http://dbpedia.org/resource/", ""))
    print('got the other movies made by that director')

    # country
    sparql.setQuery("""
                        PREFIX dbo: <http://dbpedia.org/ontology/>
                        SELECT ?c
                        WHERE { <http://dbpedia.org/resource/""" + str(uri) + """> dbo:starring ?c }
                        LIMIT 100
                    """)
    sparql.setReturnFormat(JSON)
    triples = sparql.query().convert()
    print(triples["results"]["bindings"])
    if triples["results"]["bindings"]:
        data['main_actor'] = triples["results"]["bindings"][0]['c']['value'].replace("http://dbpedia.org/resource/", "")
        print('got the actor ' + data['main_actor'])
        # main actor
        sparql.setQuery("""
                            PREFIX dbo: <http://dbpedia.org/ontology/>
                            PREFIX dbr: <http://dbpedia.org/resource/>
                            SELECT ?movie
                            WHERE { ?movie dbo:starring dbr:""" + data['main_actor'] +"""}
                            LIMIT 100
                        """)
        sparql.setReturnFormat(JSON)
        triples = sparql.query().convert()
        data['same_main_actor'] = []
        for movie in triples["results"]["bindings"]:
            data['same_main_actor'].append(movie['movie']['value'].replace("http://dbpedia.org/resource/", ""))
        print('got the other movies made by that actor')
    else:
        data['main_actor'] = None
        data['same_main_actor'] = []
    return render_template('movie.html', data=data)