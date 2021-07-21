class FractionConverter():
    def __init__(self) -> None:
        pass
    def FractionIntoFloat(self, fraction):
        """
        This function will convert your fraction 1/4 into an float 0.25 for you
        to use for your formula

        Fractions can only be in this format 1/4 and should be given as a string
        """
        SplittedList = fraction.split("/")
        #TODO finish this function and class

        return SplittedList

name = FractionConverter()

print(name.FractionIntoFloat("1/4"))