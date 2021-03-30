import mlflow
import os
import sys
import mlflow.sklearn

if __name__ == "__main__":
    mlflow.set_tracking_uri('http://127.0.0.1:5000')
    a=int(sys.argv[1])
    mlflow.log_param("val1",a)
    b=int(sys.argv[2])
    mlflow.log_param("val2",b)
    c=a*b
    print("Multiplication :"+str(c))
    #path='C:\Users\smurugan\Desktop\Image_classification\mlflow\reviewed_415_dents_csv.csv'
    output=sys.argv[3]
    #dir_path = output.rsplit("/", 1)
    #print(dir_path)
    #os.chdir(dir_path[0])
    #print(os.getcwd())
#     with open(output,'wb'):
#         mlflow.log_artifact(output)
    #cwd = os.getcwd()    
    #print(cwd)
    #with open(cwd+'/mlflowfile.txt', 'w') as f:
        #f.write("Fan of Python")
    mlflow.log_metric("mutiplication",c)
    mlflow.log_artifact(output,artifact_path="saved_files")
