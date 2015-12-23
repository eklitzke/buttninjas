def escape_input(input_buffer):
    s = input_buffer.replace('&amp;', 'buttninjas')
    s = s.replace('&', '&amp;')
    return s.replace('buttninjas', '&amp;')
