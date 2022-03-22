import plotly.graph_objects as go



def create_graphs(df):
    """
    Function to create visuals
    
    Input:
        Dataframe -> DataFrame loaded from DB
    Output:
        List -> List of created visuals
    """
    # extract data needed for visuals
    genre_counts = df.genre.value_counts().index
    category_names = df.iloc[:, 4:].sum().sort_values()
    
    
    # create visuals
    genres_plot = []
    genres_plot.append(
        go.Bar(
            x=genre_counts.tolist(),
            y=genre_counts.values.tolist(),
            hoverinfo="skip",
            marker_color="#6495ed",
        )
    )

    genres_layout = dict(
        {
            "title": {
                "text": "<b>Most of the messages were recived from "
                "social</b><br>Small percentage of the data comes"
                " from news",
                "font": {"family": "Roboto", "size": 16},
            },
        }
    )

    label_plot = []
    label_plot.append(
        go.Bar(
            x=category_names.values.tolist(),
            y=category_names.index.tolist(),
            orientation="h",
            marker_color="#6495ed",
        )
    )

    label_layout = dict(
        {
            "title": {
                "text": "<b>Most of the messages were irrelevant"
                "</b><br>majority of messages were labelled <i>related</i> ",
                "font": {"family": "Roboto", "size": 16},
            },
            "margin": {
                "pad": 10,
                "l": 140,
                "r": 40,
                "t": 80,
                "b": 40,
            },
            "hoverlabel": {
                "font_size": 18,
                "font_family": "Roboto",
            },
            "yaxis": {"dtick": 1},
        }
    )

    figures = []
    figures.append(dict(data=genres_plot, layout=genres_layout))
    figures.append(dict(data=label_plot, layout=label_layout))

    return figures