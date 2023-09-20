'''(一)用%run指令執行ipython'''
a=5
b=6
c=7.5

# 開啟終端機 > 輸入ipython
# %ipython_scripts_test.py (透過ipython執行檔名)
# 輸入a > 得出5 (b、c 以此類推)

'''（二）用％load執行jupyter notebook'''
# run ipython_script_test.py
# 執行不出來，是不是沒下載jupyter notebook?

'''（三）使用?檢查'''
# 終端機輸入ipython進入環境
# 輸入b=[1, 2, 3]
# 輸入b? > 得出以下資料：
# type:List （預設為清單？）
# strimg form （清單內容？）
# Length （清單長度？）
# Docstring：Built-in mutable sequence. （文檔字符串，內置可變序列）
# If no argument is given, the constructor creates a new empty list. （如果沒有給參數，函數將創建一個新的空列表List）
# The argument must be an iterable if specified. (如果有指定，參數必須是可以疊代的)

# 輸入print? （代表什麼意思？）
# Docstring:
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# Prints the values to a stream, or to sys.stdout by default.
# Optional keyword arguments:
# file:  a file-like object (stream); defaults to the current sys.stdout.
# sep:   string inserted between values, default a space.
# end:   string appended after the last value, default a newline.
# flush: whether to forcibly flush the stream.
# Type:      builtin_function_or_method

# 註解 python不支援多行註解 （但ipynb可以用“”“多行註解“”“？）


