# -*- coding: utf-8 -*-
import IPython
from IPython.core.display import display, HTML
from IPython.core.display import display, Markdown
import pandas as pd 
import datetime
import numpy as np
from itables import show
from scipy.stats import norm
from scipy.stats import beta

mkd = Markdown(f'''
This is *question 0* for [problem set 1](https://jbhender.github.io/Stats507/F21/ps1.html) of [Stats 507](https://jbhender.github.io/Stats507/F21/).
 > #### Question 0 is about Markdown.
 
The next question is about the **Fibonnaci sequence**, $ F_n=F_{'n-1'}+F_{'n-2'}$. In part **a** we will define a Python function `fib_rec()`.

Below is a …

### Level 3 Header
Next, we can make a bulleted list:

- Item 1

    - detail 1
    - detail 2
- Item 2

Finally, we can make an enumerated list:

1. Item 1
2. Item 2
3. Item 3

 ''')


## Q1
def fib_rec(n):
	"""
    using recursion Return Fibonnaci seuqence Fn 
    begins with the numbers $ 0,1,1,... 
    and continues so that each entry is the 
    sum of adding its two immediate predecessors. 

    Parameters
    ----------
    n: Int number of fibonnaci sequence


     Returns
     -------
    Return Fibonnaci seuqence Fn.

    """
	if n ==0 or n == 1:
		return n 
	else: return (fib_rec(n-1)+fib_rec(n-2))

def fib_for(n):
	"""
    function fib_for() with the same signature that 
    computes Fn by summation using a for loop
    Return Fibonnaci seuqence Fn begins with 
    the numbers $ 0,1,1,... 
    and continues so that each entry is the
    sum of adding its two immediate predecessors. 

    Parameters
    ----------
    n: Int number of fibonnaci sequence


     Returns
     -------
    Return Fibonnaci seuqence Fn.

    """
	map = {}
	if n == 0 or n == 1:
		return n
	else:
		for i in range(n+1):
			if i ==0 or i == 1:
				map[i] = i 
			else:
				map[i] = map[i-2] + map[i-1]
		return map[n]

def fib_whl(n):
	"""
    function fib_whl() with the same signature that 
    computes Fn by summation using a while loop
    Return Fibonnaci seuqence Fn begins with 
    the numbers $ 0,1,1,... 
    and continues so that each entry is the
    sum of adding its two immediate predecessors. 

    Parameters
    ----------
    n: Int number of fibonnaci sequence


     Returns
     -------
    Return Fibonnaci seuqence Fn.
	"""
	map = {}
	i = 0
	while i <= n:
		if i <=1:
			map[i] = i
		else: 
			map[i] = map[i-2] + map[i-1]
		i += 1
	return map[n]

def fib_rnd(n):
	"""
	function fib_for() with the same signature that 
    computes Fn by summation using a rounding
    Return Fibonnaci seuqence Fn begins with 
    the numbers $ 0,1,1,... 
    and continues so that each entry is the
    sum of adding its two immediate predecessors. 

    Parameters
    ----------
    n: Int number of fibonnaci sequence


     Returns
     -------
    Return Fibonnaci seuqence Fn.
	"""
	p = (1+np.sqrt(5)) / 2
	return round((p**n)/np.sqrt(5))

def fib_flr(n):
	"""
	function fib_for() with the same signature that 
    computes Fn by summation using floor truncate
    Return Fibonnaci seuqence Fn begins with 
    the numbers $ 0,1,1,... 
    and continues so that each entry is the
    sum of adding its two immediate predecessors. 

    Parameters
    ----------
    n: Int number of fibonnaci sequence


     Returns
     -------
    Return Fibonnaci seuqence Fn.
	"""
	p = (1+np.sqrt(5)) / 2
	return np.floor((p**n)/np.sqrt(5)+0.5)

