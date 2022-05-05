import pandas as pd
from matplotlib import pyplot as plt
import random

def plotPCARegion(component_1, component_2, groups, outpath="./"):
    """
    Plot PCA results of GWAS data, which are processed by plink.

    Parameters
    ----------
    component_1 : pandas.Series
        scores of principal component 1
    component_2 : pandas.Series
        scores of principal component 2
    groups : pandas.Series
        groups that each individual belongs to
    outpath : str
        path to which images are output
    """
    # preparation
    uniq_groups = pd.Series.unique(groups)
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

    tmp_cmp = []
    for i in range(len(uniq_groups)):
        group = uniq_groups[i]
        
        cmp1 = component_1[groups == group]
        cmp2 = component_2[groups == group]
        
        label = group
        c = colors[i]

        for j in range(len(cmp1)):
            tmp_cmp.append((cmp1.values[j], cmp2.values[j], c, label))
    #plt.title("RESULT OF PCA", size = 14)
    #plt.xlabel("COMPONENT 1")
    #plt.ylabel("COMPONENT 2")
    #plt.legend()
    #plt.savefig('{0}pca.png'.format(outpath))

    #return_lst = []
    # plot by each group
    #for i in range(len(uniq_groups)):
    #    #plt.figure(figsize = [7, 5])
    #    group = uniq_groups[i]
    #    return_lst.append(component_1[groups == group],component_2[groups == group], group, colors[i])
        
        #plt.title("RESULT OF PCA : " + group, size = 14)
        #plt.xlabel("COMPONENT 1")
        #plt.ylabel("COMPONENT 2")
        #plt.legend()
        #plt.savefig('{0}pca_{1}.png'.format(outpath, group))
    
    return tmp_cmp


def plotPCAEthnicity(component_1, component_2, groups, ethnicity, outpath="./"):
    """
    Plot PCA results of GWAS data, which are processed by plink.

    Parameters
    ----------
    component_1 : pandas.Series
        scores of principal component 1
    component_2 : pandas.Series
        scores of principal component 2
    groups : pandas.Series
        groups that each individual belongs to
    outpath : str
        path to which images are output
    """
    # join groups and ethnicity lists
    group_and_ethnicity = []
    for index, group in enumerate(groups):
        group_and_ethnicity.append((group, ethnicity[index]))
    
    uniq_groups = pd.Series.unique(groups)
    for i in range(len(uniq_groups)):
        x, y, c, labels = [], [], [], []
        

        plt.figure(figsize = [7, 5])
        group = uniq_groups[i]

        # find all the ethnicities related to the
        unique_ethnicities = []
        for j in range(len(group_and_ethnicity)):
            if group_and_ethnicity[j][0] == group and group_and_ethnicity[j][1] not in (item[0] for item in unique_ethnicities):             
                unique_ethnicities.append((group_and_ethnicity[j][1], random.choice(cnames)[0]))


        for item in unique_ethnicities:
            color = item[1]
            ethnicity = item[0]

            for index, tpl in enumerate(group_and_ethnicity):
                ethnicity_cmp = tpl[1]
                if ethnicity_cmp == ethnicity:
                    x.append(component_1[index])
                    y.append(component_2[index])
                    c.append(color)
                    labels.append(ethnicity)

        res = []
        for i in labels:
            if i not in res:
                res.append(i)
        print(res)
        plt.title("RESULT OF PCA : " + group, size = 14)
        plt.xlabel("COMPONENT 1")
        plt.ylabel("COMPONENT 2")

        fig, ax = plt.subplots()
        for i in range(len(x)):
            ax.scatter(x[i], y[i], c=c[i], label=labels[i])
        legend_without_duplicate_labels(ax)
        plt.savefig(outpath + group + ".png")

        plt.close()

