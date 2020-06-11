def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner('Moon and Stars')
banner('Moon and Stars', '*')
banner(border='.', message = 'Sun Moon and Stars')