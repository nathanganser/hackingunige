const $rdf = require("rdflib");
const fs = require('fs');

let store = $rdf.graph();

readRemote();
//readLocal();


function readRemote() {
    let fetcher = new $rdf.Fetcher(store);
    const url = "http://bigasterisk.com/foaf.rdf";
    fetcher.nowOrWhenFetched(url, function (ok, body, xhr) {
        if (!ok) {
            console.log("Oops, something happened and couldn't fetch data");
        } else {
            console.log(store.statements);
        }
    });
}

function readLocal() {
    const mimeType = 'text/turtle';
    const baseUrl = "http://cui.unige.ch/";
    fs.readFile("../data/demo2.ttl", 'utf8', function (err, data) {
        if (err) throw err;
        try {
            $rdf.parse(data, store, baseUrl, mimeType)
            console.log(store.statements)
        } catch (err) {
            console.log(err)
        }
    });
}
