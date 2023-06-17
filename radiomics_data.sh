#! /bin/bash
#pointing to the alocation where i want to save the file created
DIRECTORY=$1

# I have to check if folder exists with "if condition"
# echo is used to print out the message
if [ -d "$DIRECTORY" ]; then
  echo "$DIRECTORY does not exist. Please enter an existing directory"
  exit
fi
#after checking if a folder exists then i can start working on task
# create radiomics data structure
#create function named radiomics_directory to use
create_radiomics_directory() {

input_directory="/root/Desktop/Didier_Radiomics_Challenge/radiomicsstructure/data"
  # I have to create patient folder if patient does not exist with other sub directories

  if [  ! -d "$input_directory"/$1 ]; then
    echo "$1 does not exists"
    mkdir -p "$input_directory"/$1;
  fi
  if [  ! -d "$input_directory"/$1/$2 ]; then
    echo "$2 does not exists"
    mkdir -p "$input_directory"/$1/$2;
  fi
  # if patient exists then move data into patient folder by only
  # taking ones with "scan" extension and put them into last sub directory
  mv $4 "$input_directory"/$1/$2/$3".scan"

}

#I have to create a loop that helps to fetch all files with only "scan" extension
# store them in each sub directory whereby I have to declare the variables
# variables represents:
# input_directory=data,patient= patient0,timepoint=timepoint0, file=(head.scan,thorax.scan),filename=(head,thorax),
#patient_folder=(patient0,patient1),visit=(timepoint0,timepoint1)
for patient in $input_directory/*; do
  for timepoint in $patient/*; do
    for file in $timepoint/*; do
      if [[ $file == *".scan"* ]]; then
        filename=$(cut -d'.' -f1 <<< "$(basename ${file})")
        patient_folder=$(cut -d'.' -f1 <<< "$(basename ${patient})")
        visit=$(cut -d'.' -f1 <<< "$(basename ${timepoint})")
        echo "It's there! $patient_folder"

#Initiaze input directory as input_directory and call it wherever i need
input_directory="/root/Desktop/Didier_Radiomics_Challenge/radiomicsstructure/data"
create_radiomics_directory $filename $patient_folder $visit $file
      fi

    done
  done
done
#Display the message when a program is done to run
echo "It works Properly... $input_directory"