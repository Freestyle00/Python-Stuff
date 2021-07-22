class FractionConverter():
    def __init__(self) -> None:
        pass
    def FractionIntoFloat(self, fraction, whole = 0):
        """
        This function will convert your fraction 1/4 into an float 0.25 for you
        to use for your formula

        Fractions can only be in this format 1/4 and should be given as a string
        """
        SplittedList = fraction.split("/")
        Numerator = int(SplittedList[0])
        Denumerator = int(SplittedList[1])
        return (Numerator / Denumerator) + whole #better safe than sorry
    def _shorten_fraction(self, fraction):
            """
            This is a private function used to shorten the fractions which come out of
            the FloatIntoFraction function
            """
            from math import gcd
            listing = fraction.split("/")
            Numerator = int(listing[0])
            Denumerator = int(listing[1])
            GrCoFa = gcd(Numerator, Denumerator)
            Numerator /= GrCoFa
            Denumerator /= GrCoFa
            thething = [str(int(Numerator)), str(int(Denumerator))]
            thething = "/".join(thething)
            return thething
    def FloatIntoFraction(self, decimal):
        """
        With this function you can turn your float into a string
        please only use floats
        """
        decimalstring = str(decimal)
        decimalstring = decimalstring.split(".")
        Numerator = "".join(decimalstring)
        Numerator = int(Numerator) #this is to remove unnecesary zeros
        Numerator = str(Numerator) #but for further proccesing it has to be a string
        Denumerator = "1" + "0" * len(decimalstring[1])
        thething = [Numerator, Denumerator]
        thething = "/".join(thething)
        return self._shorten_fraction(thething)
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
        Fraction1 = self.FractionIntoFloat(Fraction1)
        Fraction2 = self.FractionIntoFloat(Fraction2)
        if operator == "+":
            return self.FloatIntoFraction(Fraction1 + Fraction2)
        elif operator == "-":
            return self.FloatIntoFraction(Fraction1 - Fraction2)
        elif operator == "*":
            return self.FloatIntoFraction(Fraction1 * Fraction2)
        elif operator == "/":
            return self.FloatIntoFraction(Fraction1 / Fraction2)
        else:
            raise Exception(f"Please use \"+\", \"-\", \"*\" or \"/\" as an operator instead of \"{operator}\"")
