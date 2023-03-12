def colorsorter(colors):
    num_red = 0
    num_green = 0
    num_blue = 0
    
    for _ in range(len(colors)):
        current_ball_pos = num_red + num_green
        if colors[current_ball_pos] == "R":
            # Intercambio rojo
            new_ball_pos = num_red
            colors[new_ball_pos], colors[current_ball_pos] = colors[current_ball_pos], colors[new_ball_pos]
            num_red += 1
        elif colors[current_ball_pos] == "V":
            # Intercambio verde
            num_green += 1
        else:
            # Intercambio azul
            new_ball_pos = len(colors) - num_blue - 1
            colors[new_ball_pos], colors[current_ball_pos] = colors[current_ball_pos], colors[new_ball_pos]
            num_blue += 1  
    return colors
    
