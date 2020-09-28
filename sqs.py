import boto3

queue_name = 'mytestqueue'
fifoqueuename = 'mytestqueue.fifo'
def sqs_client():
    sqs = boto3.client('sqs', region_name='us-east-1')
    """ :type : pyboto3.sqs """
    return sqs

def create_standard_queue():
    return sqs_client().create_queue(
        QueueName=queue_name
    )

def createfifoqueue():
    return sqs_client().create_queue(
        QueueName = fifoqueuename,
        Attributes ={
            'FifoQueue': 'true'
        }

    )

def findqueue():
    return sqs_client().list_queues(
        QueueNamePrefix='Test'
    )

def listallqueues():
    return sqs_client().list_queues()

def getqueueattributes():
    return sqs_client().get_queue_attributes(
        QueueUrl=urlofthequeue,
        AttributeNames=['All']
    )

def updatequeueattributes():
    return sqs_client().set_queue_attributes(
        QueueUrl=urlofthequeue,
        Attributes={
            "MaximumMessageSize": "131072",
            "VisibilityTimeout": "15"
        }
    )

def deletequeue():
    return sqs_client().delete_queue(
        QueueUrl=urlofthequeue
    )

#working with messages
def sendmsgtoqueue():
    return sqs_client().send_message(
        QueueUrl=url,
        MessageAttributes={
            'Title': {
                'DataType': 'String',
                'StringValue': 'My message title'
            },
            'Author': {
                'DataType': 'String',
                'StringValue': 'Himanshu'
            },
            'Time': {
                'DataType': 'Number',
                'StringValue': '6'
            }
        },
        MessageBody='This is my first sqs message'
    )

def sendbatchmessages():
    return sqs_client().send_message_batch(
        QueueUrl=urlofthequeue,
        Entries=[
            {
                'Id': 'firstmessage',
                'MessageBody': 'This is first message'
            },
            {
                'Id': 'secondmessage',
                'MessageBody': 'This is second message'
            },
            {
                'Id': 'thirdmessage',
                'MessageBody': 'This is third message'
            }
        ]
    )

def pollmessageforqueue():
    return sqs_client().receive_message(
        QueueUrl=urlofthequeue,
        MaxNumberOfMessages=10
    )

def processmessagefromqueue():
    queuedmessage = pollmessageforqueue()
    if 'Messages' in queuedmessage and len(queuedmessage['Messages']) >= 1:
        for message in queuedmessage['Messages']:
            print("processing message" + message['MessageId'] + " with " + message['Body'])
            deletemessagefromqueue(message['ReceiptHandle'])
            changevisibilitytime(message['ReceiptHandle'])

def deletemessagefromqueue(receipthandle):
    return sqs_client().delete_message(
        QueueUrl=urlofthequeue,
        ReceiptHandle=receipthandle

    )


def changevisibilitytime(receipt_handle):
    sqs_client().change_message_visibility(
        QueueUrl=url,
        ReceiptHandle=receipt_handle,
        VisibilityTimeout=5
    )


def purgequeue():
    return sqs_client().purge_queue(
        QueueUrl=urlofthequeue
    )





if __name__ = '__main__':
    print(create_standard_queue()queue())
    print(findqueue())

