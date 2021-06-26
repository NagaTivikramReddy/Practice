from datetime import datetime,timedelta

cur_time = datetime.now()

type(cur_time)

cur_time = datetime.now().replace(microsecond = 0)

print(cur_time)
new_time = cur_time + timedelta(hours = 2)

my_format = "%Y_%b_%d_%H_%M_%S"

##replace Y with y to get just last 2 digits of year --21
##replace m with b to get month in name in shortcut  --Jun
##replace m with B to get month in name in full     --June

new_format_time = datetime.strftime(new_time,my_format)
print(new_time)

my_file = "dhoni_" + str(new_format_time) + ".txt"
my_obj = open(my_file,"a")
my_obj.write("Welcome")
my_obj.close()
