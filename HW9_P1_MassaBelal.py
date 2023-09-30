#Massa Belal
#CS 100 2021F Section 035
#HW 09, November 3, 2021

#1
def file_copy(in_file, out_file):
    inF = open(in_file)
    outF = open(out_file,'w')
    outF.write(inF.read())
    inF.close()
    outF.close()
    
file_copy('created_equal.txt','copy.txt')
