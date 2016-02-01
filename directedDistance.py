#!/usr/bin/python
#-*- coding: utf-8 -*-

import math
## Functions!! Simplifying fractions and radicals.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def simplify_fraction(numer, denom):
    if denom == 0:
        return "Division by 0 - result undefined"
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
    if reduced_den == 1:
        return "%d" % (reduced_num)
    elif common_divisor == 1:
        return "%d/%d" % (numer, denom)
    else:
        return "%d/%d" % (reduced_num, reduced_den)
def simplify_fractionfornum(numer, denom):
    if denom == 0:
        return "Division by 0 - result undefined"
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
    if reduced_den == 1:
        return "%d" % (reduced_num)
    elif common_divisor == 1:
        return "%d" % (numer)
    else:
        return "%d" % (reduced_num)
def simplify_fractionforden(numer, denom):
    if denom == 0:
        return "Division by 0 - result undefined"
    common_divisor = gcd(numer, denom)
    (reduced_den) = (denom / common_divisor)
    if reduced_den == 1:
        return 1
    elif common_divisor == 1:
        return float(denom)
    else:
        return float(reduced_den)
def simpleradical(n):
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
def simpleradicalformat(n):
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
      returnstring += '√' + str(remainder)
  return returnstring
def simpleradicalformatnorad(n):
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
      returnstring += str(remainder)
  return returnstring
def simpleradicalformatfunstuff(n):
  nabs = abs(n)
  trial = math.floor(nabs**0.5)
  coeff = 1
  while trial > 1:
    if n % (trial**2) == 0:
      coeff = trial
      trial = 0
    trial -= 1
  remainder = nabs // coeff**2
  return coeff
def simpleradicalformatnotfunstuff(n):
  nabs = abs(n)
  trial = math.floor(nabs**0.5)
  coeff = 1
  while trial > 1:
    if n % (trial**2) == 0:
      coeff = trial
      trial = 0
    trial -= 1
  remainder = nabs // coeff**2
  return remainder
print "Michael Klamkin 2016"
print "This program uses equations in the standard form (Ax+By+C=0). Please convert to standard form before using this calculator."
print " " '\n'
#Ask for input
PointOREquation = raw_input("Are you comparing two parallel lines or line to point? Enter 1 or 2.")  
if PointOREquation == "1":
  A1 = raw_input('Enter the A value:')
  B1 = raw_input('Enter the B value:')
  C1 = raw_input('Enter the C value:')
  
  equation1 =  str(A1) + 'x + ' + str(B1) + 'y + ' + str(C1) + ' = ' + '0'
  print " " '\n'
  print equation1
  print " " '\n'

  print "Now the second equation"

  A2 = raw_input('Enter the A value:')
  B2 = raw_input('Enter the B value:')
  C2 = raw_input('Enter the C value:')

  if A1 != A2 or B1 != B2:
    print "#### Sorry, you messed up. These lines aren't parallel! Ignore everything after this line! ####"
  equation2 =  str(A2) + 'x + ' + str(B2) + 'y + ' + str(C2) + ' = ' + '0'
  print " " '\n'
  print equation2

  point1x = 0
  negativec1 = -1 * float(C1)
  point1yfrac = simplify_fraction(float(negativec1), float(B1))
  point1y = float(negativec1) / float(B1)
#Tells you the point used in the equation
  print " " '\n'
  print "The point we will be using is " + str(point1x) + ',' +  str(point1yfrac)
  print " " '\n'
#actaul arithmetic part
  insideabs = float(A2) * float(point1x) + float(B2) * float(point1y) + float(C2)
  absvalue = float(abs(insideabs))
#I have a simplified and non simplified value for each answer. That way I can use the original for computations and display the pretty simplified one.
  insidesqrt = float(A2) * float(A2) + float(B2) * float(B2)
  sqrtvalue = math.sqrt(insidesqrt)
  radicalsimp = simpleradicalformat(insidesqrt)
# Final steps!
  finalanswernosign = float(absvalue) / float(sqrtvalue)
  finalanswernosignfrac = simplify_fraction(float(absvalue), float(sqrtvalue))

