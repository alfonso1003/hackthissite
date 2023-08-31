def decrypt(string):
    ords = [ord(c) for c in string]
    new_ords = [o - i for i, o in enumerate(ords)]
    decrypted_string = "".join(
        [chr(no) for no in new_ords]
    )
    return decrypted_string
    

assert decrypt("ace468") == "abc123"

decrypt("cdh8e;h;")  # 'ccf5a6b4'
