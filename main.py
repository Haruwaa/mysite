from flask import Flask
from flask import render_template,redirect,url_for,request,flash
import pandas as pd
import csv

from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
app.secret_key = 'hello'
field_df=pd.read_csv(r'/home/goseniorhigh/mysite/datasets/questions.csv')

gg= []


ratings_df = pd.read_csv(r'/home/goseniorhigh/mysite/datasets/dataset.csv')

df4 = ratings_df

df2=field_df
links2=df2[['questions','qID','field']].to_records()




links4=df4[['userID','qID','ratings']].to_records()

liked_questions = []
@app.route('/')
def home():


    return render_template("base.html")

@app.route("/test", methods=["POST","GET"])
def test():

       return render_template("index.html",data=links2)

@app.route('/about')
def ab():
    return render_template("aboutus.html")

@app.route('/academictrack')
def academic():

    return render_template("academic.html")

@app.route('/techvoc')
def techvoca():
    return render_template("techvoc.html")

@app.route('/stem')
def stm():
    return render_template("stem.html")

@app.route('/abm')
def bm():
    return render_template("abm.html")

@app.route('/humss')
def hmss():
    return render_template("humss.html")

@app.route('/gas')
def gs():
    return render_template("gas.html")

@app.route('/ict')
def ct():
    return render_template("ict.html")

@app.route("/result")
def result():
             result_df =pd.read_csv(r'/home/goseniorhigh/mysite/datasets/result.csv')
             df3=result_df
             links3=df3[['track']].to_records()

             if df3.empty == True:
                         flash('Oops! Please retake the test and answer seriously' , 'error')


             return render_template('result.html',data1=links3)

