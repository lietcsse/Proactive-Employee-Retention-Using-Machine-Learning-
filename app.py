from flask import Flask,render_template,request
app=Flask(__name__)
import pickle
model=pickle.load(open('attrition.pkl','rb'))
sc=pickle.load(open('standard.pkl','rb'))
@app.route('/')
def helloworld():
    return  render_template("index.html")
@app.route('/home')
def home():
    return render_template("index.html")
@app.route('/about')
def about():
    return  render_template("about.html")
@app.route('/stats')
def stats():
    return  render_template("stats.html")
@app.route('/login',methods=['POST'])
def admin():
    b1=0
    b2=0
    b3=0
    c1=0
    c2=0
    c3=0
    e1=0
    e2=0
    e3=0
    e4=0
    e5=0
    e6=0
    g1=0
    g2=0
    g3=0
    g4=0
    g5=0
    g6=0
    h1=0
    h2=0
    h3=0
    m1=0
    m2=0
    m3=0
    m4=0
    m5=0
    m6=0
    a=request.form['age']
    b=request.form['bt']
    c=request.form['dept']
    d=request.form['distance']
    e=request.form['es']
    f=request.form['gender']
    g=request.form['js']
    h=request.form['ms']
    i=request.form['income']
    j=request.form['ot']
    k=request.form['percent']
    l=request.form['pr']
    m=request.form['rs']
    n=request.form['totalworkyear']
    o=request.form['promote']
    s=request.form['years']
    if(b=='Non-Travel'):
        b1,b2,b3=1,0,0;
    elif(b=='Travel_Frequently'):
        b1,b2,b3=0,1,0;
    elif(b=='Travel Rarely'):
        b1,b2,b3=0,0,1;  
    if(c=='Human Resources'):
        c1,c2,c3=1,0,0;
    elif(c=='Research & Development'):
        c1,c2,c3=0,1,0;
    elif(c=='Sales'):
        c1,c2,c3=0,0,1; 
    if(e==0):
        e1,e2,e3,e4,e5,e6=1,0,0,0,0,0
    elif(e==1):
        e1,e2,e3,e4,e5,e6=0,1,0,0,0,0
    elif(e==2):
        e1,e2,e3,e4,e5,e6=0,0,1,0,0,0
    elif(e==3):
        e1,e2,e3,e4,e5,e6=0,0,0,1,0,0
    elif(e==4):
        e1,e2,e3,e4,e5,e6=0,0,0,0,1,0
    elif(e==5):
        e1,e2,e3,e4,e5,e6=0,0,0,0,0,1
    if(g==0):
        g1,g2,g3,g4,g5,g6=1,0,0,0,0,0
    elif(g==1):
        g1,g2,g3,g4,g5,g6=0,1,0,0,0,0
    elif(g==2):
        g1,g2,g3,g4,g5,g6=0,0,1,0,0,0
    elif(g==3):
        g1,g2,g3,g4,g5,g6=0,0,0,1,0,0
    elif(g==4):
        g1,g2,g3,g4,g5,g6=0,0,0,0,1,0
    elif(g==5):
        g1,g2,g3,g4,g5,g6=0,0,0,0,0,1
    if(h=='Divorced'):
        h1,h2,h3=1,0,0;
    elif(h=='Married'):
        h1,h2,h3=0,1,0;
    elif(h=='Single'):
        h1,h2,h3=0,0,1; 
    if(m==0):
        m1,m2,m3,m4,m5,m6=1,0,0,0,0,0
    elif(m==1):
        m1,m2,m3,m4,m5,m6=0,1,0,0,0,0
    elif(m==2):
        m1,m2,m3,m4,m5,m6=0,0,1,0,0,0
    elif(m==3):
        m1,m2,m3,m4,m5,m6=0,0,0,1,0,0
    elif(m==4):
        m1,m2,m3,m4,m5,m6=0,0,0,0,1,0
    elif(m==5):
        m1,m2,m3,m4,m5,m6=0,0,0,0,0,1
    if(f=="Female"):
        f=0;
    elif(f=='Male'):
        f=1;
    if(j=='No'):
        j=0;
    elif(j=='Yes'):
        j=1;
    if(l=='1'):
        l=0
    elif(l=='2'):
        l=1
    elif(l=='3'):
        l=2
    elif(l=='4'):
        l=3
    elif(l=='5'):
        l=4
    t=[[int(m1),int(m2),int(m3),int(m4),
        int(h1),int(h2),int(h3),
        int(g1),int(g2),int(g3),int(g4),
        int(e1),int(e2),int(e3),int(e4),
        int(c1),int(c2),int(c3),
        int(b1),int(b2),int(b3),
        int(a),float(d),int(f),float(i),int(j),float(k),int(l),
        int(n),int(s),int(o)]]  # This creates a (1,31) shape array
    
    # Check specific conditions for employee leaving
    will_leave = (
        (int(l) in [0, 1]) and  # Performance rating 1* or 2*
        (float(d) > 7) and     # Distance from home > 7
        (float(k) < 5) and     # Salary hike < 5%
        (int(e) < 2) and       # Environment satisfaction < 2
        (int(g) < 2) and       # Job satisfaction < 2
        (int(m) < 2)           # Relationship satisfaction < 2
    )
    
    if will_leave:
        prediction = "The employee will leave..."
    else:
        # Use the model's prediction for other cases
        y = model.predict(sc.fit_transform(t))
        prediction = "The employee will leave..." if str(y[0]) == '1' else "The employee will stay."
    
    # Create a dictionary with all form data
    form_data = {
        'Business Travel': b,
        'Department': c,
        'Gender': "Female" if f == 0 else "Male",
        'Marital Status': h,
        'Over Time': "Yes" if j == 1 else "No",
        'Performance Rating': "*" * (int(l) + 1),
        'Age': a,
        'Distance from Home': d,
        'Monthly Income': i,
        'Percent Salary Hike': k,
        'Total Working Years': n,
        'Years at Company': s,
        'Years Since Last Promotion': o,
        'Environment Satisfaction': e,
        'Job Satisfaction': g,
        'Relationship Satisfaction': m
    }
    
    return render_template("result.html", data=form_data, prediction=prediction)
if(__name__=="__main__"):
    app.run(debug=True)