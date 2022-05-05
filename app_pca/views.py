import pandas as pd
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import random, string
import subprocess, os
from .utils import plotPCARegion, plotPCAEthnicity

letters = string.ascii_lowercase

# eigenvecs path 
eigenvecs_path = "app_pca/hgdpEigen.eigenvec"
population_path = 'app_pca/population.csv'

# load the eigenvec files
df_eigenvecs = pd.read_csv(
    eigenvecs_path,
    header=None,
    delim_whitespace = True
)

df_population = pd.read_csv(
    population_path,
    header=None,
)

# preprocess data
df_population = df_population.rename(columns={2 : 'region', 1 : 'ethnicity'})

# join population and eigenvecs based on population column 0 and eigenvecs column 1
df_merged = pd.merge(
    df_eigenvecs,
    df_population,
    left_on = 1,
    right_on = 0
)

df_pca = df_merged[[2, 3, 'region', 'ethnicity']]

# inputs of plot
component_1 = df_pca[2]
component_2 = df_pca[3]
groups = df_pca['region']
ethnicity = df_pca['ethnicity']

plotPoints = plotPCARegion(
    component_1=component_1,
    component_2=component_2,
    groups=groups,
)


# Create your views here.
@csrf_exempt
def pca(request):
    # read the payload
    post_data = json.loads(request.body.decode("utf-8"))

    # generate a random string
    fileName = ''.join(random.choice(letters) for i in range(10))

    fullFileName = "inputUser" + fileName

    # write post data to a file 
    text_file = open(fullFileName + ".tped", "w")
    text_file.write(post_data['data'])
    text_file.close()

    numberOfSamples = post_data['numberOfSamples']

    # run a loop and write the output to a file called fullFileName + ".tfam"
    text_file = open(fullFileName + ".tfam", "w")
    for i in range(int(numberOfSamples)):
        text_file.write("0\t" + str(i + 1) + "\t0\t0\t1\t-9\n")
    
    text_file.close()

    subprocess.run(['./pca_script_setup', fullFileName])

    subprocess.run(['./pca_script', fullFileName])    

    # make sure the eigenvecs file is there
    if os.path.isfile(fullFileName + ".eigenvec"):
        # read the eigenvecs file
        df_eigenvecs = pd.read_csv(
            fullFileName + ".eigenvec",
            header=None,
            delim_whitespace = True
        )

        lst = []
        for i in range(len(df_eigenvecs[2])):
            lst.append((df_eigenvecs[2][i], df_eigenvecs[3][i]))

    return JsonResponse(
        {
            'plotPoints': plotPoints,
            'userPoints': lst,
        }
    , safe=False)