@app.route("/forward/<var>", methods=['POST'])
def move_forward(var):
    global gg
    if request.method == 'POST':


      string = ""
    for id in gg:
      string+str(id)
    qsid = request.form['queID']
    qsid2 = request.form['queIDa']
    qsid3 = request.form['queIDb']
    qsid4 = request.form['queIDc']
    qsid5 = request.form['queIDd']
    qsid6 = request.form['queIDe']
    qsid7 = request.form['queIDf']
    qsid8 = request.form['queIDg']
    qsid9 = request.form['queIDh']
    qsid10 = request.form['queIDi']
    qsid11 = request.form['queIDj']
    qsid12= request.form['queIDk']
    qsid13= request.form['queIDl']
    qsid14= request.form['queIDm']
    qsid15 = request.form['queIDn']
    qsid16 = request.form['queIDo']
    qsid17= request.form['queIDp']
    qsid18= request.form['queIDq']
    qsid19= request.form['queIDr']
    qsid20= request.form['queIDs']
    qsid21= request.form['queIDt']
    qsid22= request.form['queIDu']
    qsid23= request.form['queIDv']
    qsid24= request.form['queIDw']
    qsid25= request.form['queIDx']
    qsid26= request.form['queIDx1']
    qsid27= request.form['queIDx2']
    qsid28= request.form['queIDx3']
    qsid29= request.form['queIDx4']
    qsid30= request.form['queIDx5']
    qsid31= request.form['queIDx6']
    qsid32= request.form['queIDx7']
    qsid33= request.form['queIDx8']
    qsid34= request.form['queIDx9']
    qsid35= request.form['queIDx10']


    rate = request.form['rat']
    rate2 = request.form['rat2']
    rate3 = request.form['rat3']
    rate4 = request.form['rat4']
    rate5 = request.form['rat5']
    rate6 = request.form['rat6']
    rate7 = request.form['rat7']
    rate8 = request.form['rat8']
    rate9 = request.form['rat9']
    rate10 = request.form['rat10']
    rate11= request.form['rat11']
    rate12 = request.form['rat12']
    rate13 = request.form['rat13']
    rate14 = request.form['rat14']
    rate15 = request.form['rat15']
    rate16 = request.form['rat16']
    rate17 = request.form['rat17']
    rate18 = request.form['rat18']
    rate19 = request.form['rat19']
    rate20 = request.form['rat20']
    rate21 = request.form['rat21']
    rate22 = request.form['rat22']
    rate23 = request.form['rat23']
    rate24 = request.form['rat24']
    rate25 = request.form['rat25']
    rate26 = request.form['rat26']
    rate27 = request.form['rat27']
    rate28 = request.form['rat28']
    rate29 = request.form['rat29']
    rate30 = request.form['rat30']
    rate31 = request.form['rat31']
    rate32 = request.form['rat32']
    rate33 = request.form['rat33']
    rate34 = request.form['rat34']
    rate35 = request.form['rat35']

    csv_list = [r'/home/goseniorhigh/mysite/datasets/dataset.csv']


    #why_df= pd.read_csv(r'/home/goseniorhigh/mysite/datasets/master.csv')
    for csv_file in csv_list:
      dff = pd.read_csv(csv_file)
      dff.to_csv(r'/home/goseniorhigh/mysite/datasets/master.csv', mode='w',  index=False)


    fieldnames= ['uID', 'queID', 'rat']
   # r'/home/goseniorhigh/mysite/datasets/125950255.0.csv'
    with open(r'/home/goseniorhigh/mysite/datasets/master.csv','a', newline='') as inFile:
     writer = csv.DictWriter(inFile,  fieldnames=fieldnames)
     writer.writerow({'uID': id, 'queID': qsid, 'rat':rate})
     writer.writerow({'uID': id, 'queID': qsid2, 'rat':rate2})
     writer.writerow({'uID': id, 'queID': qsid3, 'rat':rate3})
     writer.writerow({'uID': id, 'queID': qsid4, 'rat':rate4})
     writer.writerow({'uID': id, 'queID': qsid5, 'rat':rate5})
     writer.writerow({'uID': id, 'queID': qsid6, 'rat':rate6})
     writer.writerow({'uID': id, 'queID': qsid7, 'rat':rate7})
     writer.writerow({'uID': id, 'queID': qsid8, 'rat':rate8})
     writer.writerow({'uID': id, 'queID': qsid9, 'rat':rate9})
     writer.writerow({'uID': id, 'queID': qsid10, 'rat':rate10})
     writer.writerow({'uID': id, 'queID': qsid11, 'rat':rate11})
     writer.writerow({'uID': id, 'queID': qsid12, 'rat':rate12})
     writer.writerow({'uID': id, 'queID': qsid13, 'rat':rate13})
     writer.writerow({'uID': id, 'queID': qsid14, 'rat':rate14})
     writer.writerow({'uID': id, 'queID': qsid15, 'rat':rate15})
     writer.writerow({'uID': id, 'queID': qsid16, 'rat':rate16})
     writer.writerow({'uID': id, 'queID': qsid17, 'rat':rate17})
     writer.writerow({'uID': id, 'queID': qsid18, 'rat':rate18})
     writer.writerow({'uID': id, 'queID': qsid19, 'rat':rate19})
     writer.writerow({'uID': id, 'queID': qsid20, 'rat':rate20})
     writer.writerow({'uID': id, 'queID': qsid21, 'rat':rate21})
     writer.writerow({'uID': id, 'queID': qsid22, 'rat':rate22})
     writer.writerow({'uID': id, 'queID': qsid23, 'rat':rate23})
     writer.writerow({'uID': id, 'queID': qsid24, 'rat':rate24})
     writer.writerow({'uID': id, 'queID': qsid25, 'rat':rate25})
     writer.writerow({'uID': id, 'queID': qsid26, 'rat':rate26})
     writer.writerow({'uID': id, 'queID': qsid27, 'rat':rate27})
     writer.writerow({'uID': id, 'queID': qsid28, 'rat':rate28})
     writer.writerow({'uID': id, 'queID': qsid29, 'rat':rate29})
     writer.writerow({'uID': id, 'queID': qsid30, 'rat':rate30})
     writer.writerow({'uID': id, 'queID': qsid31, 'rat':rate31})
     writer.writerow({'uID': id, 'queID': qsid32, 'rat':rate32})
     writer.writerow({'uID': id, 'queID': qsid33, 'rat':rate33})
     writer.writerow({'uID': id, 'queID': qsid34, 'rat':rate34})
     writer.writerow({'uID': id, 'queID': qsid35, 'rat':rate35})


    questions = pd.read_csv(r'/home/goseniorhigh/mysite/datasets/questions.csv')
    rate = pd.read_csv(r'/home/goseniorhigh/mysite/datasets/master.csv')

    ff = pd.merge(rate,questions, on='qID', how='inner')
    ff.to_csv(r'/home/goseniorhigh/mysite/datasets/userdataset.csv')


    string = ""
    for ide in gg:
         string+str(ide)
    ides = int(ide)


    print(ides)


    f = pd.read_csv(r'/home/goseniorhigh/mysite/datasets/userdataset.csv')
    agg_ratings = f.groupby('field').agg(mean_rating = ('ratings', 'mean'), number_of_ratings = ('ratings', 'count')).reset_index()
