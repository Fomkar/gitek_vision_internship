def coordinate_finder(image, lower, upper, color = "Blue", x1_found = False):
    
    x1_found, y1_found = False, False
    
    color_code = -1
    
    # Color Codes Arranged According to OpenCV BGR Format.
    if color == "Blue":
        color_code = 0
    elif color == "Green":
        color_code = 1
    else:
        color_code = 2
        
    # Find Object's X1 Position.
    for x in range(0, image.shape[1]):
        for y in range(0, image.shape[0]):
            if lower < image[y, x, color_code] < upper:
                x1 = x
                x1_found = True
                break
        if x1_found:
            break
    
    # Find Object's X2 Position.
    for x in range(0, image.shape[1]):
        for y in range(0, image.shape[0]):
            if lower < image[y, x, color_code] < upper:
                x2 = x
    
    # Find Object's Y1 Position.
    for y in range(0, image.shape[0]):
        for x in range(0, image.shape[1]):
            if lower < image[y, x, color_code] < upper:
                y1 = y
                y1_found = True
                break
        if y1_found:
            break
    
    # Find Object's Y2 Position.
    for y in range(0, image.shape[0]):
        for x in range(0, image.shape[1]):
            if lower < image[y, x, color_code] < upper:
                y2 = y
    
    return x1, x2, y1, y2