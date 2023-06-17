#declare all necessary libraries
import os
import shutil
import  pandas as pd
import random


# define a function called "Visit" to do our task
 #varibles declared :

#directory : input directory
# patient : the patient's folder
#patient_path: path that stored the inputs we have in the patient's folder
# visits = stores patient0 and patient1
# proposedcsv= stores the column names we need and generated csv file
# file = stores head.scan and thorax.scan
#filename = stores head and thorax without "scan" extension
#filenamelist = stores the column "scanID"
#filelist= stores the column "path"
#patientnamelist= stores the column "patient"
# timepoint = stores timepoint0, timepoint1
#timepointlist= stores the column "visit
#visits_path= stores the timepoint0 and timepoint1 with new folders "Baseline and "Follow Up"
# baseline_path = stores  baseline folder
#follow_path = stores  follow up folder
#baseline_file_path= stores the data appended in baseline folder with only "scan" extension
# follow_file_path = stores the data appended in follow up folder with only "scan" extension

directory = "/root/Desktop/Didier_Radiomics_Challenge/radiomicsstructure/data/"


def visit(directory):


    for patient in os.listdir(directory):
        patient_path = os.path.join(directory, patient)

        if os.path.isdir(patient_path):
            for visits in os.listdir(patient_path):
                proposedcsv=pd.DataFrame(columns=["ScanID","path","patient","visit"])

                filelist =[]
                patientnamelist =[]
                timepointlist =[]
                filenamelist =[]
                visits_path = os.path.join(patient_path, visits)


                if os.path.isdir(visits_path):
                    for file in os.listdir(visits_path):
                      if os.path.isdir(visits_path):
                         baseline_path = os.path.join(visits_path, "Baseline")
                         if "Baseline" not in os.listdir(visits_path):
                             #condition to check if baseline folder exists or not
                           # Create the "Baseline" directory if it doesn't exist

                             os.mkdir(baseline_path)
                             print(f"Created 'Baseline' folder in {visits_path}")
                             filelist.append(file)

                             #condition to check if follow up folder exists or not
                         # Create the "Follow up" directory if it doesn't exist

                    for file in os.listdir(visits_path):
                      if os.path.isdir(visits_path):
                         follow_path = os.path.join(visits_path, "Follow Up")
                         if "Follow Up" not in os.listdir(visits_path):
                            os.mkdir(follow_path)
                            print(f"Created 'Follow Up' folder in {visits_path}")
                            filelist.append(file)
                           #create a for loop to check the next condition where we only keep baseline and follow up data with "scan" extension

                    for file in os.listdir(visits_path):
                          if ".scan" in file:
                             filename = os.path.splitext(file)[0]
                             filenamelist.append(filename)
                             patientname = os.path.splitext(patient)[0]
                             patientnamelist.append(patientname)
                             timepoint = os.path.splitext(visits)[0]
                             timepointlist.append(timepoint)
                             print(f"It's There! {patientname}")

                          #append data into baseline and follow up folders accordingly
                             baseline_file_path = os.path.join(visits_path, file)
                             follow_file_path=os.path.join(visits_path,file)
                             target_file_path = os.path.join(baseline_path, file)
                             target_follow_path=os.path.join(follow_path,file)
                             shutil.copy2(baseline_file_path, target_file_path)
                             shutil.copy2(follow_file_path, target_follow_path)
                             print(f"Appended baseline data to {target_file_path}")
                             print(f"Appended follow up data to{target_follow_path}")

                             filelist.append(file)
                    # attach data to the corresponding columns
                    proposedcsv["ScanID"] = filenamelist
                    proposedcsv["path"] = filelist
                    proposedcsv["patient"] = patientnamelist
                    proposedcsv["visit"] = timepointlist
                     #put the column "Scan ID" to the first line
                    proposedcsv.set_index("ScanID",inplace =True)
                    # add a column "Toprocess" to the end of the file and assign randomly "True" and "False" inputs
                    #Generate the required csv and json files with data the project manager will use to process further tasks
                    proposedcsv["Toprocess"] = [random.choice([True,False]) for _ in range(len(proposedcsv))]

                    proposedcsv.to_csv(follow_path+"/Received.csv")
                    proposedcsv.to_json(follow_path+"/Received.json",index = True)
                    proposedcsv.to_csv(baseline_path+"/Received.csv")
                    proposedcsv.to_json(baseline_path+"/Received.json",index = True)
                    print("Display Data Format:\n",proposedcsv)


directory = "/root/Desktop/Didier_Radiomics_Challenge/radiomicsstructure/data/"
# calling the function's object to get the result by passing the parent path
visit(directory)






















