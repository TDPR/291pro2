# This function handles each query that the user inputs
# then performs an intersection on all the queries
# if there is more than one

def userQueries(userInput):
    # userInput is assumed to be a list of lists
    # the output of each query function is a list

    allQueries = []
    if len(userInput) > 0:
        for query in userInput:
            if len(query) == 3:
                if query[1] in ['>','<','<=','=<','>=','=>']
                    allQueries.append(rangeSearch(query))
                else:
                    allQueries.append(equalSearch(query))
            else:
                allQueries.append(termSearch(query))
        # all query results are in allQueries
        # we perform a intersection on list of list if there is more than one query
        if len(allQueries) > 1:
            return list(set(allQueries[0]).intersection(*allQueries[1:]))
        else:
            return allQueries
    else:
        print('Something is wrong with user input')
        return

    