#This part is for directed distance.
  print " " '\n'
  sign = float(B2) * float(insideabs)
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
  if sqrtvalue != int(sqrtvalue) and insidesqrt <= 8:
    numeratorf = float(absvalue)
    denominator = radicalsimp #The denominator was the radical and will end up in the numerator when you rationalize.
    radicalsimpnorad = float(simpleradicalformatnorad(insidesqrt))
    rationalized = str(numeratorf) + str(radicalsimp) + ' / ' + str(radicalsimpnorad)
  elif sqrtvalue != int(sqrtvalue) and insidesqrt >= 8:
    numeratorfu = str(absvalue)
    #The denominator was the radical and will end up in the numerator when you rationalize.
    simpradformatfunstuff = float(simpleradicalformatfunstuff(insidesqrt))
    simpradformatnotfunstuff = float(simpleradicalformatnotfunstuff(insidesqrt))
    fdenom = float(simpradformatfunstuff)*float(simpradformatnotfunstuff)
    newnum = float(numeratorfu) * float(simpradformatfunstuff)
    rationalized = str(numeratorfu) + '√' + str(simpradformatnotfunstuff) + ' / ' + str(fdenom)
  elif sqrtvalue == 0 or 1:
    numeratorf = float(absvalue)
    rationalized = str(numeratorf) + '/' + str(radicalsimp)
    print "You done goofed1!" #Error message. Put a 1 so I can see exactly where I messed up.
  print "The rationalized answer is: " + rationalized #Yay! Rationalized! But we're not done yet!!
  print " " '\n'
  print " " '\n'
#Sometimes, you can still simplify the fraction after rationalizing the denominator. This does that.
  numeratorf = float(absvalue)
  radicalsimpnorad = float(simpleradicalformatnotfunstuff(insidesqrt))
  simplifyafterradnum =  float(simplify_fractionfornum(numeratorf, radicalsimpnorad))
  simplifyafterradden =  float(simplify_fractionforden(numeratorf, radicalsimpnorad))
  simpradformatfunstuff = float(simpleradicalformatfunstuff(insidesqrt))
  simpradformatnotfunstuff = float(simpleradicalformatnotfunstuff(insidesqrt))
  fdenom = float(simpradformatfunstuff)*float(simpradformatnotfunstuff)
  finalnumerator2 = simplify_fractionfornum(simplifyafterradnum, fdenom)
  finaldenominator2 = simplify_fractionforden(simplifyafterradnum, fdenom)
# Now we have to display that further simplified answer.
  if sqrtvalue != int(sqrtvalue): #If it's not an integer, we had to rationalize it before. If it was an integer our final answer wouldn't have a radical.
    if simplifyafterradden == 1:
      finalanswer = str(simplifyafterradnum) + '√' + str(radicalsimpnorad)
    else:
      finalanswer = str(simplifyafterradnum) + '√' + str(radicalsimpnorad) + ' / ' + str(simplifyafterradden)
  elif sqrtvalue == 0 or 1:
    finalanswer = rationalized
  elif sqrtvalue == int(sqrtvalue): # Look at my previous comment
    finalanswer = str(finalnumerator2) + str(fdenom)
  else:
    print "You gone goofed." #Another error message.

  print "The final answer is: " + str(finalanswer) #Yay! Final answer!

  print " " '\n'
  print "ALWAYS CHECK FOR MISTAKES! THIS PROGRAM DOES NOT SIMPLY FULLY, ALTHOUGH IT TRIES."
  ##############################################  ##############################################  ##############################################

# This is if you're given a line and a point instead of two lines.

elif PointOREquation == "2":
  #Asks for inputs.
  A3 = raw_input('Enter the A value:')
  B3 = raw_input('Enter the B value:')
  C3 = raw_input('Enter the C value:')
  
  equation3 =  str(A3) + 'x + ' + str(B3) + 'y + ' + str(C3) + ' = ' + '0'
  print " " '\n'
  print equation3
  print " " '\n'
  
  point1x1 = raw_input('Enter the x value')
  point1y1 = raw_input('Enter the y value')
  #Blah blah blah, same thing as before. Just copy and paste and change the variables. Although I didn't need to.
  insideabs = float(A3) * float(point1x1) + float(B3) * float(point1y1) + float(C3)
  absvalue = float(abs(insideabs))

  insidesqrt = float(A3) * float(A3) + float(B3) * float(B3)
  sqrtvalue = math.sqrt(insidesqrt)
  radicalsimp = simpleradicalformat(insidesqrt)

  finalanswernosign = float(absvalue) / float(sqrtvalue)
  finalanswernosignfrac = simplify_fraction(float(absvalue), float(sqrtvalue))

