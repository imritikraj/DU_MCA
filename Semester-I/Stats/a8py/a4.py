import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

# Rural 2009-10
rural_male_2009 = [29.4, 35.7, 16.0, 18.8]
rural_female_2009 = [46.7, 31.8, 11.1, 10.3]

# Urban 2009-10
urban_male_2009 = [16.4, 27.4, 13.6, 42.6]
urban_female_2009 = [26.4, 27.0, 13.6, 32.8]

# Combined 2009-10 (Rural + Urban)
combined_male_2009 = [rural_male_2009[i] + urban_male_2009[i] for i in range(4)]
combined_female_2009 = [rural_female_2009[i] + urban_female_2009[i] for i in range(4)]



def chi_square_test(data, label):
    chi2, p, dof, expected = chi2_contingency(data)
    print(f"\n--- {label} ---")
    contingency_table = pd.DataFrame(data, 
                                   index=['Male', 'Female'], 
                                   columns=['Not Literate', 'Primary', 'Middle', 'Secondary+'])
    print(contingency_table)
    print(f"Chi-square Statistic: {round(chi2, 4)}")
    print(f"Degrees of Freedom: {dof}")
    print(f"p-value: {round(p, 6)}")
    print(f"Significance Level: 95% (alpha = 0.05)") 
    
    if p < 0.05:
        print("RESULT: REJECT H0 -> Gender has SIGNIFICANT impact on education level")
    else:
        print("RESULT: FAIL TO REJECT H0 -> No significant impact of gender on education level")
    
    return chi2, p, dof


# Test for Rural 2009-10
chi_square_test(np.array([rural_male_2009, rural_female_2009]), "Rural Population (2009-10)")

# Test for Urban 2009-10  
chi_square_test(np.array([urban_male_2009, urban_female_2009]), "Urban Population (2009-10)")

# Test for Combined 2009-10
chi_square_test(np.array([combined_male_2009, combined_female_2009]), "Combined Population (2009-10)")
