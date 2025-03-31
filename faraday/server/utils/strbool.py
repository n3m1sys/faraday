
def strtobool(val):
    val = val.lower()
    if val in ('y', 'yes', 'yay', 't', 'true', 'on', '1'):
        return 1
    elif val in ('n', 'no', 'nay', 'f', 'false', 'off', '0'):
        return 0
    else:
        raise ValueError(f"Invalid value for boolean conversion: {val}")