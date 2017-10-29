from flask import Flask, request

def get_accession(chromosome):
    chromosome_accession_id = request.get("https://api.23andme.com/3/accession/" + chromosome + "/" )
    return chromosome_accession_id

def get_marker(accession_id ):
    marker = request.get("https://api.23andme.com/3/marker/?accession_id=" + accession_id)
    return marker

def get_variant(accession_id):
    variant = request.get("https://api.23andme.com/3/variant/?accession_id=" + accession_id)
    return variant

