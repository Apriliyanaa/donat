def konversiSuhu(C=None, F=None):
  """Fungsi untuk mengkonversi suhu antara Celcius dan Fahrenheit.

  Args:
    C: Suhu dalam Celcius ().
    F: Suhu dalam Fahrenheit ().

  Returns:
    String yang menunjukkan hasil konversi.
  """

  if C is not None:
    F = (C * 9/5) + 32
    return f"Suhu {C} Celcius setara dengan {F} Fahrenheit"
  elif F is not None:
    C = (F - 32) * 5/9
    return f"Suhu {F} Fahrenheit setara dengan {C} Celcius"
  else:
    return "Harap masukkan suhu dalam Celsius atau Fahrenheit!"
hasil = konversiSuhu(C=95)
print(hasil)