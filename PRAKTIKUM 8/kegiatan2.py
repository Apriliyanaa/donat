#konversi suhu
def konversiSuhu(suhu, satuan):
    """
    Fungsi untuk mengkonversi suhu antara Celcius dan Fahrenheit.

    Args:
        suhu (float): Nilai suhu yang akan dikonversi.
        satuan (str): Satuan suhu awal ('C' untuk Celcius, 'F' untuk Fahrenheit).

    Returns:
        float: Nilai suhu setelah dikonversi.
    """

    if satuan.upper() == 'C':
        # Konversi dari Celcius ke Fahrenheit
        fahrenheit = (suhu * 9/5) + 32
        return fahrenheit
    elif satuan.upper() == 'F':
        # Konversi dari Fahrenheit ke Celcius
        celcius = (suhu - 32) * 5/9
        return celcius
    else:
        return "Satuan tidak valid. Gunakan 'C' untuk Celcius atau 'F' untuk Fahrenheit."