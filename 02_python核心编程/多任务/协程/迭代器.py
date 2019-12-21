class Friends(object):
    def __init__(self):
        self.names = []
        self.current_num = 0
    
    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num +=1
            return ret
        else:
            raise StopIteration

        
friends = Friends()
friends.add('John')
friends.add('Susan')
friends.add('Miller')

for friend in friends:
    print(friend)
    
