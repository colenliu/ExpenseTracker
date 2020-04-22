import bottle
import pymongo
import expenseBookDAO

# default route (index page) that reads the documents from MongoDB
@bottle.route('/')
def expense_index():
    myexpenses_list = expenseBook.find_expenses()
    return bottle.template('index', dict(myexpenses = myexpenses_list))

# posts new entries to this route and inserts entries into MongoDB
@bottle.route('/newexpense', method='POST')
def insert_newexpense():
    name = bottle.request.forms.get("name")
    cost = bottle.request.forms.get("cost")
    category = bottle.request.forms.get("category")
    expenseBook.insert_expense(name,cost,category)
    bottle.redirect('/')

# posts existing/old entries to this route and removes entries from MongoDB
@bottle.route('/oldexpense', method='POST')
def insert_oldexpense():
    name = bottle.request.forms.get("name")
    cost = bottle.request.forms.get("cost")
    category = bottle.request.forms.get("category")
    expenseBook.remove_expense(name, cost, category)
    bottle.redirect('/')


# CONNECTION SETUP
# sets up a connection string (in this case, server is running on cpu (localhost))
connection_string = "mongodb://localhost"

# lets PyMongo know which MongoDB connection to use (PyMongo manages the connection pool)
connection = pymongo.MongoClient(connection_string)

# sets context to the expenses database that we made
database = connection.expenses

# lets our DAO (Data Access Object) class know about the connection
expenseBook = expenseBookDAO.expenseBookDAO(database)

bottle.debug(True)
bottle.run(host='localhost', port=8082)