# utils.py

def parse_position(pos_str):
    try:
        x, y = map(int, pos_str.strip().split(","))
        if 0 <= x < 10 and 0 <= y < 9:
            return (x, y)
    except:
        return None

