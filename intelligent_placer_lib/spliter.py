def split_contours(cnts):
    min_y = 1000000
    for cnt in cnts:
        cur_y = min(cnt[:, 0][:, 1])
        if min_y > cur_y:
            poly_cnt = cnt
            min_y = cur_y
    cnts.remove(poly_cnt)
    return poly_cnt, cnts