# Keep the questions with over 1 ratings
    agg_ratings_GT1 = agg_ratings[agg_ratings['number_of_ratings']>1]


    agg_ratings_GT1.sort_values(by='number_of_ratings', ascending=False).head()

    df_GT1 = pd.merge(f, agg_ratings_GT1[['field']], on='field', how='inner')


    matrix = df_GT1.pivot_table(index='userID', columns= 'field', values= 'ratings')


    matrix_norm = matrix.subtract(matrix.mean(axis=1), axis = 'rows')


    user_similarity = matrix_norm.T.corr()

    user_similarity_cosine = cosine_similarity(matrix_norm.fillna(0))


    picked_userid = ides
# Remove picked user ID from the candidate list
    user_similarity.drop(index=picked_userid, inplace=True)

    n = 10
# User similarity threashold
    user_similarity_threshold = 0.3
    similar_users = user_similarity[user_similarity[picked_userid]>user_similarity_threshold][picked_userid].sort_values(ascending=False)[:n]
# Print out top n similar users
    print(f'The similar users for user {picked_userid} are', similar_users)
      # if similar_users.empty:
     #  hm = "asdasdasdads"
    #  print(hm)



    picked_userid_answered = matrix_norm[matrix_norm.index == picked_userid].dropna(axis=1,how='all')
    # print(picked_userid_answered)
    similar_user_q = matrix_norm[matrix_norm.index.isin(similar_users.index)].dropna(axis=1, how='all')
    print(similar_user_q)

    item_score = {}
# Loop through items
    for i in similar_user_q.columns:
  # Get the ratings for question i
       q_rating = similar_user_q[i]
  # Create a variable to store the score
       total = 0
  # Create a variable to store the number of scores
       count = 0
  # Loop through similar users
       for u in similar_users.index:
    # If the movie has rating
         if pd.isna(q_rating[u]) == False:
      # Score is the sum of user similarity score multiply by the movie rating
          score = similar_users[u] * q_rating[u]
        # Add the score to the total score for the movie so far
          total += score
      # Add 1 to the count
          count +=1
  # Get the average score for the item
       item_score[i] = total / count
# Convert dictionary to pandas dataframe
    item_score = pd.DataFrame(item_score.items(), columns=['track', 'track_score'])

# Sort the movies by score
    ranked_item_score = item_score.sort_values(by='track_score', ascending=False)
# Select top m movies
    m = 1
    ranked_item_score.head(m)
    ranked_item_score.head(m).to_csv(r'/home/goseniorhigh/mysite/datasets/result.csv')

    return redirect(url_for('result'))

            # with open(r'C:\Users\abby\Downloads\master.csv','a', newline='') as inFile:
                 #   writer.writerow({'uID': id })

                  #  return redirect(url_for('test'))


@app.route('/check/<var>', methods= ['POST'])
def check(var):

      global gg
      if request.method == 'POST':

            id = request.form['uID']


            gg.clear()
            id = int(id)

            gg.append(id)


            print (gg)


            flash('your ID is now registered, please answer the items below', 'success')


            return redirect(url_for('test'))




if __name__ == "__main__":
 app.run(debug=True)