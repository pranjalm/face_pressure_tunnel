import math 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
tunnel_diameter = 10 # meters
mean_unit_weight_prism = 18 #kN/m3
mean_unit_weight_wedge = 18 #kN/m3
soil_height_crown = 15 # meters
overburden_stress = 10 # kN/m2

overburden_friction_phi1 = 30 # degrees
overburden_cohesion_c1 = 0 # kPa

tunnel_friction_phi2 = 30 # degrees
tunnel_cohesion_c2 = 0 # kPa

#sliding_angle = 20 # degrees ; to be iterated
K1 = 1 # Terzaghi and Jelinek(1954) and Girmsheid (2008)
K2 = 0.5 * ( (1-math.sin(math.radians(tunnel_friction_phi2))) + (1-math.sin(math.radians(tunnel_friction_phi2)))/(1+math.sin(math.radians(tunnel_friction_phi2))) )  # Jancsecz and Steiner (1994)
K2 = 1 - math.sin(math.radians(tunnel_friction_phi2))
sliding_angle = np.arange(1, 90, 0.2).tolist()
Area_prism_lst, perimeter_prism_lst, Vertical_stress_at_crown_sigma_vt_lst = [], [], []
vertical_load_on_wedge_from_prism_Pv_lst, wedge_self_weight_G_lst = [], []
Shear_force_cohesion_TC_lst, Shear_force_friction_TR1_lst, Shear_force_friction_TR2_lst = [], [], []
Shear_force_slip_T_lst, Support_force_Ere_lst = [], []
for i in sliding_angle:
    Area_prism = pow(tunnel_diameter,2)*(1/math.tan(math.radians(i))) 
    perimeter_prism = 2*tunnel_diameter* (1 + 1/math.tan(math.radians(i))) 
    if(soil_height_crown<=2*tunnel_diameter):
        Vertical_stress_at_crown_sigma_vt = mean_unit_weight_prism*soil_height_crown + overburden_stress
    else:
        Vertical_stress_at_crown_sigma_vt = ((Area_prism/perimeter_prism)*mean_unit_weight_prism - overburden_cohesion_c1)/( K1*math.tan(math.radians(overburden_friction_phi1)) ) * (1-math.exp(-1*(perimeter_prism/Area_prism)*K1*math.tan(math.radians(overburden_friction_phi1))*soil_height_crown ) ) + overburden_stress*math.exp(-1*(perimeter_prism/Area_prism)*K1*math.tan(math.radians(overburden_friction_phi1))*soil_height_crown )  
        
    vertical_load_on_wedge_from_prism_Pv = pow(tunnel_diameter,2)*(1/math.tan(math.radians(i))) * Vertical_stress_at_crown_sigma_vt * soil_height_crown
    wedge_self_weight_G = 0.5 * pow(tunnel_diameter,3)*(1/math.tan(math.radians(i))) * mean_unit_weight_wedge

    
    Shear_force_cohesion_TC = tunnel_cohesion_c2* pow(tunnel_diameter,2)/(2*math.tan(math.radians(i)))
    Shear_force_friction_TR1 = math.tan(math.radians(tunnel_friction_phi2)) * K2 * ( ( pow(tunnel_diameter,2) * Vertical_stress_at_crown_sigma_vt )/( 3*math.tan(math.radians(i)) ) + (pow(tunnel_diameter,3)*mean_unit_weight_wedge)/( 6*math.tan(math.radians(i)) ) )
    Shear_force_friction_TR2 = math.tan(math.radians(tunnel_friction_phi2)) * K2 * ( ( pow(tunnel_diameter,2) * Vertical_stress_at_crown_sigma_vt )/( 2*math.tan(math.radians(i)) ) + (pow(tunnel_diameter,3)*mean_unit_weight_wedge)/( 6*math.tan(math.radians(i)) ) )
    Shear_force_slip_T = min(Shear_force_friction_TR1,Shear_force_friction_TR2) + Shear_force_cohesion_TC
    
    Support_force_Ere = ( (wedge_self_weight_G + vertical_load_on_wedge_from_prism_Pv)*( math.sin(math.radians(i)) - math.cos(math.radians(i))*math.tan(math.radians(tunnel_friction_phi2))) - 2*Shear_force_slip_T - ( (tunnel_cohesion_c2*pow(tunnel_diameter,2))/math.sin(math.radians(i)) ) ) / ( math.sin(math.radians(i))*math.sin(math.radians(tunnel_friction_phi2))   + math.sin(math.radians(i))  )
    
    Shear_force_cohesion_TC_lst.append(Shear_force_cohesion_TC)
    Shear_force_friction_TR1_lst.append(Shear_force_friction_TR1)
    Shear_force_friction_TR2_lst.append(Shear_force_friction_TR2)
    Shear_force_slip_T_lst.append(Shear_force_slip_T)
    Area_prism_lst.append(Area_prism)
    perimeter_prism_lst.append(perimeter_prism)
    Vertical_stress_at_crown_sigma_vt_lst.append(Vertical_stress_at_crown_sigma_vt)
    vertical_load_on_wedge_from_prism_Pv_lst.append(vertical_load_on_wedge_from_prism_Pv)
    wedge_self_weight_G_lst.append(wedge_self_weight_G)
    Support_force_Ere_lst.append(Support_force_Ere)

