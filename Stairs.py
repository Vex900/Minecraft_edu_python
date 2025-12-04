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
    agent.set_slot(2)
    agent.move(FORWARD, lenght)
    agent.set_assist(PLACE_ON_MOVE, False)
    agent.turn(TurnDirection.LEFT)
    agent.turn(TurnDirection.LEFT)
    agent.move(BACK, 1)
    agent.move(UP, 1)
    agent.set_slot(1)
    for index in range(height):
        agent.move(DOWN, 1)
        agent.place(FORWARD)
        agent.move(BACK, 1)

player.on_chat("buildstairs2", buildstairs)
