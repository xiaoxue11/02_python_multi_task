from collections.abc import Iterable, Iterator

class Friends(object):

    def __init__(self):
        self.names = []
    
    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        return Friends_Iterator(self)


class Friends_Iterator(object):

    def __init__(self,obj):
        self.obj = obj
        self.current_num =0

    def __iter__(self):
        pass

    def __next__(self):
        if self.current_num < len(self.obj.names):
            ret = self.obj.names[self.current_num]
            self.current_num +=1
            return ret
        else:
            raise StopIteration

        
friends = Friends()
friends.add('John')
friends.add('Susan')
friends.add('Miller')

print('whether friends is iterable', isinstance(friends, Iterable))
print('whether friends is iterator', isinstance(iter(friends), Iterator))

for friend in friends:
    print(friend)