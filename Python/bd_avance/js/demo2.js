const $rdf = require("rdflib");
const {Namespace} = require("rdflib");
const fs = require('fs');

const RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#");
const FOAF = Namespace("http://xmlns.com/foaf/0.1/");
const XSD = Namespace("http://www.w3.org/2001/XMLSchema#");

let store = $rdf.graph();
let nodes = {};

createNodes();
addNodes();

function createNodes() {
    let bob = $rdf.sym("http://example.org/people/Bob");
    let linda = $rdf.blankNode();
    let name = $rdf.literal("Bob");
    let age = $rdf.literal("24", XSD('int'));

    const PEOPLE = Namespace("http://example.org/people/");
    let alice = PEOPLE("Alice");

    nodes['bob'] = bob;
    nodes['linda'] = linda;
    nodes['name'] = name;
    nodes['age'] = age;
    nodes['alice'] = alice;

    for (const [key, value] of Object.entries(nodes)) {
        console.log(key, value);
    }
}

function addNodes() {
    store.add(nodes['bob'], RDF('type'), FOAF('Person'));

    const CUI = Namespace("http://cui.unige.ch/people/");
    let ashley = CUI('Ashley');

    store.add(ashley, RDF('type'), FOAF('Person'));
    store.add(nodes['bob'], FOAF('age'), $rdf.literal("20"));

    console.log(store.statements);
}