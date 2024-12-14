import boto3
s3obj = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('vamsi_emp')

def lambda_handler(event,context):
    bucket_name = 'vamsource'
    file_name = 'emp.csv'
    resp = s3obj.get_object(Bucket = bucket_name, Key = file_name)
    data = resp['Body'].read().decode('utf-8')
    print(data)
    employees=data.split('\n')
    print(employees)
    
    for emp in employees:
        emp_id,emp_name,emp_prof = emp.split(',')
        #adding print function
        try:
            response = table.put_item(
                Item = {
                    'emp_id':emp_id,
                    'emp_name':emp_name,
                    'emp_prof':emp_prof
                }
                )
        except Exception as e:
            raise e
