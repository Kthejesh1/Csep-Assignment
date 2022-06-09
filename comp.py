# program to evaluate compound interest
t=int(input("enter no. of years :"));
r=int(input("enter rate of interest:"));
p=int(input("enter principle:"));
print("compount interest of given data",float(p*((1+r/100)**t)));

