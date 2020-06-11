# imports

# modules

def filtered_input(input_type='str', error_message='Try again.'):
    valid = False
    input_text = ''
    while not valid:
        input_text = input()
        valid = check_input(input_text, input_type=input_type)
        if not valid:
            print(error_message)
    return input_text

def check_input(input_text, input_type='str'):
    try:
        if input_type=='str':
            str(input_text)
        elif input_type=='int':
            int(input_text)
        elif input_type=='float':
            float(input_text)
    except ValueError:
        return False
    return True
