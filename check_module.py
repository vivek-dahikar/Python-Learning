import user_define_module1 as m #as is alias

print(m.sum(10,20))
from user_define_module1 import sum #calling specific fucn from module
print(sum(10,20))

from user_define_module1 import * # calling all function