def fun_time(function, repetition, large_sequence):
	"""
	funtion for calculating the median running time of 
	a function

	Parameters
	----------
	function: any function
	repetition: int, running function times
	large_sequence: list, array 

	Returns
	-------
	Return the median running time of function 
	on that large_sequence
	as a list/array
	"""
	run_list = [] 
	for seq in large_sequence:
		lst = []
		for i in range(repetition):
			begin_time = datetime.datetime.now()
			function(seq)
			execution_time = datetime.datetime.now() - begin_time
			lst.append(execution_time)
		median_time = np.median(lst)
		run_list.append(median_time)
	return run_list

# test
# lst_time = fun_time(fib_rec,3,np.arange(10,40,10))
# print(lst_time)
# empty_lst= []
# for i in lst_time:
# 	print(i)

fun_tuple = (fib_rec,fib_for,fib_whl,fib_flr,fib_rnd)
map = {}
large_sequence = np.arange(10,30,5)
for fun in fun_tuple:
	name = str(fun)
	map[name] = fun_time(fun,3,large_sequence)
# print(map)
df = pd.DataFrame(map)
new_colmuns = ['Recursion (ms)','For loop (ms)','While lopp (ms)','Truncate (ms)','Round (ms)']
df.set_axis(new_colmuns, axis = 1, inplace = True)
df.index = [('n='+str(x)) for x in large_sequence]
for col in df.columns:
    series = df[col].dt.microseconds
    df[col] = series
print(df)
show(df)

## Q2
def combination(n,k):
    '''
    using recursion to return combination numbers

    Parameters
    ----------
    n : int
        total number of items
    k : int
        number of selection items

    Returns
    -------
    combination 

    '''
    if n == 0 and k == 0:
        return 1
    elif n == 1 and (k==0 or k==1):
        return 1
    elif k == 0 or k == n:
        return 1
    else: 
        return combination(n-1, k-1)+combination(n-1, k)
combination(3,2)

def Pascal(n):
    """
    return the nth row of Pascal's triangle in a list

    Parameters
    ----------
    n : int
        specific row of Pascal's triangle

    Returns
    -------
    specific row of Pascal's triangle

    """
    return [combination(n,x) for x in range(n+1)]
print(Pascal(5))

def display_Psc(n):
    """
    

    Parameters
    ----------
    n : int
        specific number of rows

    Returns
    -------
    Print out Pascal's triangel

    """
    map = {}
    for row_num in range(n+1):
        str1 =  ''
        for i in Pascal(row_num):
            str1 = str1 + str(i) +'   ' # add 3 empty spaces
        map[row_num] = str1
    len_base = len(map[n])
    str2 = ''
    for key,value in map.items():
        ini_spaces = np.floor((len_base - len(value))/2)
        str2 = str2 + ' '*int(ini_spaces) + value
        str2 += "\n"
    return print(str2)

display_Psc(10)


## Q3
# a

def pe(data, ci = None,precision = None):
    """
    

    Parameters
    ----------
    data : nd_array
        population
    ci : float from 0 to 1
        confidence level. If none return 95% confidence interval.

    Returns
    -------
    None.

    """
    
    try:
        data = np.asarray(data).reshape((1,-1))
        est = data.mean()
        se = data.std()
        z  = abs(norm.ppf((1-ci)/2))
        lwr =  est - z * (se/np.sqrt(len(data)))
        upr =  est + z * (se/np.sqrt(len(data)))
        map = {'est':est,
               'lwr':lwr,
               'upr':upr,
               'level':ci*100}
        str1 = "{1:.{0}f} [{2:.{0}f}% CI: ({3:.{0}f},{4:.{0}f})]".format(precision, map['est'],
                                                        map['level'],
                                                        map['upr'],
                                                        map['lwr'])
        print(str1)
        return map, str1
    except:
        print('Data cannot be converted to array')
# testing
pe([2,4,1,41,5,3,3,36,3,63,6,3,6,363],ci = 0.95,precision = 2)

