#!/usr/bin/python
#-*- coding: utf-8 -*-

import math
## Functions!! Simplifying fractions and radicals.
def gcd(a, b): #gcd for simplifying fractions
    while b:
        a, b = b, a % b
    return a
def simplify_fraction(numer, denom, numorden): #simplify fractions
    if denom == 0:
        return "Division by 0 - result undefined"
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
    if reduced_den == 1:
        return "%d" % (reduced_num)
    elif common_divisor == 1:
        if numorden == "num":
          return "%d" % (numer)
        elif numorden == "den":
          return "%d" % (denom)
        elif numorden == "both":
          return "%d/%d" % (numer, denom)
        else: 
          return "Error on line 25"
    else:
        if numorden == "num":
          return "%d" % (reduced_num)
        elif numorden == "den":
          return "%d" % (reduced_den)
        elif numorden == "both":
          return "%d/%d" % (reduced_num, reduced_den)
        else:
          return "Error on line 34"
def simpleradical(n): #regular
  nabs = abs(n)
  trial = math.floor(nabs**0.5)
  coeff = 1
  while trial > 1:
    if n % (trial**2) == 0:
      coeff = trial
      trial = 0
    trial -= 1
  remainder = nabs // coeff**2
  return coeff, remainder
def simpleradicalformat(n, rad): #pretty
  if n == 0 or n == 1:
    return str(n)
  else:
    coeff, remainder = simpleradical(n)
    returnstring = ''
    if coeff > 1:
      returnstring = str(coeff)
    if n < 0:
      returnstring += "i"     
    if remainder > 1:
      if rad == "rad":
        returnstring += '√' + str(remainder)
      elif rad == "norad":
        returnstring += str(remainder)
      else:
        returnstring = "Error on Line 62"
  return returnstring
def simpleradicalformatfunstuff(n, remorco): # I don't know why I used funstuff. This can return the remainder or coeff as seperate values.
  nabs = abs(n)
  trial = math.floor(nabs**0.5)
  coeff = 1
  while trial > 1:
    if n % (trial**2) == 0:
      coeff = trial
      trial = 0
    trial -= 1
  remainder = nabs // coeff**2
  if remorco == "co":
    return coeff
  elif remorco == "rem":
    return remainder
  else:
    return "Error on line 79"
print "Michael Klamkin 2016"
print "This program uses equations in the standard form (Ax+By+C=0). Please convert to standard form before using this calculator."
print " " '\n' #these skip lines
#Ask for input
PointOREquation = raw_input("Are you comparing two parallel lines or line to point? Enter 1 or 2.")  
A1 = raw_input('Enter the A value:')
B1 = raw_input('Enter the B value:')
C1 = raw_input('Enter the C value:')
  
equation1 =  str(A1) + 'x + ' + str(B1) + 'y + ' + str(C1) + ' = ' + '0'
print " " '\n'
print equation1
print " " '\n'
if PointOREquation == "1":
  print "Now the second equation"

  A2 = raw_input('Enter the A value:')
  B2 = raw_input('Enter the B value:')
  C2 = raw_input('Enter the C value:')

  if (float(A1) != float(A2)) or (float(B1) != float(B2)):
    print "############ Sorry, the equations aren't parallel! Ignore everything after this line! ############"
  equation2 =  str(A2) + 'x + ' + str(B2) + 'y + ' + str(C2) + ' = ' + '0'
  print " " '\n'
  print equation2

  point1x = 0
  negativec2 = -1 * float(C2)
  if float(C2) == 0:
    negativec2 = float(C2)
  else:
    negativec2 = negativec2
  point1yfrac = simplify_fraction(float(negativec2), float(B2), "both")
  point1y = float(negativec2) / float(B1)
#Tells you the point used in the equation
  print " " '\n'
  print "The point we will be using is " + str(point1x) + ',' +  str(point1yfrac)
  print " " '\n'
elif PointOREquation == "2":
  # Point mode is a bit buggy. Be careful and make sure to check your work by hand or with a different calculator.
  point1x = raw_input('Enter the x value')
  point1y = raw_input('Enter the y value')
else:
  print "Please enter 1 or 2."
#actaul arithmetic part
insideabs = float(A1) * float(point1x) + float(B1) * float(point1y) + float(C1)
absvalue = float(abs(insideabs))
#I have a simplified and non simplified value for each answer. That way I can use the original for computations and display the pretty simplified one.
insidesqrt = float(A1) * float(A1) + float(B1) * float(B1)
sqrtvalue = math.sqrt(insidesqrt)
radicalsimp = simpleradicalformat(insidesqrt, "rad")
# Final steps!
finalanswernosign = float(absvalue) / float(sqrtvalue)
finalanswernosignfrac = simplify_fraction(float(absvalue), float(sqrtvalue), "both")

