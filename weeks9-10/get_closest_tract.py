import pandas as pd
def get_closest_tract( pantrygdf, geom):
    tract = geom.centroid 
    distances = pantrygdf.distance(tract)
    closest_pantry, min_dist = distances.idxmin(), distances.min()
    return pd.Series([closest_pantry, min_dist]) # the Series notation is because we are returning more than one column