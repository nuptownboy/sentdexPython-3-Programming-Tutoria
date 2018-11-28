#Ways to import the module

import examplemod

examplemod.do_a_thing()#Output:doing something realllly cool!!


from examplemod import do_a_thing as dat,do_another_thing

dat()#Output:doing something realllly cool!!
do_another_thing()#Output:doing some other cool thing!!


from colorama import init,Fore, Back, Style
init()


print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')


