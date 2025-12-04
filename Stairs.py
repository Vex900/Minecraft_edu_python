def buildstairs(height, lenght):
    agent.set_assist(PLACE_ON_MOVE, False)
    agent.set_slot(1)
    for index in range(height):
        agent.place(BACK)
        agent.move(FORWARD, 1)
        agent.move(UP, 1)
    agent.move(DOWN, 1)
    agent.move(BACK, 1)
    agent.set_assist(PLACE_ON_MOVE, True)
