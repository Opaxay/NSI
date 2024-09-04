def dec2bin(nb, zeronb):

    if nb < 0:
        nb = (1 << zeronb) + nb
    
    bin_result = bin(nb)[2:]
    bin_result = bin_result.zfill(zeronb)
    print(bin_result)


dec2bin(5,10 )
