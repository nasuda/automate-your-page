
def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="maincontent">
    <p><h3>''' + concept_title + '</h3></p>'
    html_text_2 = '''
    <p>''' + concept_description + '</p>'
    html_text_3 = '''
    </div>'''



    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)


conceptList = [['List', 'Structured data type is a sequence of data. <br>Text is one data type and it is a sequence of characters<br> List is another data type. It is a sequence of anything. List can store characters, numbers, list..etc..  ,<br> Use square brackets to identify list while quotes are used for text.' ],
['Problem Solving', 'Computers are good at doing simple things in mechanical way <br>  so it is usually not good algorithm with following how human would solve a problem. <br> 3 steps to solve a problem with computational thinking<br> 1. Understanding the problem. what are the inputs / what are the outputs<br> 2. Understanding the relationship. some real example and algorithm with pseudocode<br>3. Develop incrementally and test as we go']]                          

def make_HTML_for_many_concepts(list_of_concepts):
    content =''
    for i in list_of_concepts:
        content += make_HTML(i)
    return content
        

print make_HTML_for_many_concepts(conceptList)


