mapping = {
  "5EAYBxtPhkVgkoyW6rAYTLhiM3Rbv8s32oaxeEK6QbD5Z4Ld" : {"sigma" : 0.98, "algo" : "simulate_single_price_path_gbm", "strategy" : "regular"}, # making money
  "5EbbNM6JBtKVF7gwdW3fcp78J2EQYx1Y3Gg8wwZhhcPHNme7" : {"sigma" : 0.96, "algo" : "simulate_single_price_path", "strategy" : "regular"}, # making money
  "5H9RWmJ48VHXxYJidKa8qGvYCHuyxGyUqisGSbbHakB14oqq" : {"sigma" : 0.94, "algo" : "simulate_single_price_path_gbm", "strategy" : "regular"}, # making money
  "5HBPzDhwAJqXbBtqaaShKojisx7rybxAdfmLRvNwnmo4za9f" : {"sigma" : 0.92, "algo" : "simulate_single_price_path", "strategy" : "regular"}, # making money
  "5DLF2dzifMBZTBRBSytTaGWPWeNzd1MZpAkAqD65n9KjJXnF" : {"sigma" : 1.2, "algo" : "simulate_single_price_path_gbm", "strategy" : "regular"},
  "5CDZqing5GnN9ftZ2g7oBVYR5mSsoFZwfPBWVgQxEd1rEzMi" : {"sigma" : 1.1, "algo" : "simulate_single_price_path", "strategy" : "regular"},
  "5FLC6usUvg7aMrr2Jh1eaYExFdT15H7FqwLW9E6mo4cS3GUg" : {"sigma" : 0.8, "algo" : "simulate_single_price_path_gbm", "strategy" : "regular"},


  # student
  "5DbxBFeEfxnsNYnx95YqDG74fpxMLQQwBnGrskDCNzjJFvxW" : {"sigma" : 1.06, "algo" : "simulate_price_path_student_t", "strategy" : "spyros"}, # making money
  "5CDZtpfGqmWPnMsZHSoXTr8hbHjkA7KfBc7pYSm5rdkhyQJh" : {"sigma" : 1.2, "algo" : "simulate_price_path_student_t", "strategy" : "regular"},
  "5CSKHRJwDiBEeyhc2ziUkQbTGkcMK2xSmbHFGTtnZDrYttUi" : {"sigma" : 0.9, "algo" : "simulate_price_path_student_t", "strategy" : "spyros"},
  "5EJ4LUq7RJoEzq5wREh3hYWze1SCr4YKdrvEnpLc1PTbdaA4" : {"sigma" : 0.8, "algo" : "simulate_price_path_student_t", "strategy" : "regular"},
  "5GsZ4uJL6UC2tucgKtojzXCVMSVrQ3oDxvRUT3nKJL54TXZi" : {"sigma" : 0.7, "algo" : "simulate_price_path_student_t", "strategy" : "spyros"},
  "5GpCoNpSYxQ2Fpgxm7Eyoghkb8bTmbd7Dh1XsERLVX6p5w7f" : {"sigma" : 0.6, "algo" : "simulate_price_path_student_t", "strategy" : "regular"},



  # spyros
  "5HT6iGZ8KBJLifhEpWwfV8ZfoFjz1tPoaBEydvoJvMsnYZsy" : {"sigma" : 0.9, "algo" : "simulate_single_price_path", "strategy" : "spyros"}, # making money
  "5FYhH1JMNe22G7PqmJfXXRGLmbZGY65SL2z6d73WWp5ftda5" : {"sigma" : 1.2, "algo" : "simulate_single_price_path_gbm", "strategy" : "spyros"}, # live
  "5D2D5rRPZSzqvS1d7KDqSzbqbL6Eo6PteShd7i2oNcXboYpi" : {"sigma" : 1.1, "algo" : "simulate_single_price_path_gbm", "strategy" : "spyros"},
  "5HoviLrfGLJC1N2dKhuqxb33PP57v5tSg9zNd59xFZoCdymY" : {"sigma" : 1.0, "algo" : "simulate_single_price_path_gbm", "strategy" : "spyros"},
  "5Fvfszm7RqYpqUqS9UFimsxcS5EpoD7z1D8PnwmJcYDSrzKf" : {"sigma" : 0.8, "algo" : "simulate_single_price_path_gbm", "strategy" : "spyros"},


  "5GHeboa3d4QTdnboR1oQLeQiZudX9cKYyBpY6VHjxsSvCC29" : {"sigma" : 1.16, "algo" : "simulate_single_price_path", "strategy" : "historic"}, # dead
  "5Hj5DvTSXoUWMga4HzJrw3EZYrbF2S6zeRVVEWeKouL73LkB" : {"sigma" : 0.7, "algo" : "simulate_single_price_path", "strategy" : "spyros"} # dead

}


def get_factor(hot_key, asset):
  if hot_key in mapping:
    return mapping[hot_key]["sigma"]
  else:
    return 0.666

def get_algo(hot_key, asset):
  if hot_key in mapping:
    return mapping[hot_key]["algo"]
  else:
    return "simulate_single_price_path"

def get_strategy(hot_key, asset):
  if hot_key in mapping:
    return mapping[hot_key]["strategy"]
  else:
    return "regular"    

