#Write a function that takes a list value as an argument
#and returns a string with all the items separated by a comma
#and a space, with and inserted before the last item.
#Be sure to test the case where an empty list [] is passed to your function.


spam = ['apples', 'bananas', 'tofu', 'cats']
first_aid = ['band-aid', 'gauze', 'flare']
music_room = ['piano', 'guitar', 'uke', 'flute']
empty_list = []

def separate(list):
    list.insert(-1, 'and')
    new_list = ', '.join(list)
    print(new_list)
        
separate(spam)
separate(first_aid)
separate(music_room)
separate(empty_list) #empty list test

