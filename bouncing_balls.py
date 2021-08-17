def bouncing_ball(h, bounce, window):
    if h < 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    how_many_bounces = 0
    while h > window:
        how_many_bounces+=1
        h = h*bounce
        if h > window:
            how_many_bounces+=1
    return how_many_bounces