cnames = [
    ('aliceblue',           '#F0F8FF'),
    ('antiquewhite',        '#FAEBD7'),
    ('aqua',                '#00FFFF'),
    ('aquamarine',          '#7FFFD4'),
    ('azure',               '#F0FFFF'),
    ('beige',               '#F5F5DC'),
    ('bisque',              '#FFE4C4'),
    ('black',               '#000000'),
    ('blanchedalmond',      '#FFEBCD'),
    ('blue',                '#0000FF'),
    ('blueviolet',          '#8A2BE2'),
    ('brown',               '#A52A2A'),
    ('burlywood',           '#DEB887'),
    ('cadetblue',           '#5F9EA0'),
    ('chartreuse',          '#7FFF00'),
    ('chocolate',           '#D2691E'),
    ('coral',               '#FF7F50'),
    ('cornflowerblue',      '#6495ED'),
    ('cornsilk',            '#FFF8DC'),
    ('crimson',             '#DC143C'),
    ('cyan',                '#00FFFF'),
    ('darkblue',            '#00008B'),
    ('darkcyan',            '#008B8B'),
    ('darkgoldenrod',       '#B8860B'),
    ('darkgray',            '#A9A9A9'),
    ('darkgreen',           '#006400'),
    ('darkkhaki',           '#BDB76B'),
    ('darkmagenta',         '#8B008B'),
    ('darkolivegreen',      '#556B2F'),
    ('darkorange',          '#FF8C00'),
    ('darkorchid',          '#9932CC'),
    ('darkred',             '#8B0000'),
    ('darksalmon',          '#E9967A'),
    ('darkseagreen',        '#8FBC8F'),
    ('darkslateblue',       '#483D8B'),
    ('darkslategray',       '#2F4F4F'),
    ('darkturquoise',       '#00CED1'),
    ('darkviolet',          '#9400D3'),
    ('deeppink',            '#FF1493'),
    ('deepskyblue',         '#00BFFF'),
    ('dimgray',             '#696969'),
    ('dodgerblue',          '#1E90FF'),
    ('firebrick',           '#B22222'),
    ('floralwhite',         '#FFFAF0'),
    ('forestgreen',         '#228B22'),
    ('fuchsia',             '#FF00FF'),
    ('gainsboro',           '#DCDCDC'),
    ('ghostwhite',          '#F8F8FF'),
    ('gold',                '#FFD700'),
    ('goldenrod',           '#DAA520'),
    ('gray',                '#808080'),
    ('green',               '#008000'),
    ('greenyellow',         '#ADFF2F'),
    ('honeydew',            '#F0FFF0'),
    ('hotpink',             '#FF69B4'),
    ('indianred',           '#CD5C5C'),
    ('indigo',              '#4B0082'),
    ('ivory',               '#FFFFF0'),
    ('khaki',               '#F0E68C'),
    ('lavender',            '#E6E6FA'),
    ('lavenderblush',       '#FFF0F5'),
    ('lawngreen',           '#7CFC00'),
    ('lemonchiffon',        '#FFFACD'),
    ('lightblue',           '#ADD8E6'),
    ('lightcoral',          '#F08080'),
    ('lightcyan',           '#E0FFFF'),
    ('lightgoldenrodyellow', '#FAFAD2'),
    ('lightgreen',          '#90EE90'),
    ('lightgray',           '#D3D3D3'),
    ('lightpink',           '#FFB6C1'),
    ('lightsalmon',         '#FFA07A'),
    ('lightseagreen',       '#20B2AA'),
    ('lightskyblue',        '#87CEFA'),
    ('lightslategray',      '#778899'),
    ('lightsteelblue',      '#B0C4DE'),
    ('lightyellow',         '#FFFFE0'),
    ('lime',                '#00FF00'),
    ('limegreen',           '#32CD32'),
    ('linen',               '#FAF0E6'),
    ('magenta',             '#FF00FF'),
    ('maroon',              '#800000'),
    ('mediumaquamarine',    '#66CDAA'),
    ('mediumblue',          '#0000CD'),
    ('mediumorchid',        '#BA55D3'),
    ('mediumpurple',        '#9370DB'),
    ('mediumseagreen',      '#3CB371'),
    ('mediumslateblue',     '#7B68EE'),
    ('mediumspringgreen',   '#00FA9A'),
    ('mediumturquoise',     '#48D1CC'),
    ('mediumvioletred',     '#C71585'),
    ('midnightblue',        '#191970'),
    ('mintcream',           '#F5FFFA'),
    ('mistyrose',           '#FFE4E1'),
    ('moccasin',            '#FFE4B5'),
    ('navajowhite',         '#FFDEAD'),
    ('navy',                '#000080'),
    ('oldlace',             '#FDF5E6'),
    ('olive',               '#808000'),
    ('olivedrab',           '#6B8E23'),
    ('orange',              '#FFA500'),
    ('orangered',           '#FF4500'),
    ('orchid',              '#DA70D6'),
    ('palegoldenrod',       '#EEE8AA'),
    ('palegreen',           '#98FB98'),
    ('paleturquoise',       '#AFEEEE'),
    ('palevioletred',       '#DB7093'),
    ('papayawhip',          '#FFEFD5'),
    ('peachpuff',           '#FFDAB9'),
    ('peru',                '#CD853F'),
    ('pink',                '#FFC0CB'),
    ('plum',                '#DDA0DD'),
    ('powderblue',          '#B0E0E6'),
    ('purple',              '#800080'),
    ('red',                 '#FF0000'),
    ('rosybrown',           '#BC8F8F'),
    ('royalblue',           '#4169E1'),
    ('saddlebrown',         '#8B4513'),
    ('salmon',              '#FA8072'),
    ('sandybrown',          '#FAA460'),
    ('seagreen',            '#2E8B57'),
    ('seashell',            '#FFF5EE'),
    ('sienna',              '#A0522D'),
    ('silver',              '#C0C0C0'),
    ('skyblue',             '#87CEEB'),
    ('slateblue',           '#6A5ACD'),
    ('slategray',           '#708090'),
    ('snow',                '#FFFAFA'),
    ('springgreen',         '#00FF7F'),
    ('steelblue',           '#4682B4'),
    ('tan',                 '#D2B48C'),
    ('teal',                '#008080'),
    ('thistle',             '#D8BFD8'),
    ('tomato',              '#FF6347'),
    ('turquoise',           '#40E0D0'),
    ('violet',              '#EE82EE'),
    ('wheat',               '#F5DEB3'),
    ('white',               '#FFFFFF'),
    ('whitesmoke',          '#F5F5F5'),
    ('yellow',              '#FFFF00'),
    ('yellowgreen',         '#9ACD32')
]