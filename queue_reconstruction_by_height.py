class Solution(object):
    def reconstructQueue(self, people):
        if not people:
            return []
        ordered_line = []
        insertion_order = sorted(people, key = lambda x: (-x[0], x[1]))
        for person in insertion_order: 
            ordered_line.insert(person[1], person)
        return ordered_line