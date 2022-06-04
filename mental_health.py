import pandas as pd


def main():

    data = read_file('health.csv')
    #print the first 5 rows of the dataframe
    #print(data.head())

    anxiety = 'anxiety'
    depression = 'depression'
    male = 'Male'
    female = 'Female'
    gend_a = gender_anxiety(data)
    gend_d = gender_depression(data)

    mean_age = calculate_mean(data,'Age')
    print(f'\nThe mean age among students is {round(mean_age)}')

    print_count_gender(gend_a,male,anxiety)
    print_count_gender(gend_a,female,anxiety)
    print_count_gender(gend_d,male,depression)
    print_count_gender(gend_d,female,depression)

    #Print a list of all courses and the number of the students interviewed for each course.
    courses = data['Course']
    course = []
    for j in courses:
        course.append(j)
    course_dict = {}
    for k in course : 
        course_dict[k] = [course.count(k)]
    df2 = pd.DataFrame(data=course_dict)
    df2_transposed = df2.transpose()
    print('\nList of courses and number of students for each course')
    print(df2_transposed)

    dep_anx = get_courses_anxiety_depression(data)
    list_courses = [] #empty list
    for i in dep_anx : 
        list_courses.append(i) #append the data obtained from the function to the list
    anx_dep_dict = {} #empty dictionary
    for n in list_courses : 
        anx_dep_dict[n] = [list_courses.count(n)] #convert the list into a dictionary with courses as keys and the count of each course repeated as values
    df = pd.DataFrame(data=anx_dep_dict)
    df_transposed = df.transpose() #Reflect the DataFrame over its main diagonal by writing rows as columns and vice-versa
    print('\nList of courses and number of students who suffer from both anxiety and depression:')
    print(df_transposed)

    seek_sp = seek_specialist(data,'Yes')
    print('\nSTUDENTES WHO SEEKED HELP FROM A SPECIALIST:')
    print(seek_sp)
    not_seek = seek_specialist(data,'No')
    print('\n\nSTUDENTS WHO DIDNT SEEK HELP FROM A SPECIALIST:')
    print(not_seek)



def read_file(filename) :

    #Read the csv file and change the title of the columns to work easier with them
    data = pd.read_csv(filename)
    data.rename(columns={'Choose your gender':'Gender'}, inplace=True)
    data.rename(columns={'What is your course?':'Course'}, inplace=True)
    data.rename(columns={'Your current year of Study':'Year'}, inplace=True)
    data.rename(columns={'What is your CGPA?':'CGPA'}, inplace=True)
    data.rename(columns={'Marital status':'Married'}, inplace=True)
    data.rename(columns={'Do you have Depression?':'DepressionYN'}, inplace=True)
    data.rename(columns={'Do you have Anxiety?':'AnxietyYN'},inplace=True)
    data.rename(columns={'Do you have Panic attack?':'PanicYN'}, inplace=True)
    data.rename(columns={'Did you seek any specialist for a treatment?':'SpecialistYN'}, inplace=True)
    #I FOUND A MISSING VALUE IN THE AGE COLUMN, I REPLACED THAT MISSING VALUE BY THE MEAN AGE BETWEEN 18 AND 24
    age_40 = data['Age'][40]
    age_41 = data['Age'][41]
    mean = (age_40 + age_41) / 2
    data.fillna(value=mean, inplace=True)
    return data


def calculate_mean(data,title) :
    #calculates the mean of a column
    mean_data = data[title].mean()
    return mean_data

def get_courses_anxiety_depression(data):
    #from all the dataset get the courses where students suffer from anxiety and depression at the same time. 
    anx_dep = data[(data.DepressionYN == 'Yes')&(data.AnxietyYN=='Yes')].Course
    return anx_dep

def print_count_gender(gender_list,gender,mental_disorder):
    #APPEND THE GENDER OF THE STUDENTS WITH DEPRESSION TO A LIST, AND THEN COUNT THEM.
    genders = []
    for i in gender_list :
        genders.append(i)
    i = 0
    while i < len(genders) :
        i += 1
        count = genders.count(gender)
    print(f'The number of {gender.lower()} with {mental_disorder} is: {count}')

def gender_depression(data):
    #FROM THE DATASET GET THE GENDER OF THE STUDENTS WHO AFFIRMED TO HAVE DEPRESSION
    depression_gender = data[data.DepressionYN=='Yes'].Gender
    return depression_gender

def gender_anxiety(data):
    #FROM THE DATASET GET THE GENDER OF THE STUDENTS WHO AFFIRMED TO HAVE ANXIETY 
    anxiety_gender = data[data.AnxietyYN=='Yes'].Gender
    return anxiety_gender

def seek_specialist(data,answer):
    #get the students who seeked or not help from a specialist -(depending on the parameter if the answer is yes or no)-
    specialist = data.loc[data.SpecialistYN==answer,['Gender','Age','Course','CGPA','Married','SpecialistYN']]
    return specialist



if __name__ == '__main__' :
    main()