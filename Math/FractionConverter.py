class FractionConverter():
    def __init__(self) -> None:
        pass
    def FractionIntoFloat(self, fraction, whole = 0):
        """
        This function will convert your fraction 1/4 1 into an float 1.25 for you
        to use for your formula

        Fractions can only be in this format Numerator/Denumerator(string), whole(int)
        """
        SplittedList = fraction.split("/") #First we will split the fraction into
        Numerator = int(SplittedList[0]) #The Numerator and the
        Denumerator = int(SplittedList[1]) #The Denumerator
        return (Numerator / Denumerator) + whole #better safe than sorry
    def _shorten_fraction(self, fraction):
            """
            This is a private function used to shorten the fractions which come out of
            the FloatIntoFraction function
            """
            from math import gcd
            listing = fraction.split("/") #First we will split the into
            Numerator = int(listing[0]) #The Numerator and the
            Denumerator = int(listing[1]) #Denumerator
            GrCoDi = gcd(Numerator, Denumerator) #Then we will find the Greatest common division
            Numerator /= GrCoDi #Divide both of them with that
            Denumerator /= GrCoDi 
            thething = [str(int(Numerator)), str(int(Denumerator))] #Now we will first convert them into integers
                                                                    #To have unecesary zeros removed then back into a string
                                                                    #Both of them are also in a list
            thething = "/".join(thething) #So we can join them together
            return thething #and return it as a fraction
    def FloatIntoFraction(self, decimal):
        """
        With this function you can turn your float into a string
        please only use floats
        """
        decimalstring = str(decimal) #first we will convert the decimal into a string
        decimalstring = decimalstring.split(".") #So that we will be able to split it
        Numerator = "".join(decimalstring) #The numerator can be the whole number later it will be shortened
        Numerator = int(Numerator) #this is to remove unnecesary zeros
        Numerator = str(Numerator) #but for further proccesing it has to be a string
        Denumerator = "1" + "0" * len(decimalstring[1]) #In here for every after point place we add a zero
        thething = [Numerator, Denumerator] #Now we put them in a list
        thething = "/".join(thething) #to join them together as a string
        return self._shorten_fraction(thething) #and in here we will shorten it first before showing it to the user
    def FractionMath(self, Fraction1, operator, Fraction2):
        """
        With this you are able too do mathematical operations with
        fractions 

        NOTE on the operator:
        +(Addition)
        -(subtraction)
        /(division)
        *(multiplikation)
        please insert the operator as a string
        using anything else will raise an error
        """
        Fraction1 = self.FractionIntoFloat(Fraction1) #I will take the easy way instead of doing some weird stuff with them
        Fraction2 = self.FractionIntoFloat(Fraction2) #I will just convert them into decimals (ONLY BECAUSE IT IS NOT HOW YOU TEACHED ME DOESNT MEAN IT IS WRONG)
        if operator == "+": #I think this i pretty self explanatory
            return self.FloatIntoFraction(Fraction1 + Fraction2)
        elif operator == "-":
            return self.FloatIntoFraction(Fraction1 - Fraction2)
        elif operator == "*":
            return self.FloatIntoFraction(Fraction1 * Fraction2)
        elif operator == "/":
            return self.FloatIntoFraction(Fraction1 / Fraction2)
        else:
            raise Exception(f"Please use \"+\", \"-\", \"*\" or \"/\" as an operator instead of \"{operator}\"") #in case somebody has mistyped something we
                                                                                                                 #we will gently notify him by rasing an exception
                                                                                                                 #instead of breaking his entire formula by returning
                                                                                                                 #a string with the info so he can fix it