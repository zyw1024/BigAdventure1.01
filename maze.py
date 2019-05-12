import numpy
from numpy.random import randint as rand
import tile as t


def make_maze(s):
    """make the  maze matrix"""
    shape = s.maze_height, s.maze_width
    # Build empty Maze
    maze = numpy.zeros(shape, dtype=int)
    print("1st, Build empty maze:\n",maze)
    # Fill border walls
    maze[0, :] = maze[-1, :] = 1
    maze[:, 0] = maze[:, -1] = 1
    print("2nd, fill border walls:\n", maze)
    minx = 0
    maxx = s.maze_width - 1
    miny = 0
    maxy = s.maze_height - 1
    maze = maze_section(maze, minx, maxx, miny, maxy, 1)
    #test
    # print(maze)
    # print("maze_width: " + str(s.maze_width))
    # print("maze_height: " + str(s.maze_height))
    # print(maze[:,1])
    # print(maze[miny+1,:])
    # print(maze[miny+2,:])
    return maze



def maze_section(maze, minx, maxx, miny, maxy, iteration):
    skip = 0
    # Test to see if there is room for walls
    invalidcols = [(miny + 1), (maxy - 1)]
    for y in range((miny + 1), (maxy - 1)):
        if maze[y, minx] != 1 or maze[y, maxx] != 1:
            if y not in invalidcols:
                invalidcols.append(y)
    invalidrows = [(minx + 1), (maxx - 1)]
    for x in range((minx + 1), (maxx - 1)):
        if maze[miny, x] != 1 or maze[maxy, x] != 1:
            if x not in invalidrows:
                invalidrows.append(x)
    print("0th, invalidcols and invalidrows")
    print(invalidcols)
    print(invalidrows)
    # check for corridors that are too small for a wall due to the 1 space on either side limit and door positioning
    if (maxx - minx) <= len(invalidrows) + 1 or (maxy - miny) <= len(invalidcols) + 1:
        return maze
    # Push wall & corr out of min, but leave it in the max as the max is never picked
    wallx = 0
    while wallx == 0 or wallx in invalidrows:
        wallx = rand((minx + 2), maxx - 1)
        # wallx = rand((minx + 0), maxx - 1)
    wally = 0
    while wally == 0 or wally in invalidcols:
        wally = rand((miny + 2), maxy - 1)

    print("3rd, set cross walls")
    print("wally, wallx = ",wally,",",wallx)
    # set bits to 1 for the walls
    maze[wally, (minx + 1):maxx] = 1
    maze[(miny + 1):maxy, wallx] = 1
    print(maze)

    # Make 3 doors at random
    # coin flip to see if a door should be placed, otherwise flag a skip
    if rand(1, 3) == 1:
        maze = door(maze, "x", wallx, miny, wally)  #  left
    else:
        skip = 1
    if rand(1, 3) == 1 or skip > 0:
        maze = door(maze, "y", wally, wallx, maxx)  #  lower
    else:
        skip = 2
    if rand(1, 3) == 1 or skip > 0:
        maze = door(maze, "x", wallx, wally, maxy)  #  right
    else:
        skip = 3
    if skip > 0:
        maze = door(maze, "y", wally, minx, wallx)  #  upper

    print("4th, make 3 random doors among the corss walls")
    print(maze)
    # Determine where the start and end are
    if iteration == 1:
        if skip == 1:
            #point is start door or end door
            if rand(1, 3) == 1:
                point = 2
            else:
                point = 3

            #put door at top left
            if rand(1, 3) == 1:
                maze[rand((miny + 1), wally), minx] = point
            #put door at left upper
            else:
                maze[miny, rand((minx + 1), wallx)] = point

             #exchange the value of the point
            if point == 2:
                point = 3
            else:
                point = 2

            #put door at bottom left
            if rand(1, 3) == 1:
                maze[rand((miny + 1), wally), maxx] = point
            #put door at left lower
            else:
                maze[miny, rand((wallx + 1), maxx)] = point

        elif skip == 2:
            if rand(1, 3) == 1:
                point = 2
            else:
                point = 3

            #put the door at bottom left
            if rand(1, 3) == 1:
                maze[rand((miny + 1), wally), maxx] = point
            #put the door at left lower
            else:
                maze[miny, rand((wallx + 1), maxx)] = point

            #exchange the value of the point
            if point == 2:
                point = 3
            else:
                point = 2

            #put the door at bottom right
            if rand(1, 3) == 1:
                maze[rand((wally + 1), maxy), maxx] = point
            #put the door at right lower
            else:
                maze[maxy, rand((wallx + 1), maxx)] = point

        elif skip == 3:
            if rand(1, 3) == 1:
                point = 2
            else:
                point = 3
            #put the door at bottom right
            if rand(1, 3) == 1:
                maze[rand((wally + 1), maxy), maxx] = point
            #put the right lower
            else:
                maze[maxy, rand((wallx + 1), maxx)] = point

            #exchange the point value
            if point == 2:
                point = 3
            else:
                point = 2

             #put the door at top right
            if rand(1, 3) == 1:
                maze[rand((wally + 1), maxy), minx] = point
            #put the door at right upper
            else:
                maze[maxy, rand((minx + 1), wallx)] = point
        else:
            if rand(1, 3) == 1:
                point = 2
            else:
                point = 3

            #put the door at top right
            if rand(1, 3) == 1:
                maze[rand((wally + 1), maxy), minx] = point
            #put the door at right upper
            else:
                maze[maxy, rand((minx + 1), wallx)] = point

            #exchange the point value
            if point == 2:
                point = 3
            else:
                point = 2

            #put the door at top left
            if rand(1, 3) == 1:
                maze[rand((miny + 1), wally), minx] = point
            #put the door at left upper
            else:
                maze[miny, rand((minx + 1), wallx)] = point

    print("5th, make the start and end point at edges")
    print(maze)
    # Check to see if each chamber needs to be broken into more chambers
    maze = maze_section(maze, minx, wallx, miny, wally, (iteration + 1))
    maze = maze_section(maze, wallx, maxx, miny, wally, (iteration + 1))
    maze = maze_section(maze, minx, wallx, wally, maxy, (iteration + 1))
    maze = maze_section(maze, wallx, maxx, wally, maxy, (iteration + 1))
    return maze


def door(maze, axis, wallpoint, mind, maxd):
    doorpoint = rand((mind + 1), maxd)
    if axis == "x":
        maze[doorpoint, wallpoint] = 0
    else:
        maze[wallpoint, doorpoint] = 0
    return maze


def define_maze(s, maze):
    """define the number in the marix as specific meanings"""
    walls = []
    roads = []
    skeleton_soldiers = []
    # for (x, y), value in numpy.ndenumerate(maze):
    for (y, x), value in numpy.ndenumerate(maze):
        wall = t.Wall(s, (x * s.maze_block_width), (y * s.maze_block_height))
        road = t.Road(s, (x * s.maze_block_width), (y * s.maze_block_height))
        if value == 0:
            roads.append(road)
        if value == 1:
            walls.append(wall)
        if value == 2:
            start = wall
        elif value == 3:
            end = wall
    return walls, roads, start, end


