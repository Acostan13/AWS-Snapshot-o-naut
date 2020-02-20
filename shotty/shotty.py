import boto3

# best practice to put your script code in a if(name==main) block
if __name__ == '__main__':
    session = boto3.Session(profile_name='shotty')
    ec2 = session.resource('ec2')

    for i in ec2.instances.all():
        print(i)