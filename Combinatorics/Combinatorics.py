class Combinatorics:

    @staticmethod
    def permutationsDup(list_of_occurancies, length, explicitely = False):
        '''Function that computes the number of permutations with dublicates
        from a list of values. If the third parameter is set True, than 
        this function will return the actual set of all permutations with dublicates.'''

        answer_set = set([()])
        for i in range(length):
            temp_set = set()
            for occurance in list_of_occurancies:
                for element in answer_set:
                    temp_list = list(element)
                    temp_list.append(occurance)
                    temp_set.add(tuple(temp_list))
            answer_set = temp_set
        if explicitely:
            return answer_set
        else:
            return len(answer_set)


    @staticmethod
    def permutations(list_of_occurancies, length, explicitely = False):
        '''Same as the previous function but without dublicates.'''

        answer_set = set([()])
        for i in range(length):
            temp_set = set()
            for occurance in list_of_occurancies:
                for element in answer_set:
                    temp_list = list(element)
                    if occurance not in temp_list:
                        temp_list.append(occurance)
                        temp_set.add(tuple(temp_list))
            answer_set = temp_set
        if explicitely:
            return answer_set
        else:
            return len(answer_set)


    @staticmethod
    def combinationsDub(list_of_occurancies, length, explicitely = False):
        '''Same as before only this time the function returns all
        the combinations with dublicates.'''

        answer_set = set([()])
        for i in range(length):
            temp_set = set()
            for occurance in list_of_occurancies:
                for element in answer_set:
                    temp_list = list(element)
                    temp_list.append(occurance)
                    temp_list.sort()
                    temp_set.add(tuple(temp_list))
            answer_set = temp_set
        if explicitely:
            return answer_set
        else:
            return len(answer_set)


    @staticmethod
    def combinations(list_of_occurancies, length, explicitely = False):
    	'''Same as before only this time the function returns all
        the combinations without dublicates.'''

        answer_set = set([()])
        for i in range(length):
            temp_set = set()
            for occurance in list_of_occurancies:
                for element in answer_set:
                    temp_list = list(element)
                    if occurance not in temp_list:
                        temp_list.append(occurance)
                        temp_list.sort()
                        temp_set.add(tuple(temp_list))
            answer_set = temp_set
        if explicitely:
            return answer_set
        else:
            return len(answer_set)

print Combinatorics.combinations(range(1,50), 6)