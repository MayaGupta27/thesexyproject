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

def get_demo_alleles(token):
    header = {'Authorization': "Bearer demo_oauth_token"}
    alleles = requests.get("https://api.23andme.com/3/profile/demo_profile_id/marker/?gene_name=genomes", headers =header )
    return alleles

def get_account(token):
    header = {'Authorization': "Bearer " + token}
    account = requests.get("https://api.23andme.com/3/account", headers=header)
    return account

def get_profile(id, token):
    header = {'Authorization': "Bearer demo_oauth_token"}
    profile = requests.get("https://api.23andme.com/3/profile/demo_profile_id/report", headers=header)
    return profile
