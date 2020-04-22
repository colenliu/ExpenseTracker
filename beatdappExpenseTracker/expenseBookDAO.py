class expenseBookDAO(object):

    # initailize our DAO class with the database and set the desired MongoDB collection
    def __init__(self, database):
        self.db = database
        self.myexpenses = database.myexpenses

    # function that handles expense finding
    def find_expenses(self):
        l = []
        for each_expense in self.myexpenses.find():
            l.append({'name':each_expense['name'], 'cost':each_expense['cost'],
                      'category':each_expense['category']})

        return l

    # function that handles the insertion of expenses
    def insert_expense(self,newname,newcost,newcategory):
        newexpense = {'name':newname,'cost':newcost, 'category':newcategory}
        self.myexpenses.insert(newexpense)

    # function that handles the removal of expenses
    def remove_expense(self, oldname, oldcost, oldcategory):
        oldexpense = {'name':oldname, 'cost':oldcost, 'category':oldcategory}
        self.myexpenses.remove(oldexpense)