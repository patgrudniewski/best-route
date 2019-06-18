# TODO: implement cache as some of the values are calculated multiple times
# TODO: verify if input is correct? for now it's duck typing
def best_route(pyramid, indexes = None, acc = 0):
    upper_pyramid = pyramid[:-1]
    current_level = pyramid[::-1][0] # lowest level is always processed one
    level_size = len(current_level)

    if not upper_pyramid:
        # assumption made that if there's no upper_pyramid it means current_level contains only one value
        return current_level[0] + acc

    if indexes is None:
        indexes = range(0, level_size)

    routes = ()
    for index in indexes:
        ancestors = [x for x in (index - 1, index) if x >= 0 and x <= level_size - 2]

        routes = routes + (best_route(
            upper_pyramid,
            ancestors,
            acc + current_level[index]
        ),)

    return max(routes)

__all__ = ['best_route']
