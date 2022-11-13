from pydoc import describe
from rdflib import Graph, Namespace
from rdflib.namespace import NamespaceManager, SKOS, DCTERMS
import json
from rdflib import Graph, plugin
from rdflib.serializer import Serializer
import pyRdfa
import re
import csv
import json, ast
import rdflib
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
import networkx as nx
import numpy
import sys

maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt / 10)


def csv_to_json(csv_file_path, json_file_path):
    # create a dictionary
    data_dict = {}

    # Step 2
    # open a csv file handler
    with open(csv_file_path, encoding='utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)

        # convert each row into a dictionary
        # and add the converted data to the data_variable

        for rows in csv_reader:
            # assuming a column named 'No'
            # to be the primary key
            key = rows['url']
            data_dict[key] = rows['metadata:']

    # open a json file handler and use json.dumps
    # method to dump the data
    # Step 3
    with open(json_file_path, 'w', encoding='utf-8') as json_file_handler:
        # Step 4
        json_file_handler.write(json.dumps(data_dict, indent=4))


# driver code
# be careful while providing the path of the csv file
# provide the file path relative to your machine

# Step 1
# csv_file_path = input('Enter the absolute path of the CSV file: ')
# json_file_path = input('Enter the absolute path of the JSON file: ')

escape_sequence = re.compile(r'\\x([a-fA-F0-9]{2})')


def fix_xinvalid(m):
    return chr(int(m.group(1), 16))


def repair(string):
    return escape_sequence.sub(r'\\u00\1', string)


def fix(s):
    return escape_sequence.sub(escape_sequence, s)


csv_to_json("C:\\Users\\elena\\scrapy_crawler\\scrapy_crawler\\spiders\\final_set.csv", "newFile.json")
with open('newFile.json', 'r') as data_file:
    main = Graph();
    m = open("testFile.json", "a", encoding="utf-8")
    json_data = json.load(data_file)
    content2 = json.dumps(json_data)
    json_data_string = json.loads(content2)
    for key in json_data_string:
        value = json_data_string[key]
        if (value != ""):
            value = value[1:-1]
            print("first value" + value)
            json_dat = json.dumps(ast.literal_eval(value))
            dict_dat = json.loads(json_dat)
            value = json.dumps(dict_dat)
            string = "\"@id\":" + "\"" + key + "\","
            value = value[:1] + string + value[1:]
            value = value.replace(r'(?<!\\)\\(?!["\\/bfnrt]|u[0-9a-fA-F]{4})', r'')
            value = value.replace(r"\xa0", r"\\xa0")
            data2 = value
            g = main.parse(data=data2, format='json-ld')

    g.serialize(destination='outputfinalset_imdb.ttl', format='ttl')
    i = 1
    for s, p, o in g.triples((None, None, None)):
        i = i + 1
    print(i)
