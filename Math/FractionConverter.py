class FractionConverter():
    def __init__(self) -> None:
        pass
    def FractionIntoFloat(self, fraction):
        """
        This function will convert your fraction 1/4 into an float 0.25 for you
        to use for your formula

        Fractions can only be in this format 1/4 and should be given as a string
        """
        #TODO Add that you can also do 1 1/4 which is 1.25 
        SplittedList = fraction.split("/")
        convertleft = int(SplittedList[0])
        convertright = int(SplittedList[1])
        return convertleft / convertright

name = FractionConverter()

print(name.FractionIntoFloat("1/4"))