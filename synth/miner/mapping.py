def get_factor(hot_key, asset):
  mapping = {
    "5EAYBxtPhkVgkoyW6rAYTLhiM3Rbv8s32oaxeEK6QbD5Z4Ld" : 0.81225,
    "5EbbNM6JBtKVF7gwdW3fcp78J2EQYx1Y3Gg8wwZhhcPHNme7" : 0.83255625,
    "5FYhH1JMNe22G7PqmJfXXRGLmbZGY65SL2z6d73WWp5ftda5" : 0.95,
    "5HoviLrfGLJC1N2dKhuqxb33PP57v5tSg9zNd59xFZoCdymY" : 0.876375,
    "5H9RWmJ48VHXxYJidKa8qGvYCHuyxGyUqisGSbbHakB14oqq" : 0.792439024,
    "5HBPzDhwAJqXbBtqaaShKojisx7rybxAdfmLRvNwnmo4za9f" : 0.773571429,
    "5DLF2dzifMBZTBRBSytTaGWPWeNzd1MZpAkAqD65n9KjJXnF" : 0.839534884,
    "5CDZqing5GnN9ftZ2g7oBVYR5mSsoFZwfPBWVgQxEd1rEzMi" : 0.7,
    "5FLC6usUvg7aMrr2Jh1eaYExFdT15H7FqwLW9E6mo4cS3GUg" : 0.68,
    "5Hj5DvTSXoUWMga4HzJrw3EZYrbF2S6zeRVVEWeKouL73LkB" : 0.66,
    "5HT6iGZ8KBJLifhEpWwfV8ZfoFjz1tPoaBEydvoJvMsnYZsy" : 0.64,
    "5Fvfszm7RqYpqUqS9UFimsxcS5EpoD7z1D8PnwmJcYDSrzKf" : 0.7,
    "5CDZtpfGqmWPnMsZHSoXTr8hbHjkA7KfBc7pYSm5rdkhyQJh" : 0.7,
    "5CSKHRJwDiBEeyhc2ziUkQbTGkcMK2xSmbHFGTtnZDrYttUi" : 0.7,
    "5EJ4LUq7RJoEzq5wREh3hYWze1SCr4YKdrvEnpLc1PTbdaA4" : 0.7,
    "5GsZ4uJL6UC2tucgKtojzXCVMSVrQ3oDxvRUT3nKJL54TXZi" : 0.7,
    "5GpCoNpSYxQ2Fpgxm7Eyoghkb8bTmbd7Dh1XsERLVX6p5w7f" : 0.7,
    "5D2D5rRPZSzqvS1d7KDqSzbqbL6Eo6PteShd7i2oNcXboYpi" : 0.7,
    "5DbxBFeEfxnsNYnx95YqDG74fpxMLQQwBnGrskDCNzjJFvxW" : 0.7,
    "5GHeboa3d4QTdnboR1oQLeQiZudX9cKYyBpY6VHjxsSvCC29" : 0.7    
  }

  if hot_key in mapping:
    return mapping[hot_key]
  else:
    return 0.666


