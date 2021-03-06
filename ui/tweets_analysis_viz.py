'''
Visualizations for Tweets text analytics
'''

from wordcloud import WordCloud
import plotly.graph_objects as go

from models.lda import retrieve_topics


def create_wordcloud(tweets):
    '''
    Create tweets word cloud visualization and save it in .png file.

    Inputs:
        tweets (Pandas Dataframe): tweet data
    '''

    words = ' '.join(tweets['Text'].astype(str))

    wordcloud = WordCloud(
        background_color = 'white',
        max_words = 100,
        max_font_size = 30,
        scale = 3,
        random_state = 1)

    wordcloud = wordcloud.generate(str(words))

    wordcloud.to_file('ui/tweets_wordcloud.png')


def create_lda_table(tweets):
    '''
    Retrieve main 3 topics from tweets (7 words per topic) and visualize a
    table.

    Inputs:
        tweets: list of tweets

    Outputs:
        list of lists, with list of 7 words per topic
    '''

    topics_words = retrieve_topics(tweets)

    fig = go.Figure(
        data = [go.Table(
            header = dict(values=['Topic 1', 'Topic 2', 'Topic 3'],
                font_color='white',
                fill_color='blue',
                align='left'),
            cells = dict(values = topics_words,
               line_color='black',
               fill_color='white',
               align='left'))
                     ])

    fig.update_layout(autosize = True)

    return fig
