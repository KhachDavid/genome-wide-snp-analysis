# Population Structure Inference Using PCA

Demo: 

https://user-images.githubusercontent.com/65775837/166978687-276fd7b4-324b-4380-a9b3-2bc3cd2b92b5.mov

## Requirements
Tools and packages required to successfully install this project.

For Windows 

1) Linux [Install](https://youtu.be/xzgwDbe7foQ) 

2) Python 3.8 and up [Install](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server)

For MacOS
1) Python 3.8 and up [Install](https://docs.python-guide.org/starting/install3/osx/)

Both Windows and MacOS

You must also download [plink 1.9](https://www.cog-genomics.org/plink/) and place the executable in the root directory. Please make sure to download the correct version for your CPU architecture.

You must also download the population sample data from here: [population.csv](https://drive.google.com/file/d/1GED_wzU3VAKP_gCgCYEFcH0JeqX-VZzl/view?usp=sharing). Please place this file inside the app_pca directory. 

# Set up. Run the following commands after clonging the project.

`apt-get install python3-venv`

`python -m venv venv`

`source venv/bin/activate`

`cd config/`

`pip install -r core/requirements.txt`

`cd ..`

`./run`

# Data
Data submitted to this web application must follow the [GT](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3137218/) format described in the linked paper

It can be either a **csv file** or a **tab/space separated** text file. 

The Sample that you submit has no information about the population structure. Each column will be treated as a random id number. 

The goal of the project is to infer the population structure of the sample, using the [HGDP](https://en.wikipedia.org/wiki/Human_Genome_Diversity_Project) dataset and the PCA algorithm.

[Here is a sample of the data that you can submit](https://drive.google.com/file/d/1yRf4WpUonKULweEg08EVsLw2My-1e8Wt/view?usp=sharing)

It must have the following columns:

    1. #CHROM
    2. POS
    3. ID
    4. REF
    5. ALT
    6. QUAL
    7. FILTER
    8. INFO
    9. FORMAT

Starting from column 10, the columns will be treated as the samples. **The program will fail** if the submitted file doesn't follow this format.

# Background

The goal of this project is to infer the population structure of the sample, using the [HGDP](https://en.wikipedia.org/wiki/Human_Genome_Diversity_Project) dataset and the PCA algorithm. For this to happen, the eigenvectors of the HGDP dataset was calculated. The result could be found in the app_pca directory, [hgdpEigen.eigenvec](https://github.com/KhachDavid/genome-wide-snp-analysis/blob/main/app_pca/hgdpEigen.eigenvec). In addition, we need to know the population structure of the sample. Each population has a specific set of individuals, that are given the id that starts with HGDP followed by a number. The population structure can be mapped from the eigenvalues to the corresponding population using the following csv file: [population.csv](https://drive.google.com/file/d/1GED_wzU3VAKP_gCgCYEFcH0JeqX-VZzl/view?usp=sharing). After the calculation, we plot the eigenvalues and the population structure. Resulting plot is shown in the following [figure](https://github.com/KhachDavid/genome-wide-snp-analysis/blob/main/pca.png). More details about the different visualization options can be found in the [presentation](https://docs.google.com/presentation/d/1rMCgYIulIFf-SFfONSjLfZQP29ACTk121y1aBOw_Pec/edit?usp=sharing). 

This web app allows a user to plot their sample onto the famous HGDP dataset and infer the population structure. Visually it will show you which one it is closest to. 

<img width="500" alt="image" src="https://user-images.githubusercontent.com/65775837/166975693-a7edbd6c-8370-4fbd-a172-f8a90944e794.png">

Ultimately it goes down to this format. Where the structure of HGDP is labeled, but the user input file is not labeled. By visualizing these points, we can learn more about our population sample's structure.

# Troubleshooting

- If scripts do not run, please make sure that you have given access to the scripts in the root directory and to the scripts in the config directory.

`chmod +x config/run.sh` 

could be one way of solving it

- If the program fails, please make sure that you have the correct version of the plink executable. It must be 1,9 at least, and be in the root directory of this project.