angle_crit = sliding_angle[Support_force_Ere_lst.index(max(Support_force_Ere_lst))]
print(angle_crit)

'''
fig, ax1 = plt.subplots()
ax1.plot(sliding_angle, Support_force_Ere_lst, label = 'Ere')
ax1.set_xlim([0,100])
ax1.set_ylim([0,60])
ax1.legend(loc = 4)
ax1.grid(axis='both')
ax1.set_xlabel('Liquid Limit (%)')
ax1.set_ylabel('Plasticity Index (%)')
plt.savefig("PI_test.png",format='png', dpi=1200)
'''



'''
if(soil_height_crown<=2*tunnel_diameter):
    Vertical_stress_at_crown_sigma_vt = mean_unit_weight_prism*soil_height_crown + overburden_stress
else:
    Vertical_stress_at_crown_sigma_vt = ((Area_prism/perimeter_prism)*mean_unit_weight_prism - overburden_cohesion_c1)/( K1*math.tan(math.radians(overburden_friction_phi1)) ) * (1-math.exp(-1*(perimeter_prism/Area_prism)*K1*math.tan(math.radians(overburden_friction_phi1))*soil_height_crown ) ) + overburden_stress*math.exp(-1*(perimeter_prism/Area_prism)*K1*math.tan(math.radians(overburden_friction_phi1))*soil_height_crown )  

vertical_load_on_wedge_from_prism_Pv = pow(tunnel_diameter,2)*(1/math.tan(math.radians(sliding_angle))) * Vertical_stress_at_crown_sigma_vt * soil_height_crown

wedge_self_weight_G = 0.5 * pow(tunnel_diameter,3)*(1/math.tan(math.radians(sliding_angle))) * mean_unit_weight_wedge


K2 = 0.5 * ( (1-math.sin(math.radians(tunnel_friction_phi2))) + (1-math.sin(math.radians(tunnel_friction_phi2)))/(1+math.sin(math.radians(tunnel_friction_phi2))) )  # Jancsecz and Steiner (1994)
Shear_force_cohesion_TC = tunnel_cohesion_c2* pow(tunnel_diameter,2)/(2*math.tan(math.radians(sliding_angle)))
Shear_force_friction_TR1 = math.tan(math.radians(tunnel_friction_phi2)) * K2 * ( ( pow(tunnel_diameter,2) * Vertical_stress_at_crown_sigma_vt )/( 3*math.tan(math.radians(sliding_angle)) ) + (pow(tunnel_diameter,3)*mean_unit_weight_wedge)/( 6*math.tan(math.radians(sliding_angle)) ) )
Shear_force_friction_TR2 = math.tan(math.radians(tunnel_friction_phi2)) * K2 * ( ( pow(tunnel_diameter,2) * Vertical_stress_at_crown_sigma_vt )/( 2*math.tan(math.radians(sliding_angle)) ) + (pow(tunnel_diameter,3)*mean_unit_weight_wedge)/( 6*math.tan(math.radians(sliding_angle)) ) )

Shear_force_slip_T = min(Shear_force_friction_TR1,Shear_force_friction_TR2) + Shear_force_cohesion_TC

Support_force_Ere = ( (wedge_self_weight_G+vertical_load_on_wedge_from_prism_Pv)*( math.sin(math.radians(sliding_angle)) - math.cos(math.radians(sliding_angle))*math.tan(math.radians(tunnel_friction_phi2))) - 2*Shear_force_slip_T - ( (tunnel_cohesion_c2*pow(tunnel_diameter,2))/math.sin(math.radians(sliding_angle)) ) ) / ( math.sin(math.radians(sliding_angle))*math.sin(math.radians(tunnel_friction_phi2))   + math.sin(math.radians(sliding_angle))  )
'''