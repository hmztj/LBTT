# -----------------------------------------------------------
# calculates Land and building transaction tax - takes property's value as an arguement
# Hamza Ali, london, UK
# hmztj1@gmail.com
# -----------------------------------------------------------

import sys

# Data Class for custom data type to hold required attributes of a band
# i.e. lower limit, higher limit, tax rate and tax amount of that band difference.
class TaxBand:
    def __init__(self, low, high, rate):
        self.low = low
        self.high = high
        self.rate = rate
        self.tax = (self.high - self.low) * self.rate
        
    def get_tax(cls, property_value):    
        if(property_value > cls.high):
            return (cls.high - cls.low) * cls.rate
        elif(property_value < cls.low):
            return 0
        else:
             return (property_value - cls.low) * cls.rate


NON_TAXABLE_LIMIT = 145000

# helper function to extract required bands only, based on the property value.
# e.g. if property value is lower than any of the bands, we do not need to include any bands after that.
def get_taxable_bands(property_value):
    
    low_band = TaxBand(NON_TAXABLE_LIMIT, 250000, 0.02)
    mid_band = TaxBand(low_band.high, 325000, 0.05)
    #mid_band2 = TaxBand(500000, 700000, 0.075)
    high_band = TaxBand(mid_band.high, 750000, 0.10)
     
    # max band is used if the value of property excedes the highest band limit - it incurs 12% tax => above £750,000.00
    # here higher limit of the band doesn't matter as long as it is above the property value as-
    # the main function will use the porperty value itself as higher limit.
    max_band = TaxBand(high_band.high, float('inf'), 0.12)

    # list of All bands
    bands = [low_band, mid_band, high_band, max_band]

    # extracts the required bands and stores them in a list using filter function.
    # if lower limit of the current band is less than propertyValue
    taxable_bands = filter(lambda band: band.low < property_value, bands)

    return taxable_bands


# main function to calculate the LBTT
# takes property's value as an argument
def get_lbtt(property_value):
   
    # edge case if property value is lower or equal to the non taxable limit, no tax is incurred.
    if(property_value <= NON_TAXABLE_LIMIT):  # £145,000
        return 0.0

    taxable_bands = get_taxable_bands(property_value)

    # tax sum is accumulated in 'tax_amount' after looping through all of the taxable bands
    # if propertValue is not greater than higher limit of band than propertyValue is used as higher limit
    tax_amount = 0
    for band in taxable_bands:
        tax_amount += band.tax if property_value > band.high else (
            property_value - band.low)*band.rate

    return round(tax_amount, 2)


# sets a starting point for execution of the code.
if __name__ == '__main__':

    # validates the input and throws an error if caught any exceptions. 
    try:
        #property_value = float(input("please enter property value: £"))
        property_value = 100
        if(property_value < 0):
            raise ValueError
        tax = get_lbtt(property_value)
        amountAfterTax = property_value + tax
        print("\nLBTT incurred on property of value", "£{:,.2f}".format(property_value), "is", "£{:,.2f}".format(tax),
                "\n\nTotal Payable amount after tax:", "£{:,.2f}".format(amountAfterTax), "\n")
    except KeyboardInterrupt:
        print("\nStopped")
        sys.exit()
    except:
        print("\nInvalid Input\nPlease enter positive numbers only.\n")
