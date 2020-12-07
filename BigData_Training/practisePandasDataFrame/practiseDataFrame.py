import pandas as pds

salary = {'备注': ['不及格', '良好', '最佳', '优秀'],
          '工资': [5000, 7000, 9000, 8500],
          '绩效分': [60, 84, 98, 91]}

frame = pds.DataFrame(salary,
                      columns=['备注', '工资', '绩效分'],
                      index=['老王', '小刘', '小赵', '老龚'])

print(frame)

