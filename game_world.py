objects = [[], []]

def add_object(o, depth):
    objects[depth].oppend(o)

def add_objects(ol, depth):
    objects[depth] += ol

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            del(o)
            return



