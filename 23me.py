import requests

def get_accession(chromosome):
    chromosome_accession_id = requests.get("https://api.23andme.com/3/accession/" + chromosome + "/" )
    return chromosome_accession_id

def get_marker(accession_id ):
    marker = requests.get("https://api.23andme.com/3/marker/?accession_id=" + accession_id)
    return marker

def get_variant(accession_id):
    variant = requests.get("https://api.23andme.com/3/variant/?accession_id=" + accession_id)
    return variant

def getUserAlleles(geneName, token):
    headString = "Authorization: Bearer " + token
    alleles = requests.get("https://api.23andme.com/3/profile/demo_profile_id/variant/?gene_name=" + geneName, headers =(headString) )
    return alleles


