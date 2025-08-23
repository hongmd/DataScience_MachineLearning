import tidypolars4sci as tp

df = tp.tibble({"x" : range(6),
                "y" : range(6, 12),
                "w" : range(6, 12),
                "z" : ['a', 'a', 'b', 'c', 'd', 'e']})

df = (df
      .select('x', 'y', 'z') 
      .filter(tp.col('x') < 4, tp.col('y') >=7) 
      .arrange(tp.desc('z'), 'x') 
      .mutate(double_x = tp.col('x') * 2, 
              x_plus_y = tp.col('x') + tp.col('y'), 
              z_num = tp.case_when(tp.col("z")=='a', 1, 
                                   tp.col("z")=='b', 2,
                                   True, 0), 
              )

      )

print(df)