#This part is for directed distance.
sign = float(B1) * float(insideabs)
if sign > 0:
  sign = ''
  print "The first line is above the second one."
elif sign < 0:
  sign = '-'
  print "The second line is above the first one."
else:
  print "Please go back and enter a number. >:("



print " " '\n'
#For displaying the final answer. Yes, I know, it's not very pretty.
numeratorf = float(absvalue)

  
if sqrtvalue != int(sqrtvalue) and insidesqrt <= 8: # 8 because thats the inside of 2sqrt(2). It's the smallest number that can be simplified in a radical.
  denominator = radicalsimp #The denominator was the radical and will end up in the numerator when you rationalize.
  radicalsimpnorad = float(simpleradicalformat(insidesqrt, "norad")) #radical(denom) without the radical sign for making the display pretty
  rationalized = str(numeratorf) + str(radicalsimp) + ' / ' + str(radicalsimpnorad)
    
elif sqrtvalue != int(sqrtvalue) and insidesqrt >= 8: # 8 because thats the inside of 2sqrt(2). It's the smallest number that can be simplified in a radical.
  #The denominator was the radical and will end up in the numerator when you rationalize.
  simpradformatfunstuff = float(simpleradicalformatfunstuff(insidesqrt, "co")) #coefficient of radical to display in the denominator
  simpradformatnotfunstuff = float(simpleradicalformatfunstuff(insidesqrt, "rem")) #remainder that would be under a radical in the numerator after rationalization.
  fdenom = float(simpradformatfunstuff)*float(simpradformatnotfunstuff) #denominator for elif
  rationalized = str(numeratorf) + '√' + str(simpradformatnotfunstuff) + ' / ' + str(fdenom)
    
elif sqrtvalue == 0 or 1: #if it's 0 or 1 there's a special case. Actually it can't ever be 0 but I'm too scared to touch it at this point.
  rationalized = str(numeratorf)
  print "You done goofed1!" #Error message. Put a 1 so I can see exactly where I messed up.
    
print "The rationalized answer is: " + rationalized #Yay! Rationalized! But we're not done yet!!
print " " '\n'
  

#Sometimes, you can still simplify the fraction after rationalizing the denominator. This does that.
#This section splits up the numerator into its two parts- radical and float. It throws out the radical and then does a fraction simplification of float/denominator(rationalized) and then spits it out.
radicalsimpnorad = float(simpleradicalformatfunstuff(insidesqrt, "rem"))

simplifyafterradnum =  float(simplify_fraction(numeratorf, radicalsimpnorad, "num"))
simplifyafterradden =  float(simplify_fraction(numeratorf, radicalsimpnorad, "den"))
  
simpradformatfunstuff = float(simpleradicalformatfunstuff(insidesqrt, "co"))
simpradformatnotfunstuff = float(simpleradicalformatfunstuff(insidesqrt, "rem"))

fdenom = float(simpradformatfunstuff)*float(simpradformatnotfunstuff) #denominator for elif1
finalnumerator = simplify_fraction(simplifyafterradnum, fdenom, "num")
  
# Now we have to display that further simplified answer.
if sqrtvalue != int(sqrtvalue): #If it's not an integer, we had to rationalize it before. If it was an integer our final answer wouldn't have a radical.
  if simplifyafterradden == 1: #if theres no denominator
    finalanswer = str(simplifyafterradnum) + '√' + str(radicalsimpnorad)
  else: #if there is a denominator
    if (sqrtvalue != int(sqrtvalue)) and (insidesqrt >= 8) and (numeratorf == simplifyafterradnum): #if the rationalized answer couldn't be simplified
      finalanswer = str(simplifyafterradnum) + '√' + str(radicalsimpnorad) + ' / ' + str(fdenom)
    else: #if the rationalized answer could be simplified
      finalanswer = str(simplifyafterradnum) + '√' + str(radicalsimpnorad) + ' / ' + str(simplifyafterradden)
elif (sqrtvalue == 0 or 1): #same as above(159)
  finalanswer = rationalized
elif sqrtvalue == int(sqrtvalue): # Look at my comment(180)
  finalanswer = str(finalnumerator) + str(fdenom)
else:
  print "You gone goofed." #Another error message.

print "The final answer is: " + str(finalanswer) #Yay! Final answer!

print " " '\n'
print "ALWAYS CHECK FOR MISTAKES! THIS PROGRAM DOES NOT SIMPLY FULLY, ALTHOUGH IT TRIES."
##############################################  ##############################################  ##############################################

# To do : Work on the bugs in mode 2.