#Blah, blah 
  print " " '\n'
  sign = float(B3) * float(insideabs)
  if sign > 0:
    sign = ''
    print "The point is above the line."
  elif sign < 0:
    sign = '-'
    print "The line is above the point."
  else:
    print "Please go back and enter a number. >:("

  directedd = str(sign) + str(finalanswernosignfrac)

#Blah.
  print " " '\n'
#For displaying the final answer. Yes, I know, it's not very pretty.
  if sqrtvalue != int(sqrtvalue) and insidesqrt <= 8:
    numeratorf = float(absvalue)
    denominator = radicalsimp #The denominator was the radical and will end up in the numerator when you rationalize.
    radicalsimpnorad = float(simpleradicalformatnorad(insidesqrt))
    rationalized = str(numeratorf) + str(radicalsimp) + ' / ' + str(radicalsimpnorad)
  elif sqrtvalue != int(sqrtvalue) and insidesqrt >= 8:
    numeratorfu = str(absvalue)
    #The denominator was the radical and will end up in the numerator when you rationalize.
    simpradformatfunstuff = float(simpleradicalformatfunstuff(insidesqrt))
    simpradformatnotfunstuff = float(simpleradicalformatnotfunstuff(insidesqrt))
    fdenom = float(simpradformatfunstuff)*float(simpradformatnotfunstuff)
    print numeratorfu, simpradformatfunstuff
    newnum = float(numeratorfu) * float(simpradformatfunstuff)
    rationalized = str(numeratorfu) + '√' + str(simpradformatnotfunstuff) + ' / ' + str(fdenom)
  elif sqrtvalue == 0 or 1:
    numeratorf = float(absvalue)
    rationalized = str(numeratorf) + '/' + str(radicalsimp)
    print "You done goofed1!" #Error message. Put a 1 so I can see exactly where I messed up.
  print "The rationalized answer is: " + rationalized #Yay! Rationalized! But we're not done yet!!
  print " " '\n'
  print " " '\n'
#Sometimes, you can still simplify the fraction after rationalizing the denominator. This does that.
  numeratorf = float(absvalue)
  radicalsimpnorad = float(simpleradicalformatnotfunstuff(insidesqrt))
  simplifyafterradnum =  float(simplify_fractionfornum(numeratorf, radicalsimpnorad))
  simplifyafterradden =  float(simplify_fractionforden(numeratorf, radicalsimpnorad))
  simpradformatfunstuff = float(simpleradicalformatfunstuff(insidesqrt))
  simpradformatnotfunstuff = float(simpleradicalformatnotfunstuff(insidesqrt))
  fdenom = float(simpradformatfunstuff)*float(simpradformatnotfunstuff)
  finalnumerator2 = simplify_fractionfornum(simplifyafterradnum, fdenom)
  finaldenominator2 = simplify_fractionforden(simplifyafterradnum, fdenom)
# Now we have to display that further simplified answer.
  if sqrtvalue != int(sqrtvalue): #If it's not an integer, we had to rationalize it before. If it was an integer our final answer wouldn't have a radical.
    if simplifyafterradden == 1:
      finalanswer = str(simplifyafterradnum) + '√' + str(radicalsimpnorad)
    else:
      finalanswer = str(simplifyafterradnum) + '√' + str(radicalsimpnorad) + ' / ' + str(simplifyafterradden)
  elif sqrtvalue == 0 or 1:
    finalanswer = rationalized
  elif sqrtvalue == int(sqrtvalue): # Look at my previous comment
    finalanswer = str(finalnumerator2) + str(fdenom)
  else:
    print "You gone goofed." #Another error message.

  print "The final answer is: " + str(finalanswer) #Yay! Final answer!

  print " " '\n'
  print "ALWAYS CHECK FOR MISTAKES! THIS PROGRAM DOES NOT SIMPLY FULLY, ALTHOUGH IT TRIES."
  
else:
  print "You messed up, didn't you. (AGAIN????)" #This shows up when you don't type 1 or 2.
  
  
  #To do: add an error message for when you don't input a number for a, b, c, or points.
