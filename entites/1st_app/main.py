import pandas as pd
import streamlit as st

import utils
from analyzer import TextAnalyzer

analyzer = TextAnalyzer()

with st.form("my_form"):
    st.write('Please enter a URL or a text')

    text_input = st.text_area('Please enter a URL or a text', 'https://www.enelx.com/it/it/privati/mobilita-elettrica')
    is_url = utils.is_url(text_input)
    meta_tags_only = st.checkbox('Extract only using meta tags')
    submitted = st.form_submit_button("Submit")
    if submitted:
        response = analyzer.analyze(text_input, is_url)
        output = []
        for entity in response.entities():
            output.append({
                "type": "thing",
                "name": entity.id,
                "Wikidata Id": entity.wikidata_id,
                "Freebase Id": entity.freebase_id
            })
        df = pd.DataFrame(output)
        st.table(df)

# output = [
#     {
#         "type": "thing",
#         "name": "thing",
#         "description": "thing",
#         "sameAs_wikipedia": "thing",
#         "sameAs_dbpedia": "thing",
#         "q": 5,
#     },
# {
#         "type": "thing",
#         "name": "thing",
#         "description": "thing",
#         "sameAs_wikipedia": "thing",
#         "sameAs_dbpedia": "thing",
#         "q": 1,
#     },
# {
#         "type": "thing",
#         "name": "thing",
#         "description": "thing",
#         "sameAs_wikipedia": "thing",
#         "sameAs_dbpedia": "thing",
#         "q": 15,
#     },
# {
#         "type": "thing",
#         "name": "thing",
#         "description": "thing",
#         "sameAs_wikipedia": "thing",
#         "sameAs_dbpedia": "thing",
#         "q": 7,

#     },
# {
#         "type": "thing",
#         "name": "thing",
#         "description": "thing",
#         "sameAs_wikipedia": "thing",
#         "sameAs_dbpedia": "thing",
#         "q": 15,
#     },
# {
#         "type": "thing",
#         "name": "thing",
#         "description": "thing",
#         "sameAs_wikipedia": "thing",
#         "sameAs_dbpedia": "thing",
#         "q": 15,
#     }
# ]