# b
def CI(data ,ci,method = None,precision = None):
    # med = (1,2,3,4)
    map = {}
    if precision == None:
        precision = 0 
    try:
        data = np.asarray(data).reshape((1,-1))
        a,b = data.shape
    except: 
        return print('Data cannot be converted to array')
    else:
        n = int(a) * int(b)
        p = data.sum() / n 
        while method == 1:
            if min([n*p,n*(1-p)]) <=12:
                return print('Error message: the condition of np^n(1-p) is not satisfied')
                break
            else:
                z  = abs(norm.ppf((1-ci)/2))
                lwr =  p - z * np.sqrt(p * (1 - p)/n)
                upr =  p + z * np.sqrt(p * (1 - p)/n)
                map = {'est':p,
                       'lwr':lwr,
                       'upr':upr,
                       'level':ci*100}
                str1 = "{1:.{0}f} [{2:.{0}f}% CI: ({4:.{0}f},{3:.{0}f})]".format(precision,map['est'],
                                                                map['level'],
                                                                map['upr'],
                                                                map['lwr'])
                print(str1)
                return map, str1

# testing
# CI([1,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1], ci = 0.95, method = 1)

    # method 2
        while method == 2:
            x = data.sum()
            alpha = 1 - ci
            map['est'] = p
            map['level'] = ci*100
            map['lwr'] = beta.ppf(alpha/2,x,n-x+1)
            map['upr'] = beta.ppf(1-alpha/2,x+1,n-x)
            str1 = "{1:.{0}f} [{2:.{0}f}% CI: ({4:.{0}f},{3:.{0}f})]".format(precision,map['est'],
                                                            map['level'],
                                                            map['upr'],
                                                            map['lwr'])
            print(str1)
            return map, str1
# test
# CI([1,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1], ci = 0.95, method = 2)


        while method == 3:
            x = data.sum()
            alpha = 1 - ci
            map['est'] = p
            map['level'] = ci*100
            map['lwr'] = max(beta.ppf(alpha/2,x+0.5,n-x+0.5),0)
            map['upr'] = min(beta.ppf(1-alpha/2,x+0.5,n-x+0.5),1)
            str1 = "{1:.{0}f} [{2:.{0}f}% CI: ({4:.{0}f},{3:.{0}f})]".format(precision,map['est'],
                                                            map['level'],
                                                            map['upr'],
                                                            map['lwr'])
            print(str1)
            return map, str1
# test
# CI([1,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1], ci = 0.95, method = 3)

        while method == 4:
            x = data.sum()
            z  = abs(norm.ppf((1-ci)/2))
            n_tilda = n + z**2
            p = (x + (z**2)/2)/n_tilda
            lwr =  p - z * np.sqrt(p * (1 - p)/n)
            upr =  p + z * np.sqrt(p * (1 - p)/n)
            map = {'est':p,
                   'lwr':lwr,
                   'upr':upr,
                   'level':ci*100}
            str1 = "{1:.{0}f} [{2:.{0}f}% CI: ({4:.{0}f},{3:.{0}f})]".format(precision,map['est'],
                                                            map['level'],
                                                            map['upr'],
                                                            map['lwr'])
            print(str1)
            return map, str1  
# CI([1,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1], ci = 0.95, method = 4)
test_data = np.concatenate((np.zeros(48),np.ones(42)),axis = None)
def generate_table(precision = None):
    df_test = pd.DataFrame()
    method_map = {1:'standard',2:'Clopper-Pearson',3:"Jeffrey's interval",4:"Agresti-Coull" }
    for i, name in method_map.items():
        input = []
        for ci in (0.9,0.95,0.99):
            map, str1 = CI(test_data,
                           ci,
                           method = i,
                           precision = precision)
            tup = "({1:.{0}f},{2:.{0}f})".format(precision,map['lwr'],map['upr'])
            # print(tup)
            input.append(tup)
        df_test[name] = input
    gau_list = []
    for ci in (0.9,0.95,0.99):
        gau_map,_ = pe(test_data,ci=ci,precision =3)
        tup = "({1:.{0}f},{2:.{0}f})".format(precision,gau_map['lwr'],gau_map['upr'])
        gau_list.append(tup)
    df_test['Gaussian'] = gau_list
    return df_test
df_result = generate_table(3)
df_result.index = [x for x in (0.9,0.95,0.99)]
show(df_result)
print(df_result)
            
            
            




