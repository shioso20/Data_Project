import math
def calculate_credit_risk(df): 
    
    
    low = round(df[df["Credit Risk"]=="Low"]["Credit Risk"].count(),2)

    high = round(df[df["Credit Risk"]=="High"]["Credit Risk"].count(),2)

    ratio = round(high/low-1,2)

    
    return str(low),str(high),str(ratio)


def calculate_credit_risk_by_gender(df): 
    
    low_male = df[(df["Credit Risk"]=="Low") & (df["Gender"]=="M")]["Credit Risk"].count()
    low_female = df[(df["Credit Risk"]=="Low") & (df["Gender"]=="F")]["Credit Risk"].count()

    high_female = df[(df["Credit Risk"]=="High") & (df["Gender"]=="F")]["Credit Risk"].count()
    high_male = df[(df["Credit Risk"]=="High") & (df["Gender"]=="M")]["Credit Risk"].count()

    ratio_high = round(high_male/high_female-1,2)
    ratio_low = round(low_male/low_female-1,2) 
    
    
    return str(high_male)+" / "+str(high_female),str(low_male)+" / "+str(low_female),str(ratio_high),str(ratio_low)
    
    