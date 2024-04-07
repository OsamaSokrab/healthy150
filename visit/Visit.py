from datetime import datetime
from dictionary_healthy150 import add_item_with_subitem, add_item_with_two_subitems, add_item_with_three_subitems, save_data_to_personData


class Visit:
    def __init__(self, visit_id, person_id, professional_id, provider_id, year, month, day):
        self.visit_id = visit_id
        self.person_id = person_id
        self.professional_id = professional_id
        self.provider_id = provider_id
        self.date = datetime(year, month, day).strftime("%A %d/%B/%Y")

   #step 1
    def add_visit_details(self):
         add_item_with_subitem(self.person_id, 'visits', self.visit_id, date =self.date, professional=self.professional_id, provider=self.provider_id)
         save_data_to_personData()
          
    #step 2
    def add_complain(self, pain=False, painSite='', painRightOrLeft='',painDuration='', 
                           painRadiation='', painAssociation='', painAtNight=False,   painOtherKnee=False, painHand=False, painFoot=False,trauma=False, traumaHow='',traumaWhen='', swelling=False, givingway=False, locking=False, hotness=False, crepitus=False, numbness=False, weakness=False, dislocation=False, dislocation_site='', unable_to_walk=False):
	    add_item_with_two_subitems(self.person_id, 'visits', self.visit_id, 'complain', pain=pain, painSite=painSite, painRightOrLeft=painRightOrLeft,painDuration=painDuration, painRadiation=painRadiation, painAssociation=painAssociation, painAtNight=painAtNight, painOtherKnee=painOtherKnee, painHand=painHand, painFoot=painFoot,trauma=trauma,traumaHow=traumaHow, traumaWhen=traumaWhen, swelling=swelling, givingway=givingway, locking=locking, hotness=hotness, crepitus=crepitus, numbness=numbness, weakness=weakness, dislocation=dislocation, dislocation_site=dislocation_site, unable_to_walk=unable_to_walk)
          
    #step 4
    def add_systemic_enquiries(self, diabetes=False, diabetes_duration='', diabetes_treatment='', high_cholesterol=False, hypertension=False, hypothyroidism=False, hypothyroidism_treatment='', hyperthyroidism=False, hyperthyroidism_treatment='', gastric_upset=False):
	    add_item_with_two_subitems(self.person_id, 'visits', self.visit_id,'systemic enquiries',  diabetes=diabetes, diabetes_duration=diabetes_duration, diabetes_treatment=diabetes_treatment, hypothyroidism=hypothyroidism, hypothyroidism_treatment=hypothyroidism_treatment, hyperthyroidism=hyperthyroidism, hyperthyroidism_treatment=hyperthyroidism_treatment, hypertension=hypertension, high_cholesterol=high_cholesterol, gastric_upset=gastric_upset)	

    #step 4
    def add_past_medical_history(self, previous_surgery=False, previous_surgery_type='', previous_surgery_when=False):
	    add_item_with_two_subitems(self.person_id, 'visits', self.visit_id,'past medical history',  previous_surgery=previous_surgery, previous_surgery_type=previous_surgery_type, previous_surgery_when=previous_surgery_when)	

    #step 4
    def add_on_examination(self, obesity=False, benign_ligament_hypermobility=False, alignment='', wasting='', tenderness='', loose_bodies=False, range_of_motion='normal', valgus_stress=False, varus_stress=False, lachman=False, anterior_drawer=False, posterior_drawer=False, mcmurry=False, appley=False, straight_leg_raising=False, femoral_stretch=False, power='', sensation='', reflexes='', patellar_tracking='', gait='', squatting='', extension=0, flexion=110):
	    add_item_with_two_subitems(self.person_id, 'visits', self.visit_id, 'on examination',  obesity=obesity, benign_ligament_hypermobility=benign_ligament_hypermobility, alignment=alignment, wasting=wasting, tenderness=tenderness, loose_bodies=loose_bodies, range_of_motion=range_of_motion, valgus_stress=valgus_stress, varus_stress=varus_stress, lachman=lachman, anterior_drawer=anterior_drawer, posterior_drawer=posterior_drawer, mcmurry=mcmurry, appley=appley, straight_leg_raising=straight_leg_raising, femoral_stretch=femoral_stretch, power=power, sensation=sensation, reflexes=reflexes, patellar_tracking=patellar_tracking, gait=gait, squatting=squatting, flexion=flexion, extension=extension)

    #step 6
    def add_mri(self, mri_requested=False, medial_meniscus_tear=False, lateral_meniscus_tear=False, meniscus_tear_type='', mcl_tear=False, acl_tear=False, pcl_tear=False, ocd=False, ocd_site='', discoid_meniscus=False, discoid_meniscus_side='', other='', hoffa_fat_pad_mass=False, nodular_synovitis=False, osteochondritis_dissicans=False, osteochondritis_dissicans_site=''):
	    if mri_requested == True:
		    add_item_with_three_subitems(self.person_id, 'visits', self.visit_id, 'imaging', 'mri',  mri_requested=mri_requested)
	    else:
		    add_item_with_three_subitems(self.person_id, 'visits', self.visit_id, 'imaging', 'mri',  medial_meniscus_tear=medial_meniscus_tear, lateral_meniscus_tear=lateral_meniscus_tear, meniscus_tear_type=meniscus_tear_type, acl_tear=acl_tear, mcl_tear=mcl_tear, pcl_tear=pcl_tear, ocd=ocd, ocd_site=ocd_site, discoid_meniscus=discoid_meniscus, discoid_meniscus_side=discoid_meniscus_side, other=other, hoffa_fat_pad_mass=hoffa_fat_pad_mass, nodular_synovitis=nodular_synovitis, osteochondritis_dissicans=osteochondritis_dissicans, osteochondritis_dissicans_site=osteochondritis_dissicans_site)

    def add_xray(self,xray_pelvis=False, xray_spine=False, xray_pelvis_finding='', xray_spine_findings='', osteoarthritis=False):
	    if osteoarthritis==True or xray_pelvis==True or xray_spine==True:
		    add_item_with_three_subitems(self.person_id, 'visits', self.visit_id, 'imaging', 'xray', xray_pelvis=xray_pelvis, xray_pelvis_finding=xray_pelvis_finding, xray_spine=xray_spine, xray_spine_findings=xray_spine_findings, osteoarthritis=osteoarthritis)

    #step 4
    def add_lab(self, cbc='', esr='', crp='', uric_acid='', rheumatoid_factor='', culture=''):
        add_item_with_two_subitems(self.person_id, 'visits', self.visit_id,'lab', cbc=cbc, crp=crp, esr=esr, uric_acid=uric_acid, rheumatoid_factor=rheumatoid_factor, culture=culture)

    def add_plan_not_made(self, plan_made=False):
        add_item_with_two_subitems(self.person_id, 'visits', self.visit_id, 'plan', plan_made=plan_made)

   #step 8
    def add_surgery(self,meniscus_repair=False, acl_reconstruction=False, pcl_reconstruction=False, mcl_reconstruction=False, posterolateral_corner_reconstruction=False, mpfl_reconstruction=False, microfracture=False, arthroscopic_partial_meniscectomy=False, surgery_done=False, achilles_tendon_repair=False, distal_femoral_osteotomy=False, shoulder_arthroscopy=False, saucerization=False, tkr=False, meniscus_transplant=False, surgery_year=0, surgery_month=0, surgery_day=0, ankle_syndesmosis_fixation=False):
        if surgery_done == False:
            add_item_with_three_subitems(self.person_id, 'visits', self.visit_id, 'plan', 'surgery', meniscus_repair=meniscus_repair, acl_reconstruction=acl_reconstruction, pcl_reconstruction=pcl_reconstruction, mcl_reconstruction=mcl_reconstruction, posterolateral_corner_reconstruction=posterolateral_corner_reconstruction, mpfl_reconstruction=mpfl_reconstruction, microfracture=microfracture, arthroscopic_partial_meniscectomy=arthroscopic_partial_meniscectomy, achilles_tendon_repair=achilles_tendon_repair, distal_femoral_osteotomy=distal_femoral_osteotomy, shoulder_arthroscopy=shoulder_arthroscopy, tkr=tkr, saucerization=saucerization, meniscus_transplant=meniscus_transplant, ankle_syndesmosis_fixation=ankle_syndesmosis_fixation)
        else:
            add_item_with_subitem(self.person_id, 'visits', self.visit_id, 'plan', 'surgery', surgery_done=True, meniscus_repair=meniscus_repair, acl_reconstruction=acl_reconstruction, pcl_reconstruction=pcl_reconstruction, mcl_reconstruction=mcl_reconstruction, posterolateral_corner_reconstruction=posterolateral_corner_reconstruction, mpfl_reconstruction=mpfl_reconstruction, microfracture=microfracture, arthroscopic_partial_meniscectomy=arthroscopic_partial_meniscectomy, achilles_tendon_repair=achilles_tendon_repair, distal_femoral_osteotomy=distal_femoral_osteotomy, shoulder_arthroscopy=shoulder_arthroscopy, tkr=tkr, saucerization=saucerization, meniscus_transplant=meniscus_transplant, ankle_syndesmosis_fixation=ankle_syndesmosis_fixation)

    def add_drugs(self, drugName='', dose='', duration='', drugName1='', dose1='', duration1='', drugName2='', dose2='', duration2=''):
        add_item_with_three_subitems(self.person_id, 'visits', self.visit_id,'plan', 'medications', drugName=drugName, dose=dose, duration=duration, drugName1=drugName1, dose1=dose1, duration1=duration1, drugName2=drugName2, dose2=dose2, duration2=duration2)

    def add_appointment(self, appointment_year, appointment_month, appointment_day):
        from datetime import datetime
        appointment_date= datetime(appointment_year, appointment_month, appointment_day).strftime(f"%A %d/%B/%Y")
        add_item_with_three_subitems(self.person_id, 'visits', self.visit_id, 'plan', 'appointment', appointment_date=appointment_date)

    def add_physiotherapy(self, physiotherapy_site='', muscle_strengthening_exercises=False, range_of_motion_exercises=False):
        add_item_with_three_subitems(self.person_id, 'visits', self.visit_id, 'plan', 'physiotherapy', physiotherapy_site=physiotherapy_site, muscle_strengthening_exercises=muscle_strengthening_exercises, range_of_motion_exercises=range_of_motion_exercises)

   # step 9
    def add_opd_procedure(self, remove_stitches=False, remove_lock=False, remove_brace=False, remove_walker=False, dressing=False, prp=False, reassurance=False, referTo='', knee_support=False):
        add_item_with_three_subitems(self.person_id, 'visits', self.visit_id, 'plan', 'opd_procedure', remove_stitches=remove_stitches, dressing=dressing, remove_lock=remove_lock, remove_brace=remove_brace, remove_walker=remove_walker, prp=prp, reassurance=reassurance, referTo=referTo, knee_support=knee_support)

    def createNewVisit(self, mri_requested=False, plan_made=True,  pain=True, painSite='knee' , painRightOrLeft='',painDuration='', painRadiation='', painAssociation='', painAtNight=False, painOtherKnee=False, painHand=False, painFoot=False,trauma=False, traumaHow='', traumaWhen='', swelling=False, givingway=False, locking=False, hotness=False, crepitus=False, numbness=False, weakness=False, dislocation=False, dislocation_site='', unable_to_walk=False, diabetes=False, diabetes_duration='', diabetes_treatment='', high_cholesterol=False, hypertension=False, hypothyroidism=False, hypothyroidism_treatment='', hyperthyroidism=False, hyperthyroidism_treatment='', gastric_upset=False, previous_surgery=False, previous_surgery_type='', previous_surgery_when='', obesity=False, benign_ligament_hypermobility=False, alignment='normal', wasting='', tenderness='medial joint line', loose_bodies=False, range_of_motion='normal', valgus_stress=False, varus_stress=False, lachman=False, anterior_drawer=False, posterior_drawer=False,  mcmurry=False, appley=False, patellar_tracking='normal', straight_leg_raising=False, femoral_stretch=False, power='', sensation='', reflexes='', gait='normal', squatting='painful', medial_meniscus_tear=False, lateral_meniscus_tear=False, meniscus_tear_type='', acl_tear=False, mcl_tear=False, pcl_tear=False, ocd=False, ocd_site='', discoid_meniscus=False, discoid_meniscus_side='', other='', osteochondritis_dissicans=False, osteochondritis_dissicans_site='', hoffa_fat_pad_mass=False, nodular_synovitis=False, xray_pelvis=False, xray_spine= False, xray_pelvis_finding='', xray_spine_findings='', osteoarthritis=False, cbc='', esr='', crp='', uric_acid='', rheumatoid_factor='', culture='', meniscus_repair=False, acl_reconstruction=False, pcl_reconstruction=False, mcl_reconstruction=False, posterolateral_corner_reconstruction=False, mpfl_reconstruction=False, microfracture=False, arthroscopic_partial_meniscectomy=False, achilles_tendon_repair=False, distal_femoral_osteotomy=False, shoulder_arthroscopy=False, tkr=False, saucerization=False, meniscus_transplant=False, surgery_done=False, surgery_year=0, surgery_month=0, surgery_day=0, ankle_syndesmosis_fixation=False, drugName='', dose='', duration='', drugName1='', dose1='', duration1='', drugName2='', dose2='', duration2='', appointment_year=0, appointment_month=0, appointment_day=0, physiotherapy_site='', muscle_strengthening_exercises=False, range_of_motion_exercises=False, dressing=False, remove_stitches=False, remove_lock=False, remove_brace=True, remove_walker=True, prp=False, reassurance=False, referTo='', knee_support=False, extension=0, flexion=110):

        self.add_visit_details()

        self.add_complain(pain=pain, painSite=painSite, painRightOrLeft=painRightOrLeft,painDuration=painDuration, painRadiation=painRadiation, painAssociation=painAssociation, painAtNight=painAtNight, painOtherKnee=painOtherKnee, painHand=painHand, painFoot=painFoot,trauma=trauma,traumaHow=traumaHow, traumaWhen=traumaWhen, swelling=swelling, givingway=givingway, locking=locking, hotness=hotness, crepitus=crepitus, numbness=numbness, weakness=weakness, dislocation=dislocation, dislocation_site=dislocation_site, unable_to_walk=unable_to_walk)

        self.add_systemic_enquiries(diabetes=diabetes, diabetes_duration=diabetes_duration, diabetes_treatment=diabetes_treatment, high_cholesterol=high_cholesterol, hypertension=hypertension, hypothyroidism=hypothyroidism,hypothyroidism_treatment=hypothyroidism_treatment, hyperthyroidism=hyperthyroidism, hyperthyroidism_treatment=hyperthyroidism_treatment, gastric_upset=gastric_upset)	

        self.add_past_medical_history(previous_surgery=previous_surgery, previous_surgery_type=previous_surgery_type, previous_surgery_when=previous_surgery_when)

        self.add_on_examination(obesity=obesity, benign_ligament_hypermobility=benign_ligament_hypermobility, alignment=alignment, wasting=wasting, tenderness=tenderness, loose_bodies=loose_bodies, valgus_stress=valgus_stress, varus_stress=varus_stress, lachman=lachman, anterior_drawer=anterior_drawer, posterior_drawer=posterior_drawer, mcmurry=mcmurry, appley=appley, straight_leg_raising=straight_leg_raising, femoral_stretch=femoral_stretch, power=power, sensation=sensation, reflexes=reflexes, patellar_tracking=patellar_tracking, gait=gait, squatting=squatting, extension=extension, flexion=flexion, range_of_motion=range_of_motion)

        self.add_mri(mri_requested=mri_requested, medial_meniscus_tear=medial_meniscus_tear, lateral_meniscus_tear=lateral_meniscus_tear, meniscus_tear_type=meniscus_tear_type, acl_tear=acl_tear, mcl_tear=mcl_tear, pcl_tear=pcl_tear, ocd=ocd, ocd_site=ocd_site, discoid_meniscus=discoid_meniscus, discoid_meniscus_side= discoid_meniscus_side,  other=other, hoffa_fat_pad_mass=hoffa_fat_pad_mass, nodular_synovitis=nodular_synovitis, osteochondritis_dissicans=osteochondritis_dissicans, osteochondritis_dissicans_site=osteochondritis_dissicans_site)

        self.add_xray(xray_pelvis=xray_pelvis, xray_spine=xray_spine, xray_pelvis_finding=xray_pelvis_finding, xray_spine_findings=xray_spine_findings, osteoarthritis=osteoarthritis)

        self.add_lab(cbc=cbc, crp=crp, esr=esr, uric_acid=uric_acid, rheumatoid_factor=rheumatoid_factor, culture=culture)
        
        if plan_made == False:
            self.add_plan_not_made(plan_made=plan_made)
        else:
            self.add_surgery(meniscus_repair=meniscus_repair, acl_reconstruction=acl_reconstruction, pcl_reconstruction=pcl_reconstruction, mcl_reconstruction=mcl_reconstruction, posterolateral_corner_reconstruction=posterolateral_corner_reconstruction, mpfl_reconstruction=mpfl_reconstruction, microfracture=microfracture, arthroscopic_partial_meniscectomy=arthroscopic_partial_meniscectomy, achilles_tendon_repair=achilles_tendon_repair, distal_femoral_osteotomy=distal_femoral_osteotomy, shoulder_arthroscopy=shoulder_arthroscopy, tkr=tkr, saucerization=saucerization, meniscus_transplant=meniscus_transplant, surgery_done=surgery_done, surgery_year=surgery_year, surgery_month= surgery_month, surgery_day=surgery_day, ankle_syndesmosis_fixation=ankle_syndesmosis_fixation)

            if drugName != '':
                self.add_drugs(drugName=drugName, dose=dose, duration=duration, drugName1=drugName1, dose1=dose1, duration1=duration1, drugName2=drugName2, dose2=dose2, duration2=duration2)

            if dressing == True or remove_lock == True or remove_stitches == True or prp==True or reassurance==True or referTo != '' or knee_support==True or remove_brace==True or remove_walker==True:
                self.add_opd_procedure(dressing=dressing, remove_lock=remove_lock, remove_stitches=remove_stitches, prp=prp, reassurance=reassurance, referTo=referTo, knee_support=knee_support, remove_brace=remove_brace, remove_walker=remove_walker)

            if physiotherapy_site != '':
                self.add_physiotherapy(physiotherapy_site=physiotherapy_site, muscle_strengthening_exercises=muscle_strengthening_exercises, range_of_motion_exercises=range_of_motion_exercises)

            if appointment_year != 0: 
                self.add_appointment(appointment_year=appointment_year, appointment_month=appointment_month, appointment_day=appointment_day)
        save_data_to_personData()
        return print("data added to personData")

    
    def create_followup_visit(self,year, month, day, mri_requested=False, plan_made=True,  pain=True, painSite='knee' , painRightOrLeft='',painDuration='', painRadiation='', painAssociation='', painAtNight=False, painOtherKnee=False, painHand=False, painFoot=False,trauma=False, traumaHow='', traumaWhen='', swelling=False, givingway=False, locking=False, hotness=False, crepitus=False, numbness=False, weakness=False, dislocation=False, dislocation_site='', unable_to_walk=False, diabetes=False, diabetes_duration='', diabetes_treatment='', high_cholesterol=False, hypertension=False, hypothyroidism=False, hypothyroidism_treatment='', hyperthyroidism=False, hyperthyroidism_treatment='', gastric_upset=False, previous_surgery=False, previous_surgery_type='', previous_surgery_when='', obesity=False, benign_ligament_hypermobility=False, alignment='normal', wasting='', tenderness='medial joint line', loose_bodies=False, range_of_motion='normal', valgus_stress=False, varus_stress=False, lachman=False, anterior_drawer=False, posterior_drawer=False,  mcmurry=False, appley=False, patellar_tracking='normal', straight_leg_raising=False, femoral_stretch=False, power='', sensation='', reflexes='', gait='normal', squatting='painful', medial_meniscus_tear=False, lateral_meniscus_tear=False, meniscus_tear_type='', acl_tear=False, mcl_tear=False, pcl_tear=False, ocd=False, ocd_site='', discoid_meniscus=False, discoid_meniscus_side='', other='', osteochondritis_dissicans=False, osteochondritis_dissicans_site='', hoffa_fat_pad_mass=False, nodular_synovitis=False, xray_pelvis=False, xray_spine= False, xray_pelvis_finding='', xray_spine_findings='', osteoarthritis=False, cbc='', esr='', crp='', uric_acid='', rheumatoid_factor='', culture='', meniscus_repair=False, acl_reconstruction=False, pcl_reconstruction=False, mcl_reconstruction=False, posterolateral_corner_reconstruction=False, mpfl_reconstruction=False, microfracture=False, arthroscopic_partial_meniscectomy=False, achilles_tendon_repair=False, distal_femoral_osteotomy=False, shoulder_arthroscopy=False, tkr=False, saucerization=False, meniscus_transplant=False, surgery_done=False, surgery_year=0, surgery_month=0, surgery_day=0, ankle_syndesmosis_fixation=False, drugName='', dose='', duration='', drugName1='', dose1='', duration1='', drugName2='', dose2='', duration2='', appointment_year=0, appointment_month=0, appointment_day=0, physiotherapy_site='', muscle_strengthening_exercises=False, range_of_motion_exercises=False, dressing=False, remove_stitches=False, remove_lock=False, remove_brace=False, remove_walker=False, prp=False, reassurance=False, referTo='', knee_support=False, extension=0, flexion=110):
        self.add_complain(pain=pain, painSite=painSite, painRightOrLeft=painRightOrLeft,painDuration=painDuration, painRadiation=painRadiation, painAssociation=painAssociation, painAtNight=painAtNight, painOtherKnee=painOtherKnee, painHand=painHand, painFoot=painFoot,trauma=trauma,traumaHow=traumaHow, traumaWhen=traumaWhen, swelling=swelling, givingway=givingway, locking=locking, hotness=hotness, crepitus=crepitus, numbness=numbness, weakness=weakness, dislocation=dislocation, dislocation_site=dislocation_site, unable_to_walk=unable_to_walk)

        self.add_systemic_enquiries(diabetes=diabetes, diabetes_duration=diabetes_duration, diabetes_treatment=diabetes_treatment, high_cholesterol=high_cholesterol, hypertension=hypertension, hypothyroidism=hypothyroidism,hypothyroidism_treatment=hypothyroidism_treatment, hyperthyroidism=hyperthyroidism, hyperthyroidism_treatment=hyperthyroidism_treatment, gastric_upset=gastric_upset)	

        self.add_past_medical_history(previous_surgery=previous_surgery, previous_surgery_type=previous_surgery_type, previous_surgery_when=previous_surgery_when)

        self.add_on_examination(obesity=obesity, benign_ligament_hypermobility=benign_ligament_hypermobility, alignment=alignment, wasting=wasting, tenderness=tenderness, loose_bodies=loose_bodies, valgus_stress=valgus_stress, varus_stress=varus_stress, lachman=lachman, anterior_drawer=anterior_drawer, posterior_drawer=posterior_drawer, mcmurry=mcmurry, appley=appley, straight_leg_raising=straight_leg_raising, femoral_stretch=femoral_stretch, power=power, sensation=sensation, reflexes=reflexes, patellar_tracking=patellar_tracking, gait=gait, squatting=squatting, extension=extension, flexion=flexion, range_of_motion=range_of_motion)

        self.add_mri(mri_requested=mri_requested, medial_meniscus_tear=medial_meniscus_tear, lateral_meniscus_tear=lateral_meniscus_tear, meniscus_tear_type=meniscus_tear_type, acl_tear=acl_tear, mcl_tear=mcl_tear, pcl_tear=pcl_tear, ocd=ocd, ocd_site=ocd_site, discoid_meniscus=discoid_meniscus, discoid_meniscus_side= discoid_meniscus_side,  other=other, hoffa_fat_pad_mass=hoffa_fat_pad_mass, nodular_synovitis=nodular_synovitis, osteochondritis_dissicans=osteochondritis_dissicans, osteochondritis_dissicans_site=osteochondritis_dissicans_site)

        self.add_xray(xray_pelvis=xray_pelvis, xray_spine=xray_spine, xray_pelvis_finding=xray_pelvis_finding, xray_spine_findings=xray_spine_findings, osteoarthritis=osteoarthritis)

        self.add_lab(cbc=cbc, crp=crp, esr=esr, uric_acid=uric_acid, rheumatoid_factor=rheumatoid_factor, culture=culture)
        
        if plan_made == False:
            self.add_plan_not_made(plan_made=plan_made)
        else:
            self.add_surgery(meniscus_repair=meniscus_repair, acl_reconstruction=acl_reconstruction, pcl_reconstruction=pcl_reconstruction, mcl_reconstruction=mcl_reconstruction, posterolateral_corner_reconstruction=posterolateral_corner_reconstruction, mpfl_reconstruction=mpfl_reconstruction, microfracture=microfracture, arthroscopic_partial_meniscectomy=arthroscopic_partial_meniscectomy, achilles_tendon_repair=achilles_tendon_repair, distal_femoral_osteotomy=distal_femoral_osteotomy, shoulder_arthroscopy=shoulder_arthroscopy, tkr=tkr, saucerization=saucerization, meniscus_transplant=meniscus_transplant, surgery_done=surgery_done, surgery_year=surgery_year, surgery_month= surgery_month, surgery_day=surgery_day, ankle_syndesmosis_fixation=ankle_syndesmosis_fixation)

            if drugName != '':
                self.add_drugs(drugName=drugName, dose=dose, duration=duration, drugName1=drugName1, dose1=dose1, duration1=duration1, drugName2=drugName2, dose2=dose2, duration2=duration2)

            if dressing == True or remove_lock == True or remove_stitches == True or prp==True or reassurance==True or referTo != '' or knee_support==True or remove_brace==True or remove_walker==True:
                self.add_opd_procedure(dressing=dressing, remove_lock=remove_lock, remove_stitches=remove_stitches, prp=prp, reassurance=reassurance, referTo=referTo, knee_support=knee_support, remove_brace=remove_brace, remove_walker=remove_walker)

            if physiotherapy_site != '':
                self.add_physiotherapy(physiotherapy_site=physiotherapy_site, muscle_strengthening_exercises=muscle_strengthening_exercises, range_of_motion_exercises=range_of_motion_exercises)

            if appointment_year != 0: 
                self.add_appointment(appointment_year=appointment_year, appointment_month=appointment_month, appointment_day=appointment_day)
        return print("data added to personData")
