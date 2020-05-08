from flask import Flask, flash, redirect, render_template, request, url_for
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import requests
import re


def cinema(lang,categ):
    try:
        if(lang == 'Telugu'):
            l='te'
        elif(lang == 'Hindi'):
            l='hi'
        elif(lang == 'English'):
            l='en'
        elif(lang == 'Malayalam'):
            l='ml'
        elif(lang == 'Kannada'):
            l='kn'
        elif(lang == 'Tamil'):
            l='ta'
        elif(lang == 'Korean'):
            l='ta'

        my_url ='https://www.imdb.com/search/title?title_type=feature&countries=in&languages='+l+'&runtime=100,&sort=user_rating,desc'
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        data=[]
        c=0
        #grabs each product
        containers = page_soup.findAll("div",{"class":"lister-item mode-advanced"})
        for container in containers:
            # movie name
            movie = container.a.img["alt"]
            #rating
            rating = container.strong.text
            #catageory
            catageory = container.findAll("span",{"class":"genre"})
            cat = str(catageory)
            #release date
            Date_rel= container.findAll("span",{"class":"lister-item-year text-muted unbold"})
            date = Date_rel[0].text.strip()
            # Run time
            Run_time= container.findAll("span",{"class":"runtime"})
            duration = Run_time[0].text.strip()
            # Director and actors
            act = container.findAll("p",{"class":""})
            actt = act[0].text
            act1 = actt.replace("\n","")
            act2 = act1.replace('|',"\n")
            act3 = act2.replace(' ','')
            # Introduction to movuie
            intr = container.findAll("p",{"class":"text-muted"})
            intro = intr[1].text.replace('   ','')
            intro1 = intro.replace("\n","")
            
            if categ in cat:
                c=c+1
                sub=[]
                sub.append(movie)
                sub.append(rating)
                sub.append(date)
                sub.append(duration)
                sub.append(act3)
                sub.append(intro1)
                data.append(sub)
                if(c>10):
                    
                    break
        x=51
        while(len(data)<10):
            if(len(data)<10):
                my_url=my_url+'&start='+str(x)+'&ref_=adv_nxt'
                # for open the given link
                uClient = uReq(my_url)
                page_html = uClient.read()
                uClient.close()
                # html storing
                page_soup = soup(page_html, "html.parser")

                #grabs each product
                containers = page_soup.findAll("div",{"class":"lister-item mode-advanced"})
                for container in containers:
                    # movie name
                    movie = container.a.img["alt"]
                    #rating
                    rating = container.strong.text 
                    #release date
                    Date_rel= container.findAll("span",{"class":"lister-item-year text-muted unbold"})
                    date = Date_rel[0].text.strip()
                    #catageory
                    catageory = container.findAll("span",{"class":"genre"})
                    cat = str(catageory)
                    # Run time
                    Run_time= container.findAll("span",{"class":"runtime"})
                    duration = Run_time[0].text.strip()
                    # Director and Actors
                    act = container.findAll("p",{"class":""})
                    actt = act[0].text
                    act1 = actt.replace("\n","")
                    act2 = act1.replace('|',"\n")
                    act3 = act2.replace(' ','')
                    # Introduction to movie
                    intr = container.findAll("p",{"class":"text-muted"})
                    intro = intr[1].text.replace('   ','')
                    intro1 = intro.replace("\n","")
                    if  categ in cat:
                        c=c+1
                        if(len(data)<10):
                            sub=[]
                            sub.append(movie)
                            sub.append(rating)
                            sub.append(date)
                            sub.append(duration)
                            sub.append(act3)
                            sub.append(intro1)
                            data.append(sub)
                x=x+50
                if(c>10):
                    break

    except Exception as exc:
        print("sorry not found")
        print(exc)
        data = None
    print(data)
    return data






app = Flask(__name__)
@app.route('/')
def index():
    return render_template(
        'movie.html',
        data=[{'x':'Telugu'}, {'x':'English'}, {'x':'Hindi'},{'x':'Malayalam'}, {'x':'Tamil'},{'x':'Kannada'},],
        data1=[{'y':'Horror'}, {'y':'Romance'}, {'y':'Action'},{'y':'Sci-Fi'}, {'y':'Drama'},{'y':'Crime'}, {'y':'Music'},{'y':'War'}, {'y':'Biography'},{'y':'Family'},{'y':'Mystery'}, {'y':'Fantasy'},])
    

@app.route("/result" , methods=['GET', 'POST'])
def result():
    resp = []
    tops = []
    error = None
    select = request.form.get('comp_select')
    select1 = request.form.get('comp_categiory')
    tops=[select,select1]
    resp = cinema(select,select1)
    if resp:
        data = resp
        tops =tops
        error = {}
    else:
        data = {}
        tops = {}
        error = {"error":"something bad happened"}
    #data=[select,select1]

    return render_template(
        'result.html',
        data=data,
        tops=tops,
        error=error)


if __name__=='__main__':
    app.run(debug=True)